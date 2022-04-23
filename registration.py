import hashlib, random
from anusha_isha_shamirSecretSharing import secretToShares
prime = 2**11213 - 1 #Mersenne Prime - 23 from https://mathworld.wolfram.com/MersennePrime.html
random.seed(0)
# The following values can also be taken as input from the user
password = "password"
userID = "Ishanusha"
serverS = "S1"

def getASCII(string):
    new = ""
    for s in string:
        n = str(ord(s))
        new += n
    return new

def genSafePW(p, u, s):
    numShares = 10
    threshold = 5

    singleString = u+p+s
    new = getASCII(singleString)
    # final = singleString + new
    # print(final)
    # print(hashlib.sha256(final.encode('utf-8')).hexdigest())

    shares = secretToShares(int(new),numShares,threshold, prime)
    fewerThanTShares = shares[0:threshold-1]

    newPW = ""
    for s in fewerThanTShares:
        newPW += str(s[0]) + str(s[1])

    newPW = hashlib.sha256(newPW.encode('utf-8')).hexdigest()
    print("New PW:",newPW)


# Function definition ends here

genSafePW(password,userID, serverS)
