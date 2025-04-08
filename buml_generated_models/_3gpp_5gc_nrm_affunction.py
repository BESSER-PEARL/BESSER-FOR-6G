# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)



# Classes
AFFunction = Class(name="AFFunction")

# AFFunction class attributes and methods
AFFunction_AFFunction: Property = Property(name="AFFunction", type=DataType('Top_Grp'), multiplicity=Multiplicity(0, "*"), synonyms=["5G Core AF Function"])
AFFunction.attributes={AFFunction_AFFunction}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-affunction",
    types={AFFunction},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC is defined only to describe the IOCs representing its interaction interface with 5GC (i.e. EP_Rx and EP_N5). It has no attributes defined."]
