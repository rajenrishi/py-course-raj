"""
Assignment: 76
Write a filter function to get the list of fruits whose name has more than 6 characters.
Input List: values = ["apple", "orange", "blueberry", "pineapple", "strawberry", "grape",
"pear", "muskmelon", "raspberry", "guava", "papaya", “blackberry”, "custard apple"]
"""

values = ["apple", "orange", "blueberry", "pineapple", "strawberry", "grape", "pear", "muskmelon", "raspberry", "guava", "papaya", "blackberry", "custard apple"]
ret = list(filter(lambda x: len(x) > 6, values))
print(ret)
