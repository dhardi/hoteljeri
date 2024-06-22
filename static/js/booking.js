document.addEventListener('DOMContentLoaded', function() {
    // Get references to the room select dropdown, the room image element, and the small images container div
    var roomSelect = document.getElementById('room');
    var smallImagesContainerDiv = document.getElementById('smallImagesContainerDiv');
    var roomImage = document.getElementById('roomImage');
    var smallImage1 = document.getElementById('smallImage1');
    var smallImage2 = document.getElementById('smallImage2');
    var smallImage3 = document.getElementById('smallImage3');
    var descriptionRoom = document.getElementById('descriptionR');
    var priceNight = document.getElementById('priceNight');

    // Add event listener to the room select dropdown
    roomSelect.addEventListener('change', function() {
        // Get the selected option from the dropdown
        var selectedOption = roomSelect.options[roomSelect.selectedIndex];

        // Get the value of the data-image-url attribute from the selected option
        var imageUrl = selectedOption.getAttribute('data-image-url');
        var smallImageUrl1 = selectedOption.getAttribute('data-small-image-1');
        var smallImageUrl2 = selectedOption.getAttribute('data-small-image-2');
        var smallImageUrl3 = selectedOption.getAttribute('data-small-image-3');
        var description = selectedOption.getAttribute('description-room');
        var priceRoomNight = selectedOption.getAttribute('price-night');

        // Set the src attribute of the room image element to the selected image URL
        roomImage.src = imageUrl || selectedOption.getAttribute('data-placeholder-image');
        // Set the src attribute of the small image elements to the respective URLs
        smallImage1.src = smallImageUrl1;
        smallImage2.src = smallImageUrl2;
        smallImage3.src = smallImageUrl3;
        // Update the description of the room
        descriptionRoom.textContent = description;
        priceNight.textContent = priceRoomNight;

        if (roomSelect.value) {
            smallImagesContainerDiv.style.display = 'block';
        } else {
            smallImagesContainerDiv.style.display = 'none';
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    var roomSelect = document.getElementById('room');
    var smallImagesContainerDiv = document.getElementById('smallImagesContainerDiv');

    roomSelect.addEventListener('change', function() {
        if (roomSelect.value) {
            smallImagesContainerDiv.style.display = 'block';
        } else {
            smallImagesContainerDiv.style.display = 'none';
        }
    });

    if (!roomSelect.value) {
        smallImagesContainerDiv.style.display = 'none';
    }
});