from stix2 import ThreatActor, Malware, Campaign, Identity, Relationship, Bundle
from random_word import RandomWords

totalObjects = 3
totalCampaign = 3
totalMalware = 3
totalThreat = 1
totalRelationship = 3
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


if len(threatArray) == 1:
    for i in range(totalRelationship):
    # Creating Relationship object
        objtype = "relationship"
        relationship_type = "uses"
        relationship_type2 = "executes"
        relationship = Relationship(type=objtype, relationship_type=relationship_type, source_ref=campaignArray[i], target_ref=malwareArray[i])
        print ("test")
        relationship2 = Relationship(type=objtype, relationship_type=relationship_type2,source_ref=threatArray[0], target_ref=campaignArray[i])
        objects.extend([relationship,relationship2])
if len(threatArray) > 1:
    for i in range(totalRelationship):
    # Creating Relationship object
        objtype = "relationship"
        relationship_type = "uses"
        relationship_type2 = "executes"
        relationship = Relationship(type=objtype, relationship_type=relationship_type, source_ref=campaignArray[i], target_ref=malwareArray[i])
        print ("test2")
        relationship2 = Relationship(type=objtype, relationship_type=relationship_type2,source_ref=threatArray[i], target_ref=campaignArray[i])
    # Adding objects to the objects list
        objects.extend([relationship,relationship2])
# Creating the bundle object
bundle = Bundle(objects=objects)

# Serializing and printing the bundle object
print(bundle.serialize(pretty=True))
