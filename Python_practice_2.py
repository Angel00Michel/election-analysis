from itertools import count

my_votes = int(input("How many votes did you get in the election? "))

total_votes = int(input("What is the total votes in the election? "))

percentage_votes = (my_votes / total_votes) * 100
print("I received" + str(percentage_votes) + "% of the total votes.")

# If/ If-Else statements

counties = ("Arapahoe", "Denver", "Jefferson")
if counties[1] == 'Denver': 
    print(counties[1])


temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC. ")
else:
    print("Open the windows. ")

# What is the score? 
score = int(input("What is your test score? "))

## Determine the grade
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')


counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print["El Paso is not in the list of counties."]

counties = ["Arapahoe", "Denver", "Jefferson"]
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties.")
else:
    print("Arapahoe and El Paso is not in the list of counties.")

counties = ["Arapahoe", "Denver", "Jefferson"]
if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

