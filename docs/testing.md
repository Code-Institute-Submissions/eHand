# eHand Testing

## Index

Deployment

**<details><summary>Home</summary>**

+ [Home visual testing](#home-visual-testing)
+ [Home Operation testing](#home-operation-testing)
+ [Home Templates testing](#home-templates-testing)
+ [Home Urls testing](#home-urls-testing)
+ [Home Views testing](#home-views-testing)
    
</details>

 **<details><summary>Memberships</summary>**

+ [Memberships visual testing](#memberships-visual-testing)
+ [Memberships Operation testing](#memberships-operation-testing)
+ [Memberships Templates testing](#memberships-templates-testing)
+ [Memberships Css testing](#memberships-css-testing)
+ [Memberships JavaScript testing](#memberships-javascript-testing)
+ [Memberships Models testing](#memberships-models-testing)
+ [Memberships Urls testing](#memberships-urls-testing)
+ [Memberships Views testing](#memberships-views-testing)
    
</details>

 **<details><summary>Notices</summary>**

+ [Notices visual testing](#notices-visual-testing)
+ [Notices Operation testing](#notices-operation-testing)
+ [Notices Templates testing](#notices-templates-testing)
+ [Notices Models testing](#notices-models-testing)
+ [Notices Urls testing](#notices-urls-testing)
+ [Notices Views testing](#notices-views-testing)

</details>

 **<details><summary>Profiles</summary>**

+ [Profiles visual testing](#profiles-visual-testing)
+ [Profiles Operation testing](#profiles-operation-testing)
+ [Profiles Templates testing](#profiles-templates-testing)
+ [Profiles Models testing](#profiles-models-testing)
+ [Profiles Urls testing](#profiles-urls-testing)
+ [Profiles Views testing](#profiles-views-testing)

</details>

 **<details><summary>Comments</summary>**

+ [Comments visual testing](#comments-visual-testing)
+ [Comments Operation testing](#comments-operation-testing)
+ [Comments Templates testing](#comments-templates-testing)
+ [Comments Models testing](#comments-models-testing)
+ [Comments Urls testing](#comments-urls-testing)
+ [Comments Views testing](#comments-views-testing)

</details>

 **<details><summary>User Stories Testing</summary>**

- [User Stories Testing](#user-stories-testing)
  * [As a non member: I want to visit the sites homepage and get a clear overview of what the site does and how i can sign up.](#user-story-1)
  * [As a Free member i want to be able to sign in to eHand and view Posts and offer help](#user-story-2)
  * [As a premium member when i create my membership, i want to know my payment donates to charity](#user-story-3)
  * [As a premium member when i create my membership, i want to be awarded the 2 free hours of time to spend on the site.](#user-story-4)
  * [As a premium member i want to be able to create a posting/ or hand.](#user-story-5)
  * [As a Premium member i want other members to be able to see my post/hand - and offer help.](#user-story-6)
  * [As a premium member i want to be able to offer my help to others.](#user-story-7)
  * [As a premium member i want to be able to transfer my time to another member who helped me.](#user-story-8)
  * [As a premium member i want to be able to accept payment of time from a member i helped.](#user-story-9)
  * [As a premium member i want to get a notification when i log in - if another member has offered help](#user-story-10)
  * [As a member i want a way to communicate to a member who is offering help, or if i am offering it.](#user-story-11)
  * [As a member i would like to see commitments i have made in my profile](#user-story-12)
  * [As a member i would like to see my notices in my profile.](#user-story-13)

</details>

# Apps Manual Continuous Testing

## Home


### Home visual testing
* :hammer: TEST:  
    * Expected tailored Javascript to force Page logo to disappear when scroll down the page, and the navbar to roll up to a fixed position at the top of the page.
* :clipboard: RESULT: 
    * Page displayed as expected
    * No errors in console.

* :hammer: TEST: (Responsiveness)   
    * Expected tailored Javascript to force navbar to become fixed to the top when screen size was reduced below 768px in width.
* :clipboard: RESULT: 
    * Page displayed as expected
    * No errors in console.

* :hammer: TEST: (Messages)  
    * Expected to see a modal display a message after an upgrade attempt of a membership.
* :clipboard: RESULT: 
    * Modal displayed as expected with ghost white body and lime green border.

* :hammer: TEST: (Username)  
    * Expected to see a logged in user message at top of screen
    * Expected this to be a clickable link
* :clipboard: RESULT: 
    * Link displayed as expected.

* :hammer: TEST: (Fade-in)  
    * Expected to see a elements fade into view after 25% of a container linked to the fade-in class is reavealed
* :clipboard: RESULT: 
    * Fade in elements displayed as expected.

[Back to Index](#index)

### Home Operation testing
* :hammer: TEST: (Navbar) 
    * Check all navbar links
* :clipboard: RESULT: 
    * All navbar links work as expected

* :hammer: TEST: (Info Readmore links) 
    * Expected Read more links in page introduction to bring user to correct section on page to read more about that article.
* :clipboard: RESULT: 
    * Read more links took user to correct part of page

* :hammer: TEST: (Get Started links) 
    * Expected Get Started links in information containers to bring user to the upgrade page.
* :clipboard: RESULT: 
    * For a non authenticated member - they are taken to the sign in page / with option to register.
    * Once signed in, the user arrives at the upgrade page.
    * An authenticated user arrives straight to the upgrade page.

* :hammer: TEST: (footer) 
    * Expected Social icons to have correct colour on hover.
    * Expected footer social links to take me to correct site destinations
* :clipboard: RESULT: 
    * Icons displayed correctly before and after hover.
    * Each link takes the user to the social media website relevant to the link, in a new tab.

[Back to Index](#index)

### Home Templates testing
* :hammer: TEST: 
    * Tested the Html Markup for index.htmel using [W3Validator](https://validator.w3.org/nu/#textarea)
* :clipboard: RESULT: 
    * No errors found
![index.html](https://i.ibb.co/6PVVRNy/image.png "Index.html validation result")


[Back to Index](#index)


### Home Urls testing
* :hammer: TEST:    
    * Expect url for index.html to provide correct path for my home page
* :clipboard: RESULT: 
    * Correct path was provided in urls.py

* :hammer: TEST:    
    * Checked code using gitpod built in python validator and [pep8online](http://pep8online.com/)
* :clipboard: RESULT: 
    * No code errors or linting issues found

[Back to Index](#index)

### Home Views testing
* :hammer: TEST: (views.index)
    * Expected the index view to render the home page
* :clipboard: RESULT: 
    * Page was rendered as expected

* :hammer: TEST:    
    * Checked code using gitpod built in python validator and [pep8online](http://pep8online.com/)
* :clipboard: RESULT: 
    * No code errors or linting issues found

[Back to Index](#index)

---

## Memberships

### Memberships visual testing
* :hammer: TEST:    
    * Expected package payment to be rendered with common site styling and dark transparent card
* :clipboard: RESULT: 
    * Membership payments rendered as expected

* :hammer: TEST:    
    * Expected select_package.html to be rendered with common site styling with 2 cards displaying the membership options and benefits
* :clipboard: RESULT: 
    * Membership select_package.html rendered as expected.

* :hammer: TEST:    
    * Expected upgrade page to display current membership.
    * Expect upgrade page to display benefits of each membership package
* :clipboard: RESULT: 
    * Upgrade page displays as expected

* :hammer: TEST:    
    * Expected current membership status to be displayed in users profile page
* :clipboard: RESULT: 
    * Current membership is displayed as expected

* :hammer: TEST:    
    * Expected a link to discover the premium membership in the profile view
* :clipboard: RESULT: 
    * A discover premium button is displayed only when current user is on a free membership plan.

* :hammer: TEST:    
    * Expected to be able to cancel my premium membership from the profile
* :clipboard: RESULT: 
    * A Cancel my Subscription button is available in the profile page when the user has a current valid premium subscription.

[Back to Index](#index)

### Memberships Operation testing
* :hammer: TEST:    
    * Expected a free membership to be automatically created for each new user
* :clipboard: RESULT: 
    * A new 'Free' membership is created for each new user, by the 
    [post_save_create_membership](https://github.com/Mr-Smyth/eHand/blob/e738bfb46193ac54dcb1678be8141be38447c919/memberships/models.py#L46) signal, in 
    memberships.models.

* :hammer: TEST:    
    * I expect that when i am a free member, the upgrade page gives me the option to upgrade.
* :clipboard: RESULT: 
    * Option to select premium is always available to a free member.

* :hammer: TEST:    
    * I expect that i can enter the test credit card info from stripe ***"4242 4242 4242 4242"*** in the 
    packages payment page and purchase a premium subscription.
    I expect some visual confirmation of a successful transaction.
* :clipboard: RESULT: 
    * Upon all cases of testing i was able to enter the stripe test card data and successfully subscribe to a premium membership.

* :hammer: TEST:    
    * I expect that i can cancel my premium subscription at any stage.
* :clipboard: RESULT: 
    * User can cancel their subscription from the profile page at any stage.

[Back to Index](#index)

### Memberships Templates testing
* :hammer: TEST: (package_payment.html)
    * Tested the Html Markup for package_payment.html using [W3 Validator](https://validator.w3.org/nu/#textarea)
* :clipboard: RESULT: 
    * 1 warning found - reccomended H2-H6 element after page block section
    * 0 errors found
![package_payment.html](https://i.ibb.co/tLK5Ycg/image.png "package_payment.html validation result")

* :hammer: TEST: (select_package.html)
    * Tested the Html Markup for select_package.html using [W3 Validator](https://validator.w3.org/nu/#textarea)
* :clipboard: RESULT: 
    * 0 errors found
![select_package.html](https://i.ibb.co/LNv7G7r/image.png "select_package.html validation result")

[Back to Index](#index)

### Memberships Css testing
* :hammer: TEST: (checkout.css)
    * Tested the CSS in checkout.css using [W3 CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
* :clipboard: RESULT: 
    * 0 errors found
![checkout.css](https://i.ibb.co/d4HVkZ0/image.png "checkout.css validation result")

[Back to Index](#index)

### Memberships JavaScript testing
* :hammer: TEST: (checkout.js)
    * Tested code using JsHint
* :clipboard: RESULT: 
    * This code is from stripe docs - but tested it for any errors as had adjusted it for my own needs.
    * No errors found

* :hammer: TEST:    
    * Expected stripe payments to work correctly
* :clipboard: RESULT: 
    * Stripe paymesnts all work as expected

[Back to Index](#index)

### Memberships Models testing
* :hammer: TEST:   
    * Does the model store and provide the expected information
* :clipboard: RESULT: 
    * Membership models displayed all correct information when viewed in the admin or shell and 
    also outputted the correct information in the views

* :hammer: TEST:    
    * Check IDE for any linting errors
* :clipboard: RESULT: 
    * *"Instance of 'OneToOneField' has no 'username' member"* and *"Class 'Memberships' has no 'objects' member"* errors
     from linter - After research online and on slack, I discovered it was pylint not understanding the django model 
     reference. I am still checking for answers to this.

[Back to Index](#index)

### Memberships Urls testing
* :hammer: TEST:    
    * Did urls.py provide correct paths for all urls.
* :clipboard: RESULT: 
    * All membership urls arrived at correct views

* :hammer: TEST:    
    * Checked code using gitpod built in python validator and [pep8online](http://pep8online.com/)
* :clipboard: RESULT: 
    * No code errors or linting issues found

[Back to Index](#index)

### Memberships Views testing
* :hammer: TEST:    
    * Did Views return correct templates and data when requested
* :clipboard: RESULT: 
    * All views worked as expected

* :hammer: TEST:    
    * Checked code using gitpod built in python validator and [pep8online](http://pep8online.com/)
* :clipboard: RESULT: 
    * Errors returned:
        *   Class 'Subscriptions' has no 'objects' member - ***After research online and on slack, I discovered it was pylint not understanding the django model 
     reference. I am still checking for answers to this.***
        *   Class 'Packages' has no 'objects' member - ***After research online and on slack, I discovered it was pylint not understanding the django model 
     reference. I am still checking for answers to this.***
        *   Unused variable 'created' - ***this is because pylint does not know about using it as a search of stripe.***

[Back to Index](#index)

---

## Notices

### Notices visual testing
* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

[Back to Index](#index)

### Notices Operation testing
* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

[Back to Index](#index)

### Notices Templates testing
* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

* :hammer: TEST:    
    * Can user manually enter a URL such as delete to access forbidden functionality
* :clipboard: RESULT: 
    * The user is unable to gain access via manual url manipulation

[Back to Index](#index)

### Notices Models testing
* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

[Back to Index](#index)

### Notices Urls testing
* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

[Back to Index](#index)

### Notices Views testing
* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

[Back to Index](#index)

---

## Profiles

### Profiles visual testing
* :hammer: TEST:    
    * Does page load with correct common styling?
    * Does console display any errors?
* :clipboard: RESULT: 
    * Page loads as expected with site common styling.
    * No errors in console.

* :hammer: TEST: (user Subscriptions)
    * Does correct User Membership Subscription data display?
    * Do the correct dates for the subscription display as intended?
* :clipboard: RESULT: 
    * All User Subscription data displays as intended.

* :hammer: TEST: (Cancel Subscriptions)   
    * Expect the cancel membership button - only when currently subscribed to premium
* :clipboard: RESULT: 
    * The Cancel subscription button will only display when the user is subscribed to Premium

* :hammer: TEST: (Subscriptions) 
    * Expect the Discover Premium button to display when user is subscribed to free
* :clipboard: RESULT: 
    * The Discover premium button only displays when the user is subscribed to free.

* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

[Back to Index](#index)

### Profiles Operation testing
* :hammer: TEST: (Manage Subscriptions) 
    * Expect The Cancel subscription button to remove the premium subscription and apply the free subscription when clicked.
* :clipboard: RESULT: 
    * The cancel subscription button behaves as expected and removes the premium and applies the free membership.

* :hammer: TEST: (Subscriptions)   
    * Expect the Discover Premium button to redirect user to the upgrade page.
* :clipboard: RESULT: 
    * User gets redirected to the upgrade page when user clicks on the discover Premium button.

[Back to Index](#index)

### Profiles Templates testing
* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

[Back to Index](#index)

### Profiles Models testing
* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

[Back to Index](#index)

### Profiles Urls testing
* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

[Back to Index](#index)

### Profiles Views testing 
* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

[Back to Index](#index)

---

## Comments

### Comments visual testing
* :hammer: TEST:    
    * Does page load with correct common styling?
    * Does console display any errors?
* :clipboard: RESULT: 
    * Page loads as expected with site common styling.
    * No errors in console.

* :hammer: TEST: (user Subscriptions)
    * Does correct User Membership Subscription data display?
    * Do the correct dates for the subscription display as intended?
* :clipboard: RESULT: 
    * All User Subscription data displays as intended.

* :hammer: TEST: (Cancel Subscriptions)   
    * Expect the cancel membership button - only when currently subscribed to premium
* :clipboard: RESULT: 
    * The Cancel subscription button will only display when the user is subscribed to Premium

* :hammer: TEST: (Subscriptions) 
    * Expect the Discover Premium button to display when user is subscribed to free
* :clipboard: RESULT: 
    * The Discover premium button only displays when the user is subscribed to free.

* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

[Back to Index](#index)

### Comments Operation testing
* :hammer: TEST: (Manage Subscriptions) 
    * Expect The Cancel subscription button to remove the premium subscription and apply the free subscription when clicked.
* :clipboard: RESULT: 
    * The cancel subscription button behaves as expected and removes the premium and applies the free membership.

* :hammer: TEST: (Subscriptions)   
    * Expect the Discover Premium button to redirect user to the upgrade page.
* :clipboard: RESULT: 
    * User gets redirected to the upgrade page when user clicks on the discover Premium button.

[Back to Index](#index)

### Comments Templates testing
* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

[Back to Index](#index)

### Comments Models testing
* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

[Back to Index](#index)

### Comments Urls testing
* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

[Back to Index](#index)

### Comments Views testing 
* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

* :hammer: TEST:    
    * 
* :clipboard: RESULT: 
    * 

[Back to Index](#index)

---

## User Stories Testing

### User story 1

As a non member: I want to visit the sites homepage	and get a clear overview of what the site does and how i can sign up.

[Back to Index](#index)
### User story 2

As a Free member i want to be able to sign in to eHand and view Posts and offer help

[Back to Index](#index)
### User story 3

As a premium member when i create my membership, i want to know my payment donates to charity

[Back to Index](#index)
### User story 4

As a premium member when i create my membership, i want to be awarded the 2 free hours of time to spend on the site.

[Back to Index](#index)
### User story 5

As a premium member i want to be able to create a posting/ or hand.

[Back to Index](#index)
### User story 6

As a Premium member i want other members to be able to see my post/hand - and offer help.

[Back to Index](#index)
### User story 7

As a premium member i want to be able to offer my help to others.

[Back to Index](#index)
### User story 8

As a premium member i want to be able to transfer my time to another member who helped me.

[Back to Index](#index)
### User story 9

As a premium member i want to be able to accept payment of time from a member i helped. 

[Back to Index](#index)
### User story 10

As a premium member i want to get a notification when i log in - if another member has offered help

[Back to Index](#index)
### User story 11

As a member i want a way to communicate to a member who is offering help, or if i am offering it.

[Back to Index](#index)
### User story 12

As a member i would like to see commitments i have made in my profile

[Back to Index](#index)
### User story 13

As a member i would like to see my notices in my profile.

[Back to Index](#index)

---
