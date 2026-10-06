import notas_ponderadas

print("calcula notas de um aluno")
print()


nota1 = float(input("informe a primera nota:"))
nota2 = float(input("informe a segunda nota: "))
nota3 = float(input("informe a terceira nota:"))

resultado = notas_ponderadas.calcular(nota1, nota2, nota3)



print()
print(f"o resultado é: {resultado:.2f}")  

