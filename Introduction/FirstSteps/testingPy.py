fruits = ['apple', 'orange', 'pear', 'banana']  # List
otherFruits = ['kiwi', 'strawberry']    # List
print(otherFruits[0])
print(fruits[0:2])
print(len(fruits))

lstOfLists = [['a', 'b', 'c'], [1, 2, 3], ['one', 'two', 'three']]  # List of lists or matrix
print(lstOfLists[1][2])

pair = (3, 5)   # Tuple
pair[0]

shapes = ['circle', 'square', 'triangle', 'circle']  # Sets, no-repeating items
setOfShapes = set(shapes)
print(setOfShapes)
print('circle' in setOfShapes)

studentIds = {'knuth': 42.0, 'turing': 56.0, 'nash': 92.0}  # Dictionary
print(studentIds['turing'])


# Example
fruits = ['apples', 'oranges', 'pears', 'bananas']
for fruit in fruits:
    print fruit + ' for sale'

fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75}
for fruit, price in fruitPrices.items():
    if price < 2.00:
        print '%s cost %.2f a pound' % (fruit, price)
    else:
        print fruit + ' are too expensive!'

# Lambda expressions
square = map(lambda y: y * y, [1, 2, 3])
print(filter(lambda y: y % 2 == 0, square))

# List comprehension
nums = [1, 2, 3, 4, 5, 6]
oddNums = [x for x in nums if x % 2 == 1]
print(oddNums)

