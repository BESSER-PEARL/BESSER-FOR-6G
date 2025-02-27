# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
NWDAFFunction = Class(name="NWDAFFunction", synonyms=["5G Core NWDAF Function"])

# NWDAFFunction class attributes and methods
NWDAFFunction_commModelList: Property = Property(name="commModelList", type=list, synonyms=["Specifies a list of commModel. It can be used by NF and NF services to interact with each other in 5G Core network"])
NWDAFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
NWDAFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
NWDAFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType, synonyms=["The FQDN of the registered NF instance in the service-based interface."])
NWDAFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list, synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
NWDAFFunction.attributes={NWDAFFunction_commModelList, NWDAFFunction_managedNFProfile, NWDAFFunction_pLMNIdList, NWDAFFunction_sBIFQDN, NWDAFFunction_sNSSAIList}

NWDAFFunctionGrp = Class(name="NWDAFFunctionGrp", synonyms=["Represents the NWDAFFunction IOC"])

# NWDAFFunctionGrp class attributes and methods
NWDAFFunctionGrp_commModelList: Property = Property(name="commModelList", type=list, synonyms=["Specifies a list of commModel. It can be used by NF and NF services to interact with each other in 5G Core network"])
NWDAFFunctionGrp_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
NWDAFFunctionGrp_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
NWDAFFunctionGrp_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType, synonyms=["The FQDN of the registered NF instance in the service-based interface."])
NWDAFFunctionGrp_sNSSAIList: Property = Property(name="sNSSAIList", type=list, synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
NWDAFFunctionGrp.attributes={NWDAFFunctionGrp_commModelList, NWDAFFunctionGrp_managedNFProfile, NWDAFFunctionGrp_pLMNIdList, NWDAFFunctionGrp_sBIFQDN, NWDAFFunctionGrp_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-nwdaffunction",
    types={NWDAFFunction, NWDAFFunctionGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the NWDAF function in 5GC. For more information about the NWDAF, see 3GPP TS 23.501."]
