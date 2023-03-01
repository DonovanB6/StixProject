from stix2.v21 import (ThreatActor, Identity, AttackPattern, Campaign, IntrusionSet, Relationship, ExternalReference, Bundle)
from stix2validator import validate_file, validate_instance, print_results, validate_string


threat_actor = ThreatActor(
    type="threat-actor",
    spec_version="2.1",
    created="2023-03-01T14:00:00.983Z",
    name="Rouge Student",
    description="A disgruntled student angry about a bad test grade",
    threat_actor_types=["Insider"],
    roles=["Student"],
    goals=["Take the OneUp service offline until grade adjusted"],
    primary_motivation="Revenge",
    sophistication="Advanced"
)
identity1 = Identity(
    type="identity",
    spec_version="2.1",
    created="2023-03-01T14:00:00.983Z",
    modified="2023-03-01T14:00:00.983Z",
    name="OneUp",
    identity_class="WebService"
)
attack_pattern1 = AttackPattern(
    type="attack-pattern",
    spec_version="2.1",
    created="2016-08-08T15:50:10.983Z",
    modified="2017-01-30T21:15:04.127Z",
    name="DDOS attack"
)
relationship1 = Relationship(threat_actor, 'targets', identity1)
relationship2 = Relationship(threat_actor, 'uses', attack_pattern1)

bundle = Bundle(objects=[threat_actor, identity1,attack_pattern1, relationship1, relationship2])
print(bundle.serialize(pretty=True))

results = validate_string(bundle.serialize(pretty=True))
print_results(results)
