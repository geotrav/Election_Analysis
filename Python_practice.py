print("Hello World")

counties=["Arapahoe","Denver","El Paso"]
if counties[1] == "Denver":
    print (counties[1])
print (counties[1])

counties_tuple=("arapahoe","Denver","El Paso")
print (len(counties_tuple))
counties_dict={}
counties_dict["Arapahoe"]=422829
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438
print(counties_dict)
print (len(counties_dict))
voting_data=[]
voting_data.append({"county":"Arapahoe","registered_voters": 422829})
voting_data.append({"county":"Denver","registered_voters":463353})
voting_data.append({"county":"Jefferson","registered_voters": 432438})
print(voting_data)
voting_data.insert(1,{"county":"El Paso","registered_voters":461149})
voting_data.pop(0)
voting_data.pop(1)
voting_data.insert(2,{"county":"Denver","registered_voters":463353})
voting_data.append({"county":"Arapahoe","registered_voters":422829})
print(voting_data)
counties =["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print ("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso is not in the list of counties.")
x=0
while x <= 5:
    print (x)
    x= x+1
for county in counties:
    print(county)
for county in counties_dict.keys():
    print(county)
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])
for county, voters in counties_dict.items():
    print(county, voters)

for county, voters in counties_dict.items():
   #print (f"{county} county has {str (voters)}  registered voters.")
   #print (counties_dict)
    print (county + " county has " + str (voters) + " registered voters." )













