# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
GNBCUCPFunction = Class(name="GNBCUCPFunction")

# GNBCUCPFunction class attributes and methods
GNBCUCPFunction_gNBId: Property = Property(name="gNBId", type=IntegerType)
GNBCUCPFunction_gNBIdLength: Property = Property(name="gNBIdLength", type=IntegerType)
GNBCUCPFunction_gNBCUName: Property = Property(name="gNBCUName", type=StringType)
GNBCUCPFunction_configurable5QISetRef: Property = Property(name="configurable5QISetRef", type=types3gpp:DistinguishedName)
GNBCUCPFunction_dynamic5QISetRef: Property = Property(name="dynamic5QISetRef", type=types3gpp:DistinguishedName)
GNBCUCPFunction_pLMNId: Property = Property(name="pLMNId", type=list)
GNBCUCPFunction.attributes={GNBCUCPFunction_gNBId, GNBCUCPFunction_gNBIdLength, GNBCUCPFunction_gNBCUName, GNBCUCPFunction_configurable5QISetRef, GNBCUCPFunction_dynamic5QISetRef, GNBCUCPFunction_pLMNId}

