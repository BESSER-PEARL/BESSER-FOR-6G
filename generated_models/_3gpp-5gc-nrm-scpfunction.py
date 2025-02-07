# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
SCPFunction = Class(name="SCPFunction")

# SCPFunction class attributes and methods
SCPFunction_address: Property = Property(name="address", type=inet:host)
SCPFunction_supportedFuncList: Property = Property(name="supportedFuncList", type=list)
SCPFunction.attributes={SCPFunction_address, SCPFunction_supportedFuncList}

