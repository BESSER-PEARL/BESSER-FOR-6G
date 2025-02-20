# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
NRFFunction = Class(name="NRFFunction")

# NRFFunction class attributes and methods
NRFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=inet:domain-name)
NRFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
NRFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
NRFFunction_nFProfileList: Property = Property(name="nFProfileList", type=list)
NRFFunction.attributes={NRFFunction_sBIFQDN, NRFFunction_pLMNIdList, NRFFunction_sNSSAIList, NRFFunction_nFProfileList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-nrffunction",
    types={NRFFunction},
    associations={},
    generalizations={}
)
