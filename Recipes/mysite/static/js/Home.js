const searchInput = document.getElementById("searchInput");
const searchBtn = document.getElementById("searchBtn");
const resultsBox = document.getElementById("searchResults");

document.addEventListener("DOMContentLoaded", function () {

  const searchInput = document.getElementById("searchInput");
  const searchBtn = document.getElementById("searchBtn");
  const resultsBox = document.getElementById("searchResults");

  if (!searchInput || !searchBtn || !resultsBox) return;

  // LIVE SEARCH
  searchInput.addEventListener("input", function () {

    const query = searchInput.value.toLowerCase().trim();

    resultsBox.innerHTML = "";

    if (query === "") return;

    recipes.forEach(recipe => {

      if (recipe.name.toLowerCase().includes(query)) {

        const item = document.createElement("div");

        item.textContent = recipe.name;

        item.classList.add("result-item");

        item.onclick = function () {

          searchInput.value = recipe.name;

          resultsBox.innerHTML = "";

        };

        resultsBox.appendChild(item);
      }
    });
  });

  // SEARCH BUTTON
  searchBtn.addEventListener("click", function () {

    const query = searchInput.value.toLowerCase().trim();

    const found = recipes.find(recipe =>
      recipe.name.toLowerCase().includes(query)
    );

    if (found) {
      window.location.href = `/recipes/${found.id}/`;
    } else {
      alert("Recipe not found!");
    }
  });

  // ENTER KEY
  searchInput.addEventListener("keydown", function (e) {

    if (e.key === "Enter") {
      searchBtn.click();
    }
  });

  // CLOSE RESULTS
  document.addEventListener("click", function (e) {

    if (!searchInput.contains(e.target) &&
        !resultsBox.contains(e.target)) {

      resultsBox.innerHTML = "";
    }
  });

});

function goToCategory(category) {

    window.location.href =
    `/recipes/?category=${encodeURIComponent(category)}`;
}