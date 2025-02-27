# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
SMFFunction = Class(name="SMFFunction")

# SMFFunction class attributes and methods
SMFFunction_commModelList: Property = Property(name="commModelList", type=list)
SMFFunction_configurable5QISetRef: Property = Property(name="configurable5QISetRef", type=StringType)
SMFFunction_dynamic5QISetRef: Property = Property(name="dynamic5QISetRef", type=StringType)
SMFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
SMFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
SMFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType)
SMFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
SMFFunction.attributes={SMFFunction_commModelList, SMFFunction_configurable5QISetRef, SMFFunction_dynamic5QISetRef, SMFFunction_managedNFProfile, SMFFunction_pLMNIdList, SMFFunction_sBIFQDN, SMFFunction_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-smffunction",
    types={SMFFunction},
    associations={},
    generalizations={}
)
