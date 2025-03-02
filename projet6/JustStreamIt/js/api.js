class MovieAPI {
    static BASE_URL = 'http://localhost:8000/api/v1';

    static async fetchBestMovie() {
        try {
            const response = await fetch(`${this.BASE_URL}/titles/?sort_by=-imdb_score`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            return data.results[0];
        } catch (error) {
            console.error('Erreur lors de la récupération du meilleur film:', error);
            throw error;
        }
    }

    static async fetchMoviesByGenre(genre, page = 1) {
        try {
            const response = await fetch(`${this.BASE_URL}/titles/?genre=${genre}&sort_by=-imdb_score&page=${page}`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            return data.results;
        } catch (error) {
            console.error(`Erreur lors de la récupération des films du genre ${genre}:`, error);
            throw error;
        }
    }

    static async fetchMovieDetails(id) {
        try {
            const response = await fetch(`${this.BASE_URL}/titles/${id}`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error('Erreur lors de la récupération des détails du film:', error);
            throw error;
        }
    }

    static async fetchTopMovies(page = 1) {
        try {
            const response = await fetch(`${this.BASE_URL}/titles/?sort_by=-imdb_score&page=${page}`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            return data.results;
        } catch (error) {
            console.error('Erreur lors de la récupération des films les mieux notés:', error);
            throw error;
        }
    }
    static async fetchGenres() {
        try {
            // Récupérer d'abord tous les films
            const response = await fetch(`${this.BASE_URL}/titles/`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            
            // Extraire tous les genres uniques
            const genres = new Set();
            data.results.forEach(movie => {
                if (movie.genres) {
                    movie.genres.forEach(genre => genres.add(genre));
                }
            });
            
            // Convertir le Set en tableau et trier
            return Array.from(genres).sort();
        } catch (error) {
            console.error('Erreur lors de la récupération des genres:', error);
            throw error;
        }
    }
}


export { MovieAPI };