# for item in "Hello!":
#     print(item)
#
# for item in range(5):
#     print(item)
#

names = ["Alice", "Brittany", "Zoey"]

for name in names:
    print(f'Hello, {name}!')
    if name == "Zoey":
        print(f"{name} is my daughter!")
        for name in names:
            print("I'm inside the if clause")
    else:
        print("Hello there...")