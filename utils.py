import random

def throw_dice():
    results = []
    results.append(random.randint(1, 6))
    results.append(random.randint(1, 6))
    return results
    
def throw_die():
    return random.randint(1, 6)

def play(previus_score, show_game):
    score = 0
    first_throw_result = throw_dice()
    die1 = first_throw_result[0]
    die2 = first_throw_result[1]
    
    if show_game:
        # If previus_score is None, Juan is playing, otherwise Maria is playing
        if previus_score == None: 
            print("Juan turns\n")
        else:
            print("Maria turns\n")

    if show_game:
        print("First throw: ")
        print("First die value: ", die1)
        print("Second die value: ", die2, "\n")

    # The player got a 4 in both dice, the final score is 4
    if(die1 == 4 and die2 == 4):
        score = 4       
        if show_game: print("Final score: ", score, "\n")
        return score
    else: 
        # The player got a 4 in one of the dice, the final score is the other die value       
        if (die1 == 4 and die2 >= 4) or (die2 == 4 and die1 >= 4 ):
            if die1 == 4:
                score = die2
            else:
                score = die1
            if show_game: print("Final score: ", score, "\n")
            return score
        # The player got a 4 in one of the dice and a number lower than 3 in the other, can throw 
        # the other die again
        if(die1==4 or die2==4):
            if die1 == 4 and die2 <= 3:
                if(previus_score == None):
                    # Juan strategy, he must throw again
                    if show_game: print("Throw again the second die.")
                    die2 = throw_die()
                    if show_game: print("Second die new value: ", die2)
                    score = die2
                    if show_game: print("Final score: ", score, "\n")
                    return score
                else:
                    # Maria already knows Juan's result
                    if(previus_score >= die2):
                        # Maria must throw again because she will lose
                        if show_game: print("Throw again the second die.")
                        die2 = throw_die()
                        if show_game: print("Second die new value: ", die2)
                    score = die2
                    if show_game: print("Final score: ", score, "\n")
                    return score

            if die2 == 4 and die1 <= 3:
                if(previus_score == None):
                    # Juan strategy, he must throw again
                    if show_game: print("Throw again the first die.")
                    die1 = throw_die()
                    if show_game: print("First die new value: ", die1)
                    score = die1
                    if show_game: print("Final score: ", score, "\n")
                    return score
                else:
                    # Maria already knows Juan's result
                    if(previus_score > die1):
                        # Maria must throw again because she will lose
                        if show_game: print("Throw again the first die.")
                        die2 = throw_die()
                        if show_game: print("First die new value: ", die2)
                    if (previus_score == die2):
                        # Maria  throw again because she is more probably to win with a new value
                        if show_game: print("Throw again the second die.")
                        die2 = throw_die()
                        if show_game: print("Second die new value: ", die2)
                    score = die1
                    if show_game: print("Final score: ", score, "\n")
                    return score
        
        if die1 != 4 and die2 != 4:
            if show_game: print("You must throw again \n")
            second_throw_results = throw_dice()
            die1 = second_throw_results[0]
            die2 = second_throw_results[1]
            if show_game: 
                print("Second throw: ")
                print("First die value: ", die1)
                print("Second die value: ", die2, "\n")
            if die1 == 4:
                score = die2
            if die2 == 4:
                score = die1
    if show_game: print("Final score: ", score, "\n")
    return score



def winner_and_results(show_game):
    juan_results = play(None, show_game)
    maria_results = play(juan_results, show_game)
    if juan_results > maria_results:
        winner = "Juan wins"
    elif juan_results < maria_results:
        winner = "Maria wins"
    else:
        winner = "Draw"

    return winner, juan_results, maria_results
    
def print_results():
    print("Dices game\n")
    winner, results_juan, results_maria = winner_and_results(True)
    print("Final results of the game between Juan and Maria after throwing the dices:")
    print("\tJuan: ", results_juan)
    print("\tMaria: ", results_maria)
    print(winner)

def simulate_games(n, show_game):
    juan_wins = 0
    maria_wins = 0
    draws = 0
    for i in range(n):
        winner, _, _ = winner_and_results(show_game)
        if winner == "Juan wins":
            juan_wins += 1
        elif winner == "Maria wins":
            maria_wins += 1
        else:
            draws += 1
    print("Results after played ", n, " games:")
    print("\tJuan has won ", juan_wins, " times")
    print("\tMaria has won ", maria_wins, " times")
    print("\tThere were ", draws, " draws\n")
    print("\tJuan relative frequence:", float(juan_wins/n))
    print("\tMaria relative frequence:", float(maria_wins/n))
    print("\tDraws relative frequence:", float(draws/n), "\n")