class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = False
user1 = User("Anna Propas", "anna@anna.com")
print user1.name
print user1.logged
print user1.email
user2 = User("Brian Kang", "brian@brian.com")
print user2.name
print user2.logged
print user2.email