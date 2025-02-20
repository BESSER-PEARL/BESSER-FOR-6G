# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
AUSFFuntion = Class(name="AUSFFuntion")

# AUSFFuntion class attributes and methods
AUSFFuntion_commModelList: Property = Property(name="commModelList", type=list)
AUSFFuntion_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
AUSFFuntion_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
AUSFFuntion_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType)
AUSFFuntion_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
AUSFFuntion.attributes={AUSFFuntion_commModelList, AUSFFuntion_managedNFProfile, AUSFFuntion_pLMNIdList, AUSFFuntion_sBIFQDN, AUSFFuntion_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-ausffunction",
    types={AUSFFuntion},
    associations={},
    generalizations={}
)
