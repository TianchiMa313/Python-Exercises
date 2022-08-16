'''
This script helps John Smith to add his wife Jane Sr (age 90) to his records.
This script uses for loop, .items(), .update() to prints John Smith's attributes, 
Jane Sr's attributes and all their combined children's attributes individually without 
any repeated information, with children noting who their parent is, in the order of their age.
'''
john_smith = {
    "firstname": "john",
    "lastname": "smith",
    "age": 99,
    "company": "Google",
    "children": ["john jr", "jane", "bob"],
}
# #john's info
print(list(john_smith.items())[:4])

# # wife's info
john_smith["wife"] = {'firstname': 'jane sr', 'lastname': 'smith', 'age': 90}
print(john_smith["wife"])


#mary's info
john_smith['wife']['children'] = [{'firstname': 'mary', 'lastname': john_smith["lastname"], 'age': 12, 'parent': john_smith["wife"]['firstname'] + ' ' + john_smith["wife"]['lastname']}]
for i in john_smith['wife']['children']:
    print(i)

#children’s info
john_smith.update(
        {'children': 
            [{'firstname': 'john jr', 'lastname': john_smith["lastname"], 'age': 9, 'favourite_fruit': 'apple', 
            'parent': john_smith["firstname"] + ' ' + john_smith["lastname"] +' and ' + john_smith["wife"]['firstname'] + ' ' + john_smith["wife"]['lastname']},

            {'firstname': 'jane', 'lastname': john_smith["lastname"], 'age': 6, 'favourite_fruit': 'orange', 
            'parent': john_smith["firstname"] + ' ' + john_smith["lastname"] +' and ' + john_smith["wife"]['firstname'] + ' ' + john_smith["wife"]['lastname']},
            
            {'firstname': 'bob', 'lastname': john_smith["lastname"], 'age': 1, 'favourite_fruit': 'banana', 
            'parent': john_smith["firstname"] + ' ' + john_smith["lastname"]}]
        }
    )

for i in john_smith["children"]:
    print(i)
    