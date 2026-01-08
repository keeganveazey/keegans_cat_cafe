# my random fun side project since I love cats and don't want my coding skills to get too rusty

import random
import pandas as pd

class Cat:

    archetypes_data = pd.read_csv("cat_archetypes.csv")

    def __init__(self):
        # note to self: want to set nametag, fav color and skill through user interaction /
        # results of user actions
        self.nametag = "not_named"
        self.coat = random.choice(["orange", "tabby", "grey", "calico", "black"])
        self.aggression = random.randint(1, 10) / 10
        self.energy = random.randint(1, 10) / 10
        self.hunger = random.randint(1, 10) / 10
        self.affection = random.randint(1, 10) / 10
        self.favorite_color = "unknown"
        self.favorite_fish = random.choice(["salmon", "haddock", "sardines", "tuna"])
        self.stinky = random.choice([True, False])
        self.skill = "unknown"

    def set_cat_attributes_manually(self, nametag, coat, aggression,energy,hunger,affection, favorite_color, favorite_fish, stinky,skill):
        self.nametag = nametag
        self.coat = coat
        self.aggression = aggression
        self.energy = energy
        self.hunger = hunger
        self.affection = affection
        self.favorite_color = favorite_color
        self.favorite_fish = favorite_fish
        self.stinky = stinky
        self.skill = skill

    def set_cat_attribute_by_archetype(self,desired_archetype):
        row = self.archetypes_data.loc(self.archetypes_data["archetype"] == desired_archetype)
        self.nametag = row["nametag"]
        self.coat = row["coat"]
        self.aggression =row["aggression"]
        self.energy = row["energy"]
        self.hunger = row["hunger"]
        self.affection = row["affection"]
        self.favorite_color = row["favorite_color"]
        self.favorite_fish = row["favorite_fish"]
        self.stinky = row["stinky"]
        self.skill = row["skill"]

    def respond_to_action(self, action):
        # plan for user to have 4 actions: pet, treat, play, hat, catnip, gentle nose boop
        if action == "PET"
        elif action == "TREAT"









def main():
    print("Welcome to Keegan's Cat Cafe!")

if __name__ == "__main__":
    main()



