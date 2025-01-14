"""File to define Bear class."""


class Bear:
    """Represents bears near a river."""
    age: int
    hunger_score: int
    
    def __init__(self):
        """Initializes Bear object."""
        self.age: int = 0
        self.hunger_score: int = 0
        return None
    
    def one_day(self):
        """Increases age and decreases hunger each day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Updates number fish eaten by bear."""
        self.hunger_score += num_fish
        return None
