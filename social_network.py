class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''
    
    def __init__(self, name):
        self.name = name # The name of the person
        self.friends = []  # A list of friends

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)

class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''

    
    def __init__(self):
        self.people = {}  # Dictionary: # person_name -> person object

    def add_person(self, name):
        """Add a new person to the network"""
        if name in self.people:
            print("⚠️  This person already exists")
            return
        
        if name not in self.people:
            self.people[name] = Person(name)
                   
    def add_friendship(self, person1_name, person2_name):
        """Add a bidirectional friendship between two people"""
        persons = []
        persons.append(person1_name)
        persons.append(person2_name)

        for person in persons :
            if person not in self.people:  
                print(f"⚠️  Friendship not created. {person} doesn't exist!")
                return 

        # if person1_name in self.people and person2_name in self.people:
        person1 = self.people[person1_name]
        person2 = self.people[person2_name]
                    
        # Create bidirectional connection
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self): 
        for person_name, person_obj in self.people.items(): 
            # List of connected friends 
            friend_names = [friend.name for friend in person_obj.friends]
            
            # Join names with a comma
            connected_friends = ", ".join(friend_names)
            print(f"{person_name} connects to: {connected_friends}")

# Test your code here
alex = Person("Alex")
jordan = Person("Jordan")
print(alex.friends) # []
alex.add_friend(jordan)
print(alex.friends[0].name)  # Jordan

network = SocialNetwork()

# Add people
network.add_person("Alex")
network.add_person("Jordan") 
print(network.people) # {'Alex': <__main__.Person object at 0x1004c7380>,'Jordan': <__main__.Person object at 0x10503d810>}
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")

# Create friendships
network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Jordan", "Johnny") # "Friendship not created. Johnny doesn't exist!"
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

network.print_network()
'''
Alex is friends with: Jordan, Morgan, Taylor
Jordan is friends with: Alex, Taylor
Morgan is friends with: Alex, Casey, Riley
Taylor is friends with: Jordan, Riley, Alex
Casey is friends with: Morgan, Riley
Riley is friends with: Taylor, Casey, Morgan 
'''

# Create the social network
network = SocialNetwork()

# Add people
network.add_person("Alice")
network.add_person("Bob")
network.add_person("Charlie")
network.add_person("Diana")
network.add_person("Eve")
network.add_person("Frank")

# Test adding a duplicate person
network.add_person("Alice")  # ⚠️ Should warn that Alice already exists

# Add friendships
network.add_friendship("Alice", "Bob")
network.add_friendship("Alice", "Charlie")
network.add_friendship("Bob", "Diana")
network.add_friendship("Charlie", "Diana")
network.add_friendship("Charlie", "Eve")
network.add_friendship("Diana", "Frank")
network.add_friendship("Eve", "Frank")
network.add_friendship("Bob", "Frank")

# Test adding a friendship where one person doesn't exist
network.add_friendship("Alice", "George")  # ⚠️ George doesn't exist

# Print the network
network.print_network()

"""
# Why is a graph the right structure to represent a social network?
A list only shows a sequence. A graph on the other hand can show a data structure that can represent complex, interconnected relationships.
Social networks can go bothways since for example people can have many friends that are reciprocal
In other words, having a graph is beneficial since it supports connections that are complex and multi-directional.

# Why wouldn’t a list or tree work as well for this?
A list is a linear structure that can never show that is connected to multiple values without excluding others. 
For instance [1,2,3], 1 and 3 might be connected, while 2 doeesnt have a connection with 1. However there is no way to show that with a list
A tree has multiple connections, however there is hierarchy in a tree, whereas there might be no hierarchy in a friendship or social network.

# What performance or structural trade-offs did you notice when adding friends or printing the network?
A trade off i notice is that if there are more people is self.people, the program will print the network slower since we check with a for loop 
Using a set is fast for lookups, but at the cost of memory
"""
