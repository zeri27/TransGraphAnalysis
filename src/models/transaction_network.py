import networkx as nx
from matplotlib import pyplot as plt

from src.models.user import User


class TransactionNetwork:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_user(self, user: User):
        self.graph.add_node(user.id, data=user)

    def commit_transaction(self, sender: User, receiver: User, amount):
        sender.send(receiver.id, amount)
        transaction = receiver.receive(sender.transactions)
        self.graph.add_edge(transaction.sender, transaction.receiver, amount=transaction.amount)

    def create_graph(self, transactions):
        for tx in transactions:
            self.graph.add_node(tx.sender_id)
            self.graph.add_node(tx.receiver_id)
            self.graph.add_edge(tx.sender_id, tx.receiver_id, amount=tx.amount)

    def visualize(self):
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10)
        edge_labels = nx.get_edge_attributes(self.graph, 'amount')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels, font_color='black')
        plt.show()
