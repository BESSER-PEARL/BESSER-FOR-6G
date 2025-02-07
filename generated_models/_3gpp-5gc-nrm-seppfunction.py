# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
SEPPFunction = Class(name="SEPPFunction")

# SEPPFunction class attributes and methods
SEPPFunction_sEPPType: Property = Property(name="sEPPType", type=sepp3gpp:SEPPType)
SEPPFunction_sEPPId: Property = Property(name="sEPPId", type=IntegerType)
SEPPFunction_fqdn: Property = Property(name="fqdn", type=inet:domain-name)
SEPPFunction.attributes={SEPPFunction_sEPPType, SEPPFunction_sEPPId, SEPPFunction_fqdn}

