# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
DANRManagementFunction = Class(name="DANRManagementFunction")

# DANRManagementFunction class attributes and methods
DANRManagementFunction_intrasystemANRManagementSwitch: Property = Property(name="intrasystemANRManagementSwitch", type=BooleanType)
DANRManagementFunction_intersystemANRManagementSwitch: Property = Property(name="intersystemANRManagementSwitch", type=BooleanType)
DANRManagementFunction.attributes={DANRManagementFunction_intrasystemANRManagementSwitch, DANRManagementFunction_intersystemANRManagementSwitch}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-danrmanagementfunction",
    types={DANRManagementFunction},
    associations={},
    generalizations={}
)
