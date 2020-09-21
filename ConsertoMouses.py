mousesAll = []
mousesOK = []
mousesInutil = []
mousesEsfera = []
mousesLimpeza = []
mousesCabo = []


def verificaNumero(numero):
    try:
        val = int(numero)
        while val not in (0, 1):
            val = int(input("Número inválido, digite 1 ou 0\n"))
        return val
    except ValueError:
        val = input("Número inválido, digite 1 ou 0\n")
        verificaNumero(val)


def relatorioParcial(lista):
    # print([mouse['id'] for mouse in mousesAll if mouse['defEsfera'] == 1])
    print("Nenhum" if len(lista) == 0 else lista)
    print("Total", len(lista))


def relatorioCompleto():
    print("\n---- Identificação dos mouses sem defeito ----")
    mousesOK.sort()
    relatorioParcial(mousesOK)

    print("\n---- Identificação dos mouses que necessitam de esfera ----")
    mousesEsfera.sort()
    relatorioParcial(mousesEsfera)

    print("\n---- Identificação dos mouses que necessitam de limpeza ----")
    mousesLimpeza.sort()
    relatorioParcial(mousesLimpeza)

    print("\n---- Identificação dos mouses que necessitam troca de cabo ou conector ----")
    mousesCabo.sort()
    relatorioParcial(mousesCabo)

    print("\n---- Identificação dos mouses que estão quebrados ou inutilizados ----")
    mousesInutil.sort()
    relatorioParcial(mousesInutil)

    print("\nRelatório - Resumo")
    print("\nQuantidade de mouses cadastrados: {} ".format(len(mousesAll)))

    print("\n% de mouses sem defeito: {}% ".format((len(mousesOK) / len(mousesAll)) * 100))

    mousesUmDefeito = []
    for mouse in mousesAll:
        if buscaApenasUmDefeito(mouse['id']) is True:
            mousesUmDefeito.append(mouse['id'])
    print("\n% de mouses com apenas um defeito: {}% ".format((len(mousesUmDefeito) / len(mousesAll)) * 100))


def existeProduto(id):
    for mouse in mousesAll:
        if mouse['id'] == id:
            return True
    return False


def simNao(resposta):
    resposta = str.upper(resposta)
    while resposta != "S" and resposta != "N":
        resposta = str.upper(input("Resposta inválida, tente novamente. S/N\n"))
    if resposta == "S":
        return True
    elif resposta == "N":
        return False


def buscaSemDefeito(id):
    if id in mousesOK:
        print("Não é possível adicionar um defeito a esse mouse "
              "pois foi este mouse foi marcado como sem defeito")
        resposta = input("Caso ache que isso é um erro, posso remover esse mouse "
                         "da base de dados. Gostaria de removê-lo e retornar ao menu? S/N\n")
        if simNao(resposta) is True:
            mousesOK.remove(id)
            for mouse in mousesAll:
                if mouse['id'] == id:
                    mousesAll.remove(mouse)
            print("Mouse removido com sucesso da base de mouses funcionais\n")
        elif simNao(resposta) is False:
            print("Mouse continuará cadastrado e marcado como funcional\n")
        return True
    else:
        return False


def buscaInutil(id):
    if id in mousesInutil:
        print("Não é possível adicionar um defeito a esse mouse "
              "pois foi este mouse foi marcado como quebrado/inutilizado")
        resposta = input("Caso ache que isso é um erro, posso remover esse mouse "
                         "da base de dados. Gostaria de removê-lo e retornar ao menu? S/N\n")
        if simNao(resposta) is True:
            mousesInutil.remove(id)
            for mouse in mousesAll:
                if mouse['id'] == id:
                    mousesAll.remove(mouse)
            print("Mouse removido com sucesso da base de mouses quebrados\n")
        elif simNao(resposta) is False:
            print("Mouse continuará cadastrado e marcado como quebrado\n")
        return True
    else:
        return False


def buscaApenasUmDefeito(id):
    if (id in mousesEsfera and id not in (mousesLimpeza and mousesCabo)) \
            or (id in mousesLimpeza and id not in (mousesEsfera and mousesCabo)) \
            or (id in mousesCabo and id not in (mousesEsfera and mousesLimpeza)):
        return True
    else:
        return False


