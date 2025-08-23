# Two example lists
keys = ["name", "age", "city", "email"]
values = ["rutvi","20", "rajkot", "r@example.com"]

# Empty dictionary
my_dict = {}

# Converting lists into dictionary using a for loop
for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

# Printing the dictionary
print("Dictionary created from two lists:", my_dict)
