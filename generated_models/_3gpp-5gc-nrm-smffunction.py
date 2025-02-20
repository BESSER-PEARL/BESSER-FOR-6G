# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
SMFFunction = Class(name="SMFFunction")

# SMFFunction class attributes and methods
SMFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=inet:domain-name)
SMFFunction_configurable5QISetRef: Property = Property(name="configurable5QISetRef", type=StringType)
SMFFunction_dynamic5QISetRef: Property = Property(name="dynamic5QISetRef", type=StringType)
SMFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
SMFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
SMFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
SMFFunction_commModelList: Property = Property(name="commModelList", type=list)
SMFFunction.attributes={SMFFunction_sBIFQDN, SMFFunction_configurable5QISetRef, SMFFunction_dynamic5QISetRef, SMFFunction_pLMNIdList, SMFFunction_sNSSAIList, SMFFunction_managedNFProfile, SMFFunction_commModelList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-smffunction",
    types={SMFFunction},
    associations={},
    generalizations={}
)
