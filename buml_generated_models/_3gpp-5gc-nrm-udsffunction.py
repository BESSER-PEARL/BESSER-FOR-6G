# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
UDSFFunction = Class(name="UDSFFunction", synonyms=["5G Core UDSF Function"])

# UDSFFunction class attributes and methods
UDSFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list, synonyms=["Managed Network Function profile"])
UDSFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
UDSFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType, synonyms=["The FQDN of the registered NF instance in the service-based interface."])
UDSFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list, synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
UDSFFunction.attributes={UDSFFunction_managedNFProfile, UDSFFunction_pLMNIdList, UDSFFunction_sBIFQDN, UDSFFunction_sNSSAIList}

UDSFFuntion = Class(name="UDSFFuntion", synonyms=["Represents the UDSFFuntion IOC"])

# UDSFFuntion class attributes and methods
UDSFFuntion_managedNFProfile: Property = Property(name="managedNFProfile", type=list, synonyms=["Managed Network Function profile"])
UDSFFuntion_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
UDSFFuntion_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType, synonyms=["The FQDN of the registered NF instance in the service-based interface."])
UDSFFuntion_sNSSAIList: Property = Property(name="sNSSAIList", type=list, synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
UDSFFuntion.attributes={UDSFFuntion_managedNFProfile, UDSFFuntion_pLMNIdList, UDSFFuntion_sBIFQDN, UDSFFuntion_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-udsffunction",
    types={UDSFFunction, UDSFFuntion},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the UDSF function which can be interacted with any other 5GC NF defined in 3GPP TS 23.501."]
