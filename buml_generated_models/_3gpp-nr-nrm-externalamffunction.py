# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
ExternalAMFFunction = Class(name="ExternalAMFFunction")

# ExternalAMFFunction class attributes and methods
ExternalAMFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
ExternalAMFFunction.attributes={ExternalAMFFunction_pLMNIdList}

ExternalAMFFunctionWrapper = Class(name="ExternalAMFFunctionWrapper")

# ExternalAMFFunctionWrapper class attributes and methods
ExternalAMFFunctionWrapper_ExternalAMFFunction: Property = Property(name="ExternalAMFFunction", type=list)
ExternalAMFFunctionWrapper.attributes={ExternalAMFFunctionWrapper_ExternalAMFFunction}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-externalamffunction",
    types={ExternalAMFFunction, ExternalAMFFunctionWrapper},
    associations={},
    generalizations={}
)
