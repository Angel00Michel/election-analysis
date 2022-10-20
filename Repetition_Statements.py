from multiprocessing.sharedctypes import Value
import numbers
from itertools import count

x = 0
while x <= 5:
    print(x)
    x = x + 1

count = 7

while count < 1:

    print("Hello World")

counties = ["Arapahoe", "Denver", "Jefferson"]
for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

counties_tuple = ("Arapahoe", "Denver", "Jefferson")
for county in counties_tuple:
    print(county)
for i in range(len(counties_tuple)):
    print(counties_tuple[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)

#skill drill 
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict.keys():
    print (county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for voters in counties_dict.values():
    print(voters)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(counties_dict[county])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(counties_dict.get(county))

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(county, voters)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
voting_data = [{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
for county_dict in voting_data:
    print(county_dict)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
voting_data = [{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
for i in range(len(voting_data)):
      print(voting_data[i]['county'])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
voting_data = [{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
voting_data = [{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
for county_dict in voting_data:
     print(county_dict['registered_voters'])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
voting_data = [{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
for county_dict in voting_data:
    print(county_dict['county'])

# How many votes did you get
my_votes = int(input("How many votes did you get in the election? "))

## Total votes in the election
total_votes = int(input("What is the total votes in the election? "))

### Calculate the percentage of votes you received. 
percentage_votes = (my_votes / total_votes) * 100
print("I received" + str(percentage_votes) + "% of the total votes.")

#### F-strings variation
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters")

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
voting_data = [{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes"
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

for county, voters in counties_dict.items():
    print(message_to_candidate)

# Format Floating-Point Decimals
# [EXAMPLE.] f'{value:{width}.{precision}}'
# [EXAMPLE.]f'{value:{width},.{precision}}'

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes"
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

#SKILL DRILL (3.2.11)
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

#SKILL DRILL (3.2.11)
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for county, voters in voting_data():
    print(f"{county} county has {voters} registered voters")