def cadastrarNovoProduto():
    mouseTemp = {'id': id, 'defEsfera': None, 'defLimpeza': None, 'defCabo': None, 'defInutil': None}
    mousesAll.append(mouseTemp)

    if simNao(input("Esse mouse está quebrado/inutilizado? S/N\n")) is True:
        mousesAll[-1]['defInutil'] = 1
        mousesInutil.append(id)
        print("Mouse salvo com sucesso!")
    else:
        defEsfera, defLimpeza, defCabo = \
            input("\nEscreva 1 para 'defeituoso' ou 0 para 'funcional' "
                  "em relação aos seguintes defeitos."
                  "Escreva os números separados por vírgula e sem espaço:\n"
                  "1. Esfera\n"
                  "2. Limpeza\n"
                  "3. Troca cabo/conector\n"
                  "Exemplo: 1,0,0\n").split(",")

        defEsfera = verificaNumero(defEsfera)
        defLimpeza = verificaNumero(defLimpeza)
        defCabo = verificaNumero(defCabo)

        mousesAll[-1]['defEsfera'] = defEsfera
        mousesAll[-1]['defLimpeza'] = defLimpeza
        mousesAll[-1]['defCabo'] = defCabo

        print("Mouse salvo com sucesso!")

        if mousesAll[-1]['defEsfera'] == 0 \
                and mousesAll[-1]['defLimpeza'] == 0 \
                and mousesAll[-1]['defCabo'] == 0:
            mousesOK.append(id)
        if mousesAll[-1]['defEsfera'] == 1:
            mousesEsfera.append(id)
        if mousesAll[-1]['defLimpeza'] == 1:
            mousesLimpeza.append(id)
        if mousesAll[-1]['defCabo'] == 1:
            mousesCabo.append(id)


def cadastrarNovoDefeito(id):
    if id in mousesEsfera:
        print("Mouse marcado com defeito de esfera. Você pode adicionar outros defeitos:\n")
        defLimpeza, defCabo = \
            input("Escreva 1 para 'defeituoso' ou 0 para 'funcional' "
                  "em relação aos seguintes defeitos."
                  "Escreva os números separados por vírgula e sem espaço:\n"
                  "1. Limpeza\n"
                  "2. Troca cabo/conector\n"
                  "Exemplo: 1,0\n").split(",")

        defLimpeza = verificaNumero(defLimpeza)
        defCabo = verificaNumero(defCabo)

        mousesAll[-1]['defLimpeza'] = defLimpeza
        mousesAll[-1]['defCabo'] = defCabo

        print("Mouse salvo com sucesso!")

        if mousesAll[-1]['defLimpeza'] == 1:
            mousesLimpeza.append(id)
        if mousesAll[-1]['defCabo'] == 1:
            mousesCabo.append(id)

    elif id in mousesLimpeza:
        print("Mouse marcado com defeito de limpeza. Você pode adicionar outros defeitos:\n")
        defEsfera, defCabo = \
            input("Escreva 1 para 'defeituoso' ou 0 para 'funcional' "
                  "em relação aos seguintes defeitos."
                  "Escreva os números separados por vírgula e sem espaço:\n"
                  "1. Esfera\n"
                  "2. Troca cabo/conector\n"
                  "Exemplo: 1,0\n").split(",")

        defEsfera = verificaNumero(defEsfera)
        defCabo = verificaNumero(defCabo)

        mousesAll[-1]['defEsfera'] = defEsfera
        mousesAll[-1]['defCabo'] = defCabo

        print("Mouse salvo com sucesso!")

        if mousesAll[-1]['defEsfera'] == 1:
            mousesEsfera.append(id)
        if mousesAll[-1]['defCabo'] == 1:
            mousesCabo.append(id)

    elif id in mousesCabo:
        print("Mouse marcado com defeito de cabo. Você pode adicionar outros defeitos:\n")
        defEsfera, defLimpeza = \
            input("Escreva 1 para 'defeituoso' ou 0 para 'funcional' "
                  "em relação aos seguintes defeitos."
                  "Escreva os números separados por vírgula e sem espaço:\n"
                  "1. Esfera\n"
                  "2. Limpeza\n"
                  "Exemplo: 1,0\n").split(",")

        defEsfera = verificaNumero(defEsfera)
        defLimpeza = verificaNumero(defLimpeza)

        mousesAll[-1]['defEsfera'] = defEsfera
        mousesAll[-1]['defLimpeza'] = defLimpeza

        print("Mouse salvo com sucesso!")

        if mousesAll[-1]['defEsfera'] == 1:
            mousesEsfera.append(id)
        if mousesAll[-1]['defLimpeza'] == 1:
            mousesLimpeza.append(id)


#######################################################################################

continuar = True
print("Para encerrar digite 0 na identificação!")
while continuar is True:
    id = int(input("\nDigite o número de identificação do mouse (ou 0 para finalizar o sistema)\n"))
    if (id == 0):  # FINALIZA
        continuar = False
    else:
        if existeProduto(id) is True:
            print("\nA identificação", id, "já existe no cadastro!")
            if buscaSemDefeito(id) is True:
                continue
            elif buscaInutil(id) is True:
                continue
            else:
                cadastrarNovoDefeito(id)
                relatorioCompleto()
        else:
            cadastrarNovoProduto()
            relatorioCompleto()