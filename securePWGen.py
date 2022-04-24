import hashlib, random
from anusha_isha_shamirSecretSharing import secretToShares
prime = 2**11213 - 1 #Mersenne Prime - 23 from https://mathworld.wolfram.com/MersennePrime.html

# The following values can also be taken as input from the user

def getASCII(string):
    new = ""
    for s in string:
        n = str(ord(s))
        new += n
    return new

def genSafePW(p, u, numShares, threshold):
    random.seed(0)

    s = random.randint(1,100000) # salt value generated randomly

    s = str(s)
    singleString = u+p+s
    new = getASCII(singleString)

    shares = secretToShares(int(new),numShares,threshold, prime)
    fewerThanTShares = shares[0:threshold-1]

    newPW = ""
    for s in fewerThanTShares:
        newPW += str(s[0]) + str(s[1])

    newPW = hashlib.sha256(newPW.encode('utf-8')).hexdigest()
    return newPW


# Function definition ends here

if __name__ == "__main__":
    password = "password"
    userID = "ishanusha"

    numShares = 15
    threshold = 10
    pw = genSafePW(password,userID, numShares, threshold)
    print("New PW:",pw)
