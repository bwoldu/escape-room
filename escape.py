def sea_level_check(sea_level):
    if sea_level >= 100:
        print("The island has been submerged. GAME OVER")
        return True
    return False

def room3(sea_level):
    secret_word = "planet"

    num_guess = 6
    print("You have reached the top of the lighthouse.")
    print("The door to end the game is locked.")
    print("A screen pops up with a word guessing game")
    print("You have 6 guesses to guess the 6-letter secret word")

    while num_guess > 0:
        word = []
        guess = input("Please input your guess:").lower()
    

        if len(guess) != len(secret_word):
            print("Enter a 6 letter word")
            continue

        if guess == secret_word:
            print("Correct!")
            print("You escaped!!")
            return 

        num_guess -=1
        sea_level += 10

        print("? = correct letter wrong position")
        print("X = letter not in word")

        for i in range(len(secret_word)):
            if guess[i] == secret_word[i]:
                word.append(guess[i])
            elif guess[i] in secret_word:
                word.append("?")
            else:
                word.append("X")

        print(" ".join(guess.upper()))
        print(" ".join(word))
        print("Guesses remaining:", num_guess)
        print(f"SEA LEVEL: {sea_level}%")

        if sea_level_check(sea_level):
            return 

    print("You have run out of guesses")
    print("GAME OVER")
    
def lighthouse(sea_level : int, answers : list):
    print("You have reached the lighthouse but the door is locked")
    print("A screen on the door pops up:")

    door_answer = int("".join(map(str, answers)))
    while True:
        try:
            player_input = int(input("Enter the digits from each bridge sequence:"))
        except ValueError:
            print("Please enter a whole number")
            continue 

        if player_input == door_answer:
            print("DOOR UNLOCKED")
            print("You have now reached the last room")
            room3(sea_level)
            return 
        
        sea_level +=10
        print(f"INCORRECT SEA LEVEL NOW: {sea_level}%")

        if sea_level_check(sea_level):
            return 



def room2_bridge(sea_level):
    sequences = {
                 "1,8,27, _ ": 64,
                 "79, 95, _, 127": 111,
                 "4,23, 60, 121, ?": 212,
                 }

    answers = []
    print("A screen at the first part of the bridge pops up with a sequence:")
    for sequence, answer in sequences.items():
        print(sequence)
        while True:
            try:
                player_answer = int(input("What is the next answer?"))
            except ValueError:
                print("Please enter a number")
                continue

            if player_answer != answer:
                sea_level += 10
                print(f"Incorrect! SEA LEVEL: {sea_level}%")

                if sea_level_check(sea_level):
                    return
                continue 
            else:
                answers.append(player_answer)
                break
    lighthouse(sea_level, answers)


def room2():
    print("You're now on an abandoned island. Water is slowly moving further inland. \n SEA LEVEL: 15%. You need to escape.")
    print("Reach the lighthouse before the island is submerged")
    sea_level = 15

    start_paths = {"Beach Path": ["2m above sea level", 10],
             "Forest Path": ["8m above sea level",15],
             "Rocky Path": ["12m above sea level", 25], 
             }

    middle_paths = ["Hill path", "Bridge path", "River path"]

    for i, value in enumerate(start_paths, start =1):
        print(f"{i}: {value} - {start_paths[value][0]} - {start_paths[value][1]} minutes")

    print("WARNING: There has been a landslide on the rocky path" \
    "\n The evacuation point must be reached within 35 minutes")

    while True:
        try:
            choice = int(input("Which path do you choose?"))

            if choice == 2:
                print("You take the Forest Path and continue further inland")
                break
            elif choice == 1 or choice == 3:
                sea_level +=10
                print(f"Incorrect: Sea level has now risen to {sea_level}%")

            else:
                print("Please choose a path from 1-3.")

            if sea_level_check(sea_level):
                return

        except ValueError:
            print("Please enter a number")
            continue 


    #second path challenge 
    print("There are three more paths to choose from but they are all blocked")
    print("A sign reads:")
    print("To reveal the safe path answer this riddle:")
    print("What grows bigger with each passing year, affecting weather across the sphere?")

    for path in middle_paths:
        print(path)

    riddle_answer = "Climate Change"

    while True:
        user_answer = input("Answer:")
        if user_answer.lower() == riddle_answer.lower():
            print("The Bridge path opens")
            room2_bridge(sea_level)
            return 

        sea_level += 10
        print(f"Incorrect! SEA LEVEL: {sea_level}%")

        if sea_level_check(sea_level):
            return
    
    

def room1():
    objects = {"Painting": ["Portrait of a man", "1791 - 1872", "A small plaque underneath with the name: Samuel Morse"],
               "Table": {"A newspaper": "The newspaper is dated 1812", "Piece of paper": "-.-. --- ---. -..", "Thermometer": "24"},
               "Door": "----",
               "Bookshelf": {"Weather Through the Ages": "Pages of unusual weather records. Several mention record-breaking temperatures.", "Harry Potter and the Cursed Child": "HP", "Cryptography & Secret Messages": "\nA = .- \n  B = -... \n C = -.-. \n L = .-.. \n T = -, O = --- \n, S = ...", "Great Inventors": "Collection of famous inventor. One page is bookmarked: Samuel Morse - developer of the Morse code system."}, 
               "Clock": "4:13"
               }
 
    print("The door slams shut behind you")
    print("ROOM TEMPERATURE: 24 C\n")
    print("A few seconds later...\n")
    print("ROOM TEMPERATURE: 25 C")
    print("!!! WARNING !!! TEMPERATURE RISING \n")

    while True:
        i = 1
        for key in objects.keys():
            print(f"{i}: {key}")
            i+=1

        try:
            number = int(input("What would you like to investigate?"))
            for index, value in enumerate(objects, start=1):
                if index == number:
                    if value == "Door":
                        print(objects[value])
                        code = input("Enter the code:")

                        if code.lower() == "cool":
                            print("Access granted. Entering room 2...")
                            return
                        else:
                            print("Access denied")
                    
                    elif isinstance(objects[value], dict):
                        i=1
                        for item in objects[value]:
                            print(f"{i} {item}")
                            i+=1

                        option2 = int(input("Which object would you like to investigate?"))
                        for index, item in enumerate(objects[value], start=1):
                            if index == option2:
                                print(objects[value][item])

                    elif isinstance(objects[value], list):
                        for item in objects[value]:
                            print(item)
                    else:
                        print(objects[value])
        except Exception as e:
            print(e)

def start_game():
    print("10:00  'Three rooms. One exit. ESCAPE'")
    while True:
        start = input("Start? Yes/Y")

        if start.lower() == "y" or start.lower() == "yes":
            room1()
            room2()
            break
        elif start.lower() == "no" or start.lower() == "n":
            print("Stopping game")
            break
        else:
            print("Invalid input. Please enter Yes/Y or No/N")
start_game()