# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
UDRFunction = Class(name="UDRFunction", synonyms=["5G Core UDR Function"])

# UDRFunction class attributes and methods
UDRFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
UDRFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
UDRFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType, synonyms=["The FQDN of the registered NF instance in the service-based interface."])
UDRFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list, synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
UDRFunction.attributes={UDRFunction_managedNFProfile, UDRFunction_pLMNIdList, UDRFunction_sBIFQDN, UDRFunction_sNSSAIList}

UDRFuntion = Class(name="UDRFuntion", synonyms=["Representse the UDRFuntion IOC"])

# UDRFuntion class attributes and methods
UDRFuntion_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
UDRFuntion_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
UDRFuntion_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType, synonyms=["The FQDN of the registered NF instance in the service-based interface."])
UDRFuntion_sNSSAIList: Property = Property(name="sNSSAIList", type=list, synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
UDRFuntion.attributes={UDRFuntion_managedNFProfile, UDRFuntion_pLMNIdList, UDRFuntion_sBIFQDN, UDRFuntion_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-udrfunction",
    types={UDRFunction, UDRFuntion},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the UDR function in 5GC. For more information about the UDR, see 3GPP TS 23.501."]
