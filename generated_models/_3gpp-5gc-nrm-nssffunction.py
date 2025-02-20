# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
NSSFFunction = Class(name="NSSFFunction")

# NSSFFunction class attributes and methods
NSSFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=inet:domain-name)
NSSFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
NSSFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
NSSFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
NSSFFunction.attributes={NSSFFunction_sBIFQDN, NSSFFunction_pLMNIdList, NSSFFunction_sNSSAIList, NSSFFunction_managedNFProfile}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-nssffunction",
    types={NSSFFunction},
    associations={},
    generalizations={}
)
