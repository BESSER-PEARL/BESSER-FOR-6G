# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
UDRFuntion = Class(name="UDRFuntion")

# UDRFuntion class attributes and methods
UDRFuntion_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
UDRFuntion_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
UDRFuntion_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType)
UDRFuntion_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
UDRFuntion.attributes={UDRFuntion_managedNFProfile, UDRFuntion_pLMNIdList, UDRFuntion_sBIFQDN, UDRFuntion_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-udrfunction",
    types={UDRFuntion},
    associations={},
    generalizations={}
)
