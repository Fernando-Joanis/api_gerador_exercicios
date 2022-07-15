from rest_framework.views import APIView
from rest_framework.response import Response
from django import FileResponse
from random import randint


class Exercicios:

    operador = '+'
    def gerador(self):
        x = 1
        x_final = 56
        exercicios = {}
        while x <= x_final:
            fator1 = randint(1, 100)
            fator2 = randint(1, 100)
            exercicios[x] = f'{x}) {fator1} + {fator2} = '
        return exercicios

class ExercicioAPIView(APIView):
    """
    API Exercicios Matematicos
    """

    def get(self, request):
        return Response(Exercicios().gerador())
