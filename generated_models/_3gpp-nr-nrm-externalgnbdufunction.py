# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
ExternalGNBDUFunction = Class(name="ExternalGNBDUFunction")

# ExternalGNBDUFunction class attributes and methods
ExternalGNBDUFunction_gNBId: Property = Property(name="gNBId", type=IntegerType)
ExternalGNBDUFunction_gNBIdLength: Property = Property(name="gNBIdLength", type=IntegerType)
ExternalGNBDUFunction_pLMNId: Property = Property(name="pLMNId", type=list)
ExternalGNBDUFunction.attributes={ExternalGNBDUFunction_gNBId, ExternalGNBDUFunction_gNBIdLength, ExternalGNBDUFunction_pLMNId}

ExternalGNBDUFunctionWrapper = Class(name="ExternalGNBDUFunctionWrapper")

# ExternalGNBDUFunctionWrapper class attributes and methods
ExternalGNBDUFunctionWrapper_ExternalGNBDUFunction: Property = Property(name="ExternalGNBDUFunction", type=list)
ExternalGNBDUFunctionWrapper.attributes={ExternalGNBDUFunctionWrapper_ExternalGNBDUFunction}

