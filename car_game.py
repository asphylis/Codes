command = ""
print("Enter help for support")
started = False
while True:
    command = input(">").upper()
    if command == 'HELP':
        print("start - to start the car\nstop - to stop car\ngo - to move\nquit - to quit\n")
    elif command == 'START':
        if started:
            print("Car is already stared")
        else:
            started = True
            print("Car started...Ready to go!")
    elif command == 'STOP':
        if not started :
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped.")
    elif command == 'GO':
        if started:
            print("We're going full speed ahead")
        else:
            print("Start the car first")
    elif command == 'QUIT':
        print("Thank You!")
        break
    else:
        print("Sorry! I don't understand")