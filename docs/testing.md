
![eHandTesting](https://i.ibb.co/ry2dNYk/image.png "eHand testing Logo")

# eHand Testing

#### [<< Return to Readme](https://github.com/Mr-Smyth/eHand/blob/master/README.md)

## Index


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
+ [Notices Css testing](#notices-css-testing)
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
* :hammer: TEST:    (Notices)
    * Expected notices page to display each notice in a paginated view, stacked on mobile device and side by side on descktop
* :clipboard: RESULT: 
    * Notice page rendered as expected on all screen sizes.

* :hammer: TEST:  (Notices)  
    * Expected each notice to display the details entered and to display the status of the notice - ie: if anybody had committed to the 
    notice yet
* :clipboard: RESULT: 
    * The notice displayed all the correct details and the current status

* :hammer: TEST:  (Notice Details)  
    * Expected the Notice Details to display full information for the post
    * Expected the Notice Details to display additional directions and information for the post, when relevant
* :clipboard: RESULT: 
    * The correct details were displayed for each notice details, depending on the circumstances.

* :hammer: TEST:    (Notice Details - comments)  
    * Expect comments to display "no comments yet" on a new notice.
    * Expect Comments to display current users comments in blue.
    * Expect Comments to display authors comments in black.
    * Expect Comments to display other members comments in yellow.
    * Expected comments to appear stacked on either side of the comment window.
* :clipboard: RESULT: 
    * Comments all displayed as expected.   
    * ***Possible upgrade for next version - include ajax to improve UX and stop page reload.***

[Back to Index](#index)

### Notices Operation testing

* :hammer: TEST: (Notices)    
    * Expected notice Details button to take me to the details of the correct notice
* :clipboard: RESULT: 
    * Clicking details always took me to the correct notice details

* :hammer: TEST: (Notices)  
    * Expected each notice to not allow un-authenticated users to click on the details
* :clipboard: RESULT: 
    * Un-authenticated users are unable to click details of a notice, instead they are diverted to the sign in page.

* :hammer: TEST:   (Notice Details)   
    * Expected notice details to allow me to commit to a notice if i am not the author
* :clipboard: RESULT: 
    * The commit button allowed me to commit to any notice that i was not the author of.
    * If the notice has been already committed to, and current user is neither the member who committed of the author,
    Then it is not possible to view the details.
    * If i am the member who committed, the option to commit is no longer there, and some extra information regarding how to manage the commitment is displayed

* :hammer: TEST:   (Notice Details)   
    * Expected notice details to allow me to enter a comment to be read by anyone viewing the details
* :clipboard: RESULT: 
    * Comment worked as expected and displayed for the correct notice only.

* :hammer: TEST: (Notices - create/update notice)   
    * Expected to click create notice and be taken to the create notice form
* :clipboard: RESULT: 
    * Create notice will take any premium member to the create notice form, 
    * A check is made for users membership and the button is removed and the view restricted if current user is on a free membership

* :hammer: TEST:  (Notices - create/update notice)     
    * Expected to be able to enter all relevent details of my notice into the form and click submit.
    * Expect to be redirected to the notice details after clicking submit
* :clipboard: RESULT: 
    * Notice create/update worked as expected - redirecting to the same notice deta after clicking submit.

[Back to Index](#index)

### Notices Templates testing
* :hammer: TEST: (notice_list.html)
    * Tested the Html Markup for notice_list.html using [W3 Validator](https://validator.w3.org/nu/#textarea)
* :clipboard: RESULT: 
    * 0 errors found.   
![notice_list.html](https://i.ibb.co/vZhv3CL/image.png "notice_list.html validation result")

* :hammer: TEST: (notice_detail.html)
    * Tested the Html Markup for notice_detail.html using [W3 Validator](https://validator.w3.org/nu/#textarea)
* :clipboard: RESULT: 
    * 0 errors found.   
![notice_detail.html](https://i.ibb.co/rQ4f9by/image.png "notice_detail.html validation result")

* :hammer: TEST: (notice_form.html)
    * Tested the Html Markup for notice_form.html using [W3 Validator](https://validator.w3.org/nu/#textarea)
* :clipboard: RESULT: 
    * 1 warning found - reccomended H2-H6 element after page block section
    * 0 errors found
![notice_form.html](https://i.ibb.co/NpPsrZB/image.png "notice_form.html validation result")

* :hammer: TEST: (notice_confirm_delete.html)
    * Tested the Html Markup for notice_confirm_delete.html using [W3 Validator](https://validator.w3.org/nu/#textarea)
* :clipboard: RESULT: 
    * 0 errors found.   
![notice_confirm_delete.html](https://i.ibb.co/10K8yNp/image.png "notice_confirm_delete.html validation result")

* :hammer: TEST:    
    * Can user manually enter a URL such as delete to access forbidden functionality
* :clipboard: RESULT: 
    * The user is unable to gain access via manual url manipulation

[Back to Index](#index)

### Notices Css testing

* :hammer: TEST: (notices.css)
    * Tested the CSS in notices.css using [W3 CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
* :clipboard: RESULT: 
    * 0 errors found
![notices.css](https://i.ibb.co/BKCpDxQ/image.png "notices.css validation result")

[Back to Index](#index)

### Notices Models testing
* :hammer: TEST:   (Notice Model)
    * Does the model store and provide the expected information
* :clipboard: RESULT: 
    * Notice models displayed all correct information when viewed in the admin or shell and 
    also outputted the correct information in the views

* :hammer: TEST:    
    * Check IDE for any linting errors
* :clipboard: RESULT: 
    * No errors found

[Back to Index](#index)

### Notices Urls testing
* :hammer: TEST:    
    * Did urls.py provide correct paths for all urls.
* :clipboard: RESULT: 
    * All notice urls arrived at correct views

* :hammer: TEST:    
    * Checked code using gitpod built in python validator and [pep8online](http://pep8online.com/)
* :clipboard: RESULT: 
    * No code errors or linting issues found

[Back to Index](#index)

### Notices Views testing

Used several Django Generic class views for this app, with some mixins associated with tests and login checks

* :hammer: TEST:   (notice.views) 
    * Did Views return correct templates and data when requested
* :clipboard: RESULT: 
    * All views worked as expected

* :hammer: TEST:    (notice.views)
    * Checked code using gitpod built in python validator and [pep8online](http://pep8online.com/)
* :clipboard: RESULT: 
    * ENo Errors or warnings returned or highlighted

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

* :hammer: TEST:    (Profile) 
    * Expect the time account section to only display for premium members.
* :clipboard: RESULT: 
    * Time account balance only displays for premium members.

* :hammer: TEST:   (Profile) 
    * Expect members information to display in the Profile information window.
* :clipboard: RESULT: 
    * Any entered profile information is always displayed within the Profile Information window.

* :hammer: TEST:    (Profile) 
    * Expect the members current own notices to display in My Notices section of the Profile.
* :clipboard: RESULT: 
    * All members current notices are displayed in the My notices section of the profile.

* :hammer: TEST:    (Profile) 
    * Expect the members current commitments to display in My commitments section of the Profile.
* :clipboard: RESULT: 
    * All members current commitments are displayed in the My commitments section of the profile.

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

* :hammer: TEST:    (Profile)
    * Expect user to be able to click on edit profile in the Profile Information window and be directed to the edit profile page.
* :clipboard: RESULT: 
    * When clicked the edit profile button takes the member to a page where they can enter/edit their profile data.

* :hammer: TEST:    (My Commitments)
    * Expect to be able to remove my commitment to a notice in my commitments page of my profile.
* :clipboard: RESULT: 
    * Yes the member can remove their commitment to a message from the profile - my commitments page.

* :hammer: TEST:   (My Notices) 
    * Expect to be able to remove a notice by deleting it in the My Notices page
* :clipboard: RESULT: 
    * Yes a member can click the delete notice button in the my Notices page of their profile.
    * This is only possible if nobdy has committed to the notice.
    * Any committed to notice may not be deleted until complete

* :hammer: TEST:   (My Notices) 
    * Expect to be able to update a notice by in the My Notices page
* :clipboard: RESULT: 
    * Yes a member can click the Update notice button in the my Notices page of their profile.
    * This is only possible if nobdy has committed to the notice.
    * Any committed to notice may not be updated.

* :hammer: TEST:   (Update profile form) 
    * Expected that current information would be displayed inside the edit profile form
* :clipboard: RESULT: 
    * Current information is displayed inside the update user profile form.

* :hammer: TEST:   (Update profile form) 
    * Expected that clicking submit on the update user profile form will take and apply values from the form
* :clipboard: RESULT: 
    * Current information is updated upon form submit.

[Back to Index](#index)

### Profiles Templates testing
* :hammer: TEST: (profile.html)
    * Tested the Html Markup for profile.html using [W3 Validator](https://validator.w3.org/nu/#textarea)
* :clipboard: RESULT: 
    * 0 errors found.   
![profile.html](https://i.ibb.co/2kXnFd8/image.png "profile.html validation result")

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
