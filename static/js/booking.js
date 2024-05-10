document.addEventListener('DOMContentLoaded', function() {
    // Get references to the room select dropdown and the room image element
    var roomSelect = document.getElementById('room');
    var roomImage = document.getElementById('roomImage');

    // Add event listener to the room select dropdown
    roomSelect.addEventListener('change', function() {
        // Get the selected option from the dropdown
        var selectedOption = roomSelect.options[roomSelect.selectedIndex];

        // Get the value of the data-image-url attribute from the selected option
        var imageUrl = selectedOption.getAttribute('data-image-url');

        // Set the src attribute of the room image element to the selected image URL
        roomImage.src = imageUrl;
    });
});