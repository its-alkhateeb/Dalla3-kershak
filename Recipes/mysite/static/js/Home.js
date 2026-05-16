const searchInput = document.getElementById("searchInput");
const searchBtn = document.getElementById("searchBtn");
const resultsBox = document.getElementById("searchResults");

document.addEventListener("DOMContentLoaded", function () {
  if (!searchInput || !searchBtn || !resultsBox) return;

  // LIVE SEARCH dropdown
  searchInput.addEventListener("input", function () {
    const query = searchInput.value.toLowerCase().trim();
    resultsBox.innerHTML = "";

    if (!query) {
      resultsBox.classList.remove('has-results');
      return;
    }

    const matches = recipes.filter(r => r.name.toLowerCase().includes(query));

    if (matches.length === 0) {
      const item = document.createElement("div");
      item.textContent = "No matches — press Enter to search all recipes";
      item.classList.add("result-item");
      resultsBox.appendChild(item);
    } else {
      matches.forEach(recipe => {
        const item = document.createElement("div");
        item.textContent = recipe.name;
        item.classList.add("result-item");
        item.onclick = function () {
          window.location.href = `/recipes/?q=${encodeURIComponent(recipe.name)}`;
        };
        resultsBox.appendChild(item);
      });
    }
    resultsBox.classList.add('has-results');
  });

  // SEARCH BUTTON / ENTER → Recipes list with query
  function doSearch() {
    const query = searchInput.value.trim();
    if (query) {
      window.location.href = `/recipes/?q=${encodeURIComponent(query)}`;
    }
  }

  searchBtn.addEventListener("click", doSearch);
  searchInput.addEventListener("keydown", function (e) {
    if (e.key === "Enter") doSearch();
  });

  // Click outside to close
  document.addEventListener("click", function (e) {
    if (!searchInput.contains(e.target) && !resultsBox.contains(e.target)) {
      resultsBox.innerHTML = "";
      resultsBox.classList.remove('has-results');
    }
  });
});

function goToCategory(category) {
  window.location.href = `/recipes/?category=${encodeURIComponent(category)}`;
}


const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.15 });