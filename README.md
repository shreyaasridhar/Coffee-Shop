# Coffee Shop Full Stack

This project is done to understand the concepts of access management and permissions for users in a system.

This is a digitally enabled cafe to order drinks. This allows,

* Public users to view drink names and graphics.

* Shop baristas to see the recipe information.

* Shop managers to create new drinks and edit existing drinks.

## About the Stack

### Backend

Flask server with a SQLAlchemy module to interact with a sqlite database. The endpoints are configured and integrated with Auth0 for authentication. 

### Frontend

Ionic frontend to consume the data from the Flask server. Update the environment variables found within (./frontend/src/environment/environment.ts) to reflect the Auth0 configuration details set up for the backend app. 

### Tests

The enpoints are tested with Postman testing tool. Update the file in the `./backend` folder with the appropriate credentials for the JWT tokens from Auth0 to successfully run all the tests.
