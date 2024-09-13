import random
dice_art = {
    1: ("┌─────────┐", 
        "│         │", 
        "│    ●    │", 
        "│         │", 
        "└─────────┘"),
    2: ("┌─────────┐", 
        "│    ●    │", 
        "│         │", 
        "│    ●    │", 
        "└─────────┘"),
    3: ("┌─────────┐", 
        "│    ●    │", 
        "│    ●    │", 
        "│    ●    │", 
        "└─────────┘"),
    4: ("┌─────────┐", 
        "│  ●   ●  │", 
        "│         │", 
        "│  ●   ●  │", 
        "└─────────┘"),
    5: ("┌─────────┐", 
        "│  ●   ●  │", 
        "│    ●    │", 
        "│  ●   ●  │", 
        "└─────────┘"),
    6: ("┌─────────┐", 
        "│  ●   ●  │", 
        "│  ●   ●  │", 
        "│  ●   ●  │", 
        "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input("How many dice would you like to roll? "))
for i in range(num_of_dice):
    dice.append(random.randint(1, 6))

for i in range(num_of_dice):
    for line in dice_art[dice[i]]:
        print(f"{line}")

for i in dice:
    total += i
print(f"Total: {total}")