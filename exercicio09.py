"""
Exercício 9

A equipe de desenvolvimento de software da 'LinkManager Solutions' está criando uma ferramenta interna para padronizar a construção de URLs de API.
Eles precisam garantir que todas as requisições para seus serviços sigam um formato específico, combinando o domínio principal com os caminhos de acesso aos recursos.
Para isso, você será responsável por desenvolver um programa em Python, executado em blocos no Deepnote, que montará essas URLs.
Este programa ajudará a automatizar a criação de endereços de acesso, otimizando o trabalho dos desenvolvedores ao gerar URLs consistentes.

Tarefa:

Você receberá o domínio base de um serviço (por exemplo, dominio_base = 'api.linkmanager.com'), um nome para o caminho principal (por exemplo, caminho = 'clientes'), um identificador único de recurso (por exemplo, identificador = '123') e uma ação específica (por exemplo, acao = 'detalhes').
A URL deve começar com o domínio base, seguido por uma barra /.
Em seguida, adicione o caminho principal, outra barra / e o identificador único.
Finalmente, concatene mais uma barra / e a ação específica para completar a URL.
O programa deve exibir a URL completa resultante (por exemplo, api.linkmanager.com/clientes/123/detalhes).
"""

dominio_base = "api.linkmanager.com"
caminho = "clientes"
identificador = "123"
acao = "detalhes"

print(f"{dominio_base}/{caminho}/{identificador}/{acao}")