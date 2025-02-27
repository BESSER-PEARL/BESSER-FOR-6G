# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
NWDAFFunction = Class(name="NWDAFFunction")

# NWDAFFunction class attributes and methods
NWDAFFunction_commModelList: Property = Property(name="commModelList", type=list)
NWDAFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
NWDAFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
NWDAFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType)
NWDAFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
NWDAFFunction.attributes={NWDAFFunction_commModelList, NWDAFFunction_managedNFProfile, NWDAFFunction_pLMNIdList, NWDAFFunction_sBIFQDN, NWDAFFunction_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-nwdaffunction",
    types={NWDAFFunction},
    associations={},
    generalizations={}
)
