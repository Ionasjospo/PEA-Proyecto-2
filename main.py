import  utils

def main():
    print("Juego de dados\n")

    print("Tirada Juan \n")
    resultadosJuan = utils.jugar(None)
    print("-----------------------------------------------------------------------------")
    print("Tirada Maria \n")
    resultadosMaria = utils.jugar(resultadosJuan)
    print("-----------------------------------------------------------------------------")

    print("Resultados finales")
    print("\tJuan: ", resultadosJuan)
    print("\tMaria: ", resultadosMaria)

    if resultadosJuan > resultadosMaria:
        print("Gano Juan")
    elif resultadosJuan < resultadosMaria:
        print("Gano Maria")
    else:
      print("Empate")

main()