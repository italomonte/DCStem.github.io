
let currentSlide = 0;
    const slides = document.querySelectorAll('.slide');

    function showSlide(index) {
        slides.forEach((slide, i) => {
            if (i === index) {
                slide.style.display = 'inline-block';
                slide.scrollIntoView({ behavior: 'smooth', block: 'start' });
            } else {
                slide.style.display = 'none';
            }
        });
    }
    
    function nextSlide() {
        currentSlide = (currentSlide + 1) % slides.length;

        showSlide(currentSlide);
        console.log("foi");
    }
    
    function previousSlide() {
        currentSlide = (currentSlide - 1 + slides.length) % slides.length;
        showSlide(currentSlide);
        console.log("voltou");
    }
    

    document.addEventListener('DOMContentLoaded', function () {
        showSlide(currentSlide);
        document.getElementById('nextSlideButton').addEventListener('click', nextSlide);
        document.getElementById('previousSlideButton').addEventListener('click', previousSlide);
        
        new DataTable('#example');
        var form = document.querySelector('form');
        var outputElement = document.getElementById('output');
        var editor = ace.edit('editora');
        outputElement.readOnly = true;


        form.addEventListener('submit', function (event) {
            event.preventDefault();

            var code = editor.getValue();
            var formData = new FormData(form);
            formData.append('code', code);

            outputElement.textContent = '';

            fetch(form.action, {
                method: 'POST',
                body: formData,
            })
                .then(response => response.json())
                .then(data => {

                    outputElement.textContent = data.output;

                })
                .catch(error => {
                    console.error('Erro:', error);
                    outputElement.textContent = 'Ocorreu um erro ao executar o código.';

                });
        });
    });