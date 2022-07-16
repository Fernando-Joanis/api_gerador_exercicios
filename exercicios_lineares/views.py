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
        operador = data['operador']
        ordem = data['ordem']
        intervalo1 = data['intervalo1']
        intervalo2 = data['intervalo2']
        file_path = LinearExercises(operador=operador,
                                    gerador=gerando_numeros,
                                    ordem=ordem,
                                    intervalo1=intervalo1,
                                    intervalo2=intervalo2).questions()
        return FileResponse(open(file_path), 'rb')
