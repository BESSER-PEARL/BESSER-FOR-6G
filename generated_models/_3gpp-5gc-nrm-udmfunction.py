# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
UDMFuntion = Class(name="UDMFuntion")

# UDMFuntion class attributes and methods
UDMFuntion_commModelList: Property = Property(name="commModelList", type=list)
UDMFuntion_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
UDMFuntion_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
UDMFuntion_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType)
UDMFuntion_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
UDMFuntion.attributes={UDMFuntion_commModelList, UDMFuntion_managedNFProfile, UDMFuntion_pLMNIdList, UDMFuntion_sBIFQDN, UDMFuntion_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-udmfunction",
    types={UDMFuntion},
    associations={},
    generalizations={}
)
