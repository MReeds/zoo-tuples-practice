#Create a variable for the animals in your zoo tuple, 
#and print them to the console.
#Convert your tuple into a list.
#Use extend() to add three more animals to your zoo.
#Convert the list back into a tuple.

zoo = ("Kangaroo", "Elephant", "Lion", "Monkey", "Anteater")
new_animals = ["Rhino", "Ostrich", "Cheetah"]

zoo_list = list(zoo)
zoo_list.extend(new_animals)

zoo_tuple = tuple(zoo_list)

print(zoo_tuple)

# animal_to_find = "Kangaroo"

# if animal_to_find in zoo:
#     print(f"The {animal_to_find} is in our zoo!")