from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse
from exercicios_lineares.exercicios_lineares import LinearExercises
from utils.gerador_numeros import gerando_numeros


class LinearAPIView(APIView):
    """
    API Exercicios Matematicos

    operador = (soma/multi/sub/div)
    ordem = (n/s)
    intervalo1 = (-9999/9999)
    intervalo2 = (-9999/9999)

    {
    "operador":"soma",
    "ordem":"n",
    "intervalo1":10,
    "intervalo2":100
    }
    """

    def get(self, request):
        return Response('API COM METODOS POST APENAS')

    def post(self, request):
        data = request.data
        operador = operadores(data['operador'])
        ordem = data['ordem']
        intervalo1 = int(data['intervalo1'])
        intervalo2 = int(data['intervalo2'])

        if int(intervalo2) < int(intervalo1):
            intervalo1 = int(data['intervalo2'])
            intervalo2 = int(data['intervalo1'])

        file_path = LinearExercises(operador=operador,
                                    gerador=gerando_numeros,
                                    ordem=ordem,
                                    intervalo1=intervalo1,
                                    intervalo2=intervalo2).questions()
        return FileResponse(open(file_path, 'rb'))


def operadores(operador):
    if operador == 'soma':
        return '+'
    elif operador == 'multi':
        return 'x'
    elif operador == 'sub':
        return '-'
    elif operador == 'div':
        return '÷'
    else:
        return None

