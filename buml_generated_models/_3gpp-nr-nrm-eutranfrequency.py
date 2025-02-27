# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
EUtranFrequency = Class(name="EUtranFrequency")

# EUtranFrequency class attributes and methods
EUtranFrequency_earfcnDL: Property = Property(name="earfcnDL", type=IntegerType)
EUtranFrequency.attributes={EUtranFrequency_earfcnDL}

EUtranFrequencyWrapper = Class(name="EUtranFrequencyWrapper")

# EUtranFrequencyWrapper class attributes and methods
EUtranFrequencyWrapper_EUtranFrequency: Property = Property(name="EUtranFrequency", type=list)
EUtranFrequencyWrapper.attributes={EUtranFrequencyWrapper_EUtranFrequency}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-eutranfrequency",
    types={EUtranFrequency, EUtranFrequencyWrapper},
    associations={},
    generalizations={}
)
