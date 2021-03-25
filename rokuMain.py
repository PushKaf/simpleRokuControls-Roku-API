from roku import Roku


#connect to roku with your IP, you can get this from your roku in settings network about section.
IP = "ENTER YOUR IP HERE"
roku = Roku(IP)
#check all the apps you have
donwloadedApps = roku.apps

#keywords it looks for
_keywordOpenApp = ["open", "launch"]
_keywordMovement = ["w", "a", "s", "d", "up", "left", "right", "down"]
_keywordFuncs = ["back", "enter", "play", "backspace", "forward", "search"]
_keywordActive = ["active"]
_keywordHelp = ["?", "help", "cmds"]

#opens an app passed with params ex: "open netflix"
def openApp(app):
    for apps in donwloadedApps:
        if app == str(apps.name).lower():
            appToLaunch = roku[apps.name]
            appToLaunch.launch()

#some basic remote movments includes just the cardinal directions
def basicMovement(movementChoice):
    if movementChoice in ["w", "up"]:
        cmd = "up"
    elif  movementChoice in ["a", "left"]:
        cmd = "left"
    elif  movementChoice in ["s", "down"]:
        cmd = "down"
    elif  movementChoice in ["d", "right"]:
        cmd = "right"

    eval(f"roku.{cmd}()")

#runs some basic functions from the remote such as play, search, forward, etc. | check _keywordFuncs for more
def remoteFuncs(func):
    eval(f"roku.{func}()")

#displat the currently activte app
def whatsPlaying():
    print(eval(f"roku.active_app"))

#launches the help menu
def helpMe():
    print("\n=================================================================================================================================")
    print(f"To launch an app use 'open' or 'launch' followed by the name. Ex) 'launch netflix'")
    print(f"To use remote movements (like moving left, right, etc.) use any of the following: {_keywordMovement}")
    print(f"Functions for doing things include: {_keywordFuncs}")
    print(f"To see the current openned app use: {_keywordActive}")
    print(f"To display this menu again use any of the follwing: {_keywordHelp}")
    print("=================================================================================================================================\n")

#translate user input into commands for the roku; this is the main function that connects other functions
def translateUser(userInput):
    chc = userInput.split(" ")
    if len(chc) >= 2:
        if chc[0].lower() in _keywordOpenApp:
            openApp(chc[1])
            print(f"\n<Running>: {userInput}")
        else:
            print(f"App Not Found: <{chc[1]}>") 
    elif chc[0].lower() in _keywordMovement:
        basicMovement(chc[0])
    elif chc[0].lower() in _keywordFuncs:
        remoteFuncs(chc[0])
    elif chc[0].lower() in _keywordActive:
        whatsPlaying()
    elif chc[0].lower() in _keywordHelp:
        helpMe()

if __name__ == "__main__":
    #loooooooooooooooooooooooooooooooooooooooooooooooop
    while True:
        user = input("<Roku> Awaiting User Command: ")
        translateUser(user)
        
