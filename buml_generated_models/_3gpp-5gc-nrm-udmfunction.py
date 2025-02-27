# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
UDMFunction = Class(name="UDMFunction", synonyms=["5G Core UDM Function"])

# UDMFunction class attributes and methods
UDMFunction_commModelList: Property = Property(name="commModelList", type=list, synonyms=["Specifies a list of commModel. It can be used by NF and NF services to interact with each other in 5G Core network"])
UDMFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
UDMFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
UDMFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType, synonyms=["The FQDN of the registered NF instance in the service-based interface."])
UDMFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list, synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
UDMFunction.attributes={UDMFunction_commModelList, UDMFunction_managedNFProfile, UDMFunction_pLMNIdList, UDMFunction_sBIFQDN, UDMFunction_sNSSAIList}

UDMFuntion = Class(name="UDMFuntion", synonyms=["Represents the UDMFuntion IOC"])

# UDMFuntion class attributes and methods
UDMFuntion_commModelList: Property = Property(name="commModelList", type=list, synonyms=["Specifies a list of commModel. It can be used by NF and NF services to interact with each other in 5G Core network"])
UDMFuntion_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
UDMFuntion_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
UDMFuntion_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType, synonyms=["The FQDN of the registered NF instance in the service-based interface."])
UDMFuntion_sNSSAIList: Property = Property(name="sNSSAIList", type=list, synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
UDMFuntion.attributes={UDMFuntion_commModelList, UDMFuntion_managedNFProfile, UDMFuntion_pLMNIdList, UDMFuntion_sBIFQDN, UDMFuntion_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-udmfunction",
    types={UDMFunction, UDMFuntion},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the UDM function in 5GC. For more information about the UDM, see 3GPP TS 23.501."]
