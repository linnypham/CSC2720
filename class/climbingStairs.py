def climbingStairs(n):
    if n <= 1:
        return n
    else:
        return climbingStairs(n-1) + climbingStairs(n-2)

#def countWays(s):
   # return climbingStairs(s + 1)

a = int(input("Number of stairs:"))
#print(f'Ways to reach to the top: {countWays(a)}')
print(f'Ways to reach to the top: {climbingStairs(a+1)}')