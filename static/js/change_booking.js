document.addEventListener('DOMContentLoaded', function () {
    // Função para atualizar os detalhes do quarto com base no quarto selecionado
    function updateRoomDetails() {
        // Obter o valor selecionado do menu suspenso
        var selectedRoomId = document.getElementById('room').value;

        // Obter os elementos de detalhes da sala
        var roomImage = document.getElementById('roomImage');
        var smallImage1 = document.getElementById('smallImage1');
        var smallImage2 = document.getElementById('smallImage2');
        var smallImage3 = document.getElementById('smallImage3');
        var descriptionR = document.getElementById('descriptionR');
        var priceNight = document.getElementById('priceNight');

        // Obter a opção selecionada
        var selectedOption = document.getElementById('room').options[document.getElementById('room').selectedIndex];

        // Atualizar os elementos de detalhes da sala com os valores dos atributos de dados da opção selecionada
        roomImage.src = selectedOption.getAttribute('data-image-url');
        smallImage1.src = selectedOption.getAttribute('data-small-image-1');
        smallImage2.src = selectedOption.getAttribute('data-small-image-2');
        smallImage3.src = selectedOption.getAttribute('data-small-image-3');
        descriptionR.textContent = selectedOption.getAttribute('data-description-room');
        priceNight.textContent = "Price per Night: " + selectedOption.getAttribute('data-price-night');
    }

    // Ouvinte de evento para detectar mudanças no menu suspenso
    document.getElementById('room').addEventListener('change', updateRoomDetails);

    // Atualizar os detalhes do quarto quando a página é carregada inicialmente
    updateRoomDetails();
});