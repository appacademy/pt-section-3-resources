# Python Flask Group Project
This is your only group project
here at App Academy.  You will have 2-3 other students on your team to complete
this project.  Very often, because this is the only non solo project, this could
very well be your most complete clone site!

## Important Notes
- Please note that **multiple user types upon sign-up creation are not allowed**. *(Ex- Business owner and customers)*

- *Please do not reference the **exact name** of the target website as this will be flagged by Google for being deceptive.*

- *If your feature includes an image or video upload, include AWS s3 buckets for file uploads.*

- *Students who plan to update, add, or remove their user stories during project development need to be approved by their Project Manager.*

- Avoid using copyright resources for seed data.

## Using External Packages (NPM / PIP)

* Any package *(outside curriculum)* needs to be approved by your Instructor
* CSS frameworks *(Tailwind, Bootstrap, MaterialUI, etc.)* are **not allowed**
* No Copying and Pasting CSS code

*Any questions related to third-party APIs (AWS, Google Maps, Socket.io, NPM Packages, etc.) that are outside of the curriculum are the student's responsibility to debug. Instructor's may offer advice/guidance but are not expected to help debug.*

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
- Faker
- React Drag and Drop *(https://github.com/atlassian/react-beautiful-dnd)*
- Rich Text Editor's
- React star ratings
- Carousel packages

**Please note that some packages require you to add information to your environment variables. Adding these to your local .env does *NOT* affect your Render deployment. You will need to be sure to also add that information to your Render Environment variables.**


## Workflow Expectations

### Do not Silo into Frontend/Backend
* Every team member should be working throughout the entire tech stack in your project.

### GitHub
* Utilize creating a KanBan Board on Github to effectively manage your time in completing tasks and objectives.
* Make sure to push to GitHub daily. *(We want to see that garden green)*
* You are encouraged to use branches to complete your features and to push to your main branch when you have working functionality.
   * Please remember to test the feature not only on local but on Production as well to ensure it works as expected.

### Good Question Template

To ensure the quickest possible response to a question, you are encouraged to literally copy, paste, and fill this out when asking a question in Slack.

1. What feature/task are you working on? (modals, API routes, React components, Reducer, etc)
2. Describe the problem (what are you trying to do? What is it currently doing?)
3. What error messages do you have? (server/front-end console, *if there is one*)
4. What have you done to debug? What have you searched/tried? (THIS IS VERY HELPFUL TO DESCRIBE)
5. Relevant code snippets/screenshots (crop, mark up, or explain them, but make sure that line numbers are visible)

## Reviewing your project

### Error Validations
A User should **NOT** be allowed to update or submit a form with blank or null input fields that are assumed to be required. All input fields within a form are assumed to be required and tested as such. If certain fields within a form are not required, then all required fields must be marked by a different CSS style or an asterisk (*) next to the label to indicate a required field.

Please refer to the Error Validations Repo for more examples.
[Error Messages Considerations](https://github.com/whitnessme/capstone-minimum-required-error-messages)

### CSS Styling
* Do not leave any default styling for HTML elements such as buttons, inputs, text areas, etc.
* CSS must look as if you have made a valiant effort. You are not expected to be a designer, but attention to spacing, font, and layout must be apparent.
* Your site must be intuitive to the user. Users must not have to hunt and guess how to navigate and use your app.

### Prepopulating Data For the Update Form
When a User goes to Edit/Update a resource, the edit form should be prepopulated with the previous data.  Dynamically updating the value of the input field will create a smoother UX for recruiters to look at.


### Test Test Test Your Features
* Students are **expected** and **responsible** to test their deployed app before final grading.
    * Test the CRUD functionality of all implemented features.
    * Test the User Auth (login, sign up, error validations, demo user, logout).
    * Make sure that your site works for new users as well as the Demo/seeded users.
    * Check if the styling is consistent throughout the entire app.


## Some Useful Development Links
* [Flask-SQLAlchemy Quick Reference](https://hackmd.io/@app-academy/flask-sqlalchemy-reference)
* [Express AWS S3 for Image Uploads](https://github.com/jdrichardsappacad/aws-s3-pern-demo)
* [Flask Websockets for Chat Features](https://hackmd.io/oTn-ZTjcQRO5Ghbv9tO9ug)
* [Easy Modals Using React Context!](https://github.com/whitnessme/context-modal-instructions)
* [Using the spread operator](https://dev.to/mlgvla/javascript-using-the-spread-operator-with-nested-objects-2e7l#:~:text=The%20spread%20operator%20only,a%20true%20value%20copy.)
* [low-level and high-level wireframes](https://www.justinmind.com/wireframe/low-fidelity-vs-high-fidelity-wireframing-is-paper-dead)
* [Serialization Volume 1: JSON vs Multipart](https://github.com/bkieselEducational/Serialization)
* [Considerations for a Pleasant User Experience (including pre-population of Edit Form when using image uploads)](https://github.com/bkieselEducational/Considerations-for-User-Experience-in-Web-Development/blob/main/README.md)
