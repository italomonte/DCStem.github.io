
let currentSlide = 0;
    const slides = document.querySelectorAll('.slide');
    const buttonPrevious = document.getElementById('previousSlideButton')
    const buttonNext = document.getElementById('nextSlideButton')
    const buttonBackMenur = document.getElementById('BackMenuButtonr')
    const buttonBackMenul = document.getElementById('BackMenuButtonl')
    
    const slideLength = slides.length 

    buttonBackMenur.style.display = 'none';
    buttonBackMenul.style.display = 'none';

    function showSlide(index) {
        slides.forEach((slide, i) => {
            if (i === index ) {
                slide.style.display = 'inline-block';
                buttonBackMenur.style.display = 'none'
                buttonBackMenul.style.display = 'none'
                buttonPrevious.style.display = 'inline-block'
                buttonNext.style.display = 'inline-block'
                slide.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
            else if (i === index) {
                slide.style.display = 'inline-block';
                buttonBackMenur.style.display = 'none'
                buttonBackMenul.style.display = 'none'
                buttonPrevious.style.display = 'inline-block'
                buttonNext.style.display = 'inline-block'
                slide.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
            else if (index >= slides.length){
                buttonPrevious.style.display = 'inline-block'
                buttonNext.style.display = 'none'
                buttonBackMenur.style.display = 'inline-block';
            }
            else if (index < 0){
                buttonPrevious.style.display = 'none'
                buttonNext.style.display = 'none'
                buttonBackMenul.style.display = 'inline-block';
                buttonNext.style.display = 'inline-block'
            }
            else {
                slide.style.display = 'none';
            }
        });
    }
    
    function nextSlide() {
        currentSlide = (currentSlide + 1) ;

        showSlide(currentSlide);
        console.log("foi, slide: ", currentSlide, slides.length);
    }
    
    function previousSlide() {
        currentSlide = (currentSlide - 1 ) ;
        showSlide(currentSlide);
        console.log("voltou, slide: ", currentSlide, slides.length);
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