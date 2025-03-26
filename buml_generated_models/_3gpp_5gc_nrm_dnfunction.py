# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Classes
DNFunction = Class(name="DNFunction")

# DNFunction class attributes and methods
DNFunction_DNFunction: Property = Property(name="DNFunction", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["5G Core DN Function"])
DNFunction.attributes={DNFunction_DNFunction}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-dnfunction",
    types={DNFunction},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC is defined only to describe the IOCs representing Data Network (DN) interaction interface with 5GC (i.e. EP_N6). It has no attributes defined."]
