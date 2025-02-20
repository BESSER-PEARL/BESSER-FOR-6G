# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
EUtraNetwork = Class(name="EUtraNetwork")

# EUtraNetwork class attributes and methods
EUtraNetwork_EUtraNetwork: Property = Property(name="EUtraNetwork", type=list)
EUtraNetwork.attributes={EUtraNetwork_EUtraNetwork}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-eutranetwork",
    types={EUtraNetwork},
    associations={},
    generalizations={}
)
