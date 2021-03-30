# simulate a server that's taking connections
#  from the outside and then a load balancer 
# that ensures that there are enough servers 
# to serve those connections
#Each connection is represented by an id,
#  that could, for example, be the IP address
#  of the computer connecting to the server.
#  For our simulation, each connection creates
#  a random amount of load in the server,
#  between 1 and 10.
import random


class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        # Add the connection to the dictionary with the calculated load

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Add up the load for each of the connections
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())

#Creating a Server instance
server = Server()
server.add_connection("192.168.1.1")

print(server.load())

#After running the above code cell, 
# if you get a NameError message, be sure 
# to run the Server class definition code block first.

#The output should be 0. 
# This is because some things are missing from the Server
#  class. So, you'll need to go back and fill in the blanks
#  to make it behave properly.
#If output is a rand no btw 1..10 is ok

#Closing connection
server.close_connection("192.168.1.1")
print(server.load())
#Correct if output is 0

#Load Balancing Class. 
#This class will start with only one server 
# available. When a connection gets added, 
# it will randomly select a server to serve 
# that connection, and then pass on the connection
#  to the server. The LoadBalancing class also needs
#  to keep track of the ongoing connections to be
#  able to close them. 

class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        # Add the connection to the dictionary with the selected server
        # Add the connection to the server

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # Find out the right server
        # Close the connection on the server
        # Remove the connection from the load balancer

    def avg_load(self):
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        return 0

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        pass

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))

# Be sure that the load balancer now has an average
#  load more than 0 before proceeding.
l.servers.append(Server())
print(l.avg_load())

#The average load should now be half of what it was before.
l.close_connection("fdca:83d2::f20d")
print(l.avg_load())

#testing ensure_availability
#  method and calling it from add_connection
for connection in range(20):
    l.add_connection(connection)
print(l)

#The code above adds 20 new connections
#  and then prints the loads for each server
#  in the load balancer. If you coded correctly,
#  new servers should have been added automatically
#  to ensure that the average load of all servers
#  is not more than 50%

print(l.avg_load())

#if average load is less than 50%, then success