import random

# FUNCTIONS DEFINED BELOW

# Given a certain x coordinate a, computes the value of y on the given polynomial curve (based on the coefficients also given as input)
def valOnPol(x, coeffs):
	y = 0
	for i in range(len(coeffs)):
		curr = coeffs[i] * (x**i)
		y += curr
	return y

# Creating n shares
def secretToShares(secret, n, t, prime):
	if secret > prime:
		print("Invalid secret value")
		exit()
	# Generating the coefficients of a polynomial of degree t-1
	polyCoeff = [None]*t
	polyCoeff[0] = secret
	for i in range(1,t):
		polyCoeff[i] = (random.randint(1,10000))%prime

	# Creating n shares to be distributed to the participants
	shares = [None]*n
	for i in range(n):
		val = random.randint(1, 10000)%prime  # For each share, chooses a random x coordinate value
		polVal = valOnPol(val, polyCoeff)%prime
		shares[i] = (val,polVal)

	return shares

# Since SSS is based on polynomial interpolation, using Lagrange interpolation to obtain the secret from the shares
# Sum(Prod((x-xj)/(xi-xj))) where i and j go from 0 to n
# In our case, x = 0 since we care only about the constant value
def sharesToSecret(shares, prime):
	x = 0
	tot = 0
	secret = 0
	for i in range(len(shares)):
		xi = shares[i][0]
		yi = shares[i][1]
		prod = 1
		for j in range(len(shares)):
			if j != i:
				xj = shares[j][0]
				yj = shares[j][1]
				if xj >= xi:
					prod *= (xj - x) * pow((xj - xi), -1, prime)
				else:
					prod *= (xj - x) * pow(prime - (xi-xj), -1, prime)
		prod = prod % prime
		prod *= yi
		tot += prod
	secret = tot % prime
	return secret

# FUNCTIONS END HERE

if __name__ == "__main__":
	prime = 7919
	# The number of shares
	n = 10
	# The threshold value
	t = 4
	# The actual information / secret
	s = 7000

	print("Secret :", s)
	print("n: ", n, ", t:", t, ", Prime:", prime)

	# Taking the secret value and generating n shares
	shares = secretToShares(s, n, t, prime)
	print("n Shares :", shares)

	# Choosing t shares from n at random
	tShares = random.sample(shares, t)
	print("Number of shares brought together:", len(tShares))
	# Trying to reconstruct the original secret from just these t shares
	reconstructedSecret = sharesToSecret(tShares, prime)
	print("Retrieved secret:", reconstructedSecret)
