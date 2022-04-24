import socket

ip='127.0.0.1'
port=5001
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


    flag = ClientSocket.recv(2048).decode()
    if flag == "1":
        print("You have registered successfully!")

elif (choice == "S" or choice == "s"):
    username = input("Please enter your username: ")
    ClientSocket.send((username).encode())
    password = input("Please enter your password: ")
    ClientSocket.send((password).encode())

    flag = ClientSocket.recv(2048).decode()
    if flag == "1":
        print("You have been able to sign in successfully!")
    else:
        print("The details you entered were not valid! Please try to sign in again, or register.")

else:
    print("That is an invalid input")