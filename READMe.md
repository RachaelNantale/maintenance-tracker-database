
[![Build Status](https://travis-ci.org/RachaelNantale/maintenance-tracker-database.svg?branch=authentication)](https://travis-ci.org/RachaelNantale/maintenance-tracker-database)
[![Coverage Status](https://coveralls.io/repos/github/RachaelNantale/Flask-api-restful/badge.svg?branch=testing-files)](https://coveralls.io/github/RachaelNantale/Flask-api-restful?branch=testing-files)

## Project Link
'https://rachaelnantale.github.io/Maintenance/UI/'

Maintenance App Tracker
======================
 Maintenance Tracker App is an application that provides users with the ability to reach out to operations or repairs department regarding repair or maintenance requests and monitor the status of their request.

## Description
After creating an account, the user can make a repair or maintanenace request which the administrator is able to either approve or reject


## Installation
This is still a stricly online application. work still in progress on getting a mobile app. One only needs to go to the page and create an account and we are good to go.

## Future
* Only building the User Interface elements, pages and views!  
* Planning on  implementing the core functionality later


## Requirements
> pip install -r requirements.txt

## The API Endpoints

| End Point  | Description |
| ------------- | ------------- |
| POST /auth/signup  | Register a user  |
| POST /auth/login  | Login a user  |
| GET /users/requests | Fetch all the requests of a logged in user |
| GET /users/requests/<requestId>/ |  Fetch a request that belongs to a logged in user |
| POST /users/requests |Create a request |
| PUT /users/requests/<requestId> |Modify a request |
| Get /requests/   | Fetch all the requests. Available to only admin |

