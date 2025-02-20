# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
NRFFunction = Class(name="NRFFunction")

# NRFFunction class attributes and methods
NRFFunction_nFProfileList: Property = Property(name="nFProfileList", type=list)
NRFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
NRFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType)
NRFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
NRFFunction.attributes={NRFFunction_nFProfileList, NRFFunction_pLMNIdList, NRFFunction_sBIFQDN, NRFFunction_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-nrffunction",
    types={NRFFunction},
    associations={},
    generalizations={}
)
