# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
PCFFuntion = Class(name="PCFFuntion")

# PCFFuntion class attributes and methods
PCFFuntion_commModelList: Property = Property(name="commModelList", type=list)
PCFFuntion_configurable5QISetRef: Property = Property(name="configurable5QISetRef", type=StringType)
PCFFuntion_dynamic5QISetRef: Property = Property(name="dynamic5QISetRef", type=StringType)
PCFFuntion_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
PCFFuntion_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
PCFFuntion_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType)
PCFFuntion_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
PCFFuntion.attributes={PCFFuntion_commModelList, PCFFuntion_configurable5QISetRef, PCFFuntion_dynamic5QISetRef, PCFFuntion_managedNFProfile, PCFFuntion_pLMNIdList, PCFFuntion_sBIFQDN, PCFFuntion_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-pcffunction",
    types={PCFFuntion},
    associations={},
    generalizations={}
)
