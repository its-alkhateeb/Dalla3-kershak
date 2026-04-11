function filterSelection(category) {
  var cards = document.getElementsByClassName("recipe-card");

  for (var i = 0; i < cards.length; i++) {
    
    cards[i].classList.remove("show");

    if (category === "all" || cards[i].classList.contains(category)) {
      cards[i].classList.add("show");
    }
  }
}

var radios = document.querySelectorAll(".cat-radio");

radios.forEach(function(radio) {
  radio.addEventListener("change", function() {
    filterSelection(this.value);
  });
});

filterSelection("all");