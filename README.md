# CSSNN Technology News Site

## Introduction
For my fourth milestone project, I chose to build a reddit style news site, as recommended by the portfolio preparation module and using the "I think therefore I blog" module as a basic skeleton. 

This project includes the CRUD (create, read, update, delete) functionality--the user can create original content, read the content of others, and update/delete their own content on the site.  

A live website can be found [here](https://sagos-project-4.herokuapp.com/).

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
-   [5. Deployment](#deployment)
-   [6. End Product](#end-product)
-   [7. Bugs](#bugs)
-   [8. Credits](#credits)

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
#### All Site Users:
- As a site user, I want to be able to go to the main site and read a welcome message orienting me around the site. 
- As an site user, I want to be able to view an ordered list of existing posts. 
- As an site user, I want to be able to click on a specific post to read that post in its entirety. 
- As an site user, I want to be able to view existing comments so I can view the conversation about a speficic post. 
- As an unregistered user, I want to be able to register an account with the site. 
#### Registered User:
- As a registered user who isn't signed in, I want to be able to sign in. 
- As a registered user who is signed in, I want to be able to sign out. 
- As a registered user, I want to be able to create my own news post and upload it to the site. 
- As a registered user, I want to be able to add a comment and submit it to contribute to the discussion of a particular post.  
- As a registered user, I want to be able to delete posts I have created. 
- As a registered user, I want to be able to edit posts I have published. 
- As a registered user, I want to be able to delete comments I have made. 
#### Frequent User
- As a frequent user, I want to be able to see a newly updated and ordered post list.  

### User Expectations:
The user should be able to navigate the site efficiently, without any bugs or styling choices that present visual confusion or inconvenience.  The site should also be completely responsive across all standard device sizes. 

### Project Management
I used GitHub projects and specifically the projects board to manage existing issues and user stories. When I was ready to work on a user story, I would move it to the in progress section from the todo section. When complete, I would move it to the done section. 

![user_story_board](story board pic)

### Strategy Table
Feature| Importance| Viability/Feasibility
------------ | -------------------------|---------
Display a Welcome Page | 5 | 5
Create a New Post | 5 | 5
Register an Account | 5 | 5
Responsive design | 5 | 5
Ability to edit a post | 5 | 5
Ability to delete a post | 5 | 5
Ability to create a comment | 3 | 4
Ability to delete a comment | 3 | 4
Ability to edit a comment | 3 | 2
View list of owned posts | 3 | 2
Search through existing posts | 2 | 2
Create social profile | 2 | 1
Filter post list order parameter | 1 | 2

The above strategy table acted as a guide for me, helping me see which pieces were most necessary and most feasible as opposed to less important or less implementable pieces. 

## Scope
Following agile principles, this deployed initial version offers all core of the base functionality the site can provide, and some additional pieces.  However, there are several features, some covered above, which could possibly be added to the site in the future to improve functionality. These are discussed later in the features section. Below is a short description of the current site functionality. 

### Current Functionality
- Display Welcome Page
- View Existing Post List and Comments
- Register an Account
- Create a New Post
- Add a New Comment to a Post
- Delete Existing Post (as author)
- Edit Existing Post (as author)
- Responsivity
- Admin control

<a name="structure"></a>

## 1.2. Structure

[Go to the top](#table-of-contents)

### Database Model
Database structure:
![database_model](planned model pic)

### Post Model
- title: Post title decided by user. 
- slug: Unique slug for url distinction.
- updated_on: Date and time set automatically upon edit. 
- content: Content input by user. 
- created_on: Date and time set automatically at creation.
- status: Whether or not the post is published. Defaults to published but can be set to non published by an admin.
- Likes: Calculated total of users who have liked the post. 

### Comment Model
- post: Post comment will be added to. 
- email: Email of commenting user. 
- body: Content of comment. 
- created_on: Date and time automatically set upon creation. 
- approved: Approval status of comment. Defaults to true but can be changed by admin.
- author:  Author of comment. 

<a name="skeleton"></a>

## 1.3. Skeleton

[Go to the top](#table-of-contents)

### Wire-frames
The following wireframes offered the initial skeletal idea, upon which the site was built further. 

Landing Page:
![home_page_desktop](landing page )

Post List:
![menu_page_desktop](post list)

Post Detail:
![register_page_desktop](documentation_assets/wireframes/register_desktop.png)

Create New Post:
![login_page_desktop](documentation_assets/wireframes/login_desktop.png)

Edit/Delete Post:
![user_logged_in_desktop](documentation_assets/wireframes/user_logged_in_desktop.png)

# 2. Features

[Go to the top](#table-of-contents)

### Base
- The navigation bar is placed at the top of all pages. The navigation bar is dynamic in that meaning depending on if the user is logged in or not the options will change.
- Authenticated User Navbar:
![user_logged_in](documentation_assets/images/navbar_not_logged_in.png)
- Unauthenticated User Navbar:
![user_notlogged_in](documentation_assets/images/navbar_logged_in.png)
- The footer is placed at the bottom of each page with social media icons. 
- The site logo is also placed at the top of all pages. Clicking on it will also direct the user to the home page.
- The top right of all pages indicates the users sigin status to them, and displays their username if logged in. 

### Register Page
- A simple signup form that requires the user to enter a unique email address and a password. The password must be entered again for confirmation, this must match the already entered password above.
- If the user enters information that already associated with an existing account, the user is prompted by an error message.
![username_duplicate_error](username error pic)
- If the user enters both passwords that do not match, the user is prompted by a message.
![password_match_error](username error pic)
- Once the user has successfully signed up, this will automatically log in and lead the user back to the main site.

### Login Page
- A login form that requires the user to enter their email address and password that they used when signing up to the site.
- A line informing the user that if an account has not been created they can click the signup hyperlink to be redirected to the signup page.
- If the user enters in the wrong credentials, a message is displayed to the user.
![signup_validation_error](signup error)

### Logout Page
- When clicking logout from the navigation bar, the user is redirected to a sign-out page to confirm their action.

### Landing Page
- A large welcome line
- A short and well legible blurb informing the user of the purpose of the site, and offering links to view posts/create a post if registered, or view posts/register if unregistered. 

### Post List Page
- All posts listed, one after the other, ordered by date created. Listed is author, time created, a small cover picture, and the title of the post, which is a link to the post detail view. 
- If so many posts that there needs to be pages, pagination happens automatically with scrolling capability. 
- Small heart displaying the number of likes for each post. 
- Small text bubble displaying the number of comments for each post. 

### Post Detail Page
- Title, author, and creation date of post listed in masthead next to masthead image. 
- Full content of post displayed under masthead. 
- Interactable heart displaying number of likes. Clicking the heart toggles like/unlike for the viewing user, if registered. 
- Small text bubble dispalying number of comments. 
- Edit/Delete post buttons displayed under content if user is author of post. 
- Back to Posts button dispalyed under post content for all users. 
- Comment section ordered by date created. 
- Comment form next to comment section, allowing a registered user to add a comment. 
- Delete button under a submitted comment if the user is the author. 
- Error message if comment form is submitted blank.
[image]pic of error message blank comment

### Make Post Page
- Card presenting form in which a registered user can create a new post.
- Title input section labeled "Title"
- Content input section labeled "Post Content"
- Submit button submitting new post
- Cancel button taking user back to post list
- Post creation fail if there is already a post with the same title. 
- Error message if either title or content field is left blank
[image]pic of empty field message

### Edit Post Page
- Card presenting form in which a registered user can edit their selected post.
- Title input section labeled "Title" with prefilled data of post to be edited
- Content input section labeled "Post Content" with prefilled data of post to be edited
- Submit button taking user back to post list. 
- Same error message as above if either title or content field is left blank

### Delete Post Page
- Large banner message confirming if user wants to delete post
- "Title" and "Created On" sections reminding user which post they have selected for deletion. 
- Yes and No buttons, taking user to updated post list page based on choice. 

### Delete Comment Page
- Large banner message confirming if user wants to delete comment. 
- Yes and No buttons, taking user to updated post detail page based on choice.

## Possible New Future Features
- Ability to edit a comment.
- Ability to view only owned posts. 
- Ability to search through existing posts. 
- Requirement of posts to have a unique title inside post form, rather than a post creation fail. 
- Creation of social profile. 
- Filtration of posts by different parameters. 
- Ability to create posts as drafts. 
- Ability to delete account, as a non admin. 

<a name="technologies-used"></a>

## 3. Technologies Used

[Go to the top](#table-of-contents)

-   [HTML5](https://en.wikipedia.org/wiki/HTML)
    -   The project used HyperText Markup Language.
-   [CSS3](https://en.wikipedia.org/wiki/CSS)
    -   The project used Cascading Style Sheets.
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    -   The project used JavaScript.
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    -   The project used Python.
-   [Boostrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
    -   The project used Bootstrap 5.
-   [PostgreSQL](https://www.postgresql.org/)
    -   The project used PostgreSQL as a database.
-   [Gitpod](https://www.gitpod.io/)
    -   The project used Gitpod and Gitpod projects.
-   [Chrome](https://www.google.com/intl/en_uk/chrome/)
    -   The project used Chrome to debug and test.
-   [Balsamiq](https://balsamiq.com/)
    -   The project used Balsamiq was used to create the wireframes.
-   [GitHub](https://github.com/)
    -   The project pushed all code through GitHub.
-   [Heroku](https://dashboard.heroku.com/)
    - Heroku was used to deploy the final product.
-   [Cloudinary](https://cloudinary.com/)
    - Cloudinary was used to store image assets for the project.

<a name="testing"></a>

# 4. Testing

[Go to the top](#table-of-contents)

### Chrome Developer Tools
Chrome developer tools were used to test styling and responsivity, across various device sizes. 

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
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
View Posts links | Check that clicking any of the four "view posts" links redirects the user to the post list page. | PASS
Make a Post links | Check that clicking any of the two "create a post" links redirect the user to the post creation page. | PASS
Register links | Check that clicking any of the two "register" links redirects the user to the registration page. | PASS

### Post List page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Metadata | Check if all accompanying metadata is being displayed for each post | PASS
Pagination | Check if site automatically paginates if necessary | PASS
Sign in | Check if sign in message displays on sign in | PASS

### Post Detail page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Metadata | Check if all accompanying metadata is being displayed for the post in question | PASS
Full Content | Check if full content of the post is being displayed | PASS
Like | Check if there is togglable like heart allowing registered user to toggle their like selection for the post | PASS
Back to Posts | Check "Back to Posts" button is working, redirecting user to the post list | PASS
Edit/Delete | Check if the edit/delete post buttons are only displayed if the user is the author of the post, and if they are redirecting the user to the edit post and delete post pages properly. | 
Ordering | Check if posts are being filtered by most recent | PASS
Comments | Check if all the posts' comments are being displayed under the main content, with the comments' accompanying metadata | PASS
Comment form | Check that comment form submits successfully if input correctly, and displays an error message if left blank | PASS
Delete Comment | Check if the delete comment button only shows if the user is the author of teh comment, and redirects the user to the proper comment deletion page | PASS

### Make a Post
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Submission | Check if post submits if information is submitted correctly | PASS
Error Message | Check if post does not submit, and error message is displayed instead, if post form is invalid. | PASS
Cancel | Check if cancel button successfully redirects user back to post list | PASS

### Edit Post page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Submission | Check post edits successfully if edit form is completed. | PASS
Error Messages | Check if proper error messages are displayed if edit form is completely incorrectly. | PASS

### Delete Post page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Post Identification | Check if post to be deleted is properly identified by title and creation date within post deltion page. | PASS
Yes/No | Check if delete confirmation/rejection buttons take the user back to a post list page which refelcts their choice accordingly. | PASS

### Delete Comment page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Yes/No | Check if comment deletion confirmation/rejection takes user back to post detail page with comments reflected accordingly. | PASS

### Logout Confirmation page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Metadata | Check if confirmation of signout successfully logs out the user and redirects them to the landing page. | PASS

### Register page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Register form | Checked the form submits only when all required fields are filled out. | PASS
Sign in link | Checked the sign-in link redirects to the sign-in page. | PASS
Register user | Checked the form submitted correctly successfully registers a new user. | PASS


### Sign in page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Sign in form | Checked the form submits only when all required fields are filled out. | PASS
Signup link | Checked the signup link redirects to the signup page. | PASS
Sign in | Checked the form signs in a user assuming the correct information is input. | PASS

### Messages
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Responsiveness | Check if messages appear with sensible styling across all device sizes.| PASS
Sign in | Check if sign in message displays on sign in | PASS
Sign out | Check if sign out message displays on sign out | PASS
Register | Check if sign in message displays on registration | PASS
Make post | Check if success message displays on post creation | PASS
Edit post | Check if success message displays on post edit | PASS
Delete post | Check if success message displays on post deletion | PASS
Make comment | Check if success message displays on comment creation | PASS
Delete comment | Check if success message displays on comment deletion | PASS

<a name="deployment"></a>

# 5. Deployment

[Go to the top](#table-of-contents)

I used the terminal to deploy my project locally. To do this I had to:
1. Create a repository on GitHub
2. Open the bash terminal within GitPod
3. Enter "python3 manage.py runserver" into the terminal
4. Open the local host port on my web browser

For the final deployment to Heroku, I had to:
1. Set debug = False in my settings.py file.
3. Commit and push all files to GitHub
3. In Heroku, remove the DISABLE_COLLECTSTATIC config var.
4. In the deploy tab, go to the manual deploy sections and click deploy branch.

<a name="end-product"></a>

# 6. End Product

[Go to the top](#table-of-contents)

Home Page:
![home_page_desktop_preview](documentation_assets/images/homepage_desktop_preview.png)

Post List Page:
![post_list_preview](documentation_assets/images/menu_desktop_preview.png)

Post Detail Page:
![contact_desktop_preview](documentation_assets/images/contact_deskop_preview.png)

Register Page:
![booking_desktop_preview](documentation_assets/images/booking_desktop_preview.png)

Login Page:
![manage_booking_desktop_preview](documentation_assets/images/manage_booking_desktop_preview.png)

Logout Page:
![edit_booking_desktop_preview](documentation_assets/images/edit_booking_desktop_preview.png)

Make Post Page:
![edit_profile_desktop_preview](documentation_assets/images/edit_profile_desktop_preview.png)

Edit Post Page:
![register_desktop_preview](documentation_assets/images/register_desktop_preview.png)

Delete Post Page:
![sign_in_desktop_preview](documentation_assets/images/sign_in_desktop_preview.png)

Comment Form:
![sign_out_desktop_preview](documentation_assets/images/sign_out_desktop_preview.png)

Delete Comment Page:
![sign_out_desktop_preview](documentation_assets/images/sign_out_desktop_preview.png)

<a name="bugs"></a>

# 7. Bugs

[Go to the top](#table-of-contents)

- There is a * next to the labels in the form submissions for creating a new post and editing a post.  That is not designed and I couldn't figure out a way to remove it. 
- There are several "problems" listed in the views.py file. But fixing those problems has historically led me to many more hours of far worse problems, so for the current ones I am leaving as is.
- Much of the styling as presented when running manage.py runserver is not present in the deployed version. I could not reconcile these two, but the deployed version functions well enough, just missing some styling pieces which improved aesthetics.

<a name="credits"></a>

# 8. Credits

[Go to the top](#table-of-contents)

I used the "I Think Therefore I Blog" module as an effective skeleton for my site.  As such, several base pieces still resemble the code covered in that video.  

-   settings.py, admin.py, apps.py, models.py, views.py, manage.py, env.py, urls.py, base.html, post_detail.html, post_list.html, and requirements.txt skeleton and boilerplate django code from https://learn.codeinstitute.net/
-   Instances of pagination code taken from https://learn.codeinstitute.net/
-   Inspiration for a form based approach to making new posts and editing existing posts taken from https://github.com/josswe26/code-buddy
-   README skeleton copied from a supplied project my my code institute mentor. While almost all contained information was tailored to my own project, certain pieces retained accuracy across the two. Take for example the "technologies used" section.  It follows that I used the exact same technologies as the student whose README structure I followed, so that section remains largely the same. Credit to https://github.com/iKelvvv/MS4/, who made an excellent README.


Special thanks to mentor Marcel for efficient and remarkably pinpoint accurate advice, as always. 