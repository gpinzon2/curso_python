import getpass

def guess_word(secret_word,tets_letter,attempt_word):
    """
    Chequea si la letra está en secret word y si la palabra es igual
    ARG: secret_word = Palara secreta
    test_letter = Letra a verificar que se encuentra en Secret word
    attempt_word = Palabra que debe ser igual que secret Word
    """
    """
    Return:
    Print: La letra "A" está en la palabra Secret Word
    Print: La palabra "xxxx" es igual a Secret Word
    """
    # Aqui va la logica
    letter_in_word = tets_letter in secret_word
    if(letter_in_word == True):
        letter_in_word = "está en la palabra"
    else:
        letter_in_word = "no está en la palabra"
    print("La letra", tets_letter, letter_in_word, secret_word)

    #Logica
    result_word = attempt_word == secret_word
    if (result_word == True):
        result_word = "Es igual que "
    else:
        result_word = "No es igual que"
    print("La palabra", attempt_word,  result_word, secret_word )


def main():
    print("=== Letter and Word Guessing Game ===")
    secret_word = getpass.getpass("Introduce Palabra secreta: ")
    tets_letter = input("Introduce letra")
    attempt_word =input("Introduce palabra")
    guess_word(secret_word,tets_letter,attempt_word)


if __name__ =="__main__":
    main()

