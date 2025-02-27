# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
Top_ = Class(name="Top_", synonyms=["Abstract class supplying a naming attribute"])

# Top_ class attributes and methods
Top__id: Property = Property(name="id", type=StringType, synonyms=["Key leaf (namingAttribute) for a class/list. Should be used as a key leaf for lists representing stage 2 classes."])
Top_.attributes={Top__id}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-common-top",
    types={Top_},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["The model defines a YANG mapping of the top level information classes used for management of 5G networks and network slicing."]
