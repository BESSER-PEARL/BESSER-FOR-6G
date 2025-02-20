# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
ExternalNRFFunction = Class(name="ExternalNRFFunction")

# ExternalNRFFunction class attributes and methods
ExternalNRFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
ExternalNRFFunction.attributes={ExternalNRFFunction_pLMNIdList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-externalnrffunction",
    types={ExternalNRFFunction},
    associations={},
    generalizations={}
)
