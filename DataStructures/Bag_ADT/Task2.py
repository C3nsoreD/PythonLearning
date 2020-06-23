from linearbag import Bag

myBag = Bag()
myBag.add(12)
myBag.add(53)
myBag.add(95)
myBag.add(62)
myBag.add(19)
myBag.add(30)

value = int(input("Guess a value contained in the bag to list all the values in the bag: "))
if value in myBag:
    print("The bag contains the value", value)
    passed = True
    print("Here's a list of all the items iin the bag")
else:
    print("The bag does not contain the value", value)
    passed = False
    print("I can't show you what's in the bag")

# Create a BagIterator object for myBag.
iterator = myBag.__iter__()

# Repeat the while loop until break is called.
while passed:
    try:
        # Get the next item from the bag. If there are no
        # more items, the StopIteration exception is raised.
        item = iterator.__next__()
        # Perform the body of the for loop.
        print(item)
    # Catch the exception and break from the loop when we are done.
    except StopIteration:
        break