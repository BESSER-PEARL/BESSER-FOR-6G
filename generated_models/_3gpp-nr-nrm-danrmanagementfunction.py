# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
DANRManagementFunction = Class(name="DANRManagementFunction")

# DANRManagementFunction class attributes and methods
DANRManagementFunction_intrasystemANRManagementSwitch: Property = Property(name="intrasystemANRManagementSwitch", type=BooleanType)
DANRManagementFunction_intersystemANRManagementSwitch: Property = Property(name="intersystemANRManagementSwitch", type=BooleanType)
DANRManagementFunction.attributes={DANRManagementFunction_intrasystemANRManagementSwitch, DANRManagementFunction_intersystemANRManagementSwitch}

