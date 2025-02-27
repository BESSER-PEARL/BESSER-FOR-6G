# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
UPFFunction = Class(name="UPFFunction")

# UPFFunction class attributes and methods
UPFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
UPFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
UPFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
UPFFunction.attributes={UPFFunction_managedNFProfile, UPFFunction_pLMNIdList, UPFFunction_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-upffunction",
    types={UPFFunction},
    associations={},
    generalizations={}
)
