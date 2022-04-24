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

def genSafePW(p, u):
    random.seed(0)

    s = random.randint(1,100000) # salt value generated randomly

    numShares = 10
    threshold = 5
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

    pw = genSafePW(password,userID)
    print("New PW:",pw)
