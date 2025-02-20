# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
UDMFuntion = Class(name="UDMFuntion")

# UDMFuntion class attributes and methods
UDMFuntion_sBIFQDN: Property = Property(name="sBIFQDN", type=inet:domain-name)
UDMFuntion_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
UDMFuntion_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
UDMFuntion_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
UDMFuntion_commModelList: Property = Property(name="commModelList", type=list)
UDMFuntion.attributes={UDMFuntion_sBIFQDN, UDMFuntion_pLMNIdList, UDMFuntion_sNSSAIList, UDMFuntion_managedNFProfile, UDMFuntion_commModelList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-udmfunction",
    types={UDMFuntion},
    associations={},
    generalizations={}
)
