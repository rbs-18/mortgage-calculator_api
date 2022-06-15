# Mortgage calculator
## DESCIPTION
API service for searching and creating mortgage offers.

## ENDPOINTS

### ACTIONS WITH OFFERS
- #### CREATE NEW OFFER
`http://localhost:8000/api/v1/offer/` `POST`

*Request sample (all fields are required)*
```json
{
    "bank_name": "Test_bank_name7",
    "term_min": 20,
    "term_max": 25,
    "rate_min": 6.0,
    "rate_max": 4.0,
    "payment_min": 1000000,
    "payment_max": 10000000
}
```

- #### CHANGE OFFER
`http://localhost:8000/api/v1/offer/<pk>/` `PATCH`

*Request sample*
```json
{
    "bank_name": "Test_bank_name8"
}
```

- #### GET ALL OFFERS
`http://localhost:8000/api/v1/offer/` `GET`

*Request sample*
without data


- #### DELETE OFFER
`http://localhost:8000/api/v1/offer/<pk>/` `DELETE`

*Request sample*
    without data

### FILTRATION OFFERS AND CALCULATE PAYMENT
`http://localhost:8000/api/v1/offer/?price=10000000&deposit=10&term=20` `GET`

Sort is availible by rate and payment

*Request sample*
without data

## PROGRAMMING LANGUAGE

- Python 3.8

## TECHNOLOGY

- Django 2.2
- DRF 3.12
- Docker, docker-compose

## DATABASE

- SQLite (Default)
- PostgreSQL 12.11

## HOW TO START PROJECT

- Clone repository and going:
```bash
git clone ...
```

### With docker (with PostgreSQL)

- Create .env file, define names: DB_ENGINE, DB_USERNAME, DB_PASSWORD, DB_DATABASE, DB_HOST, DB_PORT

example:

DB_ENGINE=django.db.backends.postgresql etc

- Deploy app:
```bash
sudo docker-compose up -d --build
```

- Make migrations:
```bash
docker-compose exec web python backend/manage.py migrate
```
- Reboot app:
```bash
docker-compose stop
docker-compose start
```

### OPTIONS

host: localhost

port: 8000

### Without docker (with SQLite)

- Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
```

-Install dependencies from file requirements.txt:
```bash
pip install -r requirements.txt
```

-Make migrations:
```bash
python manage.py migrate
```

-Run project:
```bash
python manage.py runserver
```

# AUTHORS
*Kozhevnikov Aleksei*
