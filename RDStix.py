from stix2 import ThreatActor, Malware, Campaign, Identity, Relationship, Bundle
from random_word import RandomWords
import random

#Random seeding for the program
#Random Distribution through the objects
#Victims: Identity Object type victim
#Coding Time(Probably picking a range of time and have it happen over that range) Supply the created field of the time object for Identity to track time
totalObjects = 3
totalCampaign = int(input("How many Campaign objects would you like to create? ")) #3
totalMalware = int(input("How many malware objects would you like to create? "))   #5                                                                #5
totalThreat = int(input("How many threat actor objects would you like to create? ")) #2
totalRelationship = totalCampaign    #int(input("How many Relationship objects would you like to create?(This should be the same as campaign objects) ")) #3
objects = []
campaignArray = []
malwareArray = []
threatArray = []

for i in range(totalCampaign):
    # Creating Campaign object
    objtype = "campaign"
    name = RandomWords().get_random_word() + " " + objtype
    campaign = Campaign(type=objtype,name=name)
    campaignArray.extend([campaign])
    objects.extend([campaign])

for i in range(totalMalware):
    # Creating Malware object
    objtype = "malware"
    labels = "ddos"
    name = RandomWords().get_random_word() + " " + labels
    malware = Malware(type=objtype, labels=labels, name=name, is_family=False)
    malwareArray.extend([malware])
    objects.extend([malware])

for i in range(totalThreat):
    # Creating ThreatActor object
    objtype = "threat-actor"
    name = RandomWords().get_random_word() + " " + objtype
    threat_actor = ThreatActor(type=objtype, name=name)
    threatArray.extend([threat_actor])
    objects.extend([threat_actor])




# Calculate the number of malwares each campaign will receive
malwares_per_campaign = len(malwareArray) // len(campaignArray)

# Calculate the number of extra malwares to be assigned to the first few campaigns
extra_malwares = len(malwareArray) % len(campaignArray)

# Initialize malware index
malware_index = 0

# Initialize a list to keep track of the campaigns that have received malware
campaigns_with_malware = []

for i in range(len(campaignArray)):
    selected_malware = malwareArray[malware_index]
    relationship = Relationship(type="relationship", relationship_type="uses", source_ref=campaignArray[i], target_ref=selected_malware)
    objects.append(relationship)
    malware_index += 1
    campaigns_with_malware.append(campaignArray[i])

# Distribute remaining malware objects to campaigns randomly
for i in range(malware_index, len(malwareArray)):
    selected_campaign = random.choice([c for c in campaignArray if c not in campaigns_with_malware])
    selected_malware = malwareArray[i]
    relationship = Relationship(type="relationship", relationship_type="uses", source_ref=selected_campaign, target_ref=selected_malware)
    objects.append(relationship)
    campaigns_with_malware.append(selected_campaign)

    # Create a relationship between each threat actor and campaign
    relationship2 = Relationship(type="relationship", relationship_type="executes", source_ref=threatArray[i % len(threatArray)], target_ref=campaignArray[i])
    objects.append(relationship2)


# Creating the bundle object

bundle = Bundle(objects=objects)

# Serializing and printing the bundle object
#print(bundle.serialize(pretty=True))

with open('bundle.json', 'w') as jsonFile:
    jsonFile.write(bundle.serialize(pretty=True))
print("Done")
