command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started :
            print("car is already started")
        else:
            started = True  
            print("car has started")
    elif command == "stop":
        if not started:
            print("car is already stopped")
        else:
            started = False
            print("car stopped")
    elif command == "help":
        print("""
start - car get start🚘
stop - car stops🛑
quit - to exit🔙
              """)
    elif command == "quit":
        break
    else:
        print("something went wrong")