
document.addEventListener('DOMContentLoaded', function() {
    // Get references to the room select dropdown and the room image elements
    var roomSelect = document.getElementById('room');
    var roomImage = document.getElementById('roomImage');
    var smallImage1 = document.getElementById('smallImage1');
    var smallImage2 = document.getElementById('smallImage2');
    var smallImage3 = document.getElementById('smallImage3');
    var descriptionRoom = document.getElementById('descriptionR');
    var priceNight = document.getElementById('priceNight');
    
    console.log("this is room select== ",roomSelect)

    // Add event listener to the room select dropdown
    roomSelect.addEventListener('change', function() {
        // Get the selected option from the dropdown
        var selectedOption = roomSelect.options[roomSelect.selectedIndex];

        // Get the value of the data-image-url attribute from the selected option
        var imageUrl = selectedOption.getAttribute('data-image-url');
        // Get the value of the data-small-image-1 attribute from the selected option
        var smallImageUrl1 = selectedOption.getAttribute('data-small-image-1');
        // Get the value of the data-small-image-2 attribute from the selected option
        var smallImageUrl2 = selectedOption.getAttribute('data-small-image-2');
        // Get the value of the data-small-image-3 attribute from the selected option
        var smallImageUrl3 = selectedOption.getAttribute('data-small-image-3');
        // Get the description of the room
        var description = selectedOption.getAttribute('data-description-room');
        var priceRoomNight = selectedOption.getAttribute('data-price-night');

        // Set the src attribute of the room image element to the selected image URL
        roomImage.src = imageUrl || "";
        // Set the src attribute of the small image elements to the respective URLs
        smallImage1.src = smallImageUrl1 || "";
        smallImage2.src = smallImageUrl2 || "";
        smallImage3.src = smallImageUrl3 || "";
        // Update the description of the room
        descriptionRoom.textContent = description || "";
        // Update the price per night
        priceNight.textContent = `Price per night: $${priceRoomNight || 0}`;
    });

    // Trigger change event to load initial room data
    if (roomSelect.value) {
        var event = new Event('change');
        roomSelect.dispatchEvent(event);
    }

});

