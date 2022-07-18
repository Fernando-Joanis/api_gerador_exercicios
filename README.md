# api_gerador_exercicios

Essa aplicação tem como objetivo gerar exercícios matemáticos para estudantes do ensino fundamental

Para rodar a aplicação localmente, é só instalar o requiremtens.txt, e no terminal rodar o comando (python manage.py runserver)

Conceito: Ter 2 api, uma que retornará um json com os números de operações seguindo os parâmetros solicitados.

Outro que já retornará um arquivo PDF formatado com as operações seguindo os parâmetros solicitados.

Rotas (em desenvolvimento)

Conceito: url url.com/api/v1/linear/

Demais informações passadas no post body.

post_body = {"operador":"div", "ordem"="n", "intervalo1"=1, "intervalo2"=10}
operadores disponiveis = soma, sub, multi, div
ordem = n, s
intervalo1 = -9999/9999
intervalo2 = -9999/9999

Em casos como divisão, você terá a opção de com ou sem resto. Portanto, o maior número sempre será o dividendo.

Operações que teremos: Adição, Subtração, Multiplicação, Divisão, Fração, Equações de 1 Grau, Tabuada.
