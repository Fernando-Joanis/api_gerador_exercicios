# api_gerador_exercicios

This application aims to generate mathematical exercises to assist in the studies of children in elementary school.

To run the application, just install requirements and in the terminal run the server with the command  (python manage.py runserver)

Concept: Have 2 api, one that will return a json with the numbers of operations following the requested parameters.
Another one that will already return a PDF file formatted with the operations following the requested parameters.

Routes (Under development)
Concept: url = api1.com/?operador=+&inicio=1&fim=10&formato=linear&maior_primeiro=True

In cases such as division, you will have the option of answering with or without remainder. Therefore, the largest number will always be the dividend.

Operations we will have: Addition, Subtraction, Multiplication, Division, Fraction, 1 Degree Equations, Times Tables.
