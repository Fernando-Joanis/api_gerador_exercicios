from rest_framework import serializers


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


class ExerciciosSerializers(serializers.ModelSerializer):

    class Meta:
        model = Exercicios
        fields = Exercicios().gerador()
