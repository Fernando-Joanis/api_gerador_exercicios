from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse
from exercicios_lineares.exercicios_lineares import LinearExercises
from utils.gerador_numeros import gerando_numeros


class ExercicioAPIView(APIView):
    """
    API Exercicios Matematicos
    """

    def post(self, request):
        data = request.data
        operador, ordem, intervalo1, intervalo2 = validation(data)

        file_path = LinearExercises(operador=operador,
                                    gerador=gerando_numeros,
                                    ordem=ordem,
                                    intervalo1=intervalo1,
                                    intervalo2=intervalo2).questions()
        return FileResponse(open(file_path), 'rb')


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


def validation(data):
    operador = operadores(data['operador'])
    if operador == None:
        return Response('Operador invalido - (soma/multi/sub/div)', status=status.HTTP_400_BAD_REQUEST)

    ordem = data['ordem']
    if ordem != 'n' or ordem != 's':
        return Response('Ordem invalido - (n/s)', status=status.HTTP_400_BAD_REQUEST)

    intervalo1 = data['intervalo1']
    if int(intervalo1) < -9999 or int(intervalo1) > 9999:
        return Response('Intervalo invalido - (-9999/9999)', status=status.HTTP_400_BAD_REQUEST)

    intervalo2 = data['intervalo2']
    if int(intervalo2) < -9999 or int(intervalo2) > 9999:
        return Response('Intervalo invalido - (-9999/9999)', status=status.HTTP_400_BAD_REQUEST)

    if int(intervalo2) > int(intervalo1):
        intervalo1 = data['intervalo2']
        intervalo2 = data['intervalo1']

    return operador, ordem, intervalo1, intervalo2
