from src.models.transaction_network import TransactionNetwork
from src.models.user import User

alice = User("Alice", 100)
bob = User("Bob", 100)
charlie = User("Charlie", 100)

alice.send(bob.id, 50)
bob.receive(alice.transactions)

alice.send(charlie.id, 50)
charlie.receive(alice.transactions)

net = TransactionNetwork()
net.create_graph(alice.transactions)
net.visualize()

