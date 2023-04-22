"""File to define River class."""

__author__ = "730459195"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """Represents river with bear and fish."""
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes old fish and bears."""
        my_list: list[Bear] = []
        my_list2: list[Fish] = []
        for b in self.bears:
            if b.age <= 5:
                my_list.append(b)
        self.bears = my_list
        for f in self.fish:
            if f.age <= 3:
                my_list2.append(f)
        self.fish = my_list2
        return None
    
    def remove_fish(self, amount: int):
        """Removes frontmost fish from river."""
        for i in range(0, amount):
            self.fish.pop(i)
            i += 1
        return None

    def bears_eating(self):
        """Portrays bears eating fish from river."""
        for b in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                b.eat(3)
        return None
    
    def check_hunger(self):
        """Removes bear that is too hungry."""
        alive_bears: list[Bear] = []
        for i in self.bears:
            if i.hunger_score < 0:
                alive_bears.append(i)
        self.bears = alive_bears
        return None
        
    def repopulate_fish(self):
        """Adds new fish to population."""
        for i in range((len(self.fish) // 2) * 4):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Adds new bears to population."""
        for i in range(len(self.bears) // 2):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Shows fish and bear population in river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
    def one_river_week(self):
        """Shows river each day of the week."""
        i: int = 1
        while i <= 7:
            self.one_river_day()
            i += 1
