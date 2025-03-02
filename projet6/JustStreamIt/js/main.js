import { MovieAPI } from './api.js';
import { initCarousels } from './carousel.js';

document.addEventListener('DOMContentLoaded', async () => {
    try {
        await initializePage();
        // Attendre un peu que le DOM soit mis à jour avec les films
        setTimeout(() => {
            initCarousels();
        }, 100);
    } catch (error) {
        console.error('Erreur lors de l\'initialisation :', error);
    }
});

async function initializePage() {
    try {
        // Chargement du meilleur film
        const bestMovie = await MovieAPI.fetchBestMovie();
        displayBestMovie(bestMovie);

        // Chargement des films les mieux notés
        const topMovies = await MovieAPI.fetchTopMovies();
        displayMoviesCarousel('top-rated', topMovies);

        // Chargement des catégories spécifiques
        const actionMovies = await MovieAPI.fetchMoviesByGenre('Action');
        displayMoviesCarousel('category1', actionMovies);

        const comedyMovies = await MovieAPI.fetchMoviesByGenre('Comedy');
        displayMoviesCarousel('category2', comedyMovies);

        // Chargement des genres pour le sélecteur de catégorie
        const genres = await MovieAPI.fetchGenres();
        initializeCategorySelector(genres);
    } catch (error) {
        console.error('Erreur lors de l\'initialisation de la page:', error);
    }
}

function displayBestMovie(movie) {
    const bestMovieSection = document.getElementById('best-movie');
    if (bestMovieSection) {
        bestMovieSection.querySelector('#best-movie-title').textContent = movie.title;
        bestMovieSection.querySelector('#best-movie-description').textContent = movie.description;
        bestMovieSection.querySelector('#best-movie-image').src = movie.image_url;
        const btnDetails = bestMovieSection.querySelector('.btn-details');
        btnDetails.dataset.id = movie.id;
        btnDetails.addEventListener('click', () => showMovieModal(movie.id));
    }
}

function displayMoviesCarousel(sectionId, movies) {
    const section = document.getElementById(sectionId);
    const container = section.querySelector('.movies-container');
    container.innerHTML = '';

    // Limiter à 6 films
    const moviesToDisplay = movies.slice(0, 6);

    moviesToDisplay.forEach(movie => {
        const movieElement = createMovieElement(movie);
        container.appendChild(movieElement);
    });
}

function createMovieElement(movie) {
    const div = document.createElement('div');
    div.className = 'movie-card';
    div.innerHTML = `
        <div class="card">
            <div class="card-img-container">
                <img src="${movie.image_url}" 
                     alt="${movie.title}" 
                     class="card-img-top"
                     loading="lazy"
                     onerror="this.src='https://via.placeholder.com/182x268?text=No+Image'">
            </div>
            <div class="card-body p-2">
                <h5 class="card-title fs-6 text-truncate">${movie.title}</h5>
                <button class="btn btn-sm btn-outline-primary btn-details" 
                        data-id="${movie.id}">
                    Plus d'infos
                </button>
            </div>
        </div>
    `;
    return div;
}

async function showMovieModal(movieId) {
    try {
        const movieDetails = await MovieAPI.fetchMovieDetails(movieId);
        const modalElement = document.getElementById('movie-modal');
        const modal = new bootstrap.Modal(modalElement);
        
        // Remplir la modale avec les détails du film
        modalElement.querySelector('#modal-title').textContent = movieDetails.title || '';
        modalElement.querySelector('#modal-image').src = movieDetails.image_url || '';
        modalElement.querySelector('#modal-genres').textContent = movieDetails.genres?.join(', ') || '';
        modalElement.querySelector('#modal-release-date').textContent = movieDetails.date_published || '';
        modalElement.querySelector('#modal-rated').textContent = movieDetails.rated || '';
        modalElement.querySelector('#modal-imdb-score').textContent = movieDetails.imdb_score || '';
        modalElement.querySelector('#modal-director').textContent = movieDetails.directors?.join(', ') || '';
        modalElement.querySelector('#modal-actors').textContent = movieDetails.actors?.join(', ') || '';
        modalElement.querySelector('#modal-duration').textContent = movieDetails.duration ? `${movieDetails.duration} min` : '';
        modalElement.querySelector('#modal-country').textContent = movieDetails.countries?.join(', ') || '';
        modalElement.querySelector('#modal-box-office').textContent = movieDetails.worldwide_gross_income ? 
            `$${movieDetails.worldwide_gross_income.toLocaleString()}` : 'Non disponible';
        modalElement.querySelector('#modal-description').textContent = movieDetails.long_description || '';

        modal.show();
    } catch (error) {
        console.error('Erreur lors de l\'affichage des détails du film:', error);
    }
}

async function initializeCategorySelector(genres) {
    const select = document.getElementById('category-select');
    if (select) {
        // Vider d'abord le select
        select.innerHTML = '<option value="">Sélectionner une catégorie</option>';
        
        // Ajouter les genres
        genres.forEach(genre => {
            const option = document.createElement('option');
            option.value = genre;
            option.textContent = genre;
            select.appendChild(option);
        });

        // Écouter les changements
        select.addEventListener('change', async (event) => {
            const selectedGenre = event.target.value;
            if (selectedGenre) {
                try {
                    const movies = await MovieAPI.fetchMoviesByGenre(selectedGenre);
                    displayMoviesCarousel('custom-category', movies);
                    initCarousels(); // Réinitialiser le carousel après avoir chargé les nouveaux films
                } catch (error) {
                    console.error(`Erreur lors du chargement des films ${selectedGenre}:`, error);
                }
            }
        });
    }
}
