import random


def throw_dice():
    results = []
    results.append(random.randint(1, 6))
    results.append(random.randint(1, 6))
    return results
    
def throw_die():
    return random.randint(1, 6)

def play(previus_score):
    score = 0
    first_throw_result = throw_dice()
    die1 = first_throw_result[0]
    die2 = first_throw_result[1]

    print("First throw: ")
    print("First die value: ", die1)
    print("Second die value: ", die2, "\n")

    # The player got a 4 in both dice, the final score is 4
    if(die1 == 4 and die2 == 4):
        score = 4
        return score
    else: 
        # The player got a 4 in one of the dice, the final score is the other die value       
        if (die1 == 4 and die2 >= 4) or (die1 >= 4 and die2 == 4):
            if die1 == 4:
                score = die2
            else:
                score = die1
            return score
        # The player got a 4 in one of the dice and a number lower than 3 in the other, can throw 
        # the other die again
        if(die1==4 or die2==4):
            if die1 == 4 and die2 <= 3:
                if(previus_score == None):
                    # Juan strategy, he must throw again
                    print("Throw again the second die.")
                    die2 = throw_die()
                    print("Second die new value: ", die2)
                    score = die2
                    return score
                else:
                    # Maria already knows Juan's result
                    if(previus_score > die2):
                        # Maria must throw again because she will lose
                        print("Throw again the second die.")
                        die2 = throw_die()
                        print("Second die new value: ", die2)
                    score = die2
                    return score

            if die2 == 4 and die1 <= 3:
                if(previus_score == None):
                    # Juan strategy, he must throw again
                    print("Throw again the first die.")
                    die1 = throw_die()
                    print("First die new value: ", die1)
                    score = die1
                    return score
                else:
                    # Maria already knows Juan's result
                    if(previus_score > die1):
                        # Maria must throw again because she will lose
                        print("Throw again the first die.")
                        die2 = throw_die()
                        print("First die new value: ", die2)
                    score = die1
                    return score
        
        if die1 != 4 and die2 != 4:
            print("You must throw again \n")
            second_throw_results = throw_dice()
            die1 = second_throw_results[0]
            die2 = second_throw_results[1]
            print("Second throw: ")
            print("First die value: ", die1)
            print("Second die value: ", die2, "\n")
            if die1 == 4:
                score = die2
            if die2 == 4:
                score = die1
    return score



def juan_vs_maria_results():
    juan_results = play(None)
    maria_results = play(juan_results)
    if juan_results > maria_results:
        winner = "Juan wins"
    elif juan_results < maria_results:
        winner = "Maria wins"
    else:
        winner = "Draw"

    return winner, juan_results, maria_results
    
def juan_vs_maria_print():
    print("Juego de dados\n")
    winner, results_juan, results_maria = juan_vs_maria_results()
    print("Resultados finales")
    print("\tJuan: ", results_juan)
    print("\tMaria: ", results_maria)
    print(winner)

def simulate_games(n):
    juan_wins = 0
    maria_wins = 0
    draws = 0
    for i in range(n):
        winner, _, _ = juan_vs_maria_results()
        if winner == "Juan wins":
            juan_wins += 1
        elif winner == "Maria wins":
            maria_wins += 1
        else:
            draws += 1
    print("\tResults after played ", n, " games:")
    print("\tJuan has won ", juan_wins, " times")
    print("\tMaria has won ", maria_wins, " times")
    print("\tThere were ", draws, " draws")