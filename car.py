
command = ''
started = False
while True:
    command = input('> ').lower()
    if command == 'start':
        if started:
            print('Car is already started!')
        else:
            started = True
            print('Car is started...')
    elif command == 'stop':
        if not started:
            print('Car is already stoped!')
        else:
            started = False
            print('Car is stoped...')
    elif command == 'help':
        print("""
start - To start the car
stop - To stop the car
quit - to quit
        """)
    elif command == 'quit':
        break
    else:
        print('Sorry,Invalid option')



