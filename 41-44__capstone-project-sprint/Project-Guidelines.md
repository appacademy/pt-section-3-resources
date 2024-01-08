## Capstone Project Requirements
Projects must have a minimum of **2 working CRUD features** and **base requirements** *(User Auth)* completed by final grade *(W23 D1)*. Only the live site will be used for grading.

![scorecard](https://user-images.githubusercontent.com/76798385/229187286-ba7411c1-5369-4756-9228-e9d3a8234005.png)

**Ex. Project: Airbnb**
- Users (Auth): Create, Read
1. Listings: Create, Read, Update, Destroy
2. Bookings: Create, Read, Destroy (Not Editable)
3. Reviews: Create, Read, Update, Destroy
4. Ratings: Create, Read (Not Editable, Destroyed with Reviews)
5. *Bonus* Search: Backend Fetch w/ Params (ideal), Frontend filtering.
6. *Bonus* Google API: Integration

The first feature has to be **full** CRUD. and the second feature can be **3/4** CRUD or full CRUD. In the example above, the bookings feature has the create, read, and Delete. Ideally, update and delete perform the same action so this feature would be considered 3/4 CRUD.


### Error Validations
A User should **NOT** be allowed to update or submit a form with blank or null input fields that are assumed to be required. All input fields within a form are assumed to be required and tested as such. If certain fields within a form are not required, then all required fields must be marked by a different CSS style or an asterisk (*) next to the label to indicate a required field.

Please refer to the Error Validations Repo for more examples.
[Required Error Messages](https://github.com/whitnessme/capstone-minimum-required-error-messages)

### Prepopulating Data For the Update Form
When a User goes to Edit/Update a resource, the edit form must be prepopulated with the previous data. Using the "placeholder" attribute will **not** be accepted by itself. You must be able to dynamically update the value of the input field. This will create a smoother UX for recruiters to look at.

## The Big Picture

The Capstone Project is an assessment to test your programming and software engineering skills. The ideal expectation is to have a completed MVP (minimum viable product) application done by W45D1, then use the remaining time to refactor to include additional features and/or polish the user interface and improve the user experience. The long-term goal is to present our best work to recruiters to demonstrate our technical abilities.

Remember, a minimum viable product (MVP) is the absolute least you can put out that is also a usable product. For your capstone project, this means 2 fully functional CRUD features with validation error messages that are intuitive and simple to use by someone who has never seen the app before.

We want to make sure we are completing ONE FEATURE before moving on to the next. This feature-driven approach can be seen as an **agile** workflow, whereas the **waterfall** approach can be seen as completing one phase at a time before moving on to the next phase. Agile is an iterative approach where we deliver goals in small incremental amounts. An example of a waterfall workflow would be working on the entire backend first for all features then working on the frontend.

[Agile vs Waterfall Link](https://www.ibm.com/cloud/blog/agile-vs-waterfall)

Students should have a clear road map during the planning phase of what should be the MVPs for their capstone project.

> The end goal is to have 4 features working. After graduation, to be greenlit you will need to have at least 3 features and the Greenlit requirements done in the scorecard. You will have additional time to work on your projects during post-graduation however, it is ideal to shoot for completing the Greenlit requirements early on.

## Mental Health Resources
Taking care of our mental health is an important aspect of our life. Please make sure to take breaks, meditate, sleep, or go for a walk outside to do what's best for you to reduce stress. Here are some resources provided that can be informative.

- [Imposter Syndrome](https://docs.google.com/document/d/1CA5UZwDisg_1WMQIurtDsj4vOkWlZ0cZ/edit)
- [Programmer Imposter Syndrome](https://drive.google.com/file/d/1A6_x1iHqKi1aOAlKKUsx3f-jkhZUZhpM/view?usp=sharing)
- [Anxiety](https://drive.google.com/file/d/13BnCXH7XKsJhQOp_xaBH9E2BAwMTTJ2c/view?usp=sharing)
- [Academic Burnout: How to Prevent it and What to Do](https://drive.google.com/file/d/1oTIKuSqpS6S2bvLWJahQ8xmPDvZeqUqF/view?usp=sharing)
- [Avoiding Burnout](https://drive.google.com/file/d/1viR9dO-xOJSF6ouLsLs4vqvC5Qhy8dZY/view?usp=sharing)


## Cheating
Students plagiarising another student's source code will be dismissed. This is an assessment to utilize the knowledge gained from the previous modules to build what you have learned.

## Some Useful Development Links

* [Flask Project Starter](https://github.com/appacademy/aa19-python-group-project/tree/main)
* [Express Project Starter Frontend (authenticate me)](https://github.com/appacademy/practice-for-sprint-15-react-redux-authenticate-me-for-render-deployment)
* [Express Project Starter Backend (authenticate me)](https://github.com/appacademy/practice-for-sprint-12-authenticate-me-for-render-deployment)
* [Flask-SQLAlchemy Quick Reference](https://hackmd.io/@app-academy/flask-sqlalchemy-reference)
* [Express AWS S3 for Image Uploads](https://github.com/jdrichardsappacad/aws-s3-pern-demo)
* [Flask Websockets for Chat Features](https://hackmd.io/oTn-ZTjcQRO5Ghbv9tO9ug)
* [Easy Modals Using React Context!](https://github.com/whitnessme/context-modal-instructions)
* [Using the spread operator](https://dev.to/mlgvla/javascript-using-the-spread-operator-with-nested-objects-2e7l#:~:text=The%20spread%20operator%20only,a%20true%20value%20copy.)
* [low-level and high-level wireframes](https://www.justinmind.com/wireframe/low-fidelity-vs-high-fidelity-wireframing-is-paper-dead)
* [Serialization Volume 1: JSON vs Multipart](https://github.com/bkieselEducational/Serialization)
* [Considerations for a Pleasant User Experience (including pre-population of Edit Form when using image uploads)](https://github.com/bkieselEducational/Considerations-for-User-Experience-in-Web-Development/blob/main/README.md)


# Phase 1 - Project Approval

## Capstone Project Proposals

Instructors will review your GitHub repo wiki documents based on the submission order. You can view the queue to see when your project is being reviewed in the Capstone Project Proposal Responses Google Spreadsheet. [Link to Proposal Responses](https://docs.google.com/spreadsheets/d/1CkUpeCLUL0x7Oo8aVzzRiR3Kj55GHgHGbTXtsPoapp4/edit?resourcekey#gid=640829555)

## Required Github Wiki Documentation
- Feature List/MVP List
- User Stories
- Database Schema
- API Documentation
- Wireframes

## Additional Recommended Documentation to Create
- Scrum Board/Kanban Board or some Workflow Visualization
- Redux State Shape
- Front End Routes


## The Purpose of User Stories

As you are preparing your documents for project approval, if you are anything like myself, it is quite likely that you'll simply copy the example that we provide and change values where necessary to make it indicative of your app. And then, you will probably forget that you even did that. And if you don't, in both cases, you possibly will have no clear idea about WHY you did it, aside from getting your project approved. I know I did that!! But since my time going through the academy, I can now see the the value and purpose of the User Stories. Not only is this a great format to communicate your application's functionality to your boss or co-workers, but it is also a valuable tool for YOU to use as you actually begin the process of coding out your project.</br>
</br>
With an emphasis on an Agile work flow, which will have you working on a single feature from front to back, you may notice that in setting up your endpoints and routing, that simply making a GET, POST, PUT, DELETE endpoint for your feature MAY not directly correlate with how you will be using any of this data on the front end. It may also not be immediately apparent when you need to have more endpoints than you originally thought. In a lot of cases, this will be apparent when GETting data!! This is actually where User Stories can be very helpful in the development of the backend!! If you consult your User Stories and see that your first feature will have functionality on the frontend that calls for grabbing a single item from the database, this tells you that you will probably need to setup an endpoint with the route /api/feature1/<int:id> GET, for example. You may also notice in your User Stories that your first feature has a link to a page with the 10 newest additions. This may indicate that you need another endpoint where you can grab the newest entries. Something like: /api/feature1/newest GET where you will also need to query the database in such a way that it returns the 10 most recently added items (This is where a column like 'created_at' becomes VERY useful!). And the list can go on!! But I hope that you can already see that the functionality you define as essential to your app, makes it clear what you may need on the backend and frontend alike! Use your User Stories as a way to inform and structure your own workflow!! It works!!

---

## Projects that are not allowed
* Instagram
* Twitter
* Discord
* Projects that the student has already done before in previous modules.
* Mod 4/5 projects (AirBnB, Meetup)

## Using External Packages (NPM / PIP)
**Please Note: Any external packages implemented without your Project Manager's approval are a risk of having to refactor your code**

* Any package *(outside curriculum)* needs to be approved by your **Project Manager**
* CSS frameworks *(Tailwind, Bootstrap, MaterialUI, etc.)* are **not allowed**
* No Copying and Pasting CSS code

*Any questions related to third-party APIs (AWS, Google Maps, Socket.io, NPM Packages, etc.) that are outside of the curriculum are the student's responsibility to debug. IA's may offer advice/guidance but are not expected to help debug.*

### List of Approved NPM Packages
**The NPM packages listed below are already approved, free feel to implement these into your projects**

- Boto3 (AWS)
- Google Maps (@reach/combobox, @react-google-maps/api, use-places-autocomplete...)
- Moment.js
- WaveSurfer.js
- react-player
- Websockets (i.e socket.io)
- Multer
- AWS-SDK
- Faker *(Use the older versions before 6.6)*
- React Drag and Drop *(https://github.com/atlassian/react-beautiful-dnd)*
- Rich Text Editor's
- React star ratings
- Carousel packages

**Please note that some packages require you to add information to your environment variables. Adding these to your local .env does *NOT* affect your Render deployment. You will need to be sure to also add that information to your Render Environment variables.**
