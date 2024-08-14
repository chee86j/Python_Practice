# DESCRIPTION:
# Create a function that returns the name of the winner in a fight between 
# two fighters.

# Each fighter takes turns attacking the other and whoever kills the other 
# first is victorious. Death is defined as having health <= 0.

# Each fighter will be a Fighter object/instance. See the Fighter class 
# below in your chosen language.

# Both health and damagePerAttack (damage_per_attack for python) will be 
# integers larger than 0. You can mutate the Fighter objects.

# Your function also receives a third argument, a string, with the name 
# of the fighter that attacks first.

# Example:
#   declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew") => "Lew"
  
#   Lew attacks Harry; Harry now has 3 health.
#   Harry attacks Lew; Lew now has 6 health.
#   Lew attacks Harry; Harry now has 1 health.
#   Harry attacks Lew; Lew now has 2 health.
#   Lew attacks Harry: Harry now has -1 health and is dead. Lew wins.
  
# class Fighter(object):
#     def __init__(self, name, health, damage_per_attack):
#         self.name = name
#         self.health = health
#         self.damage_per_attack = damage_per_attack
        
#     def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
#     __repr__=__str__

# -------------------------------------------------------------------------------------
# -----Solution 1-----While Loop & Simulating Fight-----
def declare_winner(fighter1, fighter2, first_attacker):
    cur, opp = (fighter1, fighter2) if first_attacker == fighter1.name else (fighter2, fighter1)
    while cur.health > 0:        
        opp.health -= cur.damage_per_attack
        cur, opp = opp, cur
    return opp.name
#   1.  We simulate the fight by having each fighter take turns based on the first_attacker.
#   2.  Then Initialize the current fighter as the first attacker & the opponent as the other fighter.
#   3.  Use a while loop to continue the fight until the current fighter's health is less than or equal to 0.
#   4.  In each iteration, the opponent's health is reduced by the current fighter's damage_per_attack.
#   5.  Then swap the current fighter & the opponent to simulate the next turn.
#   6.  Once the loop ends, we return the name of the opponent as the winner.

#   This solution directly simulates the fight using a loop, checking health after each attack. 
#   This approach is straightforward & easy to understand.


# -------------------------------------------------------------------------------------
# -----Solution 2-----Recursion & Simulating Fight-----
def declare_winner(fighter1, fighter2, first_attacker):
    if(fighter1.name == first_attacker):
        winner = fight(fighter1,fighter2)
    elif(fighter2.name == first_attacker):
        winner = fight(fighter2,fighter1)
    return winner.name
    
def fight(attacker,defender):
    print('defender: ' + defender.name + ' current health: ' + str(defender.health))
    print('attacker: ' + attacker.name + ' attacks for: ' + str(attacker.damage_per_attack))

    defender.health = defender.health - attacker.damage_per_attack
    print(defender.name + ' health after being attacked is: ' + str(defender.health))
    
    if(defender.health <= 0):
        print('\r\n')
        print(defender.name + ' has been defeated')
        print(attacker.name + ' is the winner!')
        return attacker
    else:
        print('\r\n')
        return fight(defender,attacker)
#   1.  We define a helper function fight that takes in the attacker & defender fighters.
#   2.  The function prints the current health of the defender & the damage the attacker inflicts.
#   3.  The defender's health is reduced by the attacker's damage_per_attack.
#   4.  If the defender's health is less than or equal to 0, the attacker is declared the winner.
#   5.  Otherwise, the fight continues with the defender becoming the attacker & vice versa.
#   6.  The declare_winner function determines the winner based on the first attacker & calls the fight function accordingly.
#   7.  The name of the winner is returned.

#   This solution uses recursion to simulate the fight between two fighters.
#   The fight function is called recursively until one of the fighters' health drops to 0 or below.
#   This approach is more complex than the previous solution but provides a different perspective on the problem.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Math & Max-----
from math import ceil
from operator import attrgetter


def declare_winner(fighter1, fighter2, first_attacker):
    fighter1.turns = ceil(fighter1.health / float(fighter2.damage_per_attack))
    fighter2.turns = ceil(fighter2.health / float(fighter1.damage_per_attack))
    if fighter1.turns == fighter2.turns:
        return first_attacker
    return max(fighter1, fighter2, key=attrgetter('turns')).name
#   1.  We calculate the number of turns each fighter needs to defeat the other using the ceil function.
#   2.  If the number of turns is the same for both fighters, the first attacker wins.
#   3.  Otherwise, we return the name of the fighter with the maximum number of turns using the max function.
#   4.  The attrgetter function is used to access the turns attribute of the fighter objects.
#   5.  The name of the winner is returned.



# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution-----
# function declareWinner(fighter1, fighter2, firstAttacker) {
#   var fac1 = Math.ceil( fighter1.health / fighter2.damagePerAttack );
#   var fac2 = Math.ceil( fighter2.health / fighter1.damagePerAttack );
#   if(fac1 < fac2) {
#     return fighter2.name;
#   } else if(fac2 < fac1) {
#     return fighter1.name;
#   } else {
#     return firstAttacker;
#   }
# }

#   1.  The declareWinner function takes in two fighter objects & the name of the first attacker.
#   2.  The number of turns each fighter needs to defeat the other is calculated using the ceil function.
#   3.  If the number of turns for fighter 1 is less than fighter 2, fighter 2 wins.
#   4.  If the number of turns for fighter 2 is less than fighter 1, fighter 1 wins.
#   5.  If the number of turns is the same for both fighters, the first attacker wins.
#   6.  The name of the winner is returned.
