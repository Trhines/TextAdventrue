# you are in a house with no windows and doors.
# all you see is a table with a mirror on it.
# your goal is to escape

# Step 1
# Q-what do you do?
# A-look in the mirror
# Event-you see what you saw, you pick up the saw.
# add saw to inventory

# Step 2
# Q-wait for input
# A-use the saw on the table
# Event-you use the saw to cut the table in half
# add halves to inventory

# Step 3
# Q-wait for input
# A-put the two halves together
# Event-the two halves make a hole 

# Step 4
# Q-wait for input
# A-climb into hole
# Event-climb through the hole and under the house and out

# objects

# game manager
    # start new game or load save
    # has a "memory"
    # has save slots
    # memory consists of Players
    # can clear memory

# Player
    # has inventory
    # has a game state(current step)
    # can save

# Step
    # has question
    # has answer
    # has hint
    # has event that moves to next state

# Inventory
    # has items

# Item
    # has use function
    # has nothing hapens response