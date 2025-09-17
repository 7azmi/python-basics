# Task 3 Part 2: Classes (حاوية، أو قالب)

# In the video, I tried my best to convey the idea of why devs use classes in programming
# and introduced you to OOP very quickly. Hope you like it

# Video link: https://youtu.be/ksbj8UHHwLY

class Person: 
    def __init__(self, name, age, is_male): # constructor, called once when object created.
        self.name = name
        self.age = age
        # TODO: create another two **meaningful** human attributes (variables)
        # and apply them to `introduce()` or any other function. (Main Task - 2 Tokens)


    def introduce(self):
        status = "adult" if self.age >= 18 else "underage"
        print(f"{self.name} ({self.age}) - {status}")

    # TODO: Create another two useful functions and use them. Be creative! (Main Task - 2 Tokens)


# TODO: Can you pretend "classes.py" is your little fancy library 
#  and create `Person` from another script? (Subtask - 1 Token)
p = Person("Ahmed", 24) # object
p.introduce() 
