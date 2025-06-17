animals = [ { "name": "Fluffy", "type": "dog" }, 
            { "name": "Parsley", "type": "dog" }, 
            { "name": "Ginger", "type": "cat" }, 
            { "name": "Biscuit", "type": "cat" },
            { "name": "Poppet", "type": "cow"} ] 

def say_hello_to_pets(pets): 
  for pet in pets: 
    hello_message = ""; 
    if pet["type"] == "dog": 
      hello_message = "Woof" 
      pet_name = pet["name"]
      print(f'{hello_message}, {pet_name}!')
    if pet["type"] == "cat": 
      hello_message = "Meow" 
      pet_name = pet["name"] 
      print(f"{hello_message}, {pet_name}!") 
    else:
      raise Exception("Sorry, only cats and dogs are allowed as pets!")

if __name__ == "__main__": say_hello_to_pets(animals)
