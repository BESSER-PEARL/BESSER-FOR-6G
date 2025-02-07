# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
EP_RP = Class(name="EP_RP")

# EP_RP class attributes and methods
EP_RP_userLabel: Property = Property(name="userLabel", type=StringType)
EP_RP_farEndEntity: Property = Property(name="farEndEntity", type=types3gpp:DistinguishedName)
EP_RP.attributes={EP_RP_userLabel, EP_RP_farEndEntity}

EP_Common = Class(name="EP_Common")

# EP_Common class attributes and methods
EP_Common_remoteAddress: Property = Property(name="remoteAddress", type=inet:ip-address)
EP_Common_localAddress: Property = Property(name="localAddress", type=list)
EP_Common.attributes={EP_Common_remoteAddress, EP_Common_localAddress}

