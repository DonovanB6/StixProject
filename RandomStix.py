from stix2 import ThreatActor, Malware, Campaign, Identity, Relationship, Bundle
from random_word import RandomWords

objtype = "malware"
labels = "ddos"
name = RandomWords().get_random_word() + " " + labels

malware1 = Malware(type=objtype, labels=labels, name=name, is_family=False)

objtype = "threat-actor"
name = RandomWords().get_random_word() + " " + objtype  # from the random-word package

actor1 = ThreatActor(type=objtype, name=name)

objtype = "relationship"
relationship_type = "uses"  # taken from the Threat Actor relationship guidance
source_ref = actor1.id   
target_ref  = malware1.id

relationship1 = Relationship(type=objtype, relationship_type=relationship_type, source_ref=source_ref, target_ref=target_ref)

objtype = "bundle"
objects = [malware1, actor1, relationship1]
bundle1 = Bundle(type=objtype, objects = objects)

print(bundle1.serialize(pretty=True))