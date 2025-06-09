# Task 2a
name = input("What is your name?: ")
print(f"Hello {name.capitalize()}!")

# Task 2b
name = input("What is your name?: ").capitalize()
if name == "Bob" or name == "Alice":
  print(f"Hello {name.capitalize()}!")
else:
  print("Sorry... You're not authorised to be greeted!")
