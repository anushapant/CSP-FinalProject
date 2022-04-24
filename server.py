import socket
from securePWGen import genSafePW

#valid users so far
users = ["testUser"]
passwords = ["test"]

ip='127.0.0.1'
port=5000
ServerSocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ServerSocket.bind((ip,port))
ServerSocket.listen()

numShares = 15
threshold = 12

while True:

    (ClientSocket, Address) = ServerSocket.accept()

    ver = "yes"
    ClientSocket.send(str(ver).encode())

    choice = ClientSocket.recv(1024).decode()

    flag = 0
    if(choice == "R" or choice == "r"):
        username = ClientSocket.recv(1024).decode()
        password = ClientSocket.recv(1024).decode()


        if username in users:
            existing = "yes"

        else:
            existing = "no"

        ClientSocket.send(existing.encode())

        if existing == "no":
            users.append(username)
            securePW = genSafePW(password, username, numShares,threshold)

            passwords.append(securePW)

            # The client will not have access to the information being printed below
            print("Registration")
            print("For user:", username, "the password is:", password)
            print("However, for security purposes, what will now be stored is:",securePW)
            print("Even if this information is somehow exposed, no adversary will be able to obtain the original password!")

            flag = 1
            ClientSocket.send(str(flag).encode())

    elif (choice == "S" or choice == "s"):
        username = ClientSocket.recv(1024).decode()
        password = ClientSocket.recv(1024).decode()
        storedPW = genSafePW(password, username, numShares,threshold)

        print("Sign-in")
        print("For user:", username, "the entered password is:", password)
        print("However, if this user has an account, what should have been stored is:", storedPW)
        print("If the entries match, the user will be able to sign in successfully.")

        flag = 0
        for i in range(len(users)):
            if (users[i] == str(username) and passwords[i] == storedPW):
                flag = 1
                break

        ClientSocket.send(str(flag).encode())
    ClientSocket.close()
ServerSocket.close()