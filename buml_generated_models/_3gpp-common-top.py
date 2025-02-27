# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
Top_ = Class(name="Top_")

# Top_ class attributes and methods
Top__id: Property = Property(name="id", type=StringType)
Top_.attributes={Top__id}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-common-top",
    types={Top_},
    associations={},
    generalizations={}
)
