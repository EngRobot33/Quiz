# Quiz (DRF)

**A simple quiz app with _Django Rest Framework_ which you can generate one random question from each quiz topic.**

There are 4 models in this app:
* Category
* Quiz
* Question
* Answer

Foreign Key Relations:
* Each Quiz has one Category and Each Category has many Quizzes.
* Each Question has one Quiz and Each Quiz has many Questions.
* Each Answer has one Question and Each Question has many Answers.

## Installation

* First of all clone the project:
```
git clone https://github.com/EngRobot33/Quiz.git
```
* Then, we need a virtual environment you can create like this:
```
virtualenv venv
```
* Activate it with the command below:
```
source venv/bin/activate
```
* After that, you must install all of the packages in `requirements.txt` file in project directory:
```
pip install -r requirements.txt
```
* Then you should have a superuser for accessing to admin panel:
```
python3 manage.py createsuperuser
```
* After that, migration:
```
python3 manage.py migrate
```
* That's finished now you can run the project:
```
python3 manage.py runserver
```

The quiz topics list are in:
`localhost:8000/quiz/`

Questions of a special topic for e.g. 'linux':
`localhost:8000/quiz/linux/`

For generating a random question from 'linux':
`localhost:8000/quiz/random/linux/`

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


