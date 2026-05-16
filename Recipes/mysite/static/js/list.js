document.addEventListener('DOMContentLoaded', function() {
    // ====== FAVORITES ======
    const favCheckboxes = document.querySelectorAll('.fav-checkbox');
    favCheckboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            const recipeId = this.getAttribute('data-id');
            fetch(`/recipes/${recipeId}/toggle-favorite/`)
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    if (!this.checked && window.location.pathname.includes('favourites')) {
                        const card = this.closest('.recipe-card');
                        card.style.transition = "all 0.4s ease";
                        card.style.opacity = "0";
                        card.style.transform = "scale(0.9)";
                        setTimeout(() => card.remove(), 400);
                    }
                }
            });
        });
    });

    // ====== CATEGORY FILTER ======
    function filterSelection(categoryName) {
        const cards = document.getElementsByClassName("recipe-card");
        for (let i = 0; i < cards.length; i++) {
            cards[i].style.display = "none";
            cards[i].classList.remove('show');
            const cardCategory = cards[i].getAttribute("data-category");
            if (categoryName === "all" || cardCategory === categoryName) {
                cards[i].style.display = "flex";
                cards[i].classList.add('show');
            }
        }
    }

    const radios = document.querySelectorAll(".cat-radio");
    radios.forEach(function(radio) {
        radio.addEventListener("change", function () {
            filterSelection(this.value);
        });
    });

    // Read URL category on load and pre-select
    const params = new URLSearchParams(window.location.search);
    const urlCat = params.get('category');
    let initialCat = "all";
    if (urlCat) {
        radios.forEach(r => {
            if (r.value === urlCat) {
                r.checked = true;
                initialCat = urlCat;
            }
        });
    }
    filterSelection(initialCat);
});