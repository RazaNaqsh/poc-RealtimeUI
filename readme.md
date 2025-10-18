# Architecture of the application

A single docker compose file to run the application at once.

The application will contain :
 - UI - 3000
 - Backend -3001
 - Postgres DB to store the data - 8081
 - PGadmin to show the DB - 8082

Later if i want i can include following services for better learning:
- Keycloak
- Celery (if needed)