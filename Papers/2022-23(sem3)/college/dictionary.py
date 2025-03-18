my_dict = {"city":"Bareilly",
           "state":"Uttar Pradesh",
           "Country":"India"}

#adding the key value pair in the dictionary
my_dict["name"]="Vighnesh"
print(my_dict)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

new_dict = {"College":"RBCET",
            "DOB":"01/01/2003"}

my_dict.update(new_dict)
print(my_dict)

# my_dict.pop("name")
del my_dict["state"]
print(my_dict)