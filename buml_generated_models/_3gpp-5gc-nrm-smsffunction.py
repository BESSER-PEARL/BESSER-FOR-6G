# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
SMSFFunction = Class(name="SMSFFunction", synonyms=["5G Core SMSF Function"])

# SMSFFunction class attributes and methods
SMSFFunction_commModelList: Property = Property(name="commModelList", type=list)
SMSFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
SMSFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
SMSFFunction.attributes={SMSFFunction_commModelList, SMSFFunction_managedNFProfile, SMSFFunction_pLMNIdList}

SMSFFunctionGrp = Class(name="SMSFFunctionGrp")

# SMSFFunctionGrp class attributes and methods
SMSFFunctionGrp_commModelList: Property = Property(name="commModelList", type=list)
SMSFFunctionGrp_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
SMSFFunctionGrp_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
SMSFFunctionGrp.attributes={SMSFFunctionGrp_commModelList, SMSFFunctionGrp_managedNFProfile, SMSFFunctionGrp_pLMNIdList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-smsffunction",
    types={SMSFFunction, SMSFFunctionGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the SMSF function defined in 3GPP TS 23.501."]
