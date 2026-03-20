"""
Password Strength Checker

Enhancement:
Displays the password complexity score so users understand
why their password received its strength rating.

# Character lists provided in the assignment
LOWER=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
UPPER=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]


def word_in_file(word, filename, case_sensitive=False):
    #Return True if word is found in file.

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            file_word = line.strip()

            if case_sensitive:
                if word == file_word:
                    return True
            else:
                if word.lower() == file_word.lower():
                    return True

    return False


def word_has_character(word, character_list):
    # Return True if any character in word appears in character_list.

    for char in word:
        if char in character_list:
            return True

    return False


def word_complexity(word):
    # Return complexity score (0–4) based on character types.

    complexity = 0

    if word_has_character(word, LOWER):
        complexity += 1

    if word_has_character(word, UPPER):
        complexity += 1

    if word_has_character(word, DIGITS):
        complexity += 1

    if word_has_character(word, SPECIAL):
        complexity += 1

    return complexity


def password_strength(password, min_length=10, strong_length=16):
    #Determine password strength and return score (0–5).

    # Rule 1 – dictionary word
    if word_in_file(password, "wordlist.txt", False):
        print("Password is a dictionary word and is not secure.")
        return 0

    # Rule 2 – common password
    if word_in_file(password, "toppasswords.txt", True):
        print("Password is a commonly used password and is not secure.")
        return 0

    # Rule 3 – too short
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    # Rule 4 – long password
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    # Rule 5 – complexity based
    complexity = word_complexity(password)
    strength = 1 + complexity

    print(f"Complexity score: {complexity}")

    return strength


def main():
    #Main program loop.

    while True:

        password = input("Enter a password to test (q to quit): ")

        if password == "q" or password == "Q":
            print("Exiting password checker.")
            break

        strength = password_strength(password)

        print(f"Password strength: {strength}")
        print()


if __name__ == "__main__":
    main()
    """


"""
Password Strength Checker

After evaluating the password strength, the program also provides suggestions
to improve weak passwords. If the password has low complexity, the program
suggests adding uppercase letters, lowercase letters, numbers, or special
symbols to strengthen the password.
"""

# Character constants provided by Sven

LOWER=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",
       "s","t","u","v","w","x","y","z"]

UPPER=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
       "S","T","U","V","W","X","Y","Z"]

DIGITS=["0","1","2","3","4","5","6","7","8","9"]

SPECIAL=["!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","}",
         "|",";",":","'","\"",",",".","<",">","?","/","\\","`","~"]


# Function: word_in_file
def word_in_file(word, filename, case_sensitive=False):

    try:
        with open(filename,"r",encoding="utf-8") as file:
            for line in file:
                file_word = line.strip()

                if case_sensitive:
                    if word == file_word:
                        return True
                else:
                    if word.lower() == file_word.lower():
                        return True

        return False

    except FileNotFoundError:
        print(f"File {filename} not found.")
        return False

# Function: word_has_character

def word_has_character(word, character_list):

    for char in word:
        if char in character_list:
            return True

    return False

# Function: word_complexity

def word_complexity(word):

    complexity = 0

    if word_has_character(word, LOWER):
        complexity += 1

    if word_has_character(word, UPPER):
        complexity += 1

    if word_has_character(word, DIGITS):
        complexity += 1

    if word_has_character(word, SPECIAL):
        complexity += 1

    return complexity


# Function: password_strength

def password_strength(password, min_length=10, strong_length=16):

    # Dictionary check (case insensitive)
    if word_in_file(password, "wordlist.txt", False):
        print("Password is a dictionary word and is not secure.")
        return 0

    # Top passwords check (case sensitive)
    if word_in_file(password, "toppasswords.txt", True):
        print("Password is a commonly used password and is not secure.")
        return 0

    # Minimum length check
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    # Strong length check
    if len(password) > 15:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    # Complexity calculation
    complexity = word_complexity(password)

    strength = 1 + complexity

    return strength

# Enhancement Function 
# --------------------------------------------------------
def password_suggestions(password):

    suggestions = []

    if not word_has_character(password, LOWER):
        suggestions.append("Add lowercase letters")

    if not word_has_character(password, UPPER):
        suggestions.append("Add uppercase letters")

    if not word_has_character(password, DIGITS):
        suggestions.append("Add numbers")

    if not word_has_character(password, SPECIAL):
        suggestions.append("Add special symbols")

    if len(password) < 10:
        suggestions.append("Increase password length")

    if suggestions:
        print("Suggestions to improve password:")
        for s in suggestions:
            print("-", s)

# Main Program
# --------------------------------------------------------
def main():

    while True:

        password = input("Enter a password to test (or Q to quit): ")

        if password.lower() == "q":
            print("Exiting password checker.")
            break

        strength = password_strength(password)

        print("Password strength score:", strength)

        # Show suggestions for weak passwords
        if strength < 4:
            password_suggestions(password)

        print()


# Required execution block
# --------------------------------------------------------
if __name__ == "__main__":
    main()