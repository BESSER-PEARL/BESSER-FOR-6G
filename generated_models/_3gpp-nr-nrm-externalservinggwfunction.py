# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
ExternalServingGWFunction = Class(name="ExternalServingGWFunction")

# ExternalServingGWFunction class attributes and methods
ExternalServingGWFunctionWrapper = Class(name="ExternalServingGWFunctionWrapper")

# ExternalServingGWFunctionWrapper class attributes and methods
ExternalServingGWFunctionWrapper_ExternalServingGWFunction: Property = Property(name="ExternalServingGWFunction", type=list)
ExternalServingGWFunctionWrapper.attributes={ExternalServingGWFunctionWrapper_ExternalServingGWFunction}

