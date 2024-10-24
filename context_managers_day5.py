# This code creates a custom class (context manager) that uses __enter__ and __exit__ methods
# to control what happens when a file (or resource) is opened and closed, similar to how the 
# built-in 'open' function works, but customized for a database connection.

class DatabaseConnection:
    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        print(f"Opening {self.name}.....")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Closing {self.name}.....")

# The custom class is applied to the 'with' statement to manage resource acquisition and release.

with DatabaseConnection("Database Connection") as conn:
    # Perform database operations
    print("Performing operations on the database.")