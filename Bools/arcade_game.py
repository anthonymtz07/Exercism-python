"""
Instructions 
In this exercise, you need to implement some rules from Pac-Man, the clasic 1980s-era arcade-game
You need four rules to implment, all related to the game states.
"""

#Practica
"""
DEFINE IF PAC-MAN EATS A GHOST
Define the eat_ghost() function that takes two parameters (if Pac-Man has a power pellet active and if Pac-Man is touching a ghost) and returns 
a Boolean value if Pac-Man is able to eat the ghost. The function should return True only if Pac-Man has a power pellet active and is touching 
a ghost.

POINTS: 
* GhostGobbleGame > ghost does not get eaten because not power pallet active
* GhostGobbleGame > ghost does not get eaten because not touching ghost
* GhostGobbleGame > ghost gets eaten

"""
def eat_ghost(power_pellet_active, touching_ghost):
    variable = power_pellet_active and touching_ghost
    print(f'The variable is: {variable}')
#eat_ghost(True, True)

"""
DEFINE IS PAC-MAN SCORES
Define the score() function that takes two parameters (if Pac-Man is touching a power pellet and if Pac-Man is touching a dot) and returns a 
Boolean value if Pac-Man scored. The function should return True if Pac-Man is touching a power pellet or a dot.

POINTS:
* GhostGobbleGame > no score when nothing eaten
* GhostGobbleGame > score when eating dot
* GhostGobbleGame > score when eating power pellet
"""
def score(touching_power_pellet, touching_dot):
    variable = touching_power_pellet or touching_dot
    print(f'The variable is: {variable}')
#score(True, True)

"""
DEFINE IF PAC-MAN LOSES
Define the lose() function that takes two parameters (if Pac-Man has a power pellet active and if Pac-Man is touching a ghost) and returns a 
Boolean value if Pac-Man loses. The function should return True if Pac-Man is touching a ghost and does not have a power pellet active.

POINTS:
* GhostGobbleGame > dont lose if not touching a ghost
* GhostGobbleGame > dont lose if touching a ghost with a power pallet active
* GhostGobbleGame > lose if touching a ghost without a power pallet active
"""
def lose(power_pellet_active, touching_ghost):
    variable = not power_pellet_active and touching_ghost
    #print(f'The variable is: {variable}')
    return variable
#lose(False, True)

"""
DEFINE IF PAC-MAN WIN
Define the win() function that takes three parameters (if Pac-Man has eaten all of the dots, if Pac-Man has a power pellet active, and if Pac-Man is 
touching a ghost) and returns a Boolean value if Pac-Man wins. The function should return True if Pac-Man has eaten all of the dots and has not lost 
based on the parameters defined in part 3.

POINTS:
* GhostGobbleGame > dont win if all dots eaten but touching a ghost
* GhostGobbleGame > dont win if not all dots eaten
* GhostGobbleGame > win if all dots eaten
* GhostGobbleGame > if all dots eaten and touching a ghost with a power pellet active

"""
def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    #variable = has_eaten_all_dots or lose(power_pellet_active, touching_ghost)
    variable = has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)
    print(f'The variable is: {variable}')
win(True,True, True)

