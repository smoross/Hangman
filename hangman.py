def blanked(word, string):
    accum = ''
    for x in word:
      if x in string:
        accum += x 
      else:
        accum = accum + '_'

    return accum
def health_prompt(current_health, max_health): 
    max_health = max_health - current_health
    return "+"*current_health + "-"*max_health
def game_state_prompt(txt ="Nothing", h = 6, m_h = 6, word = "HELLO", guesses = ""):
    res = "\n" + txt + "\n"
    res = res + health_prompt(h, m_h) + "\n"
    if guesses != "":
      res = res + "Guesses so far: " + guesses.upper() + "\n"
    else:
      res = res + "No guesses so far" + "\n"
    res = res + "Word: " + blanked(word, guesses) + "\n"

    return(res)

def main():
	max_health = 3
    health = max_health
    secret_word = raw_input("What's the word to guess? (Don't let the player see it!)")
    secret_word = secret_word.upper() # everything in all capitals to avoid confusion
    for x in range(27):
    	print ""
    guesses_so_far = ""
    game_over = False

    feedback = "let's get started"

    # Now interactively ask the user to guess
    while not game_over:
        prompt = game_state_prompt(feedback, health, max_health, secret_word, guesses_so_far)
        next_guess = raw_input(prompt)
        next_guess = next_guess.upper()
        feedback = ""
        if len(next_guess) != 1:
            feedback = "I only understand single letter guesses. Please try again."
        elif next_guess in guesses_so_far:
            feedback = "You already guessed that"
        else:
            guesses_so_far = guesses_so_far + next_guess
            if next_guess in secret_word:
                if blanked(secret_word, guesses_so_far) == secret_word:
                    feedback = "Congratulations"
                    game_over = True
                else:
                    feedback = "Yes, that letter is in the word"
            else: # next_guess is not in the word secret_word
                feedback = "Sorry, " + next_guess + " is not in the word."
                health = health - 1
                if health <= 0:
                    feedback = " Waah, waah, waah. Game over."
                    game_over= True

    print(feedback)
    print("The word was..." + secret_word)

main()


