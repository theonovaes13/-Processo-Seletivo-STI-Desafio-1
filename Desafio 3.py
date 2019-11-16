import csv

lista_local = []   #esta lista vai guardar as informaçoes do arquivo
with open('alunos.csv', 'r') as arq_alunos:
    info_alunos = csv.reader(arq_alunos)
    for line in info_alunos:
        lista_local.append(line)  #gravando as informacoes do arquivo numa variavel do programa nao relacionada ao objeto


matricula = input("Digite o numero da sua matricula: \n")
grava_linha = 0 #esta variavel vai guardar a linha onde está localizado o aluno
marca_linha = 0 #esta variavel vai marcar a linha da tabela onde está sendo lido o arquivo
for line in lista_local:
    if line[1] == matricula: #essa condicao testa se o numero de entrada condiz com alguma matricula do arquivo
        grava_linha = marca_linha
    marca_linha += 1

aluno_ok = 0 #essa variavel vai testar se o aluno foi encontrado para, caso se, entao criar as opcoes de email
if grava_linha == 0: #caso a matricula nao seja encontrada, o valor de grava_linha vai continuar 0
    print("O aluno nao pode ser encontrado")
else:
    if (lista_local[grava_linha][5] == "Ativo") and (lista_local[grava_linha][4] == ''):
        aluno_ok = True
        #ou seja, se o aluno estiver com matrícula ATIVA e possuir a caixa de informação de iduff VAZIA:
        nome = lista_local[grava_linha][0].split(" ")
        opcao = []
        opcao.append(nome[0]+nome[1]+"@id.uff.br") #JoaoBraganca@id.uff.br
        opcao.append(nome[0]+nome[2]+"@id.uff.br") #JoaoSilva@id.uff.br
        opcao.append(nome[0][0]+nome[2]+"@id.uff.br") #JSilva@id.uff.br
        opcao.append(nome[0][0]+nome[1][0]+nome[2]+"@id.uff.br") #JBSilva@id.uff.br
        opcao.append(nome[0]+nome[1][0]+nome[2]+"@id.uff.br") #JoaoBSilva@id.uff.br
        opcao.append(nome[0][0]+nome[1]+nome[2]+"@id.uff.br") #JBragancaSilva@id.uff.br
    else:
        if lista_local[grava_linha][5] == "Inativo":
            print("A sua matricula nao se encontra ativa, procure a coordenacao. \n")
        if lista_local[grava_linha][4]:
            print("Voce ja possui um email IDUFF, que é : " + lista_local[grava_linha][4])


if aluno_ok:
    print(nome[0]+", por favor escolha uma das opcoes abaixo: \n")
    for a in range(6):
        print(str(a+1)+" - "+opcao[a])

    email = int(input())

    if email > 6 or email < 1:
        print("Escolha uma das opcoes validas")
    else:
        lista_local[grava_linha][4] = opcao[email-1]
        print("A criação de seu e-mail (" + opcao[email - 1] + ") será feita nos próximos minutos. \nUm SMS foi enviado para " + lista_local[grava_linha][2] + " com a sua senha de acesso.\n")
with open("alunos.csv", 'w', newline= '') as escreve_arquivo:
    escrever = csv.writer(escreve_arquivo)
    for line in lista_local:
        escrever.writerow(line)