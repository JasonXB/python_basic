lousy__while_condition = True  # mimics a condition that may always be true
counter = 0
while lousy__while_condition:
    if counter >= 100:
        break
    print("Execute block of code", counter)
    counter += 1
