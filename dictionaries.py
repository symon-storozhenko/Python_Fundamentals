# dict = {"key":"value"}
# keys can be a string, an integer, or a float
# value can be anything


a = {"name":"Symon", "age": 125, "my_temperature": 98.7, "list": [112, "Hello"],
     "my_internal_dict": {"first": 1}, 67: "sixty-seven", 3.14: "Pi", (1, 45): "Hello"}


name = "Symon"
age = 67
temperature = 98.9
email_4_symon = "example@google.com"

my_info = {"name": "Symon", "age": 67, }

print(my_info)
print(my_info.values())
print(my_info.pop("name"))
print(my_info)
print(my_info.get("age"))
print(my_info.update({"address":"123 Main St"}))
print(my_info)
print(my_info.keys())
print(my_info.popitem())
print(my_info.keys())

# Ctrl+C on both Win and MacOS