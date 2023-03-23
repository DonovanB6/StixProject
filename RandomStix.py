from stix2 import ThreatActor, Malware, Campaign, Identity, Relationship, Bundle
from random_word import RandomWords

totalObjects = 3
objects = []

for i in range(totalObjects):
    # Creating Campaign object
    objtype = "campaign"
    name = RandomWords().get_random_word() + " " + objtype
    campaign = Campaign(type=objtype,name=name)

    # Creating Malware object
    objtype = "malware"
    labels = "ddos"
    name = RandomWords().get_random_word() + " " + labels
    malware = Malware(type=objtype, labels=labels, name=name, is_family=False)

    # Creating ThreatActor object
    objtype = "threat-actor"
    name = RandomWords().get_random_word() + " " + objtype
    threat_actor = ThreatActor(type=objtype, name=name)

    # Creating Relationship object
    objtype = "relationship"
    relationship_type = "uses"
    relationship_type2 = "executes"
    relationship = Relationship(type=objtype, relationship_type=relationship_type, source_ref=threat_actor.id, target_ref=malware.id)
    relationship2 = Relationship(type=objtype, relationship_type=relationship_type2,source_ref=threat_actor.id, target_ref=campaign.id)
    # Adding objects to the objects list
    objects.extend([campaign, malware, threat_actor, relationship,relationship2])

# Creating the bundle object
bundle = Bundle(objects=objects)

# Serializing and printing the bundle object
print(bundle.serialize(pretty=True))
