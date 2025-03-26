# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Create the Energy Saving State enumeration
energy_saving_state_enum = Enumeration(
    name="EnergySavingState",
    literals=[
        EnumerationLiteral("isNotEnergySaving"),
        EnumerationLiteral("isEnergySaving")
    ]
)

# Create the Energy Saving Control enumeration
energy_saving_control_enum = Enumeration(
    name="EnergySavingControl",
    literals=[
        EnumerationLiteral("toBeEnergySaving"),
        EnumerationLiteral("toBeNotEnergySaving")
    ]
)

# Create CESManagementFunction class
ces_management_function_class = Class(
    name="CESManagementFunction",
    attributes=[
        Property(
            name="cesSwitch",
            type=BooleanType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["This attribute determines whether the Cross Domain-Centralized SON energy saving function is enabled or disabled."]
        ),
        Property(
            name="energySavingState",
            type=energy_saving_state_enum,
            multiplicity=Multiplicity(1, 1),
            synonyms=["Specifies the status regarding the energy saving in the cell. If the value of energySavingControl is toBeEnergySaving, then it shall be tried to achieve the value isEnergySaving for the energySavingState. If the value of energySavingControl is toBeNotEnergySaving, then it shall be tried to achieve the value isNotEnergySaving for the energySavingState."]
        ),
        Property(
            name="energySavingControl",
            type=energy_saving_control_enum,
            multiplicity=Multiplicity(1, 1),
            synonyms=["This attribute allows the Cross Domain-Centralized SON energy saving function to initiate energy saving activation or deactivation."]
        )
    ]
)

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-cesmanagementfunction",
    types={ces_management_function_class, energy_saving_state_enum, energy_saving_control_enum},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the CESManagementFunction Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
