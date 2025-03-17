'''
REMINDER:
In addition to completing the Warrior and Mage classes, you need to create two more classes that inherit from Character, such as:
- Archer
- Paladin
You don't have to create these EXACT classes, you have creative freedom about which additional classes to create. It doesn't have to be Archer & Paladin.

Each custom class must have two unique abilities, such as:
- Archer: "Quick Shot" (double arrow attack) and "Evade" (avoid next attack).
- Paladin: "Holy Strike" (bonus damage) and "Divine Shield" (blocks the next attack).

Additionally, you need to implement a heal() method in the base Character class.
Lastly, you need to randomize the damage done in the Character class' attack() method.
'''
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit

    '''
    Modify this function so that the character does a random amount of damage.
    Hint: Look up the randint() function from Python's random library.
    '''
    def attack(self, opponent):
        damage = self.attack_power
        
        # Check if the opponent has a 'evadeNextAttack' attribute. If they do not, proceed with the attack.
        if not hasattr(opponent, 'evadeNextAttack'):
            opponent.health -= damage
            print(f"\n{self.name} attacks {opponent.name} for {damage} damage!")
        # Else, if they do have an 'evadeNextAttack' attribute and the value is False, proceed with the attack.
        elif hasattr(opponent, 'evadeNextAttack') and opponent.evadeNextAttack == False:
            opponent.health -= damage
            print(f"\n{self.name} attacks {opponent.name} for {damage} damage!")
        # Else, if they do have an 'evadeNextAttack' attribute and the value is True, set the value back to False and display that the attack was evaded.
        elif hasattr(opponent, 'evadeNextAttack') and opponent.evadeNextAttack == True:
            print(f"\n{self.name} attacks {opponent.name}, but {opponent.name} evades the attack!")
            opponent.evadeNextAttack = False
            
    def heal(self):
        # Implement this method.
        print("The heal method needs to be implemented still.")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
        

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30)
        '''
        evadeNextAttack is going to be used as a flag to determine whether the Rogue is going to evade the next attack.
        '''
        self.evadeNextAttack = False
        
    def special_ability(self, opponent):
        print("\nAbilities:")
        print("1. Gathering Shadows")
        print("2. Siphoning Strikes")
        print("3. Preemptive Dodge (Evade)")
        action = input("Which ability do you want to use? ")
        
        if action == "1":
            '''
            Ability: Gathering Shadows
            Increases the Rogue's damage by 30, but does not attack.
            '''
            self.attack_power += 30
            print(f"\nShadows gather around {self.name} increasing their damage to {self.attack_power}.")
        elif action == "2":
            '''
            Ability: Siphoning Strikes
            Strikes the opponent and heals for half of the damage dealt.
            '''
            opponent.health -= self.attack_power
            self.health += self.attack_power // 2 # Floor division rounds to the nearest integer (whole number)
            if self.health > self.max_health:
                self.health = self.max_health
            print(f"\n{self.name} strikes {opponent.name} with vampiric daggers, dealing {self.attack_power} damage and siphoning the wizard's health to {self.health} health.")
        elif action == "3":
            '''
            Ability: Preemptive Dodge
            Dodge the next attack.
            '''
            self.evadeNextAttack = True
            print(f"\n{self.name} uses Preemptive Dodge. He will evade the next attack!")
            
        