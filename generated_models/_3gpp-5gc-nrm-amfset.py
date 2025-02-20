# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
AMFSet = Class(name="AMFSet")

# AMFSet class attributes and methods
AMFSet_aMFRegion: Property = Property(name="aMFRegion", type=StringType)
AMFSet_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
AMFSet_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
AMFSet.attributes={AMFSet_aMFRegion, AMFSet_pLMNIdList, AMFSet_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-amfset",
    types={AMFSet},
    associations={},
    generalizations={}
)
