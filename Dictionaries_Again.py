my_dict = {'a':645, 'b':3987, 'c': 93,'d': 111, 'e': 646, 'f': 20}
highestValues= sorted(my_dict, key=my_dict.get, reverse=True)[:3]
print(highestValues)