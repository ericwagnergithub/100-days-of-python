def greet():
    print("Hello")
    print("How do you do?")
    print("Howdy")

greet()

def greet_with_name(name, location):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"How is the weather in {location}?")


greet_with_name("Eric","Florida")
greet_with_name(location = "Florida",name ="Eric")


