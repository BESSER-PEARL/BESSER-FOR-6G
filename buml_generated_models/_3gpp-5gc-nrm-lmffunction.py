# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
LMFFunction = Class(name="LMFFunction")

# LMFFunction class attributes and methods
LMFFunction_commModelList: Property = Property(name="commModelList", type=list)
LMFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
LMFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
LMFFunction.attributes={LMFFunction_commModelList, LMFFunction_managedNFProfile, LMFFunction_pLMNIdList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-lmffunction",
    types={LMFFunction},
    associations={},
    generalizations={}
)
