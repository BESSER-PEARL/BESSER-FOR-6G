# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
NEFFunction = Class(name="NEFFunction")

# NEFFunction class attributes and methods
NEFFunction_isCAPIFSup: Property = Property(name="isCAPIFSup", type=BooleanType)
NEFFunction_isINEF: Property = Property(name="isINEF", type=BooleanType)
NEFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType)
NEFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
NEFFunction.attributes={NEFFunction_isCAPIFSup, NEFFunction_isINEF, NEFFunction_sBIFQDN, NEFFunction_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-neffunction",
    types={NEFFunction},
    associations={},
    generalizations={}
)
