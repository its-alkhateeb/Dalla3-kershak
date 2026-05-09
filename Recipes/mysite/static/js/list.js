document.addEventListener('DOMContentLoaded', function() {

    // ==========================================
    // JOB 1: THE FAVORITES BUTTON (Talking to Database)
    // ==========================================

    // Find all the hidden checkboxes inside the heart buttons
    const favCheckboxes = document.querySelectorAll('.fav-checkbox');

    favCheckboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            const recipeId = this.getAttribute('data-id');

            fetch(`/recipes/${recipeId}/toggle-favorite/`)
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // If we are on the Favorites page and we uncheck the heart, hide the card!
                    if (!this.checked && window.location.pathname.includes('favourites')) {
                        const card = this.closest('.recipe-card');
                        card.style.transition = "opacity 0.3s ease";
                        card.style.opacity = "0";
                        setTimeout(() => card.remove(), 300);
                    }
                 }
            });
        });
    });


    // ==========================================
    // JOB 2: THE CATEGORY FILTER (Organizing the page)
    // ==========================================

    function filterSelection(categoryName) {
        // Grab all the recipe cards on the page
        const cards = document.getElementsByClassName("recipe-card");

        for (let i = 0; i < cards.length; i++) {
            // First, hide the card entirely
            cards[i].style.display = "none";

            // Look at the hidden data-category we put in the HTML
            const cardCategory = cards[i].getAttribute("data-category");

            // If we selected "all", OR if the button matches the card's category, show it!
            if (categoryName === "all" || cardCategory === categoryName) {
                cards[i].style.display = "flex";
            }
        }
    }

    // Find all the radio buttons
    const radios = document.querySelectorAll(".cat-radio");

    radios.forEach(function(radio) {
        // When a user clicks a radio button...
        radio.addEventListener("change", function () {
            // Run the filter function using the button's value!
            filterSelection(this.value);
        });
    });

    // When the page first loads, run the filter for "all" so nothing is hidden by mistake
    filterSelection("all");

});