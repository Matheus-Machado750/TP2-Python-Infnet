"""
Exercício 10

Uma equipe de marketing digital está monitorando o desempenho de suas campanhas em mídias sociais para entender a repercussão de seus conteúdos.
Para isso, eles acompanham a frequência de hashtags específicas em diversas postagens.
É importante que a equipe consiga identificar não apenas o uso exato das hashtags, mas também suas variações de capitalização.
Seu objetivo é desenvolver um programa em Python, a ser executado em blocos no Deepnote, que analise textos de postagens. Este programa fornecerá insights valiosos para a equipe de marketing digital, permitindo avaliar o engajamento do público com suas estratégias de conteúdo.

Tarefa:

A equipe de marketing precisa de um programa que, para uma dada postagem (armazenada, por exemplo, em texto = 'Participe do nosso #PythonChallenge e conquiste prêmios! #pythonchallenge agora mesmo!'), determine a quantidade de vezes que a hashtag #PythonChallenge aparece com a capitalização exata.
Em seguida, é importante verificar quantas vezes a versão minúscula da mesma hashtag, #pythonchallenge, é mencionada no mesmo texto, para entender a variação de uso.
Seu programa deve exibir separadamente cada uma dessas contagens para auxiliar a equipe a analisar a visibilidade da campanha.
"""

texto = "Participe do nosso #PythonChallenge e conquiste prêmios! #pythonchallenge agora mesmo!"

capitalizacao = texto.count("#PythonChallenge")
lower = texto.count("#pythonchallenge")

print(capitalizacao)
print(lower)