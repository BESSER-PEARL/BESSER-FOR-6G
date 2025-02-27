# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
SMSFFunction = Class(name="SMSFFunction")

# SMSFFunction class attributes and methods
SMSFFunction_commModelList: Property = Property(name="commModelList", type=list)
SMSFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
SMSFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
SMSFFunction.attributes={SMSFFunction_commModelList, SMSFFunction_managedNFProfile, SMSFFunction_pLMNIdList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-smsffunction",
    types={SMSFFunction},
    associations={},
    generalizations={}
)
