import os


class View():
    def __init__(self):
        self.choice_list = []

    def menu(self):
        for value in self.choice_list:
            print(f"{value['value']} : {value['label']}")
        choice = int(input("Choisissez une option : "))
        os.system('cls' if os.name == 'nt' else 'clear')
        return choice

    def set_choice_list(self, choice_list):
        self.choice_list = choice_list
