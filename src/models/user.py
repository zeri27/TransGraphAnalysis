import uuid
from src.models.transaction import Transaction


class User:
    def __init__(self, name, balance):
        self.id = str(uuid.uuid4())
        self.name = name
        self.balance = balance
        self.transactions = []
        self.hidden_transactions = []

    def send(self, user_id, amount):
        self.balance -= amount
        transaction = Transaction(self.id, user_id, amount)
        self.transactions.append(transaction)

    def receive(self, transactions: [Transaction]):
        # Analyze transaction history here
        transaction = transactions[-1]
        self.balance += transaction.amount
        self.transactions.append(transaction)
        return transaction

    def hide_transaction(self, transaction_id):
        transaction = None
        for tx in self.transactions:
            if tx.transaction_id == transaction_id:
                transaction = tx
                break

        self.transactions.remove(transaction)
        self.hidden_transactions.append(transaction)
