# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
ExternalNRFFunction = Class(name="ExternalNRFFunction", synonyms=["5G Core External NRF Function"])

# ExternalNRFFunction class attributes and methods
ExternalNRFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
ExternalNRFFunction.attributes={ExternalNRFFunction_pLMNIdList}

ExternalNRFFunctionGrp = Class(name="ExternalNRFFunctionGrp")

# ExternalNRFFunctionGrp class attributes and methods
ExternalNRFFunctionGrp_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
ExternalNRFFunctionGrp.attributes={ExternalNRFFunctionGrp_pLMNIdList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-externalnrffunction",
    types={ExternalNRFFunction, ExternalNRFFunctionGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents external NRF function controlled by another management domain."]
