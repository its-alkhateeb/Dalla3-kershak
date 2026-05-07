let input = document.getElementById("inputimg");
let preview = document.getElementById("Recipeimg");

input.addEventListener("change", function () {

    if (input.files && input.files[0]) {

        const reader = new FileReader();

        reader.onload = function (e) {
            preview.src = e.target.result;
        };

        reader.readAsDataURL(input.files[0]);
    }
});