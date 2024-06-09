# Hotel Jeri 

![Responsive](https://www.openai.com/assets/images/openai-logo.svg)

## Design & Planning 

The design and planning of the "Hotel Jeri" web application focused on creating an intuitive and visually appealing user interface that enhances user experience. We implemented a responsive design using Bootstrap, ensuring accessibility across all devices. Google Fonts and Font Awesome icons were integrated to provide a modern and clean aesthetic. The navigation bar offers clear links to essential pages such as Home, Booking, About Jeri, and user-specific sections like My Bookings, Login, and Register, facilitating easy navigation. Secure authentication features, including registration and login, were prioritized to protect user data. The planning phase involved detailed wireframing and prototyping, incorporating stakeholder feedback to refine the design and ensure a user-centric approach.

### Introduction 

Welcome to "Hotel Jeri," a sophisticated web application designed to streamline the booking process and enhance the user experience for our valued guests. Our platform offers a seamless interface for exploring and booking accommodations at Hotel Jeri, with detailed information about our services and the beautiful surroundings of Jeri. Utilizing modern web technologies such as Bootstrap for responsiveness, Google Fonts and Font Awesome for visual appeal, and Django for dynamic content management, we ensure a smooth and enjoyable online experience. With secure authentication features, users can easily register, log in, and manage their bookings, all within a user-friendly and visually appealing environment. Whether you're planning your next vacation or managing your reservations, "Hotel Jeri" is here to provide a convenient and delightful experience.

### Project Overview 

**Hotel Jeri** is a comprehensive web application designed to simplify the hotel booking experience for users while providing a robust platform for managing reservations. The project leverages modern web technologies and follows best practices in design and user experience to deliver a seamless and engaging interface. Here are the key features and components of the project:

- **Responsive Design**: Built with Bootstrap, the application is fully responsive, ensuring a smooth user experience across all devices, including desktops, tablets, and smartphones.

- **User-Friendly Interface**: The clean and intuitive interface uses Google Fonts and Font Awesome icons to enhance readability and navigation. The design prioritizes ease of use, allowing users to find information and make bookings effortlessly.

- **Secure Authentication**: Users can register, log in, and log out securely, with their personal information and booking details protected. The platform supports user-specific features such as viewing and managing personal bookings.

- **Dynamic Content Management**: Using Django templates, the application supports dynamic content updates, making it easy to maintain and update information about hotel services, rooms, and local attractions.

- **Navigation and Accessibility**: The site includes a clear and accessible navigation bar with links to essential pages like Home, Booking, About Jeri, My Bookings, Login, and Register. This ensures users can easily access the information they need.

- **Integration with External Resources**: The project incorporates external resources such as Google Fonts for typography and Font Awesome for icons, as well as leveraging CDN-hosted Bootstrap and JavaScript libraries for enhanced performance.

By focusing on these aspects, **Hotel Jeri** aims to provide a top-notch online booking experience, combining functionality with an appealing design to meet the needs of modern travelers.

### Goals of Hotel Jeri Project

The Hotel Jeri project aims to redefine the hotel booking experience by offering a user-friendly web application that prioritizes simplicity, security, and performance. Targeted towards modern travelers, its goals include:

1. **Simplified Booking**: Streamlining the booking process for ease and efficiency.
2. **Enhanced User Experience**: Providing an intuitive interface for seamless navigation and interaction.
3. **Secure Data Handling**: Ensuring the protection of user information and booking details.
4. **Dynamic Content Management**: Offering up-to-date information on hotel services and local attractions.
5. **Accessibility and Integration**: Making the platform easily accessible and integrating external resources for enhanced functionality.
6. **Optimized Performance**: Delivering fast loading times and smooth interactions for a seamless user experience.

By achieving these objectives, Hotel Jeri aims to cater to the needs of its target audience, offering a top-notch online booking platform tailored to modern travelers.

## User Stories

Underconstruction 


## Wireframes 

### Desktop 

- Landing Page 

![Responsive](https://github.com/dhardi/hoteljeri/blob/main/static/image/landingpage.PNG)

- Booking

![Responsive](https://github.com/dhardi/hoteljeri/blob/main/static/image/booking.PNG)

- My Bookings

![Responsive](https://github.com/dhardi/hoteljeri/blob/main/static/image/mybookings.PNG)

- After Sign in 

![Responsive](https://github.com/dhardi/hoteljeri/blob/main/static/image/aftersignin.PNG)

- Registration

![Responsive](https://github.com/dhardi/hoteljeri/blob/main/static/image/registration.PNG)

- Sign in

![Responsive](https://github.com/dhardi/hoteljeri/blob/main/static/image/signin.PNG)



### Mobile Phone 

- Landing Page 

![Responsive](https://github.com/dhardi/hoteljeri/blob/main/static/image/landmobile.PNG)

- Booking

![Responsive](https://github.com/dhardi/hoteljeri/blob/main/static/image/mobilebook.PNG)

- My Bookings

![Responsive](https://github.com/dhardi/hoteljeri/blob/main/static/image/mobilemybooking.PNG)

- Registration

![Responsive](https://github.com/dhardi/hoteljeri/blob/main/static/image/mobileregis.PNG)

- Sign in

![Responsive](https://github.com/dhardi/hoteljeri/blob/main/static/image/mobilesignin.PNG)

## Agile Methodology

Underconstrutcion 


## Colour Scheme 

Main Blue (#0d6efd): Used for titles, primary buttons, and some highlighted elements.
Secondary Blue (#0b5ed7): Used to accentuate buttons on hover.
Darker Blue (#0056b3): Used for carousel arrow icons and other elements.
Light Gray (#f8f9fa): Used for background in some containers.
White (#ffffff): Used for the background of some elements like carousel slides.
Gray (#333): Used for main text.
Lighter Gray (#555): Used for secondary text.
Darker Gray (#ddd): Used for dividers and borders.

## DataBase Diagram 

![DataBase](https://github.com/dhardi/hoteljeri/blob/main/static/image/mobilesignin.PNG)

**User Table**:
- Fields: `id` (PK), ...
- Relationship: One user can make many bookings.

**Booking Table**:
- Fields: `id` (PK), `user_id` (FK), `room_id` (FK), `start_time`, `end_time`, `total_price`, `created_at`.
- Relationships: 
  - Belongs to one user (`user_id`).
  - Belongs to one room (`room_id`).

**Room Table**:
- Fields: `id` (PK), `name`, `capacity`, `image_url_main`, `description`, `price_per_night`, `small_image_url_1`, `small_image_url_2`, `small_image_url_3`.
- Relationship: One room can have many bookings.

**Review Table**:
- Fields: `id` (PK), `user_id` (FK), `room_id` (FK), `rating`, `comment`, `created_at`.
- Relationships: 
  - Belongs to one user (`user_id`).
  - Belongs to one room (`room_id`).