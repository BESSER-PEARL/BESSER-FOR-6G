# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Classes
DANRManagementFunction = Class(name="DANRManagementFunction", synonyms=["Represents the DANRManagementFunction IOC."])

# DANRManagementFunction class attributes and methods
DANRManagementFunction_intersystemANRManagementSwitch: Property = Property(name="intersystemANRManagementSwitch", type=BooleanType, synonyms=["This attribute determines whether the inter-system ANR function is activated or deactivated."])
DANRManagementFunction_intrasystemANRManagementSwitch: Property = Property(name="intrasystemANRManagementSwitch", type=BooleanType, synonyms=["This attribute determines whether the intra-system ANR function is activated or deactivated."])
DANRManagementFunction.attributes={DANRManagementFunction_intersystemANRManagementSwitch, DANRManagementFunction_intrasystemANRManagementSwitch}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-danrmanagementfunction",
    types={DANRManagementFunction},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the DANRManagementFunction Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
