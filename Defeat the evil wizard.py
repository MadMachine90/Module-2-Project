global evade_was_used
global stats_was_used
global heal_was_used
stats_was_used = False
evade_was_used = False
heal_was_used = False
# Base Character class
class Character:
    def __init__(self, name, health, attack_power, max_health):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = max_health

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def heal(self):
        self.health += 50
        print(f"{self.name} regenerates 50 health: {self.health}")
        if self.health >= self.max_health:
            print(f"{self.name} has reached max health level")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=35, max_health=200)
    def sword_strike(self, opponent):
        damage = self.attack_power 
        opponent.health -= damage
        print(f"{self.name} sword strikes {opponent.name} with {damage} damage")
    def spear_strike(self, opponent):
        damage = self.attack_power + 10
        opponent.health -= damage
        print(f"{self.name} spear strikes {opponent.name} with {damage} damage")

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=30, max_health=215)
    def magic_strike(self, opponent):
        damage = self.attack_power 
        opponent.health -= damage
        print(f"{self.name} maic strikes {opponent.name} with {damage} damage")
        damage = self.attack_power 
        opponent.health -= damage
        print(f"{self.name} magic strikes {opponent.name} with {damage} damage")

    def blind_vision(self, opponent):
       
        damage = self.attack_power + 10
        opponent.health -= damage
        print(f"{self.name} blinds {opponent.name} with {damage} vision damage")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=50, max_health=180)
    def power_spell(self, player):
        damage = self.attack_power + 50
        player.health -= damage
        print(f"The {self.name} has strucked you with a power spell of {damage} damage")
    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Create Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25, max_health=200)
    def quick_shot(self, opponent):
        damage = self.attack_power
        opponent.health -= damage
        print(f"{self.name} attacks with a quick shot of {damage} damage")
    def evade(self):
        self.health += 15
        print(f"{self.name} avoids attack and recovers health")


# Create Paladin class 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=40, max_health=180)
    def axe_strike(self, opponent):
       
        damage = self.attack_power 
        opponent.health -= damage
        print(f"{self.name} strikes with an axe of {damage} damage")
    def sheild_strike(self, opponent):
       
        damage = self.attack_power + 10
        opponent.health -= damage
        print(f"{self.name} strikes with sheild of {damage} damage")

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)  # Implement Archer class
    elif class_choice == '4':
        return Paladin(name)  # Implement Paladin class
    else:
        print("Invalid choice. Defaulting to Warrior.")
def show_special_abilities(player, opponent):
    global evade_was_used
    SPECIAL_CHOICE_INPUT = "select special ability "
    if isinstance(player, Warrior):
        print("1. sword strike")
        print("2. Spear strike")
        user_choice = int(input(SPECIAL_CHOICE_INPUT))
        if user_choice == 1:
            player.sword_strike(opponent)
        elif user_choice == 2:
            player.spear_strike(opponent)
    elif isinstance(player, Mage):
        print("1. Magic strike")
        print("2. blind vision")
        user_choice = int(input(SPECIAL_CHOICE_INPUT))
        if user_choice == 1:
            player.magic_strike(opponent)
        elif user_choice == 2:
            player.blind_vision(opponent)
    elif isinstance(player, Archer):
        print("1. quick shot")
        print("2. evade")
        user_choice = int(input(SPECIAL_CHOICE_INPUT))
        if user_choice == 1:
            player.quick_shot(opponent)
        elif user_choice == 2:
            player.evade()
            evade_was_used = True
    elif isinstance(player, Paladin):
        print("1. Axe strike")
        print("2. sheild strike")
        user_choice = int(input(SPECIAL_CHOICE_INPUT))
        if user_choice == 1:
            player.axe_strike(opponent)
        elif user_choice == 2:
            player.sheild_strike(opponent)
        
def battle(player, wizard):
    global evade_was_used
    global stats_was_used
    global heal_was_used
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            show_special_abilities(player, wizard) # Implement special abilities
        elif choice == '3': 
            player.heal() #Implement heal method
            heal_was_used = True
        elif choice == '4':
            player.display_stats()
            stats_was_used = True
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            if not evade_was_used and not stats_was_used or heal_was_used:
                wizard.attack(player)
            else:
                evade_was_used = False
                stats_was_used = False
                heal_was_used = False

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
