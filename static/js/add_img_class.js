// static/js/add_img_class.js
// Картинки в постах будут принимать размер в зависимости от размера экрана

document.addEventListener("DOMContentLoaded", function () {
    var images = document.querySelectorAll("img");
    images.forEach(function (img) {
      img.classList.add("img-fluid");
    });
  });