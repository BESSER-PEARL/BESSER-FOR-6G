# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
ExternalUPFFunction = Class(name="ExternalUPFFunction")

# ExternalUPFFunction class attributes and methods
ExternalUPFFunctionWrapper = Class(name="ExternalUPFFunctionWrapper")

# ExternalUPFFunctionWrapper class attributes and methods
ExternalUPFFunctionWrapper_ExternalUPFFunction: Property = Property(name="ExternalUPFFunction", type=list)
ExternalUPFFunctionWrapper.attributes={ExternalUPFFunctionWrapper_ExternalUPFFunction}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-externalupffunction",
    types={ExternalUPFFunction, ExternalUPFFunctionWrapper},
    associations={},
    generalizations={}
)
