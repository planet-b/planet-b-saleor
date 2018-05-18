Planet-B
===
[![Build Status](https://travis-ci.org/planet-b/planet-b-saleor.svg?branch=master)](https://travis-ci.org/planet-b/planet-b-saleor)
[![Requirements Status](https://requires.io/github/planet-b/planet-b-saleor/requirements.svg?branch=master)](https://requires.io/github/planet-b/planet-b-saleor/requirements/?branch=master)

[Planet-B homepage](http://planet-b.co/)

# Installation

Pre-install these packages below

- Python 3.4 or later (I recommend to use Anaconda instead)
- Node.js v8 or later
- PostgreSQL version 9.4 or above
- gettext 0.15 or higher: [gettext precompiled binaries for Windows](https://mlocati.github.io/articles/gettext-iconv-windows.html)
- For Linux, also install these packages 
	
	`build-essential libssl-dev libffi-dev python-dev`
[![codecov.io](http://codecov.io/github/mirumee/saleor/coverage.svg?branch=master)](http://codecov.io/github/mirumee/saleor?branch=master)

* * *

Your feedback
-------------

# Setting up
Fill out this short survey and help us grow. It will take just a minute, but mean a lot!

[Survey](https://mirumee.typeform.com/to/sOIJbJ)

* * *

## 1. Node.js

- Update Node.js and npm

	`$ npm install npm@latest -g`

- For Windows, also install Windows-Build-Tools

	`$ npm install --global --production windows-build-tools`

## 2. Setup Python dev environment using Anaconda

We need to setup a separate environment for the project, so we can use either virtualenv or Anaconda

- First update conda before processing

	`$ conda update conda`

- **(Not required)** Add Intel packages channel. I like to use Intel channel, as their build tends to process faster

	`$ conda config --add channels intel`

- Create a new environment for the project. `--name` can be anything, your choice!

        $ conda create --name py3 intelpython3_core python=3 (If you install Intel channel)
        $ conda create --name py3 python=3.5
        $ conda create --name py2 python=2 (Not required for this project)

- Using new environment when working within project:
	- To activate: `$ activate py3`
	- To deactivate: `$ deactivate` or simply closing shell

## 3. Setup project's environment variables

- `SECRET_KEY`: Random secret key for the app
- `DEBUG`: `True`, `False` or empty
- `ALLOWED_HOSTS`: `*` or `localhost, 127.0.0.1, [::1], yoursite.com`. 
- `DATABASE_URL`: `postgres://username:password@host:5432/database`, port is usually `5432`

	> Since we use PostgreSQL, we'll need to put a PostgreSql instance to populate data model. 
	> Typically a PostgreSQL URL looks like above

## 4. Setup gettext

Download the portable zip file, extract and add the bin folder to your path

# Working within project

1. Clone the repository (or use your own fork) and open a new shell inside of the new folder

- Inside of the repo folder, activate the python development environment
	
	```sh
	$ cd planet-b-saleor
	$ activate py3
	```

- Install all python dependencies
	
	`$ pip install -r requirements.txt`

- Prepare the database and populate data models:

	`$ python manage.py migrate`

- Install front-end dependencies:

	`$ npm install`

- Prepare front-end assets:

	`$ npm run build-assets`

- **(Not required)** If you’d like some data to test your new storefront you can populate the database with example products and orders:

	`$ python manage.py populatedb`

- Generate locale binary

	`$ python manage.py compilemessages`

- Start the development server:

	`$ python manage.py runserver`

