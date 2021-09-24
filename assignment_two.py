first_name = input("what is your name?")
print("hi", first_name, "that sounds like a nice name.")
place = input("where are you from?")
print("wow I wish I could visit", place, ", it sounds like a great place")
favorite_number = input("what is your favorite number?")
print("did you know your favorite number divided by my favorite number is", float(favorite_number)/7)
dream_car = input("what is your dream car?")
print( "ooooooohhh yeah ive heard good things about those" )
cost_of_dream_car = input("how much does it cost?")
print("yikes that's quite a pricey car")
yearly_interest_on_the_car = input("whats the yearly interest on a car like that?")
years = input("if you had to take a loan to buy the "+ dream_car+ " how many years would you take the loan out for?")
r = float(yearly_interest_on_the_car)/100/12
n = int(years)*12

print("if you had bought the", dream_car,"you would have a monthly payment of $",(r*float(cost_of_dream_car))/(1-(1+r)**-n), ",hopefully that's reasonable for your budget that's a total of $",(r*float(cost_of_dream_car))/(1-(1+r)**-n)*60)