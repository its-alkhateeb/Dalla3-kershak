// Filter recipes by category
// Cards use data-category="{{ recipe.category }}" from Django
// Category values match exactly what's in the DB: "Main Courses", "Appetizers", "Desserts"

function filterSelection(category) {
  var cards = document.getElementsByClassName("recipe-card");

  for (var i = 0; i < cards.length; i++) {
    cards[i].classList.remove("show");

    var cardCategory = cards[i].getAttribute("data-category");

    if (category === "all" || cardCategory === category) {
      cards[i].classList.add("show");
    }
  }
}

// Attach radio button listeners
var radios = document.querySelectorAll(".cat-radio");
radios.forEach(function (radio) {
  radio.addEventListener("change", function () {
    filterSelection(this.value);
  });
});

// Show all on page load
filterSelection("all");

// Search filter
var searchInput = document.getElementById("searchInput");
if (searchInput) {
  searchInput.addEventListener("input", function () {
    var query = this.value.toLowerCase().trim();
    var cards = document.getElementsByClassName("recipe-card");

    for (var i = 0; i < cards.length; i++) {
      var name = cards[i].querySelector(".recipe-name h2");
      if (name) {
        var nameText = name.textContent.toLowerCase();
        if (query === "" || nameText.includes(query)) {
          cards[i].classList.add("show");
        } else {
          cards[i].classList.remove("show");
        }
      }
    }
  });
}
