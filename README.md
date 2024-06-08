### Este é um projeto de implementação simples de uma calculadora em Python, aproveitando a funcionalidade da AWS Lambda. ###

Link para teste da lambda: https://by3otvhojzosk5lfgzzipws2ey0thpju.lambda-url.us-east-2.on.aws/

Corpo esperado pela requisição:

json
Copiar código
```
{
    "oneValue": 15,
    "operation": "soma",
    "anotherValue": 15
}
```
oneValue e anotherValue precisam ser valores numéricos, enquanto operation precisa ser um texto e deve ser um dos seguintes: "soma", "subtracao", "dividir" ou "multiplicacao".

A resposta esperada é um texto com o valor desejado. Partindo do exemplo de corpo da requisição, o retorno seria: 30.

