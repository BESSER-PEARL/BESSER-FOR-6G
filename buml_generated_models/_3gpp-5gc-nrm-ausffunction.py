# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
AUSFFunction = Class(name="AUSFFunction", synonyms=["5G Core AUSF Function"])

# AUSFFunction class attributes and methods
AUSFFunction_commModelList: Property = Property(name="commModelList", type=list, synonyms=["Specifies a list of commModel. It can be used by NF and NF services to interact with each other in 5G Core network"])
AUSFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
AUSFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
AUSFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType, synonyms=["The FQDN of the registered NF instance in the service-based interface."])
AUSFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list, synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
AUSFFunction.attributes={AUSFFunction_commModelList, AUSFFunction_managedNFProfile, AUSFFunction_pLMNIdList, AUSFFunction_sBIFQDN, AUSFFunction_sNSSAIList}

AUSFFuntion = Class(name="AUSFFuntion", synonyms=["Represents the AUSFFuntion IOC"])

# AUSFFuntion class attributes and methods
AUSFFuntion_commModelList: Property = Property(name="commModelList", type=list, synonyms=["Specifies a list of commModel. It can be used by NF and NF services to interact with each other in 5G Core network"])
AUSFFuntion_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
AUSFFuntion_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
AUSFFuntion_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType, synonyms=["The FQDN of the registered NF instance in the service-based interface."])
AUSFFuntion_sNSSAIList: Property = Property(name="sNSSAIList", type=list, synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
AUSFFuntion.attributes={AUSFFuntion_commModelList, AUSFFuntion_managedNFProfile, AUSFFuntion_pLMNIdList, AUSFFuntion_sBIFQDN, AUSFFuntion_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-ausffunction",
    types={AUSFFunction, AUSFFuntion},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the AUSF function in 5GC. For more information about the AUSF, see 3GPP TS 23.501."]
