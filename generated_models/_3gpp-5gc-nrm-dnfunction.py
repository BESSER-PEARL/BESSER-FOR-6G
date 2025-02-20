# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
DNFunction = Class(name="DNFunction")

# DNFunction class attributes and methods
# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-dnfunction",
    types={DNFunction},
    associations={},
    generalizations={}
)
