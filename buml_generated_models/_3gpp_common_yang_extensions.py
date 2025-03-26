# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Create Extension classes
in_variant_extension = Class(
    name="InVariantExtension",
    attributes=[
        Property(
            name="description",
            type=StringType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["Indicates that the value for the data node can only be set when its parent data node is being created. To change the value after that, the parent data node must be deleted and recreated with the data node having the new value."]
        )
    ]
)

initial_value_extension = Class(
    name="InitialValueExtension",
    attributes=[
        Property(
            name="description",
            type=StringType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["Specifies a value that the system will set for a leaf leaf-list if a value is not specified for it when its parent list or container is created."]
        ),
        Property(
            name="value",
            type=StringType,
            multiplicity=Multiplicity(1, 1),
            synonyms=["The initial value to be used"]
        )
    ]
)

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-common-yang-extensions",
    types={in_variant_extension, initial_value_extension},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["The module defines YANG extensions needed 3GPP YANG modeling."]
