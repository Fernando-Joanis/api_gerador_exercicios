from rest_framework.views import APIView
from rest_framework.response import Response
from django import FileResponse
from random import randint
from exercicios_lineares import LinearExercises


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
