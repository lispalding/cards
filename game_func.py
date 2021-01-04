##################### FUNCTIONS #####################
def getName(question):
    """ Runs and gets names. To use: getName() """

    while True:
        name = input(question)  # Getting family memeber names
        if name == name.isnumeric:  # Making sure that the name is numeric
            print("Not valid!!")
        elif len(name) > 1:
            return name
            break
        else:
            print("Not valid!!")


def getNumber(high, low, question):  # Defining the high and low values with high=7 and low=5
    """ Runs and gets a good number. To use: getNumber(high,low,question) """

    while True:
        number = input(question)
        if number.isnumeric():
            number = int(number)
            if (number >= low) and (number <= high):
                return number
                break
            else:
                print("Not valid input!")
        else:
            print("Not valid!")

def openFile(fileName,mode):
    """ Opens and returns an open file with the given permissions. To Use: openFile(fileName,mode) """
    # Try block for errors
    try:
        # Opening a file...
        file = open("assets/"+fileName,mode)
    except IOError as e:
        # Only runs if there is an IO Error
        print("Unable to open the file",fileName+". Ending program... \n",e)
        try: # Making the program check for errors
            time = datetime.now() # Getting the time
            errorTime = time.strftime("%m/%d/%Y %H:%M:%S") # Making the time format readable

            # Writing the error to error file
            file = open("assets/errors_log/error_log.txt","a")
            file.write(str(e)+" "+str(errorTime)+"\n")

            file.close()

            # Getting user input for the system exit
            input("\n\n Presss the enter key to exit.")
            sys.exit() # Exiting the program
        except: # If we get an unidentifiable error
            sys.exit() # Exiting the program

    return file

def menuChoices(options):
    """Creates a menu. To use: menuChoices(options) """

    # Creating a choice menu base that we can call to
    index = 1
    print("\n")
    for i in options:
        print(str.format("{}................{}", index, i))
        index += 1

    while True:
        userChoice = input("What do you wish to do?  ")
        if userChoice.isnumeric():
            userChoice = int(userChoice)
            if userChoice >= 1 and userChoice <= len(options):
                return userChoice
            else:
                print("Not valid...")
        else:
            print("Enter a number...")

def askYesNo(question):
    """Ask a yes or no question and get back a yes or no answer. To use: ( answer = askYesNo(question) ) """
    response = None
    while response not in ("y","n","yes","no"):
        response = input(question).lower()
    return response
######################## FIN ########################

###################### CLASSES ######################
class Player(object):
    def __init__(self,name):
        self.name = name
        self.score = Score()
        self.isAlive = True
        self.lives = 3


class Score(object):
    def __init__(self):
        self.score = 0

    def addToScore(self, points):
        self.score += points

    def subtractFromScore(self, points):
        self.score -= points
        if self.points < 0:
            self.score = 0

######################## FIN ########################

if __name__ == "__main__":
    print("This is a module with classes for playing cards, not meant to be ran on it's own.")
    input("\n\n Press the enter key to exit.")