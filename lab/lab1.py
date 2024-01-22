n = int(input("Enter n: "))
while n <= 0:
  n = int(input("Enter a positive integer for n: "))

print('Welcome to Guess My numer!')
print(f'Please think of a number between 0 and {n-1}.')
l = 0
r = n-1
while l<=r:
    m = (l+r+1)//2
    print(f'Is your number: {m}?')
    print('Please enter C for correct, H for too high, or L for too low.')

    ans = input('Enter your response (H/L/C): ')

    while ans.upper() not in ['C','H','L']:
      ans = input('Enter your response (H/L/C): ')

    if ans.upper()== 'C':
        print('Thank you for playing Guess My Number!')
        break
    elif ans.upper() == 'H':
        r = m-1
    elif ans.upper()== 'L':
        l = m+1
