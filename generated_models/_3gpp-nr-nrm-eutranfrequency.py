# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
EUtranFrequency = Class(name="EUtranFrequency")

# EUtranFrequency class attributes and methods
EUtranFrequency_earfcnDL: Property = Property(name="earfcnDL", type=IntegerType)
EUtranFrequency.attributes={EUtranFrequency_earfcnDL}

EUtranFrequencyWrapper = Class(name="EUtranFrequencyWrapper")

# EUtranFrequencyWrapper class attributes and methods
EUtranFrequencyWrapper_EUtranFrequency: Property = Property(name="EUtranFrequency", type=list)
EUtranFrequencyWrapper.attributes={EUtranFrequencyWrapper_EUtranFrequency}

