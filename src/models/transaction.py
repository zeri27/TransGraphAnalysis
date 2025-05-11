from datetime import datetime
import uuid


class Transaction:
    def __init__(self, sender_id, receiver_id, amount):
        self.transaction_id = str(uuid.uuid4())
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.amount = amount
        self.timestamp = datetime.utcnow().isoformat()
