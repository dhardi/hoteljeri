# Automated tests 

This report documents the automated tests executed for the Django application. The tests are defined in two test case classes: `RoomBookingViewTest` and `BookingTestCase`.

## Test Cases and Their Purposes

### RoomBookingViewTest

This class contains tests related to the room booking view.

#### setUp
- **Purpose:** Initializes the test client and creates a test user. Sets the URL for bookings.

#### test_booking_page_not_authenticated
- **Purpose:** Ensures that the booking page displays a message prompting the user to sign in if they are not authenticated.
- **Test Steps:**
  1. Sends a GET request to the booking page URL.
  2. Checks the response for specific HTML content.

#### test_booking_page_authenticated
- **Purpose:** Ensures that the authenticated user can access the booking page without seeing the sign-in prompt.
- **Test Steps:**
  1. Logs in the test user.
  2. Sends a GET request to the booking page URL.
  3. Verifies the response content.

#### test_booking_page_with_form_errors
- **Purpose:** Ensures that form validation errors are displayed correctly when the booking form is submitted with empty fields.
- **Test Steps:**
  1. Logs in the test user.
  2. Sends a POST request with empty form data.
  3. Checks for the error message in the response.

### BookingTestCase

This class contains tests related to booking operations such as updating and deleting bookings.

#### setUp
- **Purpose:** Initializes the test client, creates a test user, logs in the user, and creates a test room.

#### test_update_booking
- **Purpose:** Tests updating an existing booking with a new end time.
- **Test Steps:**
  1. Creates a booking.
  2. Sends a POST request to update the booking.
  3. Verifies that the booking is updated correctly in the database.

#### test_delete_booking
- **Purpose:** Tests deleting an existing booking.
- **Test Steps:**
  1. Creates a booking.
  2. Sends a POST request to delete the booking.
  3. Verifies that the booking is removed from the database.

## Test Result
![Test result](https://github.com/dhardi/hoteljeri/blob/main/static/image/test_py_ok.PNG)

# Javascript Validator 

- **Bookings**

![Test result](https://github.com/dhardi/hoteljeri/blob/main/static/image/test_py_ok.PNG)

- **Change Bookings**

![Test result](https://github.com/dhardi/hoteljeri/blob/main/static/image/change_bookingsjs_validator.PNG)

#### Aplication Validation

[JSHint](https://jshint.com/)

# Python Validator 

- **Forms.py**

![Test result](https://github.com/dhardi/hoteljeri/blob/main/static/image/forms_validator.PNG)

- **Models.py**

![Test result](https://github.com/dhardi/hoteljeri/blob/main/static/image/models_validator.PNG)

- **test.py**

**It has whitespace because I had to broke the line to fit in standard pip8**

![Test result](https://github.com/dhardi/hoteljeri/blob/main/static/image/test_validador.PNG)

- **Urls.py**

**It has whitespace because I had to broke the line to fit in standard pip8**

![Test result](https://github.com/dhardi/hoteljeri/blob/main/static/image/url_validator.PNG)

- **Views.py**

![Test result](https://github.com/dhardi/hoteljeri/blob/main/static/image/views_validator.PNG)


#### Aplication Validation

[CI Python Linter](https://pep8ci.herokuapp.com/)
 
