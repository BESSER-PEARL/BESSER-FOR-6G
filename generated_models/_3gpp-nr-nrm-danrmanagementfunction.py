# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
DANRManagementFunction = Class(name="DANRManagementFunction")

# DANRManagementFunction class attributes and methods
DANRManagementFunction_intersystemANRManagementSwitch: Property = Property(name="intersystemANRManagementSwitch", type=BooleanType)
DANRManagementFunction_intrasystemANRManagementSwitch: Property = Property(name="intrasystemANRManagementSwitch", type=BooleanType)
DANRManagementFunction.attributes={DANRManagementFunction_intersystemANRManagementSwitch, DANRManagementFunction_intrasystemANRManagementSwitch}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-danrmanagementfunction",
    types={DANRManagementFunction},
    associations={},
    generalizations={}
)
