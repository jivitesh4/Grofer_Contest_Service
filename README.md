# SIMPLE CRUD API WITH DJANGO REST FRAMEWORK
[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

## Requirements
- Python 3.6
- Django 3.1
- Django REST Framework

## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation.
You can do this by running the command
```
python -m venv env
```

After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running
```
pip install -r requirements.txt
```

## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In our case, we have one single resource, `contest`, so we will use the following URLS - `/contest/` and `/contest/<str>` for collections and elements, respectively:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`contest/generateticket` | POST | Create | Create a single ticket 
`contest/takepart`| POST | Create | Create a new row in UTC table(user ticket contest) and map the ticket to the user and contest
`contest/upcomingevent` | GET| Show | Show the upcoming contests
`contest/lastweekwinners` | GET | Show | Show all the contest in last 1 week 

## Use
We can test the API using [curl](https://curl.haxx.se/) or [httpie](https://github.com/jakubroztocil/httpie#installation), or we can use [Postman](https://www.postman.com/)

Httpie is a user-friendly http client that's written in Python. Let's try and install that.

You can install httpie using pip:
```
pip install httpie
```

First, we have to start up Django's development server.
```
python manage.py runserver
```


The API has some restrictions:
-   The tickets are always associated with the creator (user who created it).
-   Only registered  users may create and take part in contest.


### Commands
```
Generate ticket
http POST http://127.0.0.1:8000/api/v1/contest/generateticket "
Take part in a contest using a ticket
http POST http://127.0.0.1:8000/api/v1/contest/takepart 
Fetch the upcomming contest
http GET http://127.0.0.1:8000/api/v1/contest/upcomingevent  
Fetch all the contest in last 1 week
http GET http://127.0.0.1:8000/api/v1/contest/lastweekwinners 
```

------------------------------------------
Payload for genrateticket api
http://localhost:8000/api/v1/contest/generateticket  
POST request api
{
    "user_id": 4
}

-----------------------------------
Payload to take part in a contest
http://localhost:8000/api/v1/contest/takepart
{
    "user_id": 4,
    "ticket" :"9ce35626-a5dc-11eb-83d0-2c337afdd92c",
    "contest" : "aprilcontest29"

}

====================================
# DataBase
There are 3 tables -
1) User table which store all the user name and there user id
2) UTC table (user ticket contest) which store all the tickets a user have and from which ticket he takes part in ehich contest
3) contest table which store the contest name , time , winner and prize
===================================
# Cron job 
we have create a cron job which at at 8.00pm and get the contest which ends and select a random person from the people who have take part in that contest and makes him the winner and stores it in data base 