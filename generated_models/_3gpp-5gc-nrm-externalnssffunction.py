# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
ExternalNSSFFunction = Class(name="ExternalNSSFFunction")

# ExternalNSSFFunction class attributes and methods
ExternalNSSFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
ExternalNSSFFunction.attributes={ExternalNSSFFunction_pLMNIdList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-externalnssffunction",
    types={ExternalNSSFFunction},
    associations={},
    generalizations={}
)
