"""
Exercício 6

A empresa SecureNet está empenhada em fortalecer a segurança da informação para seus clientes.
Para isso, está implementando novas políticas que exigem a inclusão de caracteres especiais em todas as senhas, além de critérios básicos relacionados ao uso de letras maiúsculas e minúsculas.
Você foi encarregado de desenvolver um pequeno programa em Python, que será executado em blocos no Deepnote, para verificar a conformidade dessas senhas.

Este programa deve analisar a senha fornecida pelo usuário e determinar se ela atende aos requisitos de segurança definidos, garantindo assim uma camada extra de proteção.

Tarefa:

Considerando uma senha inserida pelo usuário por meio de input() (por exemplo, Infnet123!@#), o programa deve:
Verificar a presença do caractere arroba ('@'), do símbolo de exclamação ('!') e do caractere cerquilha ('#') na senha, utilizando o operador in.
Verificar se a senha está composta apenas por letras minúsculas.
Verificar se a senha está composta apenas por letras maiúsculas.
Para cada uma dessas verificações, o resultado deve ser armazenado em variáveis distintas, indicando se cada critério de segurança foi atendido ou não. Exiba cada uma delas devidamente sinalizadas.
"""

senha = input("Insira sua senha: ")

tem_maiuscula = senha.isupper()
tem_minuscula = senha.islower()

tem_especial = "@" in senha and "!" in senha and "#" in senha

if tem_maiuscula:
    print("Todas as letras da senha são maiúsculas.")
else:
    print("O critério de segurança de ter apenas letras maiúsculas não foi atendido.")

if tem_minuscula:
    print("Todas as letras da senha são minúsculas.")
else:
    print("O critério de segurança de ter apenas letras minúsculas não foi atendido.")

if tem_especial:
    print("A senha possui os caracteres especiais necessários.")
else:
    print("O critério de segurança de ter '@', '!' e '#' não foi atendido.")