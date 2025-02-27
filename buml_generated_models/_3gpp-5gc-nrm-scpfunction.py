# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
SCPFunction = Class(name="SCPFunction")

# SCPFunction class attributes and methods
SCPFunction_address: Property = Property(name="address", type=StringType)
SCPFunction_supportedFuncList: Property = Property(name="supportedFuncList", type=list)
SCPFunction.attributes={SCPFunction_address, SCPFunction_supportedFuncList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-scpfunction",
    types={SCPFunction},
    associations={},
    generalizations={}
)
