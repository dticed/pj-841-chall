def func(pedras="", joia=""):
    contador = 0
    lista_pedras = []
    for i in pedras:
        lista_pedras.append(i)
    for i in lista_pedras:
        for j in joia:
            if i == j:
                contador += 1
    return contador