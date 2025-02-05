# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    Constraint
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_managed_element import domain_model as me3gpp_model
from generated_models._3gpp_common_managed_function import domain_model as mf3gpp_model
from generated_models._3gpp_common_subnetwork import domain_model as subnet3gpp_model
from generated_models._3gpp_common_top import domain_model as top3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Enumerations
# Classes
PacketErrorRate = Class(name="PacketErrorRate")
FiveQICharacteristics = Class(name="FiveQICharacteristics")
Configurable5QISetGrp = Class(name="Configurable5QISetGrp")
Configurable5QISetSubtree = Class(name="Configurable5QISetSubtree")

# PacketErrorRate class attributes and methods
PacketErrorRate_scalar: Property = Property(name="scalar", type=IntegerType)
PacketErrorRate_exponent: Property = Property(name="exponent", type=IntegerType)
PacketErrorRate.attributes={PacketErrorRate_scalar, PacketErrorRate_exponent}

# FiveQICharacteristics class attributes and methods
FiveQICharacteristics_fiveQIValue: Property = Property(name="fiveQIValue", type=IntegerType)
FiveQICharacteristics_resourceType: Property = Property(name="resourceType", type=enumeration)
FiveQICharacteristics_priorityLevel: Property = Property(name="priorityLevel", type=IntegerType)
FiveQICharacteristics_packetDelayBudget: Property = Property(name="packetDelayBudget", type=IntegerType)
FiveQICharacteristics_averagingWindow: Property = Property(name="averagingWindow", type=IntegerType)
FiveQICharacteristics_maximumDataBurstVolume: Property = Property(name="maximumDataBurstVolume", type=IntegerType)
FiveQICharacteristics_packetErrorRate: Property = Property(name="packetErrorRate", type=list)
FiveQICharacteristics.attributes={FiveQICharacteristics_priorityLevel, FiveQICharacteristics_packetDelayBudget, FiveQICharacteristics_averagingWindow, FiveQICharacteristics_fiveQIValue, FiveQICharacteristics_maximumDataBurstVolume, FiveQICharacteristics_packetErrorRate, FiveQICharacteristics_resourceType}

# Configurable5QISetGrp class attributes and methods
Configurable5QISetGrp_configurable5QIs: Property = Property(name="configurable5QIs", type=list)
Configurable5QISetGrp.attributes={Configurable5QISetGrp_configurable5QIs}

# Configurable5QISetSubtree class attributes and methods
Configurable5QISetSubtree_Configurable5QISet: Property = Property(name="Configurable5QISet", type=list)
Configurable5QISetSubtree.attributes={Configurable5QISetSubtree_Configurable5QISet}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-configurable5qiset",
    types={PacketErrorRate, FiveQICharacteristics, Configurable5QISetGrp, Configurable5QISetSubtree, types3gpp_model, mf3gpp_model, me3gpp_model, top3gpp_model, types5g3gpp_model, inet_model, subnet3gpp_model},
    associations={},
    generalizations={}
)
