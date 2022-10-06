print("Hello World")

Type "help", "copyright", "credits" or "license" for more information.

type(3)
<class 'int'>

type(2019)
<class 'int'>

ballots = 1,341

ballots
(1, 341)

type (ballots)
<class 'tuple'>

type (73.81)
<class 'float'>

type ("Hello world")
<class 'str'>

type ("")
<class 'str'>

type (" ")
<class 'str'>

type (True)
<class 'bool'>

type ('True')
<class 'str'>

5 + 2 * 3
11

8 // 5 - 3
-2

8 + 22 * 2 - 4
48

16 - 3 / 2 + 7 - 1
20.5

3 ** 3 % 5
2

3 ** 3
27

27 % 5
2

5 + 9 * 3 / 2 - 4
14.5

(5 + 2) * 3
21

(8 // 5) - 3
-2

8 + (22 * (2-4))
-36

16 - 3 / (2 + 7) - 1
14.666666666666666

3 ** (3 % 5)
27

5 + (9 * 3 / 2 -4)
14.5

5 + (9 * 3 / (2 - 4))
-8.5
counties = ["Arapahoe", "Denver", "Jefferson"]

counties
['Arapahoe', 'Denver', 'Jefferson']

counties [0]
'Arapahoe'

counties [1]
'Denver'

counties [2]
'Jefferson'


counties
['Arapahoe', 'Denver', 'Jefferson']

counties [0]
'Arapahoe'

print (counties[2])
Jefferson

print (counties[-1])
Jefferson

print (counties[-2])
Denver

len (counties)
3

counties [0:2]
['Arapahoe', 'Denver']

counties [0:1]
['Arapahoe']

counties [:2]
['Arapahoe', 'Denver']

counties [1:2]
['Denver']

counties [1:3]
counties [1:3]

counties [1:3]
['Denver', 'Jefferson']

counties [0:3]
['Arapahoe', 'Denver', 'Jefferson']

counties [1:]
['Denver', 'Jefferson']

counties.append("El Paso")

counties
['Arapahoe', 'Denver', 'Jefferson', 'El Paso']

counties.insert(2, "El Paso")
counties
['Arapahoe', 'Denver', 'El Paso', 'Jefferson', 'El Paso']

counties.remove("El Paso")
counties
['Arapahoe', 'Denver', 'Jefferson', 'El Paso']

counties
['Arapahoe', 'Denver', 'Jefferson', 'El Paso']

counties.pop(3)
'El Paso'
counties
['Arapahoe', 'Denver', 'Jefferson']

counties[2] = "El Paso"
counties
['Arapahoe', 'Denver', 'El Paso']

counties[2] = "Jefferson"
counties
['Arapahoe', 'Denver', 'Jefferson']

counties.insert(1, "El Paso")
counties
['Arapahoe', 'El Paso', 'Denver', 'Jefferson']

counties.append(0)
counties
['Arapahoe', 'El Paso', 'Denver', 'Jefferson', 0]

counties[4] = "0"
counties
['Arapahoe', 'El Paso', 'Denver', 'Jefferson', '0']

counties.pop(0)
'Arapahoe'
counties
['El Paso', 'Denver', 'Jefferson', '0']

counties.pop(3)
'0'
counties
['El Paso', 'Denver', 'Jefferson']

counties.pop(1)
'Denver'
counties
['El Paso', 'Jefferson']

counties.append("Denver")
counties
['El Paso', 'Jefferson', 'Denver']

counties.append("Arapahoe")
counties
['El Paso', 'Jefferson', 'Denver', 'Arapahoe']

counties_tuple = ("Arapahoe", "Denver", "Jefferson")

len(counties_tuple)
3

counties_tuple[1]
'Denver'

counties_tuple[0]
'Arapahoe'

counties_tuple[2]
'Jefferson'

counties_tuple[:2]
('Arapahoe', 'Denver')

counties_tuple[1:2]
('Denver',)

counties_tuple[:-1]
('Arapahoe', 'Denver')

counties_tuple[:-2]
('Arapahoe',)

counties
['El Paso', 'Jefferson', 'Denver', 'Arapahoe']

counties_dict = {}

counties_dict["Arapahoe"] = 422829

counties_dict
{'Arapahoe': 422829}
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

counties_dict
{'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}

len(counties_dict)
3

counties_dict.items()
dict_items([('Arapahoe', 422829), ('Denver', 463353), ('Jefferson', 432438)])

counties_dict.keys()
dict_keys(['Arapahoe', 'Denver', 'Jefferson'])

counties_dict.values()
dict_values([422829, 463353, 432438])

counties_dict.get("Denver")
463353

print(counties_dict.get("Arapahoe"))
422829
print(counties_dict['Arapahoe'])
422829
counties_dict.get("Arapahoe")
422829
counties_dict['Arapahoe']
422829
counties_dict['Arapahoe']
422829
counties_dict["Arapahoe"]
422829

voting_data = []
voting_data
[]

voting_data.append({"county": "Arapahoe", "registered_voters": 422829})
voting_data.append({"county": "Denver", "registered_voters": 463353})
voting_data.append({"county": "Jefferson", "registered_voters": 432438})
voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
len(voting_data)
3

counties.insert(1, "El Paso")
counties
['El Paso', 'El Paso', 'Jefferson', 'Denver', 'Arapahoe']
counties.pop(0)
'El Paso'
counties
['El Paso', 'Jefferson', 'Denver', 'Arapahoe']

voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]

counties.pop(0)
'El Paso'
counties
['Jefferson', 'Denver', 'Arapahoe']
counties.insert(1, "El Paso")
counties
['Jefferson', 'El Paso', 'Denver', 'Arapahoe']
counties_dict["El Paso"] = 461149
counties_dict.items()
dict_items([('Arapahoe', 422829), ('Denver', 463353), ('Jefferson', 432438), ('El Paso', 461149)])



voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
voting_data.insert(1, {"county": "El Paso", "registered_voters": 461149})
voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
voting_data.pop(0)
{'county': 'Arapahoe', 'registered_voters': 422829}
voting_data
[{'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
voting_data.pop(1)
{'county': 'Denver', 'registered_voters': 463353}
voting_data
[{'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Jefferson', 'registered_voters': 432438}]
voting_data.append({"county": "Denver", "registered_voters": 463353})
voting_data
[{'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'Denver', 'registered_voters': 463353}]
voting_data.append({"county": "Arapahoe", "registered_voters": 422829})
voting_data
[{'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Arapahoe', 'registered_voters': 422829}]
counties
['Jefferson', 'El Paso', 'Denver', 'Arapahoe']
voting_data
[{'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Arapahoe', 'registered_voters': 422829}]
counties_dict
{'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438, 'El Paso': 461149}
counties
['Jefferson', 'El Paso', 'Denver', 'Arapahoe']
voting_data
[{'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Arapahoe', 'registered_voters': 422829}]


# How many votes did you get
my_votes = int(input("How many votes did you get in the election? "))

## Total votes in the election
total_votes = int(input("What is the total votes in the election? "))

### Calculate the percentage of votes you received. 
percentage_votes = (my_votes / total_votes) * 100
print("I received" + str(percentage_votes) + "% of the total votes.")
