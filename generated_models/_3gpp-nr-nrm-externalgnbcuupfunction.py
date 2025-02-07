# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
ExternalGNBCUUPFunction = Class(name="ExternalGNBCUUPFunction")

# ExternalGNBCUUPFunction class attributes and methods
ExternalGNBCUUPFunction_gNBId: Property = Property(name="gNBId", type=IntegerType)
ExternalGNBCUUPFunction_gNBIdLength: Property = Property(name="gNBIdLength", type=IntegerType)
ExternalGNBCUUPFunction.attributes={ExternalGNBCUUPFunction_gNBId, ExternalGNBCUUPFunction_gNBIdLength}

ExternalGNBCUUPFunctionWrapper = Class(name="ExternalGNBCUUPFunctionWrapper")

# ExternalGNBCUUPFunctionWrapper class attributes and methods
ExternalGNBCUUPFunctionWrapper_ExternalGNBCUUPFunction: Property = Property(name="ExternalGNBCUUPFunction", type=list)
ExternalGNBCUUPFunctionWrapper.attributes={ExternalGNBCUUPFunctionWrapper_ExternalGNBCUUPFunction}

