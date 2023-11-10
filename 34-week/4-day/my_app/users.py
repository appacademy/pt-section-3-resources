
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.posts = []

    # def __repr__(self):
    #     return f"{self.posts}"

    def to_dict(self):
        return{
            "name": self.name,
            "age": self.age,
            "posts": [p.to_dict() for p in self.posts]
        }

class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content
    def __repr__(self):
        return f"{self.content}"

    def to_dict(self):
        return{
            "title": self.title,
            "content": self.content,
        }

will = User("will", 30)
print(will)

# print(will.to_dict())

sally = User("sally", 30)
post1 = Post("Python is fun", "lorem ipsum ")
post2 = Post("Python is awesome", "hello world")
post3 = Post("Python is sweet", "This is a cool post ")

will.posts.append(post1)
will.posts.append(post2)
will.posts.append(post3)
# print(will.to_dict()["posts"])
# will_dict = will.to_dict()
# for p in will.to_dict()["posts"]:
    # print(p["content"])

def validate_decorator(func):
    def validate(user):
        if(isinstance(user, User)):
            name = user.to_dict()["name"]
            return func(name)
        else:
            return f"who are you?"
    return validate

@validate_decorator
def greet_user(name):
    return f"hi {name}"

print(greet_user(will))
print(greet_user(1245))
print(greet_user(sally))
