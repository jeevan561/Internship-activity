import random

P_heads = 1/2
P_six = 1/6

P_heads_and_six = P_heads * P_six

print("---- Independent Events ----")
print("Theoretical Probability (Heads AND 6):", P_heads_and_six)

trials = 100000
count = 0

for _ in range(trials):
    coin = random.choice(["H", "T"])
    die = random.randint(1, 6)
    
    if coin == "H" and die == 6:
        count += 1

experimental_prob = count / trials
print("Experimental Probability:", experimental_prob)


print("\n---- Dependent Events ----")
P_first_red = 5/10
P_second_red_given_first = 4/9

P_both_red = P_first_red * P_second_red_given_first

print("Theoretical Probability (Both Red):", P_both_red)

trials = 100000
count = 0

for _ in range(trials):
    bag = ["R"] * 5 + ["B"] * 5
    first = random.choice(bag)
    bag.remove(first)
    
    second = random.choice(bag)
    
    if first == "R" and second == "R":
        count += 1

experimental_prob = count / trials
print("Experimental Probability:", experimental_prob)
