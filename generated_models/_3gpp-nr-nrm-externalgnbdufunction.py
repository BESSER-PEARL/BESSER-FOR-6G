# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
ExternalGNBDUFunction = Class(name="ExternalGNBDUFunction")

# ExternalGNBDUFunction class attributes and methods
ExternalGNBDUFunction_gNBId: Property = Property(name="gNBId", type=IntegerType)
ExternalGNBDUFunction_gNBIdLength: Property = Property(name="gNBIdLength", type=IntegerType)
ExternalGNBDUFunction_pLMNId: Property = Property(name="pLMNId", type=list)
ExternalGNBDUFunction.attributes={ExternalGNBDUFunction_gNBId, ExternalGNBDUFunction_gNBIdLength, ExternalGNBDUFunction_pLMNId}

ExternalGNBDUFunctionWrapper = Class(name="ExternalGNBDUFunctionWrapper")

# ExternalGNBDUFunctionWrapper class attributes and methods
ExternalGNBDUFunctionWrapper_ExternalGNBDUFunction: Property = Property(name="ExternalGNBDUFunction", type=list)
ExternalGNBDUFunctionWrapper.attributes={ExternalGNBDUFunctionWrapper_ExternalGNBDUFunction}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-externalgnbdufunction",
    types={ExternalGNBDUFunction, ExternalGNBDUFunctionWrapper},
    associations={},
    generalizations={}
)
