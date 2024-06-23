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
![Test result](https://github.com/dhardi/hoteljeri/blob/main/docs/imgs/test_py_ok.PNG)

# Javascript Validator 

- **Bookings**

![Test result](https://github.com/dhardi/hoteljeri/blob/main/docs/imgs/bookings_validator.PNG)

- **Change Bookings**

![Test result](https://github.com/dhardi/hoteljeri/blob/main/docs/imgs/change_bookingsjs_validator.PNG)

#### Aplication Validation

[JSHint](https://jshint.com/)

# Python Validator 

- **Forms.py**

![Test result](https://github.com/dhardi/hoteljeri/blob/main/docs/imgs/forms_validator.PNG)

- **Models.py**

![Test result](https://github.com/dhardi/hoteljeri/blob/main/docs/imgs/models_validator.PNG)

- **test.py**

**It has whitespace because I had to broke the line to fit in standard pip8**

![Test result](https://github.com/dhardi/hoteljeri/blob/main/docs/imgs/test_validador.PNG)

- **Urls.py**

**It has whitespace because I had to broke the line to fit in standard pip8**

![Test result](https://github.com/dhardi/hoteljeri/blob/main/docs/imgs/url_validator.PNG)

- **Views.py**

![Test result](https://github.com/dhardi/hoteljeri/blob/main/docs/imgs/views_validator.PNG)


#### Aplication Validation

[CI Python Linter](https://pep8ci.herokuapp.com/)
 
# Lighthouse 

- **Home page**

![Test result](https://github.com/dhardi/hoteljeri/blob/main/docs/imgs/home_lighthouse.PNG)

- **Bookings**

![Test result](https://github.com/dhardi/hoteljeri/blob/main/docs/imgs/bookings_lighthouse.PNG)

- **About Jeri**

![Test result](https://github.com/dhardi/hoteljeri/blob/main/docs/imgs/about_lighthouse.PNG)

- **My Bookings**

![Test result](https://github.com/dhardi/hoteljeri/blob/main/docs/imgs/mybookings_lighthouse.PNG)

## Mobile 

- **Home page**

![Test result](https://github.com/dhardi/hoteljeri/blob/main/docs/imgs/home_mobile_lighthouse.PNG)

- **Bookings**

![Test result](https://github.com/dhardi/hoteljeri/blob/main/docs/imgs/booking_mobile.PNG)

- **About Jeri**

![Test result](https://github.com/dhardi/hoteljeri/blob/main/docs/imgs/about_mobile.PNG)

- **My Bookings**

![Test result](https://github.com/dhardi/hoteljeri/blob/main/docs/imgs/mybookings_mobile.PNG)

# Manual Testing Report for Hotel Jeri Website

As part of the development process for my academic project—a hotel booking website—I conducted comprehensive manual testing to ensure the site’s functionality and user experience were optimal. The testing was performed by my wife, who acted as a typical end-user to evaluate the website's behavior and performance under real-world conditions. The primary focus was to verify that all functionalities were working as intended and that the user interface was intuitive and user-friendly.

## Objectives of Manual Testing

### Validate Core Functionalities:
- Registration and creating a user account
- Booking a room
- Deleting a booking
- Modifying an existing booking
- Leaving a review

### Assess User Experience:
- Ease of navigation
- Clarity of information
- Overall satisfaction

## Testing Scenarios and Outcomes

### Registration and Creating a User Account:
**Scenario:** The user registers on the site by providing necessary information (e.g., name, email, password) and creates a user account.  
**Outcome:** The registration process was straightforward, with clear instructions and validation messages. The user successfully created an account and received a confirmation email.

### Booking a Room:
**Scenario:** The user selects a room, enters booking details, and completes the reservation.  
**Outcome:** The booking process was smooth. The confirmation message was clear, and the booking details were accurately reflected in the user’s account.

### Deleting a Booking:
**Scenario:** The user navigates to their bookings and deletes an existing reservation.  
**Outcome:** The deletion process was straightforward. The booking was successfully removed, and the user received an appropriate confirmation.

### Modifying an Existing Booking:
**Scenario:** The user edits the details of an existing reservation (e.g., changing dates or room type).  
**Outcome:** Modifications were processed correctly, and updated details were accurately displayed in the user’s account.

### Leaving a Review:
**Scenario:** The user submits a review for a recent stay, including a rating and comments.  
**Outcome:** The review submission was easy to complete, and the review appeared correctly on the hotel's page.

## User Experience Evaluation
- **Ease of Navigation:** The site was intuitive to navigate. The main sections (registration, booking, account management, reviews) were easily accessible from the homepage.
- **Clarity of Information:** Information on room types, pricing, and booking terms was clear and comprehensive. Users could make informed decisions without confusion.
- **Overall Satisfaction:** The tester was satisfied with the overall experience. The site performed well without errors or delays, providing a seamless user journey from registration to booking and review submission.

## Conclusion
The manual testing process conducted by my wife successfully verified that all key functionalities of the hotel booking website are operational and user-friendly. The feedback obtained has been invaluable in refining the user interface and ensuring a high-quality user experience. The site is now ready for launch, with confidence in its reliability and ease of use.


