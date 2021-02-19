# eHand

![eHand logo](https://i.ibb.co/nL9459P/image.png "Site logo")


[Click here to view eHand](https://mr-smyth-ehand.herokuapp.com/)


***"Time is the most valuable thing a man can spend. – Theophrastus...."***

Time is indeed a very, very precious commodity - perhaps the most precious. Time given to others is a wonderful gift and its time you cannot get back!  
Actually, that's not technically true, because now you can, with eHand.

eHand is a site where users can visit to ask for help, or provide it. Free members can browse a selection of notices by premium members 
and can offer their help.
Premium members can also offer their help and can also create notices - looking for any sort of a hand.   
Premium members can also use the sites unique currency - TIME as payment for any help provided. In doing so, you can actually get Time back.   

This website is not restricted to individuals, it can be easily extended to include community groups, offer incentives to those who help out in their communities
and provide a means to those without.

eHand will be submitted as my MS4 and final project in my Full Stack Software Development diploma.   

***For your convenience, 4 users have been setup and have linked or committed notices for demo purposes: john, paul, george and ringo - all sharing the same password: ehandpassword.***

# Table of contents


- [UX](#ux)
  * [Purpose](#purpose)
  * [Goals](#goals)
    + [Visitor Goals](#visitor-goals)
    + [Member Goals](#member-goals)
    + [Business Goals](#business-goals)
  * [User Stories](#user-stories)
- [UI](#ui)
  * [Colours](#colours)
  * [Fonts](#fonts)
  * [Styling](#styling)
  * [Database Schema](https://github.com/Mr-Smyth/eHand/blob/master/docs/schema/schema.pdf)
  * [Wireframes](#wireframes)
- [Features](#features)
  * [Existing Features](#existing-features)
    + [Common site elements](#common-site-elements)
      - [Logo](#logo)
      - [A Navbar](#a-navbar)
      - [Information area](#information-area)
      - [Footer](#footer)
    + [Home Page](#home-page)
    + [Notices page](#notices-page)
    + [Create Notice page](#create-notice-page)
    + [Notice Details page](#notice-details-page)
    + [Profile](#profile)
    + [My Commitments](#my-commitments)
    + [My Notices](#my-notices)
    + [Upgrade](#upgrade)
      - [Selecting Premium](#selecting-premium)
  * [Features for future consideration](#features-for-future-consideration)
- [Deployment](#deployment)
  * [Steps to deploy eHand to Heroku using Postgres](#steps-to-deploy-ehand-to-heroku-using-postgres)
    + [In Heroku:](#in-heroku-)
    + [In GitPod or IDE:](#in-gitpod-or-ide-)
    + [In Django - setup new database:](#in-django---setup-new-database-)
  * [Local Deployment](#local-deployment)
    + [Steps to Deploy](#steps-to-deploy)
- [Testing](#testing)
- [Tech](#tech)
- [Credits](#credits)
  * [Content and code](#content-and-code)
  * [Media](#media)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)
- [Disclaimer](#disclaimer)



---

# UX

## Purpose

eHand allows members to create a post for some form of help that they need, this can be absolutely anything.   
It allows other members to view and respond by offering to help - ***or commit*** - to the member who posted. The member who creates the post 
will also include the time/duration of the task, and this is important as this represents the amount of the TIME payment available.   

You see I believe the most precious thing we spend today is time - and to give that time to someone, freely - to help them out, is a 
wonderful gift.   

Now we've all been there - Someone helps you out - you maybe offer them money as you want to show your gratitude - 
mostly it is turned down, with a friendly - get me again!

Wouldn't it be nice if you could give back what they so freely gave? - which is their own TIME.  
Enabling them to use that TIME as a form of currency to purchase someone else's TIME - and get something done that they need?
Perhaps their car needs brakes fitted or their daughter needs help with her Maths - with TIME
they can get whatever it is they need.   

I really can't think of a greater gift - than the gift of TIME!   

So therefore I came up with the idea of creating time on the site, as a token payment system.
To be included in the payment system - you must be a premium member, this requires registering for an eHand account and then 
selecting the premium membership type in the upgrade section, or by clicking Discover Premium in your profile.  
This provides the user with a Time Account - with a balance of 10t ***(t = the time unit currency on-site, equivalent to hours)***  

The helping doesn't stop there. All profits created from membership subscriptions will be donated to a different charity each month.
Future planned incentives to be included are rewarding Time payments to members giving help with organised charity events.   

[<< ***Back to contents***](#table-of-contents)


## Goals

### Visitor Goals

The target audience is:
+ People of all ages who need help with a task.
+ People who have not means to pay for professional help.
+ Groups and organisations looking for an interesting way to encourage/incentivise people to help out and get involved in events.
+ To create a public platform that promotes helping others - and yet still gives something back.   

[<< ***Back to contents***](#table-of-contents)

### Member Goals

The Goals for members are:
+ Get help with a task or event by posting a notice.
+ Provides a way for people to help out, by reading the notices and responding.
+ A method of accumulating TIME, by helping another member.
+ A method of getting "***stuff***" done - by a method almost similar to bartering, where you trade Time for Time.  

[<< ***Back to contents***](#table-of-contents)

### Business Goals

The Goals as a business are:

+ To create a large community of members to provide a diverse mix of talents.
+ To create a large community of members to build a substantial subscription income - which will be passed onto charity.

[<< ***Back to contents***](#table-of-contents)

## User Stories

1.  As a non-member: I want to visit the homepage of the site and get a clear overview of what the site does and how I can sign up.
2.  As a Free member I want to be able to sign in to eHand and view Posts and offer help
3.  As a premium member when I create my membership, I want to know my payment donates to a charity
4.  As a premium member when I create my membership, I want to be awarded the 10t (free hours of Time) to spend on the site.
5.  As a premium member I want to be able to create a Notice looking for help.
6.  As a Premium member I want other members to be able to see my Notice - and offer help.
7.  As a premium member I want to be able to offer my help to others.
8.  As a premium member I want to be able to transfer my time to another member who helped me.
9.  As a premium member I want to be able to accept payment of time from a member I helped. 
10. As a premium member I want to get a notification when I log in - if another member has offered help
11. As a member I want a way to communicate with a member who is offering help, or if I am offering it.
12. As a member I would like to see commitments I have made in my profile
13. As a member I would like to see my notices in my profile.

[<< ***Back to contents***](#table-of-contents)

---   


# UI

eHand will use the Bootstrap framework to create a clean uncluttered intuitive layout. 
The layout will be responsive having been built from a mobile-first perspective.   
The Navbar is positioned down the page 200px as a default position - and will retreat to a fixed position, by way of some custom JavaScript, to
 the top of the page allowing content to disappear underneath it when the user scrolls.   
 The navbar will be almost focal, clean crisp and simple, with a very simple lime green glow and gradient hover effect
reverting to the simpler ghost white when not being interacted with.

The logo and choice of colours were to achieve a nice contrast between a grey hand background image and the lime green colour.
The logo was designed with pastel type colours, so it's visible when needed - but not to take over the page.

[<< ***Back to contents***](#table-of-contents)

## Colours

I choose a green and grey mix, as I find them an unusual, yet a comfortable mix of colours. The grey can be dull, but I find that the slightest touches
of a ***Wow*** colour such as the lime green, give a wonderful contrast that lifts the page.
Other bootstrap standard colours are used in places where the lime green would have been too overpowering.

*   [Ghost-white(#f8f8ff)](https://www.color-hex.com/color/f8f8ff) - will be used for windowed areas.
*   [#555555](https://www.color-hex.com/color/555555) -  as the main font colour
*   [lime green(#c2fa00)](https://www.color-hex.com/color/c2fa00) - used in all areas for text, borders, highlighting etc.  

[<< ***Back to contents***](#table-of-contents)

## Fonts

The font chosen for this site is Nunito. I liked the clear simple rounded style, which fitted with the simple clean feel of the planned site.

[<< ***Back to contents***](#table-of-contents)

## Styling

Rounded corners and gentle hover effect shading along with fade-in elements were deliberate to give a smooth relaxed feel
to the visitor as each page gently fades into view.   
A current username or logged-in status deliberately styled to be subtle, is positioned opposite the logo, just to indicate current logged-in status.   
The site logo retreats from view when the page is scrolled, returning with the lowered navbar when the page is scrolled to the top.

[<< ***Back to contents***](#table-of-contents)

## Wireframes

[Home Page: ](https://github.com/Mr-Smyth/eHand/blob/master/docs/wireframes/home-wireframe.pdf)   
[Register Page: ](https://github.com/Mr-Smyth/eHand/blob/master/docs/wireframes/register-wireframe.pdf)   
[Sign In Page: ](https://github.com/Mr-Smyth/eHand/blob/master/docs/wireframes/sign-in-wireframe.pdf)   
[Upgrade Page: ](https://github.com/Mr-Smyth/eHand/blob/master/docs/wireframes/upgrade-wireframe.pdf)   
[Create a Notice: ](https://github.com/Mr-Smyth/eHand/blob/master/docs/wireframes/create-notice-wireframe.pdf)   
[Notices: ](https://github.com/Mr-Smyth/eHand/blob/master/docs/wireframes/notices-wireframe.pdf)   
[Profile Page: ](https://github.com/Mr-Smyth/eHand/blob/master/docs/wireframes/profile-wireframe.pdf)   
[Profile - My Notices: ](https://github.com/Mr-Smyth/eHand/blob/master/docs/wireframes/my-notices-wireframe.pdf)   
[Profile - Commitments: ](https://github.com/Mr-Smyth/eHand/blob/master/docs/wireframes/commitments-wireframe.pdf)



# Features 

![Home](https://i.ibb.co/VppdCnw/image.png "Home Page example")  

## Existing Features

### Common site elements

#### Logo
Designed by myself, plays on the name using distorted lines from a lowercase letter 'e', to form the likeness of a hand. 
The colours are a Kaki type [green](https://www.color-hex.com/color/6B7365)  and a pastel [indigo/grey](https://www.color-hex.com/color/656573)
to form the text part of the logo. The logo was created using [Paint dot net](https://www.getpaint.net/features.html).

#### A Navbar

Common to every page, the same navbar styling will be applied it will only show links relevant to the user's login status.  
An additional navbar is included in the Profile section, to allow simple navigation to important information such as the user's commitments and the users own notices.

![NavBar](https://i.ibb.co/nwgn9wB/image.png "NavBar")

#### Information area

Common styling of ghost white and grey font will be applied, with a faint lime green border, matching the rest of the site. 
Page headings when required will be in [lime green(#c2fa00)](https://www.color-hex.com/color/c2fa00), providing clarity to the user.

#### Footer
A common footer with social media links will also the bottom of the page. Hovering reveals individual colours relevant to each link.   

![Footer](https://i.ibb.co/m6m9hVM/image.png "Footer section")


### Home Page

Site common styled containers gently fade into view on scrolling. The top 3 containers provide the user with a brief, what, why and how about eHand. 
These containers also provide links to read more on that particular subject. Clicking on this will take the user down to a further reading information section with an action button to get started.   
Clicking on **get started** brings the user to the membership upgrade page, if the user is not signed in, the user will be taken to the sign-in page, with option
to register if a new user.   

The home page information section has a background with a varied degree of opacity to remove the dullness that I felt a solid grey background was giving. This keeps the user's attention on the information,
while also providing a nice clouded experience of the background as they scroll.

[<< ***Back to contents***](#table-of-contents)

### Notices page

The notices page is the only page, other than the home page, which a non authenticated user can access. 
It displays the complete listing of notices in a paginated view.   

![Notice](https://i.ibb.co/jyqn0T8/image.png "Notice example")    

The Notice displays the bare bones of the requested task, clicking on the Details button will take the user to a more detailed page to display
the complete details of the notice, with a comments section for further questions.   
A Premium or Free member may click details and interact in any way possible with the notice, including committing to help the author of the notice.   

A non-logged-in member is unable to access the details and can only view the notice summary - seen in the image above. The Details button does remain though for the un-logged in visitor to see and possibly click on
and if they do click on Details they will be routed to the Sign In Page.

[<< ***Back to contents***](#table-of-contents)

### Create Notice page

Reachable from the notices page via a link at the top of the page.

This link is only available for Premium members and will not be visible to Free or non-members. Attempting to gain entry via the URL, will result in a 403 - Forbidden.

The create Notice page features a form with which the member can fill in the details of the help they require, and then submit the form to post it as a notice in the Notices section of the site. 
The member will also be able to view and edit this notice from their commitments page within their Profile section.   
By default, all notices are linked to the correct author.

[<< ***Back to contents***](#table-of-contents)

### Notice Details page

This page is reachable by clicking on the Details button on a notice. There are a few situations where the Details button is not able to be clicked on:

+ If the visitor is not an authorized member of eHand.
+ If the Notice has already been committed to by another member.

Once in the Details of a Notice, you will see 2 containers. The first container holds all the details entered for the notice, along with some 
relevant action buttons.   
The 2nd container contains a comments section enabling communication of queries between author and members interested in helping. This uses a fetch in JS to update the page with the chat without reloading.

![Details](https://i.ibb.co/nBS0gww/image.png "Notice Details example")  

[<< ***Back to contents***](#table-of-contents)

### Profile

The profile main page holds the details of the member signed in. If entered it will display all the user's information, if they have chosen to enter it.
A user can click on the Edit Profile button in the profile information section to edit their profile.   

If the member viewing the page is a Premium Member, then their TIME Account balance is displayed.   

To the right of the profile information is the member's current membership status, and an action button to act on this.

![Profile](https://i.ibb.co/Pgr5qrP/image.png "Example profile page")

[<< ***Back to contents***](#table-of-contents)

### My Commitments

Reachable from the profile page. The My Commitments page holds a copy of all the notices the current member has committed to. Each notice is displayed with full details.
An option to remove commitment to notice is at the bottom of each notice.

[<< ***Back to contents***](#table-of-contents)

### My Notices

Reachable from the profile page. The My Notices page displays all the current notices that the current member has created.   
An option to update the notice or delete it is available in this view at the bottom of each notice, these buttons will only display if the notice has not been committed to yet.
Once the message has another member committed to it, then it obviously should not be possible to change the notice or delete it.   

The complete notice button appears once the notice has been committed to by another member. Once clicked eHand will check if the member who helped, is a valid premium member.
If the member is a valid premium member, then a transfer of a Time payment - ***amount outlined in the notice*** - will take place.  
If the member is ***Not*** a valid Premium member, then ***No*** payment will take place, as Time accounts are a Premium feature.
The member who committed to the notice will then be removed from the notice.   
The user will then receive an option allowing them to delete the message, or not. The reason for the option is simply if the author would like 
to keep and edit the message as a new notice.

![MyNotices](https://i.ibb.co/CMyLmcC/image.png "Example My Notices page")

[<< ***Back to contents***](#table-of-contents)

### Upgrade 

The upgrade page is reachable from the main nav bar, or from the discover premium button inside the profile page.   
As the name suggests this page allows the user to view the benefits of upgrading to Premium and gives them an option to select Premium.

[<< ***Back to contents***](#table-of-contents)

#### Selecting Premium

Selecting Premium from the Upgrade page brings the user to the payment screen where they can enter their card details to subscribe to the monthly payment and become a premium member. After payment, the user will be returned to the profile screen showing their new time account and balance.

![Upgrade](https://i.ibb.co/DbNQm09/image.png "Example of an upgraded membership success")

[<< ***Back to contents***](#table-of-contents)

## Features for future consideration

*   Social media involvement - I had hoped to include social media sign-in, in this project. Unfortunately, I had some trouble with the Google API,
     which I feel will need further testing, within this project, for me to be confident that it is stable.
*   Introduce a more global chat option where all members can chat, also include posting pictures to better describe a situation.
*   Implement more incentives to gain Time - Introduce a notice board for charity events. Organisers of these events get a Time bonus.
*   Make the time payments into half and quarter-hour denominations.
*   Add a contact page, for member queries.

[<< ***Back to contents***](#table-of-contents)

---

# Tech

The following list of technologies was used in the development of eHand.

*   [Django](https://www.djangoproject.com/) - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
*   [Python3](https://www.python.org/) - Python is an interpreted, high-level and general-purpose programming language. Python 3 was used as the core language in this project.
*   [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - JavaScript is a scripting or programming language that allows you to implement complex features on web pages.
*   [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) - CSS describes how HTML elements are to be displayed on screen.
*   [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - HTML5 is the latest version of Hypertext Markup Language, the code that describes web pages.
*   [Bootstrap4](https://getbootstrap.com/) - Bootstrap is the most popular CSS framework for developing responsive and mobile-first websites.
*   [Google Fonts](https://fonts.google.com/) - Google Fonts is a library of free licensed font families.
*   [Favicon.io](https://favicon.io/) - A Favicon generator
*   [Allauth](https://django-allauth.readthedocs.io/en/latest/) - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.
*   [Stripe payments](https://stripe.com/docs) - Stripe offers payment processing software and application programming interfaces for e-commerce websites and mobile applications.
*   [AWS](https://aws.amazon.com/) - Amazon Web Services is a subsidiary of Amazon providing on-demand cloud computing platforms and APIs
*   [Heroku](https://www.heroku.com/) - Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
*   [Heroku PostGres](https://www.heroku.com/postgres) - Heroku Postgres is a managed SQL database service provided directly by Heroku.
*   [GitHub](https://github.com/) - GitHub is a provider of Internet hosting for software development and version control using Git.
*   [Font Awesome](https://fontawesome.com/) - Font Awesome is a font and icon toolkit based on CSS and Less.
*   [Imgbb](https://mr-smyth.imgbb.com/) - Imgbb is a free image hosting that will solve many of your file storage problems and works really well as a photo organizer.
*   [W3 Markup Validator](https://validator.w3.org/) - The Markup Validation Service is a validator by the World Wide Web Consortium (W3C) that allows Internet users to check HTML and XHTML documents for well-formed markup.
*   [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) - W3C CSS Validation Service is a free software created by the W3C to help Web designers and Web developers check Cascading Style Sheets (CSS).

[<< ***Back to contents***](#table-of-contents)

---

# Deployment

## Steps to deploy eHand to Heroku using Postgres

### In Heroku:
1. Setup and account and log in to Heroku
2. On the apps page select `NEW`.
3. Give the app a name and select the closest region – then click `Create App`.
4. Click on Resources tab to provision a new Postgres database for it.
5. Search in the Addons search bar for `Heroku Postgres`.
6. Select your Development plan (in my case - Hobby Dev Plan).

### In GitPod or IDE:
7. To use postgres open project in GitPod and install:
```
*   pip3 install dj_database_url
*   pip3 install psycopg2-binary
*   Update requirements: pip3 freeze > requirements.txt
```

### In Django - setup new database:
In `Settings.py`:   

8. Make sure import os is there.
9. Add: `import dj_database_url`.
10. Goto Database settings and comment out existing database setting and add below example to point the database at the new Postgres database.
```
example:
    DATABASES = {
        'default': dj_database_url.parse( # ***paste in the database URL from Heroku***)
    }
```
11. Run Migrations. `Migrations have now been made to the Postgres Database.`
12. After a Successful Migration goto memberships.models.

---
***Important:***

13. Comment out the `post_save_create_memberships` signal - ***this is because creating a user will trigger this signal to create a free membership. 
But as there will be no packages setup within our new database - we must stop this signal before we create our superuser.***   
---
14. Now we can create a superuser -: `python3 manage.py createsuperuser`.
15. Runserver and login as superuser to the admin page.
16. Goto Packages in the memberships section.
17. Click add package to add each of the following 2 packages
*   package type: free.
*   package price: 0.
*   stripe plan id: (price_id) get this from your stripe - Products - Free Plan - Pricing - API id.   

***and***  
*   package type: premium.
*   package price: 5.
*   stripe plan id: (price_id) get this from your stripe - Products - Premium Plan - Pricing - API id.
18. Save and logout of admin.
19. Stop the server.
20. Uncomment the signal from step 13.
21. Restart the server and check admin - the superuser will now be linked to a free package type and have a stripe customer id.
22. Goto Settings -  Database settings - remove the Postgres database URL.
23.  Create an if/else code block to check if the os.environ variable is defined. 
if it is defined that will mean we are on Heroku so we will use the Postgres database.
Else we will be in our local environment and so use the default database.
```
    Example: 
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
```

24. In the Terminal install gunicorn as our webserver: `pip3 install gunicorn`
25. Freeze requirements. `Pip3 freeze > requirements.txt`
26. Create a Procfile at the same level as the project. 
27. Enter the following code into the Procfile to tell Heroku to create a web dyno that will run gunicorn and serve eHand:
```
    web: gunicorn ehand.wsgi:application
```
28. Temporarily disable collect static – to do this:
*   login via the terminal: heroku login –i.
*   Enter heroku email and password.
*   Enter the following in the terminal:
```
    heroku config:set DISABLE_COLLECTSTATIC=1 --app mr-smyth-ehand
```
In `Settings.py`:   

29. Add the hostname of the Heroku app – to ALLOWED_HOSTS (also include localhost):
```
    ALLOWED_HOSTS = ['mr-smyth-ehand.herokuapp.com', 'localhost'].
```
30. Ensure all .env variables such as the Django and stripe secret keys remain private. Also, make sure they are set up inside Heroku's config vars.

In `The Terminal`:

31. Deploy to Heroku:
*   Add and push to GitHub
*   git add .
*   git commit –m “**your-message**”
*   git push
*   Now initialize heroku git remote (because we created our app on the website rather than with the CLI): 
*       heroku git:remote -a mr-smyth-ehand
*   Then push to heroku : git push heroku master

In `The Heroku`:

32. Setup automatic deployment in Heroku:
*   Goto the deploy tab
*   Set deployment method to GitHub
*   Search for ehand
*   Click connect
*   Scroll down and click Enable Automatic Deploys

ehand is now deployed to Heroku

[<< ***Back to contents***](#table-of-contents)

## Local Deployment

**Before starting, some prerequisites:**

*   Before starting you should have an IDE set up - [Visual Studio Code](https://code.visualstudio.com/). - for example.
*   Its advisable to have a virtual environment setup. Pythons own can be used : 

```
    python3 -m .venv venv
    .venv\Scripts\activate
```

*   Have **at least** the following installed:   
    *   Python3 - to run the application.
    *   Pip - to install any requirements.
    *   GIT - required for version control.

### Steps to Deploy

1.  Open a Git Bash Command line, in your preferred destination.
2.  Enter git clone and paste in this link `https://github.com/Mr-Smyth/eHand.git`.
3.  Open the cloned repo in your IDE.
4.  Create a .env file containing private credentials.
```
Example of env file

DEVELOPMENT_LOCAL=True
SECRET_KEY=*C*O*D*E**H*E*R*E*
STRIPE_PUBLIC_KEY=*C*O*D*E**H*E*R*E*
STRIPE_SECRET_KEY=*C*O*D*E**H*E*R*E*
```

The above example displays an env for a local purpose only.

5.  Install all requirements for the application by using this command:
```
    sudo -H pip3 -r requirements.txt
```
6.  In the IDE terminal, use the following command to start eHand:
```
    python manage.py runserver
```

eHand should now be running locally on localhost port 8000. (http://127.0.0.1:8000)

7.  After running Django initially, it will create the local database **db.SQLite3**.
8.  Make all migrations:
```
python3 manage.py makemigrations --dry-run
python3 manage.py makemigrations
python3 manage.py migrate --plan
python3 manage.py migrate
```

9.  Create a superuser:
```
python3 manage.py createsuperuser
***Enter username, email and password***
```

You should now have a local copy of eHand.

[<< ***Back to contents***](#table-of-contents)

---  
# Testing


## Testing results:

**A full and thorough continuous testing was performed on this project, the results of which can be found here:**

[Click here to view testing procedures and results](https://github.com/Mr-Smyth/eHand/blob/master/docs/testing.md)

## Testing Existing bugs.

During development, I had a serious issue where my link to the Google API, allowing me to sign in using an active google account was 
very inconsistent in its reliability on local development.
It works fine on the deployed site and often works on the local development, I have not been able to get to the bottom of this 
problem and have decided not to include it in this version.


[<< ***Back to contents***](#table-of-contents)

---  

# Credits

## Content and code
[Django Documentation](https://docs.djangoproject.com/en/3.1/) - for clear easy to understand content.  
[Stripe payments documentation](https://stripe.com/docs/payments?payments=popular) - Great content, took a few times, but we got there.  
[Chris Z](https://github.com/ckz8780) - My guide into the world of Django. Fantastic lessons and he is also a perpetual source of guidance and help on Slack.  
[Kevin Powell](https://www.youtube.com/channel/UCJZv4d5rbIKd4QHMPkcABCw) - for his lesson on Fade in elements.

[<< ***Back to contents***](#table-of-contents)

## Media

*   [Paint dot net](https://www.getpaint.net/features.html) - Used for creating eHand Logo.
*   [Font Awesome](https://fontawesome.com/) - Used quite a lot in this project, very happy with the outcome.
*   [Favicons](https://favicon.io/) - Solid site icon.
*   [Imgbb](https://mr-smyth.imgbb.com/) - Imgbb was used to store Readme related images.

[<< ***Back to contents***](#table-of-contents)

# Acknowledgments

Special Thank you to my mentor Aaron Sinnott, for his time, knowledge and clear guidance throughout this project, and the Diploma as a whole.
Thank you to the slack community, past and present. With slack, I was able to stand on a lot of shoulders to get this across the line.

[<< ***Back to contents***](#table-of-contents)

# Contact
If you have any questions relating to this project, please feel free to email me anytime:   

**e.smyth75@gmail.com**

# Disclaimer

The content of this Website is for educational purposes only. Users enter data at their own risk.

[<< ***Back to contents***](#table-of-contents)