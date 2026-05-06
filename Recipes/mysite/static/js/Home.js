// recipes is injected from Django in home.html as:
// <script>const recipes = {{ recipes_json|safe }};</script>
// Each recipe object has: { name, id } — used for search & redirect

const searchInput = document.getElementById("searchInput");
const searchBtn = document.getElementById("searchBtn");
const resultsBox = document.getElementById("searchResults");

searchInput.addEventListener("input", function () {
  const query = searchInput.value.toLowerCase().trim();
  resultsBox.innerHTML = "";

  if (query === "") return;

  for (let i = 0; i < recipes.length; i++) {
    let recipeName = recipes[i].name.toLowerCase();

    if (recipeName.includes(query)) {
      const div = document.createElement("div");
      div.textContent = recipes[i].name;
      div.classList.add("result-item");

      div.onclick = function () {
        searchInput.value = recipes[i].name;
        resultsBox.innerHTML = "";
      };

      resultsBox.appendChild(div);
    }
  }
});

searchBtn.onclick = function () {
  const query = searchInput.value.toLowerCase().trim();

  for (let i = 0; i < recipes.length; i++) {
    let recipeName = recipes[i].name.toLowerCase();

    if (recipeName.includes(query)) {
      // Redirect to Django recipe detail URL using recipe id
      window.location.href = "/recipes/" + recipes[i].id + "/";
      return;
    }
  }

  alert("Recipe not found!");
};

searchInput.onkeydown = function (e) {
  if (e.key === "Enter") {
    searchBtn.click();
  }
};

// Close results box when clicking outside
document.addEventListener("click", function (e) {
  if (!searchInput.contains(e.target) && !resultsBox.contains(e.target)) {
    resultsBox.innerHTML = "";
  }
});
