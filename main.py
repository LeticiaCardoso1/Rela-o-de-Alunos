class Estudante:
    def __init__(self, aluno, nota):
        self.aluno = aluno
        self.nota = nota

    def aprovacao(self):
        if self.nota >= 7:
            return "Aprovado"
        else:
            return "Reprovado"

aluno = input("Nome do aluno: ")
nota = float(input("Nota do aluno: "))

estudante = Estudante(aluno, nota)
resultado = estudante.aprovacao()
print(f"{estudante.aluno} está {resultado}.")

