# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
CESManagementFunction = Class(name="CESManagementFunction")

# CESManagementFunction class attributes and methods
CESManagementFunction_cesSwitch: Property = Property(name="cesSwitch", type=BooleanType)
CESManagementFunction_energySavingState: Property = Property(name="energySavingState", type=enumeration)
CESManagementFunction_energySavingControl: Property = Property(name="energySavingControl", type=enumeration)
CESManagementFunction.attributes={CESManagementFunction_cesSwitch, CESManagementFunction_energySavingState, CESManagementFunction_energySavingControl}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-cesmanagementfunction",
    types={CESManagementFunction},
    associations={},
    generalizations={}
)
