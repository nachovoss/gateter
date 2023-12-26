# Gateter Web Application

Gateter is a web application developed with Django. This version has been configured to use SQLite as the database, which facilitates deployment and initial setup feel free to chnage it.

## Technical Decisions:

1. **Django**: I have used Django due to its robustness and its ability to quickly develop web applications. It is a technical requirement for the test.

2. **SQLite**: I chose SQLite as the database to simplify the configuration and deployment, ideal for development environments or small applications.

3. **Docker**: The application is dockerized to ensure consistency across different environments and to facilitate its deployment.

4. **Environment Variables**: Sensitive and environment-specific configurations are managed using environment variables. This helps to maintain the security and modularity of the project.

*TODO :
   ADD A NICE FRONTEND 

## Deployment Instructions:

1. **Environment Setup**:
   - Copy the `.env.example` file to a new file called `.env`.
   - Update the variables in `.env` according to your configuration and environment. Currently, it is expected to configure `DEBUG` and `SECRET_KEY`.

2. **Building and Deployment with Docker**:
   ```bash
   docker-compose build
   docker-compose up
   ```

3. **Access**:
   - The application will be accessible at `http://localhost:8000`.


4. **Main Features**:
   - **User Registration**: Users can register on the application using a username and password.
   - **Login**: Users can log in to the application using their username and password.
   - **Posting Meows**: Users can post messages (meows) on the application.
   - **List of Meows**: Users can see a list of the meows posted on the application.
   - **List of Meows by User**: Users can see a list of the meows posted by a specific user at `http://localhost:8000/user/<username>`.