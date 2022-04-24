from securePWGen import genSafePW
import string, random, time

usernames = []
genPWs = []
num = 100

n = 6
t = 2

count = 0

for i in range(num):

    # To nullify the effect the seed value being set in genSafePW
    curTime = time.time() * 1000
    random.seed(int(curTime) % 2 ** 32)

    # generating a random username and password in each iteration
    l = string.ascii_lowercase
    username = ''.join(random.choice(l) for i in range(4))
    password = ''.join(random.choice(l) for i in range(4))

    while username in usernames:
        username = ''.join(random.choice(l) for i in range(4))

    usernames.append(username)

    pw = genSafePW(password,username,n,t)

    # Keeping track of the number of collisions
    if pw in genPWs:
        count += 1
    else:
        genPWs.append(pw)

print("The number of collisions:",count)