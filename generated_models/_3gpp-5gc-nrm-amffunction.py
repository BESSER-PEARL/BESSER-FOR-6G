# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
AMFFunction = Class(name="AMFFunction")

# AMFFunction class attributes and methods
AMFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=inet:domain-name)
AMFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
AMFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
AMFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
AMFFunction_commModelList: Property = Property(name="commModelList", type=list)
AMFFunction.attributes={AMFFunction_sBIFQDN, AMFFunction_pLMNIdList, AMFFunction_sNSSAIList, AMFFunction_managedNFProfile, AMFFunction_commModelList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-amffunction",
    types={AMFFunction},
    associations={},
    generalizations={}
)
