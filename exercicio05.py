"""
Exercício 5

O departamento de Recursos Humanos (RH) da empresa está organizando a emissão de crachás para os novos colaboradores.
Para que os crachás tenham uma aparência padronizada e profissional, é essencial que todos os nomes sejam formatados de maneira específica.
O nome completo de cada colaborador e uma versão simplificada para o crachá são recebidos diretamente do formulário de admissão.
Um programa em Python, executado em blocos no Deepnote, será utilizado para processar esses nomes.
O objetivo final é garantir que o sistema de crachás e os registros internos recebam os nomes formatados corretamente, assegurando a padronização necessária.

Tarefa:

Para cada novo colaborador, o programa deve receber duas informações de texto: o nome completo para o cadastro (por exemplo, nome_completo = 'joão silva pereira') e um nome único simplificado para o crachá (por exemplo, nome_cracha = 'joão').
O nome completo deve ser formatado em letras maiúsculas para o sistema interno. Já o nome simplificado para o crachá deve ser tratado de forma que apenas a primeira letra seja maiúscula.
Além disso, uma string de identificação de segurança é requerida, sendo a combinação do nome simplificado formatado, seguido de três hifens, e então o nome completo também já formatado.
O programa deve exibir essas três versões padronizadas do nome.
"""

nome_completo = input("Insira seu nome completo: ")

nome_completo_formatado = nome_completo.upper()

nome_cracha = input("Insira o nome que deve constar no seu crachá: ").capitalize()

identificacao = nome_cracha + "---" + nome_completo_formatado

print(f"Nome completo formatado: {nome_completo_formatado}")
print(f"Nome do crachá formatado: {nome_cracha}")
print(f"String de identificação: {identificacao}")