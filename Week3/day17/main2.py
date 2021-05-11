class User:
    def __init__(self, id, name, followers):
        self.id = id
        self.name = name 
        self.followers = 0
        self.following = 0
        

    def follow(self, user):
        user.followers+=1
        user.following+=1
        

user1 = User('001','Akshith', 0)
user2 = User('002', 'Ashwath', 0)

print(user1.name)
print(user1.id)
print(user2.name)
print(user2.id)
print(f"the follower count: {user1.followers}")
print(f"the follower count: {user2.followers}")
user1.follow(user2)
user2.follow(user1)
print(f"the follower count: {user1.followers}")
print(f"the follower count: {user2.followers}")
print(f"the following accounts: {user1.following}")
print(f"the following accounts: {user2.following}")
