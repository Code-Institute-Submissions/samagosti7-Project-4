# CSSNN Technology News Site

## Introduction
For my fourth milestone project, I chose to build a reddit style news site, as recommended by the portfolio preparation module and using the "I think therefore I blog" module as a basic skeleton. 

This project includes the CRUD (create, read, update, delete) functionality--the user can create original content, read the content of others, and update/delete their own content on the site.  

A live website can be found [here](deployed heroku link).

![website preview](post_list preview picture)

# Table of Contents

-   [1. UX](#ux)
    -   [1.1. Strategy](#strategy)
        -   [Project Goals](#project-goals)
            -   [User Goals:](#user-goals)
            -   [User Expectations:](#user-expectations)
            -   [Trends of Modern Websites](#trends-of-modern-websites)
            -   [Strategy Table](#strategy-table)
    -   [1.2. Structure](#structure)
    -   [1.3. Skeleton](#skeleton)
-   [2. Features](#features)
-   [3. Technologies Used](#technologies-used)
-   [4. Testing](#testing)
-   [5. Development Cycle](#development-cycle)
-   [6. Deployment](#deployment)
-   [7. End Product](#end-product)
-   [8. Bugs](#bugs)
-   [9. Credits](#credits)

<a name="ux"></a>

# 1. UX

[Go to the top](#table-of-contents)

I have been a longtime user of reddit, and immediately upon seeing the "reddit style news site" suggestion I was interested in how creating such a thing could be done.  While theoretically the site I have made could be used to post about any topic, I chose to narrow it down to being code specific, as would be more realistic for a new site. The name "CSSNN" follows, a play on words for the emergence of a new news network dedicated to programming spefically. 

<a name="strategy"></a>

## 1.1. Strategy

[Go to the top](#table-of-contents)

### Project Goals
The overarching goal of the site is to give users the ability to create original posts and upload them to the site, thereby creating a collaborative space in which to view and contribute to news in the tech landscape.  

### User Stories:
##### All Site User:
- As a site user, I want to be able to go to the main site and read a welcome message orienting me around the site. 
- As an site user, I want to be able to view an ordered list of existing posts. 
- As an site user, I want to be able to click on a specific post to read that post in its entirety. 
- As an site user, I want to be able to view existing comments so I can view the conversation about a speficic post. 
- As an unregistered user, I want to be able to register an account with the site. 
##### Registered User:
- As a registered user who isn't signed in, I want to be able to sign in. 
- As a registered user who is signed in, I want to be able to sign out. 
- As a registered user, I want to be able to create my own news post and upload it to the site. 
- As a registered user, I want to be able to add a comment and submit it to contribute to the discussion of a particular post.  
- As a registered user, I want to be able to delete posts I have created. 
- As a registered user, I want to be able to edit posts I have published. 
- As a registered user, I want to be able to delete comments I have made. 



### User Expectations:
Main expectations

-   Specific expectations

### Project Management
Github projects board

![user_story_board](story board pic)

### Strategy Table
examine if this is necessary
Opportunity/Problem/Feature| Importance| Viability/Feasibility
------------ | -------------------------|---------
Display a food Menu | 5 | 5
Account signup | 5 | 5
User profile | 5 | 5
Responsive design | 5 | 5
Contact form | 4 | 5
Ability to create a booking | 5 | 4
Ability to update a booking | 5 | 4
Ability to cancel a booking | 3 | 4
Multiple table occupancies | 4 | 1
Avoid double bookings | 4 | 1

Total | 45 | 39

## Scope
Following agile principles, the deployed initial version offers the core of the base functionality the site can provide.  However, 

### Current Functionality
- Current Functionality

### Phase 2
- Possible future functionality

<a name="structure"></a>

## 1.2. Structure

[Go to the top](#table-of-contents)

Site is responsive

- Responsive on all device sizes
- Easy navigation through labelled buttons
- Footer at the bottom of the index page that links to the social media website.
- All elements will be consistent including font size, font family, colour scheme.

### Database Model
check if this is necessary
Planned database structure:
![database_model](planned model pic)

Final database structure:

```python
class Booking(models.Model):
    booking_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_bookings")
    booking_date = models.DateField(auto_now=False)
    booking_time = models.TimeField(auto_now=False)
    booking_comments = models.TextField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    guest_count = models.IntegerField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-booking_date']


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return str(self.user)
```

<a name="skeleton"></a>

## 1.3. Skeleton

[Go to the top](#table-of-contents)

### Wire-frames

Home/Landing Page Desktop:
![home_page_desktop](documentation_assets/wireframes/home_desktop.png)

Menu Page Desktop:
![menu_page_desktop](documentation_assets/wireframes/menu_desktop.png)

Register Page Desktop:
![register_page_desktop](documentation_assets/wireframes/register_desktop.png)

Login Page Desktop:
![login_page_desktop](documentation_assets/wireframes/login_desktop.png)

User Logged In Desktop:
![user_logged_in_desktop](documentation_assets/wireframes/user_logged_in_desktop.png)

Online Booking Page Desktop:
![online_booking_page_desktop](documentation_assets/wireframes/online_booking_desktop.png)

Contact Page Desktop:
![contact_page_desktop](documentation_assets/wireframes/contact_desktop.png)

Edit Profile Page Desktop:
![edit_profile_page_desktop](documentation_assets/wireframes/edit_profile_desktop.png)

Manage Booking Page Desktop:
![manage_booking_page_desktop](documentation_assets/wireframes/manage_booking_desktop.png)

From left to right home > navigation bar > menu mobile:
![home_navbar_menu_mobile](documentation_assets/wireframes/home_navbar_menu_mobile.png)

From left to right online bookings > contact form part 1 > contact form part 2 mobile:
![online-booking_contact-1_contact_2_mobile](documentation_assets/wireframes/online-booking_contact-1_contact-2.png)

From left to right edit profile > manage bookings mobile:
![edit-profile_manage-bookings_mobile](documentation_assets/wireframes/edit-profile_manage-bookings.png)

From left to right resgister > navigation bar when user is logged in mobile:
![register_login_logged-in-navbar_mobile](documentation_assets/wireframes/register_login_logged-in-navbar.png)

# 2. Features

[Go to the top](#table-of-contents)

### All Pages
- The navigation bar is placed at the top of all pages. The navigation bar is dynamic in that meaning depending on if the user is logged in or not the options will change.
- If the user is not logged in the navigation bar will look like this:
![user_not_logged_in](documentation_assets/images/navbar_not_logged_in.png)
- If the user is logged in the navigation bar will look like this:
![user_logged_in](documentation_assets/images/navbar_logged_in.png)
- The footer is placed at the bottom of each page with social media icons. When hovering over them it creates a zoom effect giving the user more of an experience. These icons will open the links in a new tab.

- The restaurant logo is also placed at the top of all pages. Clicking on it will also direct the user to the home page.
- Animated background, to give more of a user experience instead of a plain static background.

### Register Page
- A simple signup form that requires the user to enter a unique email address and a password. The password must be entered again for confirmation, this must match the already entered password above.
- A message to prompt the user that if an account is already been created they can click the sign-in hyperlink to be redirected to the sign-in page.
- If the user enters an email address that has already been registered, the user is prompted by an error message.
![email_validation_error](documentation_assets/images/signup_email_validation.png)
- If the user enters a password that is not secure, the user will be prompted by a message.
![password_too_common](documentation_assets/images/password_too_common.png)
- If the user enters both passwords that do not match, the user is prompted by a message.
![signup_email_validation](documentation_assets/images/signup_email_validation.png)
- Once the user has successfully signed up, this will automatically log in and direct the user to the create profile page.

### Login Page
- A login form that requires the user to enter their email address and password that they used when signing up to the site.
- A message to prompt the user that if an account has not been created they can click the signup hyperlink to be redirected to the signup page.
- If the user enters in the wrong credentials, a message is displayed to the user.
![signup_email_validation](documentation_assets/images/login_validation.png)

### Logout Page
- When clicking logout from the navigation bar, the user is redirected to a sign-out page to confirm their action.

### Landing Page
- A simple but elegant banner to give the user a sense of the restaurant.
- A book now button that directs the user to create a booking page. If the user has not logged in it will prompt the user to register or log in first.
- A short introduction to describe the restaurant.


### Make Post Page
- 
![booking_time_error](documentation_assets/images/booking_time_error.png)

### Edit Post Page
- 

### Delete Post
- 

<a name="technologies-used"></a>

## 3. Technologies Used

[Go to the top](#table-of-contents)

-   [HTML5](https://en.wikipedia.org/wiki/HTML)
    -   The project uses HyperText Markup Language.
-   [CSS3](https://en.wikipedia.org/wiki/CSS)
    -   The project uses Cascading Style Sheets.
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    -   The project uses JavaScript.
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    -   The project uses Python.
-   [Boostrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
    -   The project uses Bootstrap 5.
-   [PostgreSQL](https://www.postgresql.org/)
    -   The project uses PostgreSQL as a database.
-   [Gitpod](https://www.gitpod.io/)
    -   The project uses Gitpod.
-   [Chrome](https://www.google.com/intl/en_uk/chrome/)
    -   The project uses Chrome to debug and test the source code using HTML5.
-   [Balsamiq](https://balsamiq.com/)
    -   Balsamiq was used to create the wireframes during the design process.
-   [GitHub](https://github.com/)
    -   GitHub was used to store the project's code after being pushed from Git.
- Heroku
    - Heroku was used

<a name="testing"></a>

# 4. Testing

[Go to the top](#table-of-contents)

### Chrome Developer Tools
Used Chrome dev tools to test styling and responsivity.

### W3C Validator Tools
#### HTML:
I used [W3C Markup](https://validator.w3.org/#validate_by_input+with_options) to check for any html errors.

I had an error on the following templates:
![base.html_error](error pics)

I fixed them like this:
![base.html_fix](fix pics)


#### CSS:
I used [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) to check for any errors in my CSS stylesheet.

I had no errors in my CSS file:
![css_validation](documentation_assets/images/css_validation.png)

### JavaScript:
I used [JS Hint](https://jshint.com/) to check for any errors within my JavaScript script tags. 

I had no errors in my JavaScript files:
![javascript_validation](documentation_assets/images/javascript_validation.png)

### Python:
I used [PEP8 online](http://pep8online.com/) to check for any errors in my Python files. 

 errors:
![urls_errors](error pics)

Fixed:
![urls_fixed_errors](fixed pics)

There were also "line too long" errors within my env.os file but I have chosen to ignore these as any attempts to edit them blew up the entire site.


## Manual Testing
I have tested my site on Safari and google chrome, which are the mediums available to me at this time. 

Manual testing results are detailed below. 

### Navigation Bar

All Pages:
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Home page | When clicking the "home" link in the navigation bar, the browser redirects me to the home page. | PASS
Logo | When clicking the logo in the navigation bar, the browser redirects me to the home page. | PASS
View Posts page | When clicking the "View Posts" link in the navigation bar, the browser redirects me to the post list page. | PASS
Create a Post page | If signed in, when clicking the "Create a Post" link in the navigation bar, the browser redirects me to the post creation page. | PASS
Register page | If not signed in, when clicking the "register" button in the navigation bar, the browser redirects me to the registration page. | PASS
Login page | When clicking the "login" link in the navigation bar, the browser redirects me to the login page. | PASS
Logout page | When clicking the "logout" link in the navigation bar, the browser redirects me to the logout page. | PASS
Text | Checked that all fonts and colours used are consistent. | PASS
Authorization | Checked that users only get the create post option when signed in, and only get the register option when not signed in. Also checked that they only get the logout option when logged in, and the login option when logged out. | Pass

### Footer
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Facebook | When clicking the Facebook icon, a new tab opens and redirects to the Facebook website. | PASS
Twitter | When clicking the Twitter icon, a new tab opens and redirects to the Twitter website. | PASS
Instagram | When clicking the Instagram icon, a new tab opens and redirects to the Instagram website. | PASS
Youtube | When clicking the Youtube icon, a new tab opens and redirects to the Youtube website. | PASS
LinkedIn | When clicking the LinkedIn icon, a new tab opens and redirects to the LinkedIn website. | PASS

### Landing page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS

![index_google_lighthouse](documentation_assets/images/index_google_lighthouse.png)

### Menu page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Book now button | When clicking the book now button on the page, the browser redirects to the booking page. | PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS

![menu_google_lighthouse](documentation_assets/images/menu_google_lighthouse.png)

### Contact page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Book now button | When clicking the book now button on the page, the browser redirects to the booking page. | PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS
Contact Form | Checked the form submits only when all fields are filled out. | PASS

![contact_google_lighthouse](documentation_assets/images/contact_google_lighthouse.png)

### Booking page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Book now button | When clicking the book now button on the page, the browser redirects to the booking page. | PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS
Booking Form | Checked the form submits only when all required fields are filled out. | PASS
If not signed in | Checked to see if the user has not signed in the booking form should not show and a message displays prompting the user to signup/sign-in first. | PASS

![booking_google_lighthouse](documentation_assets/images/booking_google_lighthouse.png)

### Edit booking page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS
Edit Booking Form | Checked the form submits only when all required fields are filled out. | PASS
Form validation | Checked that the telephone number input only allows number input and not any text | PASS

![edit_booking_google_lighthouse](documentation_assets/images/edit_booking_google_lighthouse.png)

### Manage booking page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS
Edit booking button | Checked that the button redirects to the edit booking page with the correct booking instance. | PASS
Cancel booking button | Checked that the button redirects to the cancel booking page with the correct booking instance. | PASS

![manage_booking_google_lighthouse](documentation_assets/images/manage_booking_google_lighthouse.png)

### Create profile page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS
Create profile form | Checked the form submits only when all required fields are filled out. | PASS
If the profile has not been created | Checked to see if the user has created a profile, if not it will redirect the user to the create profile page | PASS
Form validation | Checked that the telephone number input only allows number input and not any text | PASS

![create_profile_validation](documentation_assets/images/create_profile_input_validation.png)
![create_profile_google_lighthouse](documentation_assets/images/create_profile_google_lighthouse.png)


### Edit profile page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS
Edit profile form | Checked the form submits only when all required fields are filled out. | PASS
Form validation | Checked that the telephone number input only allows number input and not any text | PASS
If the profile has not been created | Checked to see if the user has created a profile, if not it will redirect the user to the create profile page | PASS

![edit_profile_google_lighthouse](documentation_assets/images/edit_profile_google_lighthouse.png)

### Register page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS
Register form | Checked the form submits only when all required fields are filled out. | PASS
Sign in link | Checked the sign-in link redirects to the sign-in page. | PASS

![signup_google_lighthouse](documentation_assets/images/sign_up_google_lighthouse.png)

### Sign in page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS
Sign in form | Checked the form submits only when all required fields are filled out. | PASS
Signup link | Checked the signup link redirects to the signup page. | PASS

![sign_in_google_lighthouse](documentation_assets/images/sign_in_google_lighthouse.png)

<a name="development-cycle"></a>

# 5. Development Cycle

[Go to the top](#table-of-contents)

## Project Checklist
- Install Django and the supporting libraries
    -  Install Django and Gunicorn. Gunicorn is the server I am using to run Django on Heroku.
    - Install support libraries including psycopg2, this is used to connect the PostgreSQL database
    - Install Cloudinary libraries, this is a host provider service that stores images
    - Create the requirements.txt file. This includes the project's dependencies allowing us to run the project in Heroku.

- Create a new, blank Django Project
    - Create a new project
    - Create the app
    - Add restaurant_booking to the installed apps in settings.py
    - Migrate all new changes to the database
    - Run the server to test

- Setup project to use Cloudinary and PostgreSQL
    - Create new Heroku app
        - Sign into Heroku
        - Select New
        - Select create new app
        - Enter a relevant app name
        - Select appropriate region
        - Select the create app button

    - Attach PostgreSQL database
        - In Heroku go to resources
        - Search for Postgres in the add-ons box
        - Select Heroku Postgres
        - Submit order form

    - Prepare the environment and settings.py file
        - Create env.py file
        - Add DATABASE_URL with the Postgres URL from Heroku
        - Add SECRET_KEY with a randomly generated key
        - Add SECRET_KEY and generated key to the config vars in Heroku
        - Add if statement to settings.py to prevent the production server from erroring
        - Replace insecure key with the environment variable for the SECRET_KEY
        - Add Heroku database as the back end
        - Migrate changes to new database

    - Get static media files stored on Cloudinary
        - Create a Cloudinary account
        - From the dashboard, copy the API Environment variable
        - In the settings.py file create a new environment variable for CLOUDINARY_URL
        - Add the CLOUDINARY_URL variable to Heroku
        - Add a temporary config var for DISABLE_COLLECTSTATIC
        - In settings.py add Cloudinary as an installed app
        - Add static and media file variables
        - Add templates directory
        - Change DIR's key to point to TEMPALTES_DIR
        - Add Heroku hostname to allowed hosts
        - Create directories for media, static and templates in the project workspace
        - Create a Procfile

- Deploy new empty project to Heroku
![initial_heroku_deployment](documentation_assets/images/initial_deployment_successful.png)

<a name="deployment"></a>

# 6. Deployment

[Go to the top](#table-of-contents)

I used the terminal to deploy my project locally. To do this I had to:
1. Create a repository on GitHub.
2. Clone the repository on your chosen source code editor (GitPod in my case) using the clone link.
3. Open the terminal within GitPod
4. Enter "python3 manage.py runserver into the terminal.
5. Go to local host address on my web browser.
6. All locally saved changes will show up here.

For the final deployment to Heroku, I had to:
1. Uncomment the PostgreSQL databse from my settings.py file.
2. Set debug = False in my settings.py file.
3. Commit and push all files to GitHub
3. In Heroku, remove the DISABLE_COLLECTSTATIC config var.
4. In the deploy tab, go to the manual deploy sections and click deploy branch.

I had an issue with the deployed site and the CSS was not showing on my screen.
This was rectified by restarting all dynos in Heroku.

<a name="end-product"></a>

# 7. End Product

[Go to the top](#table-of-contents)

Home Page:
![home_page_desktop_preview](documentation_assets/images/homepage_desktop_preview.png)

![home_page_mobile_preview](documentation_assets/images/homepage_mobile_preview.png)

Menu Page:
![menu_desktop_preview](documentation_assets/images/menu_desktop_preview.png)

![menu_mobile_preview](documentation_assets/images/menu_mobile_preview.png)

Contact Page:
![contact_desktop_preview](documentation_assets/images/contact_deskop_preview.png)

![contact_mobile_preview](documentation_assets/images/contact_mobile_preview.png)

Book Now Page:
![booking_desktop_preview](documentation_assets/images/booking_desktop_preview.png)

![booking_mobile_preview](documentation_assets/images/booking_mobile_preview.png)

Manage Booking Page:
![manage_booking_desktop_preview](documentation_assets/images/manage_booking_desktop_preview.png)

![manage_booking_mobile_preview](documentation_assets/images/manage_booking_mobile_preview.png)

Edit Booking Page:
![edit_booking_desktop_preview](documentation_assets/images/edit_booking_desktop_preview.png)

![edit_booking_mobile_preview](documentation_assets/images/edit_booking_mobile_preview.png)

Edit Profile Page:
![edit_profile_desktop_preview](documentation_assets/images/edit_profile_desktop_preview.png)

![edit_profile_mobile_preview](documentation_assets/images/edit_profile_mobile_preview.png)

Register Page:
![register_desktop_preview](documentation_assets/images/register_desktop_preview.png)

![register_mobile_preview](documentation_assets/images/register_mobile_preview.png)

Sign In Page:
![sign_in_desktop_preview](documentation_assets/images/sign_in_desktop_preview.png)

![sign_in_mobile_preview](documentation_assets/images/sign_in_mobile_preview.png)

Sign Out Page:
![sign_out_desktop_preview](documentation_assets/images/sign_out_desktop_preview.png)

![sign_out_mobile_preview](documentation_assets/images/sign_out_mobile_preview.png)

<a name="bugs"></a>

# 8. Bugs

[Go to the top](#table-of-contents)

- There is a * next to the labels in the form submissions for creating a new post and editing a post.  That is not designed and I couldn't figure out a way to remove it. 

- 

<a name="credits"></a>

# 9. Credits

[Go to the top](#table-of-contents)

### Code
-   The navigation bar came from [Bootstrap](https://getbootstrap.com/docs/5.0/components/navbar).

- 

### Content
-   