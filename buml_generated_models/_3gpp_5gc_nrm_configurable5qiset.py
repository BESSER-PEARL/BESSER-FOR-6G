# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models._3gpp_common_top import domain_model as top3gpp_model

# Classes
Configurable5QISet = Class(name="Configurable5QISet", synonyms=["Represents the Configurable5QISet IOC."])

# Configurable5QISet class attributes and methods
Configurable5QISet_configurable5QIs: Property = Property(name="configurable5QIs", type=list, multiplicity=Multiplicity(0, "*"))
Configurable5QISet.attributes={Configurable5QISet_configurable5QIs}

Configurable5QISetSubtree = Class(name="Configurable5QISetSubtree")

# Configurable5QISetSubtree class attributes and methods
Configurable5QISetSubtree_Configurable5QISet: Property = Property(name="Configurable5QISet", type=top3gpp_model.get_type_by_name('Top_Grp'), multiplicity=Multiplicity(0, "*"), synonyms=["Specifies the non-standardized 5QIs, including their QoS characteristics, that need to be pre-configured (and configurable) to the 5G NFs, see 3GPP TS 23.501."])
Configurable5QISetSubtree.attributes={Configurable5QISetSubtree_Configurable5QISet}

FiveQICharacteristics = Class(name="FiveQICharacteristics")

# FiveQICharacteristics class attributes and methods
FiveQICharacteristics_averagingWindow: Property = Property(name="averagingWindow", type=IntegerType)
FiveQICharacteristics_fiveQIValue: Property = Property(name="fiveQIValue", type=IntegerType, synonyms=["Identifies the 5QI value."])
FiveQICharacteristics_maximumDataBurstVolume: Property = Property(name="maximumDataBurstVolume", type=IntegerType)
FiveQICharacteristics_packetDelayBudget: Property = Property(name="packetDelayBudget", type=IntegerType, synonyms=["Indicates the Packet Delay Budget (in unit of 0.5ms)of a 5QI, as specified in TS 23.501"])
FiveQICharacteristics_packetErrorRate: Property = Property(name="packetErrorRate", type=list, multiplicity=Multiplicity(0, "*"))
FiveQICharacteristics_priorityLevel: Property = Property(name="priorityLevel", type=IntegerType)
FiveQICharacteristics_resourceType: Property = Property(name="resourceType", type=EnumerationType, synonyms=["It indicates the Resource Type of a 5QI, as specified in TS 23.501"])
FiveQICharacteristics.attributes={FiveQICharacteristics_averagingWindow, FiveQICharacteristics_fiveQIValue, FiveQICharacteristics_maximumDataBurstVolume, FiveQICharacteristics_packetDelayBudget, FiveQICharacteristics_packetErrorRate, FiveQICharacteristics_priorityLevel, FiveQICharacteristics_resourceType}

PacketErrorRate = Class(name="PacketErrorRate")

# PacketErrorRate class attributes and methods
PacketErrorRate_exponent: Property = Property(name="exponent", type=IntegerType, synonyms=["The Packet Error Rate of a 5QI expressed as Scalar x 10-k, where k is the Exponent."])
PacketErrorRate_scalar: Property = Property(name="scalar", type=IntegerType, synonyms=["The Packet Error Rate of a 5QI expressed as Scalar x 10-k where k is the Exponent."])
PacketErrorRate.attributes={PacketErrorRate_exponent, PacketErrorRate_scalar}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-configurable5qiset",
    types={Configurable5QISet, Configurable5QISetSubtree, FiveQICharacteristics, PacketErrorRate},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the non-standardized 5QIs, including their QoS characteristics, that need to be pre-configured (and configurable) to the 5G NFs."]
