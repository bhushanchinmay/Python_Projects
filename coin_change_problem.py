def getNumberOfWays(N, Coins): 

	ways = [0] * (N + 1); 

	ways[0] = 1; 

	for i in range(len(Coins)): 

		for j in range(len(ways)): 
			if (Coins[i] <= j): 

				ways[j] += ways[(int)(j - Coins[i])]; 

	return ways[N]; 

def printArray(coins): 
	for i in coins: 
		print(i); 

if __name__ == '__main__': 
	Coins = [1, 5, 10]; 

	print("The Coins Array:"); 
	printArray(Coins); 

	print("Solution:",end=""); 
	print(getNumberOfWays(6, Coins)); 
