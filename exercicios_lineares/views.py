from rest_framework.views import APIView
from rest_framework.response import Response
from django import FileResponse
from random import randint
from exercicios_lineares import LinearExercises


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

    def post(self, request):
        data = request.data
        operador = data['operador']
        ordem = data['ordem']
        intervalo1 = data['intervalo1']
        intervalo2 = data['intervalo2']
        filename = LinearExercises(operador=operador,
                                            gerador=gerador,
                                            pdf=pdf,
                                            ordem=ordem,
                                            intervalo1=intervalo1,
                                            intervalo2=intervalo2).questions()
        return FileResponse(open(filename), 'rb')
