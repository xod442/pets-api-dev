# pets-api-dev
# Running the application

- Checkout code on /opt/pets-api on local computer
- Build the containers: `docker-compose build`
- Copy settings.py.bak to settings.py and add 'mongodb' as MONGODB_HOST
- Start mongodb separately: `docker-compose up -d db`
- Start the app: `docker-compose up web`
- To start the application with pdb enabled: `docker-compose run --service-ports web`

# To access mongodb
- Find the docker web container name and run: `docker exec -it petsapi_db_1 mongo`

# To run tests
- Find the docker web container name and run: `docker exec -it petsapi_web_1 python tests.py`

# Posting a app_id and a app_secret
- Use POSTMAN or application manager to assign new users app ID and password to the database.
POST http://localhost/apps/
```{
  "app-id": "my_company_id",
  "app_secret" : "my_company_pass"
}```
This will assign the users keys to the app.app

# To connect to the mongo db
sudo docker exec -it pets-api_web_run_1 mongo --host mongodb
