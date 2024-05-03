import random


def throw_dice():
    results = []
    results.append(random.randint(1, 6))
    results.append(random.randint(1, 6))
    return results
    
def throwDie():
    return random.randint(1, 6)

def play(previus_score):
    score = 0
    result_first_throw = throw_dice()
    die1 = result_first_throw[0]
    die2 = result_first_throw[1]

    print("Primera tirada: ")
    print("Valor primer dado: ", die1)
    print("Valor segundo dado: ", die2, "\n")

    # El jugador tiene dos 4, su puntaje es 4.
    if(die1 == 4 and die2 == 4):
        score = die1
        return score
    else:        
        # El jugador tiene un 4 y un numero mayor que 3, no puede repetir la jugada.
        if (die1 == 4 and die2 >= 4) or (die1 >= 4 and die2 == 4):
            if die1 == 4:
                score = die2
            else:
                score = die1
            return score

        # El jugador tiene un 4 y un numero menor que 4, puede tirar de nuevo un dado.
        if(die1==4 or die2==4):
            if die1 == 4 and die2 <= 3:
                if(previus_score == None):
                    # Estrategia de Juan, si o si debemos tirar de nuevo
                    print("Tiramos de vuelta el dado 2.")
                    die2 = throwDie()
                    print("Nuevo valor segundo dado: ", die2)
                    score = die2
                    return score
                else:
                    # Maria ya sabe el resultado de juan
                    if(previus_score > die2):
                        #Tiramos de nuevo porque sino perdemos
                        print("Tiramos de vuelta el dado 2.")
                        die2 = throwDie()
                        print("Nuevo valor segundo dado: ", die2)
                    score = die2
                    return score

            if die2 == 4 and die1 <= 3:
                if(previus_score == None):
                    # Estrategia de Juan, si o si debemos tirar de nuevo
                    print("Tiramos de vuelta el dado 1.")
                    die1 = throwDie()
                    print("Nuevo valor primer dado: ", die1)
                    score = die1
                    return score
                else:
                    # Maria ya sabe el resultado de juan
                    if(previus_score > die1):
                        #Tiramos de nuevo porque sino perdemos
                        print("Tiramos de vuelta el dado 1.")
                        die2 = throwDie()
                        print("Nuevo valor primer dado: ", die1)
                    score = die1
                    return score
        
        if die1 != 4 and die2 != 4:
            print("Debes tirar de vuelta \n")
            results_second_throw = throw_dice()
            die1 = results_second_throw[0]
            die2 = results_second_throw[1]
            print("Segunda tirada: ")
            print("Valor primer dado: ", die1)
            print("Valor segundo dado: ", die2,  "\n")
            if die1 == 4:
                score = die2
            if die2 == 4:
                score = die1

    return score



def juan_vs_maria_results():
    results_juan = play(None)
    results_maria = play(results_juan)
    if results_juan > results_maria:
        winner = "Gano Juan"
    elif results_juan < results_maria:
        winner = "Gano Maria"
    else:
        winner = "Empate"

    return winner, results_juan, results_maria
    
def juan_vs_maria_print():
    print("Juego de dados\n")
    winner, results_juan, results_maria = juan_vs_maria_results()
    print("Resultados finales")
    print("\tJuan: ", results_juan)
    print("\tMaria: ", results_maria)
    print(winner)

def play_n_games(n):
    juan_wins = 0
    maria_wins = 0
    draws = 0
    for i in range(n):
        winner, _, _ = juan_vs_maria_results()
        if winner == "Gano Juan":
            juan_wins += 1
        elif winner == "Gano Maria":
            maria_wins += 1
        else:
            draws += 1
    print("\nResultados de las ", n, " partidas")
    print("\tJuan gano ", juan_wins, " veces")
    print("\tMaria gano ", maria_wins, " veces")
    print("\tHubo ", draws, " empates")