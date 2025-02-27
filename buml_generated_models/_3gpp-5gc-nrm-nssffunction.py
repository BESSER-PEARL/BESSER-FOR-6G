# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
NSSFFunction = Class(name="NSSFFunction", synonyms=["5G Core NSSF Function"])

# NSSFFunction class attributes and methods
NSSFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
NSSFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
NSSFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType, synonyms=["The FQDN of the registered NF instance in the service-based interface."])
NSSFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list, synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
NSSFFunction.attributes={NSSFFunction_managedNFProfile, NSSFFunction_pLMNIdList, NSSFFunction_sBIFQDN, NSSFFunction_sNSSAIList}

NSSFFunctionGrp = Class(name="NSSFFunctionGrp", synonyms=["Represents the NSSFFunction IOC"])

# NSSFFunctionGrp class attributes and methods
NSSFFunctionGrp_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
NSSFFunctionGrp_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
NSSFFunctionGrp_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType, synonyms=["The FQDN of the registered NF instance in the service-based interface."])
NSSFFunctionGrp_sNSSAIList: Property = Property(name="sNSSAIList", type=list, synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
NSSFFunctionGrp.attributes={NSSFFunctionGrp_managedNFProfile, NSSFFunctionGrp_pLMNIdList, NSSFFunctionGrp_sBIFQDN, NSSFFunctionGrp_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-nssffunction",
    types={NSSFFunction, NSSFFunctionGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the NSSF function in 5GC. For more information about the NSSF, see 3GPP TS 23.501."]
