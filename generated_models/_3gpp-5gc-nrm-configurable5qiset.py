# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
Configurable5QISet = Class(name="Configurable5QISet")

# Configurable5QISet class attributes and methods
Configurable5QISet_configurable5QIs: Property = Property(name="configurable5QIs", type=list)
Configurable5QISet.attributes={Configurable5QISet_configurable5QIs}

Configurable5QISetSubtree = Class(name="Configurable5QISetSubtree")

# Configurable5QISetSubtree class attributes and methods
Configurable5QISetSubtree_Configurable5QISet: Property = Property(name="Configurable5QISet", type=list)
Configurable5QISetSubtree.attributes={Configurable5QISetSubtree_Configurable5QISet}

FiveQICharacteristics = Class(name="FiveQICharacteristics")

# FiveQICharacteristics class attributes and methods
FiveQICharacteristics_averagingWindow: Property = Property(name="averagingWindow", type=IntegerType)
FiveQICharacteristics_fiveQIValue: Property = Property(name="fiveQIValue", type=IntegerType)
FiveQICharacteristics_maximumDataBurstVolume: Property = Property(name="maximumDataBurstVolume", type=IntegerType)
FiveQICharacteristics_packetDelayBudget: Property = Property(name="packetDelayBudget", type=IntegerType)
FiveQICharacteristics_packetErrorRate: Property = Property(name="packetErrorRate", type=list)
FiveQICharacteristics_priorityLevel: Property = Property(name="priorityLevel", type=IntegerType)
FiveQICharacteristics_resourceType: Property = Property(name="resourceType", type=EnumerationType)
FiveQICharacteristics.attributes={FiveQICharacteristics_averagingWindow, FiveQICharacteristics_fiveQIValue, FiveQICharacteristics_maximumDataBurstVolume, FiveQICharacteristics_packetDelayBudget, FiveQICharacteristics_packetErrorRate, FiveQICharacteristics_priorityLevel, FiveQICharacteristics_resourceType}

PacketErrorRate = Class(name="PacketErrorRate")

# PacketErrorRate class attributes and methods
PacketErrorRate_exponent: Property = Property(name="exponent", type=IntegerType)
PacketErrorRate_scalar: Property = Property(name="scalar", type=IntegerType)
PacketErrorRate.attributes={PacketErrorRate_exponent, PacketErrorRate_scalar}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-configurable5qiset",
    types={Configurable5QISet, Configurable5QISetSubtree, FiveQICharacteristics, PacketErrorRate},
    associations={},
    generalizations={}
)
