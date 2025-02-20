# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
NSSFFunction = Class(name="NSSFFunction")

# NSSFFunction class attributes and methods
NSSFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
NSSFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
NSSFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType)
NSSFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
NSSFFunction.attributes={NSSFFunction_managedNFProfile, NSSFFunction_pLMNIdList, NSSFFunction_sBIFQDN, NSSFFunction_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-nssffunction",
    types={NSSFFunction},
    associations={},
    generalizations={}
)
