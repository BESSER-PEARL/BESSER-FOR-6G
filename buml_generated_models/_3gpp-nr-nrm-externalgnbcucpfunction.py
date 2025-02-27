# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
ExternalGNBCUCPFunction = Class(name="ExternalGNBCUCPFunction")

# ExternalGNBCUCPFunction class attributes and methods
ExternalGNBCUCPFunction_gNBId: Property = Property(name="gNBId", type=IntegerType)
ExternalGNBCUCPFunction_gNBIdLength: Property = Property(name="gNBIdLength", type=IntegerType)
ExternalGNBCUCPFunction_pLMNId: Property = Property(name="pLMNId", type=list)
ExternalGNBCUCPFunction.attributes={ExternalGNBCUCPFunction_gNBId, ExternalGNBCUCPFunction_gNBIdLength, ExternalGNBCUCPFunction_pLMNId}

ExternalGNBCUCPFunctionWrapper = Class(name="ExternalGNBCUCPFunctionWrapper")

# ExternalGNBCUCPFunctionWrapper class attributes and methods
ExternalGNBCUCPFunctionWrapper_ExternalGNBCUCPFunction: Property = Property(name="ExternalGNBCUCPFunction", type=list)
ExternalGNBCUCPFunctionWrapper.attributes={ExternalGNBCUCPFunctionWrapper_ExternalGNBCUCPFunction}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-externalgnbcucpfunction",
    types={ExternalGNBCUCPFunction, ExternalGNBCUCPFunctionWrapper},
    associations={},
    generalizations={}
)
