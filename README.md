# Coffee Shop Full Stack

This project is done to understand the concepts of access management and permissions for users in a system.

This is a digitally enabled cafe to order drinks. This allows,

* Public users to view drink names and graphics.

* Shop baristas to see the recipe information.

* Shop managers to create new drinks and edit existing drinks.

## About the Stack

### Backend

Flask server with a SQLAlchemy module. The endpoints are configured and integrated with Auth0 for authentication.

### Frontend

Ionic frontend to consume the data from the Flask server. Update the environment variables found within (./frontend/src/environment/environment.ts) to reflect the Auth0 configuration details set up for the backend app. 

Test file using Postman with the appropriate credentials for the JWT tokens from Auth0 can be found in the `./backend` folder.
