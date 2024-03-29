from fpdf import FPDF

#dados para colocar no pdf
projeto_nome = input("Digite o nome do projeto: ")
horas_estimadas = input("Horas estimadas: ")
valor_hora = input("Valor da hora: ")
tempo_estimado = input("Tempo estimado: ")

valor_total = int(horas_estimadas) * int(valor_hora)

print("Orçamento gerado com sucesso!")
print("O valor total é R$ ",valor_total)

pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial")
pdf.image("PROJETO/Gerador de Orçamento/template.png", x=0, y=0)

#posicoes para colocar os dados no pdf
pdf.text(115, 145, projeto_nome)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, tempo_estimado)
pdf.text(115, 205, str(valor_total))

pdf.output("PROJETO/Gerador de Orçamento/Orçamento_Projeto.pdf")