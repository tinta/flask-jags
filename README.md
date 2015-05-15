Flask JAGS
==============

Leverage the latest and greatest in frontend and backend technology with Flask JAGS! This template integrates a [Flask](http://flask.pocoo.org/) backend with an [AngularJS](https://www.angularjs.org/) frontend, using [Jade](http://jade-lang.com/) for templating, SCSS for css development, and [Gulp](http://gulpjs.com/) for client side task execution.

## Rationale
Angular is a robust frontend javascript framework. Flask is a small python framework with dead simple URL routing and templating. Now you can enjoy the best of both worlds!

## Requirements


## Setup

    bin/setup_project

## Starting the dev server

    bin/runserver

## Opening a Flask REPL with the app loaded

    cd server/
    python
    >>>  from uwrtourist.routes import app
    >>>  from uwrtourist.models import db
    >>>  with app.app_context():
    >>>     # do your stuff

