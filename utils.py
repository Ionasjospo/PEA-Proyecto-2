import random


def tirarDados():
    resultados = []
    resultados.append(random.randint(1, 6))
    resultados.append(random.randint(1, 6))
    return resultados
    
def tirar1Dado():
    return random.randint(1, 6)

def jugar():
    puntaje = 0
    resultadosPrimerTiro = tirarDados()
    dado1 = resultadosPrimerTiro[0]
    dado2 = resultadosPrimerTiro[1]

    print("Primera tirada: ")
    print("Valor primer dado: ", dado1)
    print("Valor segundo dado: ", dado2, "\n")

    # El jugador tiene un 4 y un numero mayor que 3, no puede repetir la jugada.
    if (dado1 == 4 and dado2 >= 4) or (dado1 >= 4 and dado2 == 4):
        print("Puedes tirar el dado(que no es 4) de vuelta")
        if dado1 == 4:
            puntaje = dado2
            print("Resultado final:",  dado2," puntos.")
        else:
            puntaje = dado1
            print("Resultado final:",  dado1," puntos.")

    # El jugador tiene un 4 y un numero menor que 4, puede tirar de nuevo un dado.
    if(dado1==4 or dado2==4):
        if dado1 == 4 and dado2 <= 3:
            print("Puedes tirar de vuelta el dado 2.")
            print("Deseas tirar de nuevo el dado 2? (s/n) ")
            respuesta = input().lower()
            if respuesta == "s":
                dado2 = tirar1Dado()
                print("Valor segundo dado: ", dado2)
            puntaje = dado2
            print("Resultado final:",  dado2," puntos.")

        if dado2 == 4 and dado1 <= 3:
            print("Puedes tirar de vuelta el dado 1.")
            print("Deseas tirar de nuevo el dado 1? (s/n)")
            respuesta = input().lower()
            if respuesta == "s":
                dado1 = tirar1Dado()
            print("Valor primer dado: ", dado1)
            puntaje = dado1
            print("Resultado final:",  dado1," puntos.")
    
    if dado1 != 4 and dado2 != 4:
        print("Debes tirar de vuelta \n")
        resultadosSegundoTiro = tirarDados()
        dado1 = resultadosSegundoTiro[0]
        dado2 = resultadosSegundoTiro[1]
        print("Segunda tirada: ")
        print("Valor primer dado: ", dado1)
        print("Valor segundo dado: ", dado2,  "\n")
        if dado1 == 4:
            puntaje = dado2
            print("Resultado final:",  dado2," puntos.")
        elif dado2 == 4:
            puntaje = dado1
            print("Resultado final:",  dado1," puntos.")
        else:
            print("Resultado final: 0 puntos.")

    return puntaje