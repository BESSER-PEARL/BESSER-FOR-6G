# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
CESManagementFunction = Class(name="CESManagementFunction", synonyms=["Represents the CESManagementFunction IOC."])

# CESManagementFunction class attributes and methods
CESManagementFunction_cesSwitch: Property = Property(name="cesSwitch", type=BooleanType, synonyms=["This attribute determines whether the Cross Domain-Centralized SON energy saving function is enabled or disabled."])
CESManagementFunction_energySavingControl: Property = Property(name="energySavingControl", type=EnumerationType, synonyms=["This attribute allows the Cross Domain-Centralized SON energy saving function to initiate energy saving activation or deactivation."])
CESManagementFunction_energySavingState: Property = Property(name="energySavingState", type=EnumerationType, synonyms=["Specifies the status regarding the energy saving in the cell. If the value of energySavingControl is toBeEnergySaving, then it shall be tried to achieve the value isEnergySaving for the energySavingState. If the value of energySavingControl is toBeNotEnergySaving, then it shall be tried to achieve the value isNotEnergySaving for the energySavingState."])
CESManagementFunction.attributes={CESManagementFunction_cesSwitch, CESManagementFunction_energySavingControl, CESManagementFunction_energySavingState}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-cesmanagementfunction",
    types={CESManagementFunction},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the CESManagementFunction Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
