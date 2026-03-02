import random

P_spam = 0.1
P_ham = 0.9

P_free_given_spam = 0.9
P_free_given_ham = 0.05

P_free = (P_free_given_spam * P_spam) + (P_free_given_ham * P_ham)

P_spam_given_free = (P_free_given_spam * P_spam) / P_free

print("===== THEORETICAL CALCULATION =====")
print("P(Free) =", P_free)
print("P(Spam | Free) =", P_spam_given_free)

trials = 100000
spam_and_free = 0
free_count = 0

for _ in range(trials):
    
    if random.random() < P_spam:
        email_type = "Spam"
    else:
        email_type = "Ham"
    
    if email_type == "Spam":
        contains_free = random.random() < P_free_given_spam
    else:
        contains_free = random.random() < P_free_given_ham
    
    if contains_free:
        free_count += 1
        if email_type == "Spam":
            spam_and_free += 1

if free_count > 0:
    experimental_probability = spam_and_free / free_count
else:
    experimental_probability = 0

print("\n===== EXPERIMENTAL SIMULATION =====")
print("Total emails containing 'Free':", free_count)
print("Spam emails containing 'Free':", spam_and_free)
print("Experimental P(Spam | Free) =", experimental_probability)
