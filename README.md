# Tomeshack
- developed by Arthur Ambalov

## Table of Contents

1. [Overview](#overview)
2. [User Stories](#user-stories)
    1. [Tracking](#tracking)
3. [Design](#design)
    1. [Colour](#colour)
    2. [Font](#font)
    3. [Database](#database)
4. [Features](#features)
    1. [Pages](#pages)
5. [Validation](#validation-and-testing)
    1. [HTML](#html)
    2. [CSS](#css)
    3. [Javascript](#javascript)
    4. [Python](#python)
    5. [Accessibility](#accessibility)
    6. [Performance](#performance)
    7. [Browser Compatibility](#browser-compatibility)
    8. [Device Compatibility](#device-compatibility)
    9. [User Stories](#user-stories)
    10. [Automated Testing](#automated-testing)
6. [Bugs](#bugs)
7. [Deployment](#deployment)
8. [Credits](#credits)

## Overview

Tomeshack is an online bookshop where people can browse different categories of books, purchase hard copies to be delivered to them and leave reviews on the books for sale.

## User Stories
The website is designed for 8 detailed user stories, which are detailed alongside their acceptance criteria:

1. As a customer I can view a sortable list of books so that I can search for the kinds of book I am interested in.
Acceptance criteria:
- A products page displays a list of books
- Books are shown with titles, ratings, prices and excerpts of descriptions
- The list can be filtered by different categories

2. As a customer I can view or leave reviews so that I can see what people think of the books and share my thoughts.
Acceptance criteria:
- On a book's individual page, a review section is added
- Reviews appear in sequence for others to read
- Logged-in users can write reviews for others

3. As a customer I can view a detailed info page for a book so that I can read more on it.
Acceptance criteria:
- When a book's card is clicked in the main view, user is brought to its dedicated page
- This page allows for a full reading of the book's description
- The book's price and Tomeshack rating are shown

4. As a site administrator I can hide or delete reviews so that I can moderate harmful or hostile content.
Acceptance criteria:
- As a superuser viewing a book's dedicated page, a hide and delete button appear on reviews
- Hidden reviews are only visible to superusers
- Deleted posts are removed from the database entirely

5. As a customer I can add books I want to buy to my cart so that I can purchase them in a convenient manner.
Acceptance criteria:
- Viewing a book's dedicated page allows the user to add one or more copies to their cart
- Copies have a maximum of 4 in the cart to avoid scalping
- Cart items are saved to the session

6. As a customer I can view and modify my cart so that I can make final adjustments before ordering.
Acceptance criteria:
- The cart can be viewed on its own dedicated page with all products visible
- Product quantities can be modified directly from the cart page
- Items can be removed from the cart from the page

7. As a customer I can search the site for a book by title so that I can more easily find what I'm looking for.
Acceptance criteria:
- On the navbar, a search bar is visible
- Keywords can be entered into the search bar
- Searching shows only books with the keywords in their title or description

8. As a customer I can sign up to a newsletter so that I can stay up to date on new book deals.
Acceptance criteria:
- On the main page, a signup form is available
- Customers can subscribe to the newsletter
- Subscribers receive information on new deals

### Tracking

In accordance with agile principles, the user stories were tracked using GitHub's projects and issues features to create a kanban board. The project is set to visible, and a screenshot of it is shown below:

<details><summary>Image</summary>
<img src="docs/kanban.png">
</details>

## Design
A few wireframes were made in advance of starting development to plan out the most important features and the structure of code that would be required to accompany them.

The wireframes are presented below:

### Colour
Using <a href="https://mycolor.space">ColorSpace</a> a colour scheme was picked using blue shades to give the site a nice relaxing feeling appropriate for a place about stories and reading.

### Font
Open Sans was used as an easy and readable font to use throughout the site for most text. Oswald is used as an alternative to help make headings stand out.

### Search Engine Optimisation
Meta tags, a robots.txt file and a sitemap were all included in the project to optimise SEO quality.

### Database
- The website's backend database is powered by the Django framework, with the PostgresSQL relational database system provided by Code Institute.

The following models are used:

#### Category

The Category model is used to record the different categories that books are sorted by.

The category model contains:
- An internal name used for code
- A human-readable code for easier admin usage

#### Book

The Book model is used to record individual books for sale.

The book model contains:
- The category, a foreign key of the above Category model
- A unique slug ID to be defined for each book
- The title of the book as a string
- The description of the book as a string
- The book's price
- Tomeshack's rating for the book (out of 5)

#### Review

The review model is used for the reviews users can leave on books. It has the following fields:
- The review's author, a built-in Django User model
- A unique ID automatically generated for new reviews
- The book being reviewed (as in the above Book model)
- The text content of the review (capped to 200 characters)
- Whether a site administrator has hidden the review

#### Orders

The order model is used to track customer orders, with the following fields:
- A randomly generated order number
- The customer's full name
- Their email
- Their phone number
- The country they live in
- Their postcode (optional)
- Their town or city
- Their street address (in two lines)
- Their county (optional)
- The date and time the order was placed
- The total value of the order

#### Order Lines

The individual lines of an order are stored as a model with the following fields:
- The order the line is associated with (as Order model above)
- The book being purchased (as Book model above)
- The quantity of copies expressed as an integer
- The automatically-calculated total value of the line

## Features
The website has 5 main pages and X features across them.

### Pages
The 5 pages are:

- The homepage, which welcomes the customer, has a button to go to the products page and has a newsletter signup form.
- The products page, where books are displayed and can be filtered using the categories at the top or via the searchbar
- The book view page, where details of a book can be seen and reviews created or read
- The cart page, where a user can see and modify their cart and proceed to checkout
- The checkout page, where a user can enter their details to confirm their order

### Navbar
The navbar at the top of all pages has several buttons used to travel between the homepage, products page, cart and accounts pages.
User stories fulfilled: 7

<details><summary>Image</summary>
<img src="docs/features/feature-nav.png">
</details>

### Searchbar
A searchbar can be used to find specific books or description keywords. Submitting a query sends a user to the products page with only books that have the entered query in their title or description.
User stories fulfilled: 7

<details><summary>Image</summary>
<img src="docs/features/feature-search.png">
</details>

### Newsletter
A newsletter signup via Mailchimp is available on the front page to allow users to subscribe to emails containing new deals.
User stories fulfilled: 8

<details><summary>Image</summary>
<img src="docs/features/feature-newsletter.png">
</details>

### Sorting Categories
Several sort options are available on the products page to sort the list via sets of genres.
User stories fulfilled: 1

<details><summary>Image</summary>
<img src="docs/features/feature-sort.png">
</details>

### Book List
The books (sortable via the sorting categories or searchbar) are listed on the products page with a description excerpt, price and rating.
User stories fulfilled: 1, 7

<details><summary>Image</summary>
<img src="docs/features/feature-list.png">
</details>

### Detailed View
Full descriptions of a book can be seen on their dedicated page.
User stories fulfilled: 3

<details><summary>Image</summary>
<img src="docs/features/feature-detail.png">
</details>

### Quantity Selectors
These buttons on a book's detailed view can be used to select up to 4 total copies to be added to the cart.
User stories fulfilled: 5

<details><summary>Image</summary>
<img src="docs/features/feature-selectors.png">
</details>

### Reviews
A reviews section under each book allows users to see reviews left by others or to leave their own if logged in.
User stories fulfilled: 2, 4

<details><summary>Image</summary>
<img src="docs/features/feature-reviews.png">
</details>

### Cart
The cart page shows a list of all products in the cart, quantities and subtotals alongside a grand total, and quantities can be managed or products removed via this page.
User stories fulfilled: 6

<details><summary>Image</summary>
<img src="docs/features/feature-cart.png">
</details>

## Validation and Testing

### HTML
All pages on the site are validated with the W3C's Markup Validation Service and show no errors or warnings. See each page below:

<details><summary>Homepage</summary>
<img src="docs/validation/html/html-main-page.png">
</details>
<details><summary>Products Page</summary>
<img src="docs/validation/html/html-products.png">
</details>
<details><summary>Detailed View</summary>
<img src="docs/validation/html/html-view.png">
</details>
<details><summary>Cart</summary>
<img src="docs/validation/html/html-cart.png">
</details>
<details><summary>Checkout</summary>
<img src="docs/validation/html/html-checkout.png">
</details>

### CSS
The CSS style used by the site was validated with the W3C's CSS Validation Service, and showed no errors. There is one warning for the external stylesheet of Google Fonts which cannot be checked. See below:

<details><summary>Images</summary>
<img src="docs/validation/css/css-no-errors.png">
<img src="docs/validation/css/css-warning.png">
</details>


### JavaScript
The JavaScript code used for Stripe payment processing was run through the JSHint Javascript validator. There are no errors besides those caused by the unique tokens $ and Stripe tokens used by jQuery and Stripe libraries respectively.

<details><summary>Image</summary>
<img src="docs/validation/javascript.png">
</details>


### Python
<a href="https://pep8ci.herokuapp.com/">PEP8 Python Linter</a> was used to validate python files.

#### Home App ####
<details><summary>urls.py</summary>
<img src="docs/validation/python/home-urls.png">
</details>
<details><summary>views.py</summary>
<img src="docs/validation/python/home-views.png">
</details>

#### Cart App ####
<details><summary>contexts.py</summary>
<img src="docs/validation/python/cart-contexts.png">
</details>
<details><summary>test_views.py</summary>
<img src="docs/validation/python/cart-test-views.png">
</details>
<details><summary>urls.py</summary>
<img src="docs/validation/python/cart-urls.png">
</details>
<details><summary>views.py</summary>
<img src="docs/validation/python/cart-views.png">
</details>

#### Checkout App ####
<details><summary>admin.py</summary>
<img src="docs/validation/python/checkout-admin.png">
</details>
<details><summary>apps.py</summary>
<img src="docs/validation/python/checkout-apps.png">
</details>
<details><summary>forms.py</summary>
<img src="docs/validation/python/checkout-forms.png">
</details>
<details><summary>models.py</summary>
<img src="docs/validation/python/checkout-models.png">
</details>
<details><summary>signals.py</summary>
<img src="docs/validation/python/checkout-signals.png">
</details>
<details><summary>urls.py</summary>
<img src="docs/validation/python/checkout-urls.png">
</details>
<details><summary>views.py</summary>
<img src="docs/validation/python/checkout-views.png">
</details>
<details><summary>webhook_handler.py</summary>
<img src="docs/validation/python/checkout-webhook-handler.png">
</details>
<details><summary>webhooks.py</summary>
<img src="docs/validation/python/checkout-webhooks.png">
</details>

#### Products App ####
<details><summary>admin.py</summary>
<img src="docs/validation/python/products-admin.png">
</details>
<details><summary>forms.py</summary>
<img src="docs/validation/python/products-forms.png">
</details>
<details><summary>models.py</summary>
<img src="docs/validation/python/products-models.png">
</details>
<details><summary>test_forms.py</summary>
<img src="docs/validation/python/products-signals.png">
</details>
<details><summary>test_views.py</summary>
<img src="docs/validation/python/products-signals.png">
</details>
<details><summary>urls.py</summary>
<img src="docs/validation/python/products-urls.png">
</details>
<details><summary>views.py</summary>
<img src="docs/validation/python/products-views.png">
</details>

### Accessibility
Pages on the site are checked with the WAVE Website Accessibility Evaluation Tool. One error on the main page is from MailChimp's signup form, which is intentionally present to avoid bot signups. Other pages have no errors. See each page below:
<details><summary>Main Page</summary>
<img src="docs/validation/wave/wave-main.png">
</details>
<details><summary>Products</summary>
<img src="docs/validation/wave/wave-products.png">
</details>
<details><summary>Detailed View</summary>
<img src="docs/validation/wave/wave-view.png">
</details>
<details><summary>Cart</summary>
<img src="docs/validation/wave/wave-cart.png">
</details>

### Browser Compatibility
Each page has been tested to work on:
- Mozilla Firefox
- Google Chrome
- Microsoft Edge

### Device Compatibility
Each page was tested on Mozilla Firefox and Google Chrome's developer tools for responsive design. Testing was done on a desktop PC running Windows 11 and a Galaxy A50 phone.

### User Stories
Below is a list of user stories and the process by which they are fulfilled:



### Automated Testing
Automated tests were created to test the forms and views of apps where relevant.

<details><summary>Image</summary>
<img src="docs/validation/auto-test.png">
</details>

## Bugs
Notable bugs found during development:

- The behaviour of the increment and decrement buttons was found to be very unreliable during testing, sometimes resulting in attempts to decrement the quantity of an item instead doubling it. This was fixed by adjusting the imported Bootstrap and jQuery versions to ones I knew were compatible with each other, which fixed the issue.

## Deployment
The project was deployed using the online platform Heroku. The following steps were taken:

1. Log in or sign up to the Heroku website:
<details><summary>Image</summary>
<img src="docs/heroku/heroku-login.png">
</details>

2. Click the "new" button and then "Create a new app"
<details><summary>Images</summary>
<img src="docs/heroku/heroku-newapp.png">
</details>

3. Choose an app name and region to use, Europe in my case
<details><summary>Image</summary>
<img src="docs/heroku/heroku-newapp2.png">
</details>

4. Navigate to the "Settings" tab of the new app and set the config vars: the postgres database URL and the secret key it uses:
<details><summary>Image</summary>
<img src="docs/heroku/heroku-configvars.png">
</details>

5. Go to the "Deploy" page and select GitHub as a deploy method, log in via GitHub and then select the desired repository
<details><summary>Image</summary>
<img src="docs/heroku/heroku-connect.png">
</details>

6. Go to "Manual deploy", make sure the main branch is selected, and click "Deploy"
<details><summary>Image</summary>
<img src="docs/heroku/heroku-deploy.png">
</details>

### Forking
On this project's repository, at the upper-right-hand side, there is a "fork" button to create a fork of it.

### Cloning
On this project's repository, at the upper-right-hand side, there is a "Code" button. To clone the project, click the button and:
- Choose between HTTPS, SSH or GitHub CLI as preferred and click the "Copy url to clipboard" button
- Open Git Bash
- Set the working directory to where the cloned project should be
- Type "git clone " followed by the copied URL
- Hit enter to create the cloned project

## Credits
- Icons: <a href="https://fontawesome.com/icons">FontAwesome</a>
- Original dataset: <a href="https://www.kaggle.com/datasets/bishop36/bookstore">bookstore by Bishop36 on Kaggle</a>, modified for usage in this project

Technology used:
- Languages: HTML 5, CSS, JavaScript, Python
- Database management framework: Django
- IDE: GitPod
- Version control: GitHub
- Deployment: Heroku
- Wireframing: Balsamiq
- Validation: W3C HTML Validator, W3C CSS Validator, JSHints Code Quality Tool, WAVE Website Accessibility Evaluation Tool, PEP8, Google Chrome
- Color palette design: <a href="https://mycolor.space">ColorSpace</a>

### Third Party Libraries

- Bootstrap 4 was used for its easy and powerful HTML, CSS and Javascript functions to improve the site's appearance and functionality.
- Django AllAuth is used for its login/signup/logout functions alongside the base Django user features.
- Django Crispyforms is installed to create the forms that users can use to create posts or submit feedback to the admins.
- WhiteNoise is used to allow Django to serve static files such as CSS to deployment apps such as Heroku, necessary so that the site can be styled without having a CDN.

Other:
- Code Institute for walkthrough on cart and checkout code
- Mo Shami for mentoring, guidance and feedback