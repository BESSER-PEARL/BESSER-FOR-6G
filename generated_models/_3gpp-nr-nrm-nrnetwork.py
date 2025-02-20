# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
NRNetwork = Class(name="NRNetwork")

# NRNetwork class attributes and methods
NRNetwork_NRNetwork: Property = Property(name="NRNetwork", type=list)
NRNetwork.attributes={NRNetwork_NRNetwork}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-nrnetwork",
    types={NRNetwork},
    associations={},
    generalizations={}
)
