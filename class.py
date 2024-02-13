class User:
    def __init__(self, id, username, email):
        self.Id = id
        self.Username = username
        self.Email = email

user1 = User(1, "john_doe", "john@example.com")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 30)
print(person1.__dict__)