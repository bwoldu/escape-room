def room2():
    pass

def room1():
    objects = {"Painting": ["Portrait of a man", "1791 - 1872", "A small plaque underneath with the name: Samual Morse"],
               "Table": {"A newspaper": "The newspaper is dated 1812", "Piece of paper": "-. -. --- ---. -..", "Thermometer": ""},
               "Door": "----",
               "Bookshelf": {"Weather Through the Ages": "Pages of unusual weather records. Several mention record-breaking temperatures.", "Harry Potter and the Cursed Child": "HP", "Cryptography & Secret Messages": "\nA = .- \n  B = -... \n C = -.-. \n L = .-.. \n T = -, O = --- \n, S = ...", "Great Inventors": "Collection of famous inventor. One page is bookmarked: Samual Morse - developer of the Morse coded system."}, 
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
                            room2()
                            break
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
room1()

def start_game():
    print("10:00  'Four rooms. One exit. ESCAPE'")
    while True:
        start = input("Start? Yes/Y")

        if start.lower() == "y" or start.lower() == "yes":
            print(room1())
            break
        elif start.lower() == "no" or start.lower() == "n":
            print("Stopping game")
            break
        else:
            print("Invalid input. Please enter Yes/Y or No/N")

def room3():
    pass 
def room4():
    pass