# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
EP_RP = Class(name="EP_RP")

# EP_RP class attributes and methods
EP_RP_userLabel: Property = Property(name="userLabel", type=StringType)
EP_RP_farEndEntity: Property = Property(name="farEndEntity", type=StringType)
EP_RP.attributes={EP_RP_userLabel, EP_RP_farEndEntity}

EP_Common = Class(name="EP_Common")

# EP_Common class attributes and methods
EP_Common_remoteAddress: Property = Property(name="remoteAddress", type=inet:ip-address)
EP_Common_localAddress: Property = Property(name="localAddress", type=list)
EP_Common.attributes={EP_Common_remoteAddress, EP_Common_localAddress}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-common-ep-rp",
    types={EP_RP, EP_Common},
    associations={},
    generalizations={}
)
