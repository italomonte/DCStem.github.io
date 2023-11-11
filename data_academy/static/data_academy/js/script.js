let currentSlide = 0;
const slides = document.querySelectorAll('.slide');

function showSlide(index) {
  slides.forEach((slide, i) => {
    if (i === index) {
      slide.style.display = 'inline-block';
    } else {
      slide.style.display = 'none';
    }
  });
}

function nextSlide() {
  currentSlide = (currentSlide + 1) % slides.length;
  console.log("Próximo Slide:", currentSlide);
  showSlide(currentSlide);
}

function previousSlide() {
  // Subtrai 1 do índice atual e adiciona o comprimento dos slides para evitar índices negativos
  currentSlide = (currentSlide - 1 + slides.length) % slides.length;
  console.log("Slide Anterior:", currentSlide);
  showSlide(currentSlide);
}

// Mostrar o primeiro slide ao carregar a página
showSlide(currentSlide);
