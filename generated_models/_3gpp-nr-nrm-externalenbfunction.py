# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
ExternalENBFunction = Class(name="ExternalENBFunction")

# ExternalENBFunction class attributes and methods
ExternalENBFunction_eNBId: Property = Property(name="eNBId", type=IntegerType)
ExternalENBFunction.attributes={ExternalENBFunction_eNBId}

ExternalENBFunctionWrapper = Class(name="ExternalENBFunctionWrapper")

# ExternalENBFunctionWrapper class attributes and methods
ExternalENBFunctionWrapper_ExternalENBFunction: Property = Property(name="ExternalENBFunction", type=list)
ExternalENBFunctionWrapper.attributes={ExternalENBFunctionWrapper_ExternalENBFunction}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-externalenbfunction",
    types={ExternalENBFunction, ExternalENBFunctionWrapper},
    associations={},
    generalizations={}
)
