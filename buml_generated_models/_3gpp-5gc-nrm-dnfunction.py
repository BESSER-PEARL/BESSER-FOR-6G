# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
DNFunction = Class(name="DNFunction", synonyms=["5G Core DN Function"])

# DNFunction class attributes and methods
# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-dnfunction",
    types={DNFunction},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC is defined only to describe the IOCs representing Data Network (DN) interaction interface with 5GC (i.e. EP_N6). It has no attributes defined."]
