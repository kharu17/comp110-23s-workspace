"""File to define Fish class."""


class Fish:
    """Represents fish living in a river."""
    age: int

    def __init__(self):
        """Initializes fish object."""
        self.age: int = 0
        return None
    
    def one_day(self):
        """Increases fish age each day."""
        self.age += 1
        return None