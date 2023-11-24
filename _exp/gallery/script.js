document.addEventListener("DOMContentLoaded", function () {
    // Get all images and hide them
    const images = document.querySelectorAll('img');
    images.forEach(img => img.classList.remove('active'));

    // Randomly select an image
    const randomIndex = Math.floor(Math.random() * images.length);
    images[randomIndex].classList.add('active');
});

window.setTimeout( function() {
  window.location.reload();
}, 8000);