# Iterators and iterables

Numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# This turns the iterable 'Numbers' into an iterator called 'Myiter' 
Myiter = iter(Numbers)

# can also be done this way too

# Myiter = Numbers.__iter__

# This Calls the __next__() method on the iterator Myiter to get the next item in the list.
# print(Myiter.__next__())
# print(Myiter.__next__())

# can also be done this way -cleaner
# print(next(Myiter))
# print(next(Myiter))


# for x in Numbers:
#     print(x)

# this uses while loop to call the next method on Myiter continously, and an if stament
#  to check if the next item is even then print
while (True):
    try:

        element=next(Myiter)
        if element % 2 == 0:
            print(element)
            # once  stopiteration is raised it prints "no more even numbers" then breaks the loop
    except StopIteration:
        print("no more even numbers")
        break