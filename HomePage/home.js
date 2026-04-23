const searchInput = document.getElementById("searchInput");
const searchBtn = document.getElementById("searchBtn");
const resultsBox = document.getElementById("searchResults");

searchInput.addEventListener("input", function () {
  const query = searchInput.value.toLowerCase();

  resultsBox.innerHTML = "";

  if (query === "") {
    return;
  }

 
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
  const query = searchInput.value.toLowerCase();

  for (let i = 0; i < recipes.length; i++) {
    let recipeName = recipes[i].name.toLowerCase();

    if (recipeName.includes(query)) {
      window.location.href = recipes[i].link;
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