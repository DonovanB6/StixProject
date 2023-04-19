
#Random seeding for the program
#Random Distribution through the objects
#Victims: Identity Object type victim
#Coding Time(Probably picking a range of time and have it happen over that range) Supply the created field of the time object for Identity to track time
# Modified Block 1
from stix2 import ThreatActor, Malware, Campaign, Identity, Relationship, Bundle
from random_word import RandomWords
import random

totalCampaign = int(input("How many Campaign objects would you like to create? "))
totalMalware = int(input("How many malware objects would you like to create? ")) 
totalThreat = totalCampaign
objects = []
campaignArray = []
malwareArray = []
threatArray = []

for i in range(totalCampaign):
    objtype = "campaign"
    name = RandomWords().get_random_word() + " " + objtype
    campaign = Campaign(type=objtype,name=name)
    campaignArray.extend([campaign])
    objects.extend([campaign])

for i in range(totalMalware):
    objtype = "malware"
    labels = "ddos"
    name = RandomWords().get_random_word() + " " + labels
    malware = Malware(type=objtype, labels=labels, name=name, is_family=False)
    malwareArray.extend([malware])
    objects.extend([malware])

for i in range(totalThreat):
    objtype = "threat-actor"
    name = RandomWords().get_random_word() + " " + objtype
    threat_actor = ThreatActor(type=objtype, name=name)
    threatArray.extend([threat_actor])
    objects.extend([threat_actor])

# Modified Block 2
for i in range(len(campaignArray)):
    # Relationship between Campaign and Malware
    relationship1 = Relationship(type="relationship", relationship_type="uses", source_ref=campaignArray[i], target_ref=malwareArray[i])
    objects.append(relationship1)
    
    # Relationship between ThreatActor and Campaign
    relationship2 = Relationship(type="relationship", relationship_type="executes", source_ref=threatArray[i], target_ref=campaignArray[i])
    objects.append(relationship2)

# Randomly distribute remaining Malware objects
remaining_malware = malwareArray[len(campaignArray):]
random.shuffle(remaining_malware)

while remaining_malware:
    selected_campaign = random.choice(campaignArray)
    selected_malware = remaining_malware.pop()
    relationship = Relationship(type="relationship", relationship_type="uses", source_ref=selected_campaign, target_ref=selected_malware)
    objects.append(relationship)

# Creating the bundle object
bundle = Bundle(objects=objects)

# Serializing and printing the bundle object
with open('bundle.json', 'w') as jsonFile:
    jsonFile.write(bundle.serialize(pretty=True))
print("Done")
