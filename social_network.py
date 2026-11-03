class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []
        
    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''
    
    


class SocialNetwork:
    def __init__(self):
        self.people = {}
        
    def add_person(self, name):
        if name not in self.people:
            self.people[name] = Person(name)
            
    def add_friendship(self, person1_name, person2_name):
        if person1_name in self.people and person2_name in self.people:
            person1 = self.people[person1_name]
            person2 = self.people[person2_name]
            
            person1.add_friend(person2)
            person2.add_friend(person1)
        else:
            print(f"Friendship not created. One or both people do not exist.")
    
    def print_network(self):
        for person_name, person_obj in self.people.items():
            connection_names = [c.name for c in person_obj.friends]
            connected_people = ", ".join(connection_names)
            print(f"{person_name} connected with {connected_people}")
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    



# Test your code here

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