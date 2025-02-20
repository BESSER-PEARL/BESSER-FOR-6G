# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
PCFFuntion = Class(name="PCFFuntion")

# PCFFuntion class attributes and methods
PCFFuntion_sBIFQDN: Property = Property(name="sBIFQDN", type=inet:domain-name)
PCFFuntion_dynamic5QISetRef: Property = Property(name="dynamic5QISetRef", type=StringType)
PCFFuntion_configurable5QISetRef: Property = Property(name="configurable5QISetRef", type=StringType)
PCFFuntion_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
PCFFuntion_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
PCFFuntion_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
PCFFuntion_commModelList: Property = Property(name="commModelList", type=list)
PCFFuntion.attributes={PCFFuntion_sBIFQDN, PCFFuntion_dynamic5QISetRef, PCFFuntion_configurable5QISetRef, PCFFuntion_pLMNIdList, PCFFuntion_sNSSAIList, PCFFuntion_managedNFProfile, PCFFuntion_commModelList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-pcffunction",
    types={PCFFuntion},
    associations={},
    generalizations={}
)
