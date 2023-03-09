from stix2 import ThreatActor, Malware, Campaign, Identity, Relationship, Bundle
from random_word import RandomWords

i = 0
totalObjects = 3
campaignArray = []
while i < totalObjects:
    objtype = "campaign"
    name = RandomWords().get_random_word() + " " + objtype
    campaignArray.append(Campaign(type=objtype,name=name ))
    i += 1

j = 0
malwareArray = []
while j < totalObjects:
    objtype = "malware"
    labels = "ddos"
    malwareArray.append(Malware(type=objtype, labels=labels, name=name, is_family=False))
    name = RandomWords().get_random_word() + " " + labels
    j += 1

k = 0
threatArray = []
while k < totalObjects:
    objtype = "threat-actor"
    name = RandomWords().get_random_word() + " " + objtype  # from the random-word package
    threatArray.append (ThreatActor(type=objtype, name=name))
    k += 1

l = 0
relationshipArray = []
while l < totalObjects:
    objtype = "relationship"
    relationship_type = "uses"  # taken from the Threat Actor relationship guidance
    source_ref = threatArray[l].id   
    target_ref  = malwareArray[l].id
    relationshipArray.append( Relationship(type=objtype, relationship_type=relationship_type, source_ref=source_ref, target_ref=target_ref))
    l += 1

bundleArray = []
z = 0
while z < totalObjects:
    objtype = "bundle"
    objects = [campaignArray[z], malwareArray[z], threatArray[z], relationshipArray[z]]
    bundleArray.append(Bundle(type=objtype, objects = objects))
    print(bundleArray[z].serialize(pretty=True))
    z += 1