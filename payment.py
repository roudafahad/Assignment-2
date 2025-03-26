class Payment:
    def __init__(self, transaction_id, amount, method):
        self.transaction_id = transaction_id
        self.amount = amount
        self.method = method

    def process_transaction(self):
        return f"Transaction {self.transaction_id}: {self.amount} USD processed via {self.method}."

    def issue_receipt(self):
        return f"Receipt: Transaction {self.transaction_id}, Amount: {self.amount} USD, Method: {self.method}"
