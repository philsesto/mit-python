# cube = 29
# epsilon = 0.01
# guess = 0.0
# increment = 0.0001
# num_guesses = 0

# while abs(guess**3 - cube) >= epsilon and guess <= cube:
#     guess += increment
#     num_guesses += 1
# print('Number of guesses =', num_guesses)

# if abs(guess**3 - cube) >= epsilon:
#     print('Failed on the cube root of', cube)
# else:
#     print(guess, 'is close to the cube root of', cube)

# x = 25
# epsilon = 0.01
# numGuesses = 0
# low = 0.0
# high = x
# ans = (high+low)/2.0

# while abs(ans**2 - x) >= epsilon:
#     print('low = ' + str(low) + ', high = ' + str(high) + ', ans = ' + str(ans))
#     numGuesses += 1
#     if ans**2 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high+low)/2.0
# print('\n' + 'guesses = ' + str(numGuesses))
# print(str(ans) + ' is close to the square root of ' + str(x))

# x = 25
# epsilon = 0.01
# numGuesses = 0
# low = 0.0
# high = x
# ans = (high+low)/2.0

# while abs(ans**2 - x) >= epsilon:
#     print('low = ' + str(low) + ', high = ' + str(high) + ', ans = ' + str(ans))
#     numGuesses += 1
#     if ans**2 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high+low)/2.0
# print('\n' + 'guesses = ' + str(numGuesses))
# print(str(ans) + ' is close to the square root of ' + str(x))

# # cube root
# x = 27
# epsilon = 0.01
# numGuesses = 0
# low = 0.0
# high = x
# ans = (high+low)/2.0

# while abs(ans**3 - x) >= epsilon:
#     print('low = ' + str(low) + ', high = ' + str(high) + ', ans = ' + str(ans))
#     numGuesses += 1
#     if ans**3 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high+low)/2.0
# print('\n' + 'guesses = ' + str(numGuesses))
# print(str(ans) + ' is close to the cube root of ' + str(x))

# x = 
# epsilon = 0.0001
# numGuesses = 0
# low = 0
# high = x
# if x > 0 and x < 1:
#     low = x
#     high = 1
# if x < 0 and x > -1:
#     low = -1
#     high = x

# ans = (high+low)/2.0

# while abs(ans**3 - x) >= epsilon:
#     print('low = ' + str(low) + ', high = ' + str(high) + ', ans = ' + str(ans))
#     numGuesses += 1
#     if ans**3 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high+low)/2.0
# if x < 0:
#     ans = -abs(ans)
# print('\n' + 'guesses = ' + str(numGuesses))
# print(str(ans) + ' is close to the cube root of ' + str(x))
# print(str(ans**3))

x = -0.095
epsilon = 0.00000000000000001
numGuesses = 0
low = 1
high = abs(x)
if abs(x) > 0 and abs(x) < 1:     # handle cases where 0 < x < 1 or -1 < x < 0
    low = x
    high = 1

if x != 0:
    ans = (high+low)/2.0

    while abs(ans**3 - abs(x)) >= epsilon:
        print('low = ' + str(low) + ', high = ' + str(high) + ', ans = ' + str(ans))
        numGuesses += 1
        if ans**3 < abs(x):
            low = ans
        else:
            high = ans
        ans = (high+low)/2.0
else:
    ans = 0

# handle negative values for x
if x < 0:
    ans = -abs(ans)
print('\n' + 'guesses = ' + str(numGuesses))
print(str(ans) + ' is close to the cube root of ' + str(x))
print(str(ans**3))