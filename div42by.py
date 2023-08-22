def div42by (divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print ('Error: Division by Zero')

print (div42by(5))
print (div42by(9))
print (div42by(0))
print (div42by(66))

num_cats = input ('How many cats do you own? ')
if int(num_cats) == 0:
    print("Oh, you don't have any cats? Maybe consider adopting one!")
elif int(num_cats) == 1:
    print("You have one cat. Cats make great companions!")
else:
    print("You own so many cats?! That's a lot of feline friends!")       
 
