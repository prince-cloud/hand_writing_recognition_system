function readURL(input, destination) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            destination.innerText = "";
            let img = document.createElement("img");
            img.src = e.target.result;
            img.classList.add("img-default");
            img.style.height = "100%";
            destination.appendChild(img);
        }

        reader.readAsDataURL(input.files[0]); // convert to base64 string
    }
}

$(document).ready(function () {
    document.getElementsByClassName("image-form-section").forEach(item => {
        item.querySelector("input").addEventListener("change", (e) => {
            readURL(e.target, item.querySelector(".img-display"))
        });
    });

});