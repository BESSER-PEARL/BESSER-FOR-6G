# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
SEPPFunction = Class(name="SEPPFunction")

# SEPPFunction class attributes and methods
SEPPFunction_sEPPType: Property = Property(name="sEPPType", type=sepp3gpp:SEPPType)
SEPPFunction_sEPPId: Property = Property(name="sEPPId", type=IntegerType)
SEPPFunction_fqdn: Property = Property(name="fqdn", type=inet:domain-name)
SEPPFunction.attributes={SEPPFunction_sEPPType, SEPPFunction_sEPPId, SEPPFunction_fqdn}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-seppfunction",
    types={SEPPFunction},
    associations={},
    generalizations={}
)
