def c(cor):
    lista = {'sc': '\033[m',
             'white': '\033[1;97m',
             'black': '\033[1;30m',
             'red': '\033[1;31m',
             'green': '\033[1;32m',
             'magenta': '\033[1;35m',
             'yellow': '\033[1;33m',
             'blue': '\033[1;96m'}
    x = lista[cor]
    return x


def titulo(msg):
    tam = len(msg) + 15
    print(f'{c("white")}-={c("sc")}' * tam)
    print(' ' * 20, end='')
    print(f'{c("green")}{msg}{c("sc")}')
    print(f'{c("white")}-={c("sc")}' * tam)


def menu(cabecalho, item):
    titulo(cabecalho)
    print(f'{c("green")}Escolha a opção desejada:{c("sc")}')
    for i, v in enumerate(item):
        print(f'    [{c("red")}{i+1}{c("sc")}] {c("white")}{v}{c("sc")}')
    print()
    while True:
        try:
            op = int(input(f'Digite sua opção: '))
            if 1 <= op <= len(item):
                break
            else:
                print(f'{c("red")}Opção inválida, tente novamente!{c("sc")}')
        except:
            print(f'{c("red")}Opção inválida, tente novamente!{c("sc")}')
    return op


def ExibirTabuada():
    print(f'{c("white")}-={c("sc")}' * 40)
    print(f'{c("red")}{"***** TABUADA *****":^80}{c("sc")}')
    print(f'{c("white")}-={c("sc")}' * 40)
    tab = 1
    v = 0
    alt = False
    for i in range(0, 22):
        for n in range(0, 5):
            print(f'{c("white")}{tab:>2} x {v:>2}{c("sc")} = {c("green")}{tab * v:>3}{c("sc")}', end='')
            if tab != 5 and tab != 10:
                print('   ', end='')
            elif tab == 5 or tab == 10:
                print()
            if tab == 5 and v == 10:
                alt = True
            tab += 1
        if v == 10:
            v = 0
            print()
        else:
            v += 1
        if alt:
            tab = 6
        else:
            tab = 1
