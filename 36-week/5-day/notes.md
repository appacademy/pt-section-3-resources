# Tips for Monday

- Take your time filling out your model and form classes:
    - Ensure all attributes are spelled correctly.
        - Check the spelling for your Model's Column Names.
        - Check the spelling for your Form's Field Name and Label.
    - Ensure you've defined any necessary Form validations and Model constraints.
        - [DataRequired()], nullable=True, etc.
    - Check the docs if your not sure what field you should use in your Forms.
        - https://wtforms.readthedocs.io/en/2.3.x/fields/#basic-fields
        - Reference your PA, Order Up, and Package Tracker to see what we've done before.
    - Check the docs if your not sure what Data type you should use in your models.
        - https://docs.sqlalchemy.org/en/20/core/type_basics.html#generic-camelcase-types

- For debugging:
    - Try migrating your database with alembic, and running your server locally to interact with your site.
        - Remember you need to add a SECRET_KEY to your config if you're trying to run your app locally.
        - Make sure your app's configuration and setup align with what we've done previously.
    - Ensure your route paths are spelled correctly.
    - Ensure you've installed all of the required packages.
    - Ensure you've used double quotes in your Form Template just like we did on the PA:
        - `<form method="post" action="/simple-form">`
    - If you're completely and totally stuck, consider recloning the Assessment since you may have setup your app incorrectly.
        - Your app shouldn't vary significantly from the PA so you may just have a sneaky typo.

*Remember*: You have the entire class period for the Assessment.  Take your time and don't feel rushed!
