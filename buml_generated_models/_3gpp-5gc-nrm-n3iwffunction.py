# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
N3IWFFunction = Class(name="N3IWFFunction")

# N3IWFFunction class attributes and methods
N3IWFFunction_commModelList: Property = Property(name="commModelList", type=list)
N3IWFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
N3IWFFunction.attributes={N3IWFFunction_commModelList, N3IWFFunction_pLMNIdList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-n3iwffunction",
    types={N3IWFFunction},
    associations={},
    generalizations={}
)
