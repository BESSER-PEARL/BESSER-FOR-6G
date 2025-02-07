# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
PacketErrorRate = Class(name="PacketErrorRate")

# PacketErrorRate class attributes and methods
PacketErrorRate_scalar: Property = Property(name="scalar", type=IntegerType)
PacketErrorRate_exponent: Property = Property(name="exponent", type=IntegerType)
PacketErrorRate.attributes={PacketErrorRate_scalar, PacketErrorRate_exponent}

FiveQICharacteristics = Class(name="FiveQICharacteristics")

# FiveQICharacteristics class attributes and methods
FiveQICharacteristics_fiveQIValue: Property = Property(name="fiveQIValue", type=IntegerType)
FiveQICharacteristics_resourceType: Property = Property(name="resourceType", type=enumeration)
FiveQICharacteristics_priorityLevel: Property = Property(name="priorityLevel", type=IntegerType)
FiveQICharacteristics_packetDelayBudget: Property = Property(name="packetDelayBudget", type=IntegerType)
FiveQICharacteristics_averagingWindow: Property = Property(name="averagingWindow", type=IntegerType)
FiveQICharacteristics_maximumDataBurstVolume: Property = Property(name="maximumDataBurstVolume", type=IntegerType)
FiveQICharacteristics_packetErrorRate: Property = Property(name="packetErrorRate", type=list)
FiveQICharacteristics.attributes={FiveQICharacteristics_fiveQIValue, FiveQICharacteristics_resourceType, FiveQICharacteristics_priorityLevel, FiveQICharacteristics_packetDelayBudget, FiveQICharacteristics_averagingWindow, FiveQICharacteristics_maximumDataBurstVolume, FiveQICharacteristics_packetErrorRate}

Configurable5QISet = Class(name="Configurable5QISet")

# Configurable5QISet class attributes and methods
Configurable5QISet_configurable5QIs: Property = Property(name="configurable5QIs", type=list)
Configurable5QISet.attributes={Configurable5QISet_configurable5QIs}

Configurable5QISetSubtree = Class(name="Configurable5QISetSubtree")

# Configurable5QISetSubtree class attributes and methods
Configurable5QISetSubtree_Configurable5QISet: Property = Property(name="Configurable5QISet", type=list)
Configurable5QISetSubtree.attributes={Configurable5QISetSubtree_Configurable5QISet}

