# # def my_func():
# #     print("hello world")

# class Actor:
#     # is_famous = True
#     def __init__(self, nationality, age, name):
#         self.nationality = nationality
#         self.age = age
#         self.name = name

#     def my_name(self):
#         # print("hi")
#         print(f"My name is {self.name}")

#     def __str__(self):
#         return f"< {self.name} is a Level {self.age} Dragon with a {self.nationality}m wingspan >"

#     @classmethod
#     def actor_factory(cls, actor_dict):
#         print("actor_dict", actor_dict)
#         return cls(actor_dict["nationality"], actor_dict["age"], actor_dict["name"])


# # paul_dano = Actor("British", 40, "Paul Dano")

# # new_actor = Actor.actor_factory({"nationality": "British", "age": 33, "name": "Tom Cruise"})

# # print("new actor: ", new_actor.nationality, new_actor.age, new_actor.name)

# # print(paul_dano)
# # # print(paul_dano.my_name())
# # # Actor.my_name()
# # # paul_dano.give_autograph()
# # # Actor.give_autograph()


# # # my_dict = {"hello": "world"}
# # # print(my_dict["hello"])
# # # print(my_dict.hello)


# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# let arr = new Array(1,2,3)
# let arr = []
class Actor:
    def __init__(self, nationality, age, name="JIM"):
        self.nationality = nationality
        self.age = age
        self.name = name
        self.fans = ["will", "bobby", "tommy"]

    @classmethod
    def factory(constructor, my_dict):
        # return Actor("british", "33", "WILL")
        #define logic to prevent duplicate emails
        if not my_dict["email"]:

            return constructor(my_dict["nationality"], my_dict["age"], my_dict["name"])
        else:
            raise ValueError("EMAIL EXISTS")
        # return cls("british" "33", "WILL")



new_actor = Actor("british", "33", "WILL")

new_actor2 = Actor("british", "33", "JIMBO")

# new_actor.fans.append("BOBBY")
# new_actor.fans.pop()
# new_actor.fans.pop()
# print(new_actor.fans)
# print(new_actor2.fans)
cool_dict = {"nationality": "british", "age":"33", "name":"MATTHEW@m.com"}
cool_dict2 = {"nationality": "british", "age":"33", "name":"ATTHEW@m.com"}

new_actor = Actor.factory(cool_dict)
new_actor2 = Actor.factory(cool_dict2)

print("1: ", new_actor.name)
print("2: ", new_actor2.name)


# print(new_actor.name)
# print(new_actor.age)


# #     def my_name(self):
# #         print(f"My name is {self.name}")


# #     #define a repr method
# #     def __repr__(self):
# #         return f"{self.name} {self.nationality} {self.age}"

# #     @staticmethod
# #     def to_dict(self):
# #         return {
# #             "name": self.name,
# #             "age": self.age,
# #             "nationality": self.nationality
# #         }

# #     def to_dict_no_nationality(self):
# #         return {
# #             "name": self.name,
# #             "age": self.age,
# #             "fans": [x.upper() for x in self.fans]
# #         }


# # # paul_dano = Actor("British", 40, "Paul Dano")

# # # print(paul_dano.to_dict())
# # # print(paul_dano.to_dict_no_nationality())


# # class Pet:
# #     def __init__(self, name):
# #         self.name = name

# # # my_pet = Pet("fido")
# # # print(my_pet)
# # print(my_pet.name)

# # class Dog(Pet):
# #     def __init__(self, name, sound):
# #         super().__init__(name)
# #         self.sound = sound

# # class Cat(Pet):
# #     def __init__(self, name, purr_noise):
# #         super().__init__(name)
# #         self.purr_noise = purr_noise


# #             # self.name = name

# # my_dog = Dog("Rex", "WOOF")
# # my_cat = Cat("Whiskers", "Meow")

# # print(my_dog.name, my_dog.sound)
# # print(my_cat.name, my_cat.purr_noise)

# # #
# # #     def __init__(self, name, sound):
# # #         super().__init__(name):
# # #             self.sound = sound
# # #             # pass
# # #             # self.name


# # class Person:
# #     pass

# # class Child(Person):
# #     pass


# class Icon():
#     def __init__(self, color, shape, password):
#         self.color = color
#         self.shape = shape
#         self._password = password

#     # getter for ~secret~ password
#     @property
#     def password(self):
#         return self._password

#     @password.setter
#     def password(self, new_password):
#         if new_password == "12345":
#             raise ValueError("This is not a good password!!!")
#         else:
#             self._password = new_password


# my_icon = Icon("blue", "square", "superawesomecomplexpassword")
# # print(my_icon.color)

# # call the getter method as if we were just
# # reading a property

# # print(my_icon._password)
# # print(my_icon.password)
# # my_icon.password = "goodpassword"
# my_icon.password = "12345"
# print(my_icon.password)


