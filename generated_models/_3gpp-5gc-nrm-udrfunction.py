# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
UDRFuntion = Class(name="UDRFuntion")

# UDRFuntion class attributes and methods
UDRFuntion_sBIFQDN: Property = Property(name="sBIFQDN", type=inet:domain-name)
UDRFuntion_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
UDRFuntion_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
UDRFuntion_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
UDRFuntion.attributes={UDRFuntion_sBIFQDN, UDRFuntion_pLMNIdList, UDRFuntion_sNSSAIList, UDRFuntion_managedNFProfile}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-udrfunction",
    types={UDRFuntion},
    associations={},
    generalizations={}
)
