# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
NRNetwork = Class(name="NRNetwork")

# NRNetwork class attributes and methods
NRNetwork_NRNetwork: Property = Property(name="NRNetwork", type=list)
NRNetwork.attributes={NRNetwork_NRNetwork}

