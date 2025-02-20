# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
AMFFunction = Class(name="AMFFunction")

# AMFFunction class attributes and methods
AMFFunction_commModelList: Property = Property(name="commModelList", type=list)
AMFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
AMFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
AMFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType)
AMFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
AMFFunction.attributes={AMFFunction_commModelList, AMFFunction_managedNFProfile, AMFFunction_pLMNIdList, AMFFunction_sBIFQDN, AMFFunction_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-amffunction",
    types={AMFFunction},
    associations={},
    generalizations={}
)
