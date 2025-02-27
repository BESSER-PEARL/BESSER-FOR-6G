# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
Domain_ = Class(name="Domain_")

# Domain_ class attributes and methods
Domain__dnPrefix: Property = Property(name="dnPrefix", type=StringType)
Domain__userDefinedNetworkType: Property = Property(name="userDefinedNetworkType", type=StringType)
Domain__userLabel: Property = Property(name="userLabel", type=StringType)
Domain_.attributes={Domain__dnPrefix, Domain__userDefinedNetworkType, Domain__userLabel}

SubNetwork = Class(name="SubNetwork")

# SubNetwork class attributes and methods
SubNetwork_SubNetwork: Property = Property(name="SubNetwork", type=list)
SubNetwork_priorityLabel: Property = Property(name="priorityLabel", type=IntegerType)
SubNetwork.attributes={SubNetwork_SubNetwork, SubNetwork_priorityLabel}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-common-subnetwork",
    types={Domain_, SubNetwork},
    associations={},
    generalizations={}
)
