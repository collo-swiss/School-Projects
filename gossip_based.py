"""Gathumbi Collins Githiari
A program to show Gossip based communication using sockets."""
import random
import socket
from threading import Thread
import time


class GossipNode:
    #list to store all infected nodes
    infected_nodes = []

    # initialization method.
    # pass the port of the node and the ports of the nodes connected to it
    def __init__(self, port, connected_nodes):
        # create a new socket instance
        # use SOCK_DGRAM to be able to send data connectionless 
        self.node = socket.socket(type=socket.SOCK_DGRAM)

        self.hostname = socket.gethostname()
        self.port = port

        self.node.bind((self.hostname, self.port))

        #the ports of nodes passed to it as connected are set to susceptible
        self.susceptible_nodes = connected_nodes

        print("Node started on port {0}".format(self.port))
        print("Susceptible nodes =>", self.susceptible_nodes)

        #function call to use threads
        self.start_threads()

    def input_message(self):
        while True:
            #This is the message to be sent to nodes
            message_to_send = input("Enter a message to send:\n")

            #Call function transmit_message with message to be passed
            self.transmit_message(message_to_send.encode('ascii'))

    def receive_message(self):
        while True:
            # recvfrom receives the message
            message_to_forward, address = self.node.recvfrom(1024)

            # remove the node from which the message came from, from the list of susceptible nodes and add it to the list of infected nodes
            self.susceptible_nodes.remove(address[1])
            GossipNode.infected_nodes.append(address[1])

            # This 5 second delay will show difference in time
            time.sleep(5)

            # The node prints the message it receives with the current time.
            print("\nMessage is: '{0}'.\nReceived at [{1}] from [{2}]\n"
                  .format(message_to_forward.decode('ascii'), time.ctime(time.time()), address[1]))

            # The send_message function is called to forward the message to other susceptible nodes
            self.transmit_message(message_to_forward)

    def transmit_message(self, message):
        #Loop to ensure that it runs only when there is a susceptible node left
        while self.susceptible_nodes:
            
            selected_port = random.choice(self.susceptible_nodes)

            print("\nSusceptible nodes are: ", self.susceptible_nodes)
            print("Infected nodes are: ", GossipNode.infected_nodes)
            print("Port selected is [{0}]".format(selected_port))

            #sendto sends the UDP message over the protocol
            self.node.sendto(message, (self.hostname, selected_port))

            #The selectednode is then removed from susceptible to infected
            self.susceptible_nodes.remove(selected_port)
            GossipNode.infected_nodes.append(selected_port)

            print("Message: '{0}' sent to [{1}].".format(message.decode('ascii'), selected_port))
            print("Susceptible nodes are: ", self.susceptible_nodes)
            print("Infected nodes are: ", GossipNode.infected_nodes)
            print("The message received is: ", self.receive_message())

            time.sleep(5)
            print(" \n")

    def start_threads(self):
        #We create two nodes to enable each node to be able to enter a message and still be able to receive a message
        Thread(target=self.input_message).start()
        Thread(target=self.receive_message).start()
