# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
NRFFunction = Class(name="NRFFunction", synonyms=["5G Core NRF Function"])

# NRFFunction class attributes and methods
NRFFunction_nFProfileList: Property = Property(name="nFProfileList", type=list, synonyms=["Set of NFProfile(s) to be registered in the NRF instance."])
NRFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
NRFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType, synonyms=["The FQDN of the registered NF instance in the service-based interface."])
NRFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list, synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
NRFFunction.attributes={NRFFunction_nFProfileList, NRFFunction_pLMNIdList, NRFFunction_sBIFQDN, NRFFunction_sNSSAIList}

NRFFunctionGrp = Class(name="NRFFunctionGrp", synonyms=["Represents the NRFFunction IOC"])

# NRFFunctionGrp class attributes and methods
NRFFunctionGrp_nFProfileList: Property = Property(name="nFProfileList", type=list, synonyms=["Set of NFProfile(s) to be registered in the NRF instance."])
NRFFunctionGrp_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
NRFFunctionGrp_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType, synonyms=["The FQDN of the registered NF instance in the service-based interface."])
NRFFunctionGrp_sNSSAIList: Property = Property(name="sNSSAIList", type=list, synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
NRFFunctionGrp.attributes={NRFFunctionGrp_nFProfileList, NRFFunctionGrp_pLMNIdList, NRFFunctionGrp_sBIFQDN, NRFFunctionGrp_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-nrffunction",
    types={NRFFunction, NRFFunctionGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the NRF function in 5GC. For more information about the NRF, see 3GPP TS 23.501 [2]."]
