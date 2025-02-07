# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
ExternalGNBCUCPFunction = Class(name="ExternalGNBCUCPFunction")

# ExternalGNBCUCPFunction class attributes and methods
ExternalGNBCUCPFunction_gNBId: Property = Property(name="gNBId", type=IntegerType)
ExternalGNBCUCPFunction_gNBIdLength: Property = Property(name="gNBIdLength", type=IntegerType)
ExternalGNBCUCPFunction_pLMNId: Property = Property(name="pLMNId", type=list)
ExternalGNBCUCPFunction.attributes={ExternalGNBCUCPFunction_gNBId, ExternalGNBCUCPFunction_gNBIdLength, ExternalGNBCUCPFunction_pLMNId}

ExternalGNBCUCPFunctionWrapper = Class(name="ExternalGNBCUCPFunctionWrapper")

# ExternalGNBCUCPFunctionWrapper class attributes and methods
ExternalGNBCUCPFunctionWrapper_ExternalGNBCUCPFunction: Property = Property(name="ExternalGNBCUCPFunction", type=list)
ExternalGNBCUCPFunctionWrapper.attributes={ExternalGNBCUCPFunctionWrapper_ExternalGNBCUCPFunction}

