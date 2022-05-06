"""
Assignment: 75
Write a filter function to get the list of fruits of type berry.
Input List: values = ["apple", "orange", "blueberry", "pineapple", "strawberry", "grape",
"pear", "muskmelon", "raspberry", "guava", "papaya", “blackberry”, "custard apple"]
"""

values = ["apple", "orange", "blueberry", "pineapple", "strawberry", "grape", "pear", "muskmelon", "raspberry", "guava", "papaya", "blackberry", "custard apple"]
ret = list(filter(lambda x: x.endswith("berry"), values))
print(ret)
