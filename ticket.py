from datetime import datetime

# Represent a customer in line 
class Customer:
    def __init__(self, name, reason):
        self.name = name
        self.reason = reason
        self.timestamp = datetime.now()
        self.history = [("Joined Queue at ", self.timestamp)]

    def add_history(self, action):
        self.history.append((action, datetime.now()))

    def __repr__(self):
        return f"Customer (Name: {self.name}, Reason: {self.reason})"
    
    # Show the time customer will be served
    def display_history(self):
        print(f"\n📜 History for {self.name}:")
        for action, time in self.history:
            print(f" - {action} at {time.strftime('%Y-%m-%d %H:%M:%S')}")

