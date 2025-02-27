# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
CESManagementFunction = Class(name="CESManagementFunction")

# CESManagementFunction class attributes and methods
CESManagementFunction_cesSwitch: Property = Property(name="cesSwitch", type=BooleanType)
CESManagementFunction_energySavingControl: Property = Property(name="energySavingControl", type=EnumerationType)
CESManagementFunction_energySavingState: Property = Property(name="energySavingState", type=EnumerationType)
CESManagementFunction.attributes={CESManagementFunction_cesSwitch, CESManagementFunction_energySavingControl, CESManagementFunction_energySavingState}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-cesmanagementfunction",
    types={CESManagementFunction},
    associations={},
    generalizations={}
)
