# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
UDSFFuntion = Class(name="UDSFFuntion")

# UDSFFuntion class attributes and methods
UDSFFuntion_sBIFQDN: Property = Property(name="sBIFQDN", type=inet:domain-name)
UDSFFuntion_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
UDSFFuntion_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
UDSFFuntion_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
UDSFFuntion.attributes={UDSFFuntion_sBIFQDN, UDSFFuntion_pLMNIdList, UDSFFuntion_sNSSAIList, UDSFFuntion_managedNFProfile}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-udsffunction",
    types={UDSFFuntion},
    associations={},
    generalizations={}
)
