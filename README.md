# Epic-Mail
The internet is increasingly becoming an integral part of lives. Ever since the invention of electronic mail by Ray Tomlinson, emails have grown to become the primary medium of exchanging information over the internet between two or more people, until the advent of Instant Messaging (IM) Apps.  As EPIC Andelans who work towards advancing human potential and giving back to the society, we wish to empower others by building a web app that helps people exchange messages/information over the internet and here it is.

#

[![Build Status](https://travis-ci.org/neelxie/epic-mail.svg?branch=challenge3)](https://travis-ci.org/neelxie/epic-mail)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a439c5890cce4f94b3b50e53036c014e)](https://www.codacy.com/app/neelxie/epic-mail?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=neelxie/epic-mail&amp;utm_campaign=Badge_Grade)
[![Coverage Status](https://coveralls.io/repos/github/neelxie/epic-mail/badge.svg?branch=challenge3)](https://coveralls.io/github/neelxie/epic-mail?branch=challenge3)
[![Maintainability](https://api.codeclimate.com/v1/badges/a7d91faedd84ef10c429/maintainability)](https://codeclimate.com/github/neelxie/epic-mail/maintainability)

#
<b> Site has been built with these tools.</b>
*   Language - Python
*   Serverside Framework [![Flask](http://flask.pocoo.org/static/badges/flask-powered.png)](http://flask.pocoo.org)
*   [PostgreSQL](https://www.postgresql.org/)
*   Testing Framework - Pytest
*   Linting Framework - Pylint
*   Style GuideLine - Autopep8

## Application Demo 

*   Check out the [User Interface](https://neelxie.github.io/epic-mail/UI/)

## Features

  | REQUESTS | APP ROUTES | FUNCTION
  |----------|------------|----------
  |  GET | /api/v2/ | Default/Home Page.
  |  GET | /api/v2/messages | Fetch all recieved messages.
  |  GET | /api/v2/messages/unread | Fetch all unread recieved messages.
  |  GET | /api/v2/messages/sent | Fetch all sent messages.
  |  GET | /api/v2/messages/[email_id] | Fetch a specific message by id.
  |  DELETE | /api/v2/messages/[email_id] | Delete message.
  |  POST | /api/v2/messages | Create a message record.
  |  POST | /api/v2/messages/save | Create a message record and save it.
  |  POST | /api/v2/messages/reply/[email_id] | Create a message as a reply to an email.
  |  POST | /api/v2/auth/signup | Register for an account as a user.
  |  POST | /api/v2/auth/login | Log into app account.
  |  GET | /api/v2/auth/users | Get all app users.
  |  GET | /api/v2/auth/users/[user_id] | Get one app user.
  |  POST | /api/v2/groups | Create a group.
  |  GET | /api/v2/groups | Get all groups.
  |  PATCH | /api/v2/groups/[group_id]/name | Change group name.
  |  DELETE | /api/v2/groups/[group_id] | Delete group
  |  POST | /api/v2/groups/[group_id]/users/[user_id] | Add user to group.
  |  DELETE | /api/v2/groups/[group_id]/users/[user_id] | Delete user from group.
  |  POST | /api/v2/docs | API documentation.

## Installation:

*  Clone [this](https://github.com/neelxie/epic-mail.git) git repo to local directory.
``` cd epic-mail ```
*  Create a virtual environment with [Virtual Environments- Python](https://virtualenv.pypa.io/en/stable/) :
``` virtualenv venv ```
*  Activate virtual environment:
``` venv\Scripts\activate ```
*  Install dependencies:
``` pip install -r requirements.txt ```
*  Do not forget to run this in the develop branch:
``` git checkout challenge3 ```

## Running the application:

Inside the epic-mail folder.
``` python run.py ```

## Running the tests:

*  Run this command in the project directory.
``` pytest --cov=.```

## Deployment

*  This app has been deployed on Heroku at the url [here.](https://my-epic-mail.herokuapp.com/api/v1/)

##

* The API documentation can be accessed via the app url at ```https://my-epic-mail.herokuapp.com/api/v1/docs``` or [here](https://app.swaggerhub.com/apis-docs/GreatestCoderEverApi/Epic-mail/1.0.0)

## Contribute

*  Join me [here](https://github.com/neelxie/epic-mail/tree/develop) and let you and me create super amazing stuff together.

## Credits

*  I thank GOD, to whom everything plays out ALWAYS.
*  I would like to thank everyone that inspires me to be better everyday.

## Author

*  Sekidde Derrick
