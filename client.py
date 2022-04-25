import socket

ip='127.0.0.1'
port=5000
ClientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ClientSocket.connect((ip, port))

ver = ClientSocket.recv(2048).decode()

if(ver == "yes"):
    print("Connection with server established!")

choice = input("Would you like to register or sign in? Enter R or S: ")
ClientSocket.send((choice).encode())

if(choice == "R" or choice == "r"):
    username = input("Please enter your username: ")
    ClientSocket.send((username).encode())
    password = input("Please enter your password: ")
    ClientSocket.send((password).encode())

    existing = ClientSocket.recv(1024).decode()

    if existing == "yes":
        print("Sorry, an account with this username already exists!")

    else:

        flag = ClientSocket.recv(2048).decode()
        if flag == "1":
            print("Registration successful!")

elif (choice == "S" or choice == "s"):
    username = input("Please enter your username: ")
    ClientSocket.send((username).encode())
    password = input("Please enter your password: ")
    ClientSocket.send((password).encode())

    flag = ClientSocket.recv(2048).decode()
    if flag == "1":
        print("Sign-in successful!")
    else:
        print("The details you entered are not valid! Please try to sign in again, or register.")

else:
    print("Invalid input!")