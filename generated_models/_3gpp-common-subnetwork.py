# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
SubNetwork = Class(name="SubNetwork")

# SubNetwork class attributes and methods
SubNetwork_priorityLabel: Property = Property(name="priorityLabel", type=IntegerType)
SubNetwork_SubNetwork: Property = Property(name="SubNetwork", type=list)
SubNetwork.attributes={SubNetwork_priorityLabel, SubNetwork_SubNetwork}

Domain_ = Class(name="Domain_")

# Domain_ class attributes and methods
Domain__userDefinedNetworkType: Property = Property(name="userDefinedNetworkType", type=StringType)
Domain__dnPrefix: Property = Property(name="dnPrefix", type=types3gpp:DistinguishedName)
Domain__userLabel: Property = Property(name="userLabel", type=StringType)
Domain_.attributes={Domain__userDefinedNetworkType, Domain__dnPrefix, Domain__userLabel}

