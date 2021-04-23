def c(cor):
    lista = {'sc':'\033[m',
            'white': '\033[1;97m',
            'black': '\033[1;30m',
            'red': '\033[1;31m',
            'green': '\033[1;32m',
            'magenta': '\033[1;35m',
            'yellow': '\033[1;33m',
            'blue': '\033[1;34m'}
    x = lista[cor]
    return x


def titulo(msg):
    tam = len(msg) + 15
    print(f'{c("white")}-={c("sc")}' * tam)
    print(' ' * 20, end='')
    print(f'{c("green")}{msg}{c("sc")}')
    print(f'{c("white")}-={c("sc")}' * tam)

def menu(cabeçalho, item):
    titulo(cabeçalho)
    print(f'{c("green")}Escolha a opção desejada:{c("sc")}')
    for i, v in enumerate(item):
        print(f'    [{c("red")}{i+1}{c("sc")}] {c("white")}{v}{c("sc")}')
    print()
    while True:
        try:
            op = int(input(f'Digite sua opção: '))
            if op >= 1 and op <= len(item):
                break
            else:
                print(f'{c("red")}Opção inválida, tente novamente!{c("sc")}')
        except:
            print(f'{c("red")}Opção inválida, tente novamente!{c("sc")}')
    return op