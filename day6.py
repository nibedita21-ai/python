my_dict = {
    "name": "Nibedita",
    "age": 22,
    "city": "India"
}

print("Dictionary contents:")
for key, value in my_dict.items():
    print(f"{key}: {value}")                           
                                                    
  
import pprint

nested_dict = {
    "user1": {"name": "Nibedita", "email": "cnibeditaswain@gmail.com"},
    "user2": {"name": "Charlie", "email": "charlie@example.com", "details": {"active": True}}
}

print("\nPretty-printed dictionary contents:")
pprint.pprint(nested_dict)


