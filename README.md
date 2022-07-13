# Quiz (DRF)

**A simple quiz app with _Django Rest Framework_**

There are 4 models in this app:
* Category
* Quiz
* Question
* Answer

Foreign Key Relations:
* Each Quiz has one Category and Each Category has many Quizzes.
* Each Question has one Quiz and Each Quiz has many Questions.
* Each Answer has one Question and Each Question has many Answers.

The quiz topics list are in:
`localhost:8000/quiz/`


The quiz questions of a special topic are available in:
`localhost:8000/quiz/[quiz topic]/`

You can generate a random question by:
`localhost:8000/quiz/random/[quiz topic]/`
