# albert_farhutdinov_geekshop

Welcome! My name is Albert Farhutdinov. This is my realization of training project on Django from [geekbrains.ru](https://geekbrains.ru/). 

## Requirements

1. Install the necessary libraries in your virtual environment:

	pip install -r requirements.txt
	
2. Apply migrations:

	python manage.py migrate
	
3. Fill SQLite database.

	python manage.py fill_db
	
4. Also, you need access the Internet to display fonts correctly.

## Start

You can run the following command in terminal from root directory to start a project:

	python manage.py runserver
	
Also. you can change directory to bat/ and use run.bat:

	cd bat
	run
	
Then go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)