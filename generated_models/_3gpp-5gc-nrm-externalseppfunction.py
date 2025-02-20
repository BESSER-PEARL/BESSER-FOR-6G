# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
ExternalSEPPFunction = Class(name="ExternalSEPPFunction")

# ExternalSEPPFunction class attributes and methods
ExternalSEPPFunction_sEPPId: Property = Property(name="sEPPId", type=IntegerType)
ExternalSEPPFunction_fqdn: Property = Property(name="fqdn", type=inet:domain-name)
ExternalSEPPFunction.attributes={ExternalSEPPFunction_sEPPId, ExternalSEPPFunction_fqdn}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-externalseppfunction",
    types={ExternalSEPPFunction},
    associations={},
    generalizations={}
)
