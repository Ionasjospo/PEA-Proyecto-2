import random


def tirarDados():
    resultados = []
    resultados.append(random.randint(1, 6))
    resultados.append(random.randint(1, 6))
    return resultados
    
def tirar1Dado():
    return random.randint(1, 6)

def jugar(puntajeAnterior):
    puntaje = 0
    resultadosPrimerTiro = tirarDados()
    dado1 = resultadosPrimerTiro[0]
    dado2 = resultadosPrimerTiro[1]

    print("Primera tirada: ")
    print("Valor primer dado: ", dado1)
    print("Valor segundo dado: ", dado2, "\n")

    # El jugador tiene dos 4, su puntaje es 4.
    if(dado1 == 4 and dado2 == 4):
        puntaje = dado1
    else:
        # El jugador tiene un 4 y un numero mayor que 3, no puede repetir la jugada.
        if (dado1 == 4 and dado2 >= 4) or (dado1 >= 4 and dado2 == 4):
            if dado1 == 4:
                puntaje = dado2
            else:
                puntaje = dado1

        # El jugador tiene un 4 y un numero menor que 4, puede tirar de nuevo un dado.
        if(dado1==4 or dado2==4):
            if dado1 == 4 and dado2 <= 3:
                if(puntajeAnterior == None):
                    # Estrategia de Juan, si o si debemos tirar de nuevo
                    print("Tiramos de vuelta el dado 2.")
                    dado2 = tirar1Dado()
                    print("Valor segundo dado: ", dado2)
                    puntaje = dado2
                else:
                    # Maria ya sabe el resultado de juan
                    if(puntajeAnterior > dado2):
                        #Tiramos de nuevo porque sino perdemos
                        print("Tiramos de vuelta el dado 2.")
                        dado2 = tirar1Dado()
                        print("Valor segundo dado: ", dado2)
                    puntaje = dado2

            if dado2 == 4 and dado1 <= 3:
                if(puntajeAnterior == None):
                    # Estrategia de Juan, si o si debemos tirar de nuevo
                    print("Tiramos de vuelta el dado 1.")
                    dado1 = tirar1Dado()
                    print("Valor primer dado: ", dado1)
                    puntaje = dado1
                else:
                    # Maria ya sabe el resultado de juan
                    if(puntajeAnterior > dado1):
                        #Tiramos de nuevo porque sino perdemos
                        print("Tiramos de vuelta el dado 1.")
                        dado2 = tirar1Dado()
                        print("Valor primer dado: ", dado1)
                    puntaje = dado1
        
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
            if dado2 == 4:
                puntaje = dado1

    return puntaje