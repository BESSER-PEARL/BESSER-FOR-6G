# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
ExternalNSSFFunction = Class(name="ExternalNSSFFunction", synonyms=["5G Core External NSSF Function"])

# ExternalNSSFFunction class attributes and methods
ExternalNSSFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
ExternalNSSFFunction.attributes={ExternalNSSFFunction_pLMNIdList}

ExternalNSSFFunctionGrp = Class(name="ExternalNSSFFunctionGrp")

# ExternalNSSFFunctionGrp class attributes and methods
ExternalNSSFFunctionGrp_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
ExternalNSSFFunctionGrp.attributes={ExternalNSSFFunctionGrp_pLMNIdList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-externalnssffunction",
    types={ExternalNSSFFunction, ExternalNSSFFunctionGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents external NSSF function controlled by another management domain."]
