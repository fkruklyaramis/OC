class Carousel {
    constructor(element) {
        this.element = element;
        this.container = element.querySelector('.movies-container');
        this.prevButton = element.querySelector('.carousel-prev');
        this.nextButton = element.querySelector('.carousel-next');
        this.itemWidth = 220; // Largeur d'une carte de film + margin
        this.visibleItems = this.getVisibleItems();
        
        this.initEvents();
        this.updateButtonsVisibility();
    }

    getVisibleItems() {
        // Calcul du nombre d'éléments visibles selon la largeur de l'écran
        const containerWidth = this.container.offsetWidth;
        return Math.floor(containerWidth / this.itemWidth);
    }

    initEvents() {
        // Gestion des clics sur les boutons
        this.prevButton.addEventListener('click', () => this.slide('prev'));
        this.nextButton.addEventListener('click', () => this.slide('next'));

        // Mise à jour lors du redimensionnement de la fenêtre
        window.addEventListener('resize', () => {
            this.visibleItems = this.getVisibleItems();
            this.updateButtonsVisibility();
        });
    }

    slide(direction) {
        const currentScroll = this.container.scrollLeft;
        const scrollAmount = this.itemWidth * this.visibleItems;

        if (direction === 'next') {
            this.container.scrollTo({
                left: currentScroll + scrollAmount,
                behavior: 'smooth'
            });
        } else {
            this.container.scrollTo({
                left: currentScroll - scrollAmount,
                behavior: 'smooth'
            });
        }

        // Mettre à jour la visibilité des boutons après le défilement
        setTimeout(() => this.updateButtonsVisibility(), 400);
    }

    updateButtonsVisibility() {
        const currentScroll = this.container.scrollLeft;
        const maxScroll = this.container.scrollWidth - this.container.clientWidth;

        // Afficher/masquer le bouton précédent
        this.prevButton.style.display = currentScroll > 0 ? 'block' : 'none';

        // Afficher/masquer le bouton suivant
        this.nextButton.style.display = currentScroll < maxScroll ? 'block' : 'none';
    }
}

// Initialisation des carrousels
function initCarousels() {
    const carousels = document.querySelectorAll('.movies-carousel');
    carousels.forEach(carousel => {
        new Carousel(carousel);
    });
}

// Exporter pour utilisation dans main.js
export { Carousel, initCarousels };