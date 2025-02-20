# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
ExternalServingGWFunction = Class(name="ExternalServingGWFunction")

# ExternalServingGWFunction class attributes and methods
ExternalServingGWFunctionWrapper = Class(name="ExternalServingGWFunctionWrapper")

# ExternalServingGWFunctionWrapper class attributes and methods
ExternalServingGWFunctionWrapper_ExternalServingGWFunction: Property = Property(name="ExternalServingGWFunction", type=list)
ExternalServingGWFunctionWrapper.attributes={ExternalServingGWFunctionWrapper_ExternalServingGWFunction}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-externalservinggwfunction",
    types={ExternalServingGWFunction, ExternalServingGWFunctionWrapper},
    associations={},
    generalizations={}
)
