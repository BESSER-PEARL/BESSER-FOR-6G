# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
ExternalGNBCUUPFunction = Class(name="ExternalGNBCUUPFunction")

# ExternalGNBCUUPFunction class attributes and methods
ExternalGNBCUUPFunction_gNBId: Property = Property(name="gNBId", type=IntegerType)
ExternalGNBCUUPFunction_gNBIdLength: Property = Property(name="gNBIdLength", type=IntegerType)
ExternalGNBCUUPFunction.attributes={ExternalGNBCUUPFunction_gNBId, ExternalGNBCUUPFunction_gNBIdLength}

ExternalGNBCUUPFunctionWrapper = Class(name="ExternalGNBCUUPFunctionWrapper")

# ExternalGNBCUUPFunctionWrapper class attributes and methods
ExternalGNBCUUPFunctionWrapper_ExternalGNBCUUPFunction: Property = Property(name="ExternalGNBCUUPFunction", type=list)
ExternalGNBCUUPFunctionWrapper.attributes={ExternalGNBCUUPFunctionWrapper_ExternalGNBCUUPFunction}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-externalgnbcuupfunction",
    types={ExternalGNBCUUPFunction, ExternalGNBCUUPFunctionWrapper},
    associations={},
    generalizations={}
)
