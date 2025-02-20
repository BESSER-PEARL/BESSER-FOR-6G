# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
UPFFunction = Class(name="UPFFunction")

# UPFFunction class attributes and methods
UPFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
UPFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
UPFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
UPFFunction.attributes={UPFFunction_pLMNIdList, UPFFunction_sNSSAIList, UPFFunction_managedNFProfile}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-upffunction",
    types={UPFFunction},
    associations={},
    generalizations={}
)
