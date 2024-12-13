def add_new_dice(self):
        NewDice =[]
        NewDice.append(Dice())
        self.collection_of_dices.append(NewDice)
        return NewDice[0]