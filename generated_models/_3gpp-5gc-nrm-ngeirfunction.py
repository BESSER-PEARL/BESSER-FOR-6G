# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
NGEIRFunction = Class(name="NGEIRFunction")

# NGEIRFunction class attributes and methods
NGEIRFunction_commModelList: Property = Property(name="commModelList", type=list)
NGEIRFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
NGEIRFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
NGEIRFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
NGEIRFunction.attributes={NGEIRFunction_commModelList, NGEIRFunction_managedNFProfile, NGEIRFunction_pLMNIdList, NGEIRFunction_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-ngeirfunction",
    types={NGEIRFunction},
    associations={},
    generalizations={}
)
