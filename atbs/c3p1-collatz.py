#a simple game based on collatz sequence

def collatz(num):
    if num % 2 == 0:
        print(num//2)
        return num//2
    elif num % 2 != 0:
        print((3*num)+1)
        return (3*num)+1

print('Enter a number')
while True:
    #print('Enter a number')
    try:
        number = int(input())
    except ValueError:
        print('Enter a valid integer')
    if collatz(number) == 1:
        break
