# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
AUSFFuntion = Class(name="AUSFFuntion")

# AUSFFuntion class attributes and methods
AUSFFuntion_sBIFQDN: Property = Property(name="sBIFQDN", type=inet:domain-name)
AUSFFuntion_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
AUSFFuntion_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
AUSFFuntion_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
AUSFFuntion_commModelList: Property = Property(name="commModelList", type=list)
AUSFFuntion.attributes={AUSFFuntion_sBIFQDN, AUSFFuntion_pLMNIdList, AUSFFuntion_sNSSAIList, AUSFFuntion_managedNFProfile, AUSFFuntion_commModelList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-ausffunction",
    types={AUSFFuntion},
    associations={},
    generalizations={}
)
