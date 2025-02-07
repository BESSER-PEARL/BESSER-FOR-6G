# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
CESManagementFunction = Class(name="CESManagementFunction")

# CESManagementFunction class attributes and methods
CESManagementFunction_cesSwitch: Property = Property(name="cesSwitch", type=BooleanType)
CESManagementFunction_energySavingState: Property = Property(name="energySavingState", type=enumeration)
CESManagementFunction_energySavingControl: Property = Property(name="energySavingControl", type=enumeration)
CESManagementFunction.attributes={CESManagementFunction_cesSwitch, CESManagementFunction_energySavingState, CESManagementFunction_energySavingControl}

