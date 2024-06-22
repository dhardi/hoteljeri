document.addEventListener('DOMContentLoaded', function () {
    // update room details 
    function updateRoomDetails() {
        var selectedRoomId = document.getElementById('room').value;

        // get elements of the room
        var roomImage = document.getElementById('roomImage');
        var smallImage1 = document.getElementById('smallImage1');
        var smallImage2 = document.getElementById('smallImage2');
        var smallImage3 = document.getElementById('smallImage3');
        var descriptionR = document.getElementById('descriptionR');
        var priceNight = document.getElementById('priceNight');

        var selectedOption = document.getElementById('room').options[document.getElementById('room').selectedIndex];

        // update image with dropdown menu
        roomImage.src = selectedOption.getAttribute('data-image-url');
        smallImage1.src = selectedOption.getAttribute('data-small-image-1');
        smallImage2.src = selectedOption.getAttribute('data-small-image-2');
        smallImage3.src = selectedOption.getAttribute('data-small-image-3');
        descriptionR.textContent = selectedOption.getAttribute('data-description-room');
        priceNight.textContent = "Price per Night: " + selectedOption.getAttribute('data-price-night');
    }

    // check the update of dropdown menu
    document.getElementById('room').addEventListener('change', updateRoomDetails);

    // update the information 
    updateRoomDetails();
});