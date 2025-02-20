# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
UDSFFuntion = Class(name="UDSFFuntion")

# UDSFFuntion class attributes and methods
UDSFFuntion_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
UDSFFuntion_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
UDSFFuntion_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType)
UDSFFuntion_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
UDSFFuntion.attributes={UDSFFuntion_managedNFProfile, UDSFFuntion_pLMNIdList, UDSFFuntion_sBIFQDN, UDSFFuntion_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-udsffunction",
    types={UDSFFuntion},
    associations={},
    generalizations={}
)
