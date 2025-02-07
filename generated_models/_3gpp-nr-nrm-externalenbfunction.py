# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
ExternalENBFunction = Class(name="ExternalENBFunction")

# ExternalENBFunction class attributes and methods
ExternalENBFunction_eNBId: Property = Property(name="eNBId", type=IntegerType)
ExternalENBFunction.attributes={ExternalENBFunction_eNBId}

ExternalENBFunctionWrapper = Class(name="ExternalENBFunctionWrapper")

# ExternalENBFunctionWrapper class attributes and methods
ExternalENBFunctionWrapper_ExternalENBFunction: Property = Property(name="ExternalENBFunction", type=list)
ExternalENBFunctionWrapper.attributes={ExternalENBFunctionWrapper_ExternalENBFunction}

