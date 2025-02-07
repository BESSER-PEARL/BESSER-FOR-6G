# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
ExternalAMFFunction = Class(name="ExternalAMFFunction")

# ExternalAMFFunction class attributes and methods
ExternalAMFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
ExternalAMFFunction.attributes={ExternalAMFFunction_pLMNIdList}

ExternalAMFFunctionWrapper = Class(name="ExternalAMFFunctionWrapper")

# ExternalAMFFunctionWrapper class attributes and methods
ExternalAMFFunctionWrapper_ExternalAMFFunction: Property = Property(name="ExternalAMFFunction", type=list)
ExternalAMFFunctionWrapper.attributes={ExternalAMFFunctionWrapper_ExternalAMFFunction}

