nome_aluno = input("Digite o nome do aluno: ") # Armazena o nome do aluno na variavel 'nome_aluno'
idade_aluno = int(input("Digite a idade: ")) # Armazena a idade do aluno na variavel 'idade_aluno'
media_aluno = float(input("Digite a média")) # Armazena a media do aluno na variavel 'media_aluno'

print(f"Nome do aluno é {nome_aluno}, "
      f"ele tem {idade_aluno} anos"
      f"e sua media é {media_aluno:.2f}."
)