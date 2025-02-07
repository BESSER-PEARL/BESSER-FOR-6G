# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
ExternalSEPPFunction = Class(name="ExternalSEPPFunction")

# ExternalSEPPFunction class attributes and methods
ExternalSEPPFunction_sEPPId: Property = Property(name="sEPPId", type=IntegerType)
ExternalSEPPFunction_fqdn: Property = Property(name="fqdn", type=inet:domain-name)
ExternalSEPPFunction.attributes={ExternalSEPPFunction_sEPPId, ExternalSEPPFunction_fqdn}

