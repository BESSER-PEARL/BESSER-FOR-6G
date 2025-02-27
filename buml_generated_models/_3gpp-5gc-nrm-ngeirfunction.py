# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
NGEIRFunction = Class(name="NGEIRFunction", synonyms=["5G Core NGEIR Function"])

# NGEIRFunction class attributes and methods
NGEIRFunction_commModelList: Property = Property(name="commModelList", type=list, synonyms=["Specifies a list of commModel. It can be used by NF and NF services to interact with each other in 5G Core network"])
NGEIRFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
NGEIRFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
NGEIRFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list, synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
NGEIRFunction.attributes={NGEIRFunction_commModelList, NGEIRFunction_managedNFProfile, NGEIRFunction_pLMNIdList, NGEIRFunction_sNSSAIList}

NGEIRFunctionGrp = Class(name="NGEIRFunctionGrp", synonyms=["Represents the NGEIRFunction IOC"])

# NGEIRFunctionGrp class attributes and methods
NGEIRFunctionGrp_commModelList: Property = Property(name="commModelList", type=list, synonyms=["Specifies a list of commModel. It can be used by NF and NF services to interact with each other in 5G Core network"])
NGEIRFunctionGrp_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
NGEIRFunctionGrp_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
NGEIRFunctionGrp_sNSSAIList: Property = Property(name="sNSSAIList", type=list, synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
NGEIRFunctionGrp.attributes={NGEIRFunctionGrp_commModelList, NGEIRFunctionGrp_managedNFProfile, NGEIRFunctionGrp_pLMNIdList, NGEIRFunctionGrp_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-ngeirfunction",
    types={NGEIRFunction, NGEIRFunctionGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the 5G-EIR function in 5GC. For more information about the 5G-EIR, see 3GPP TS 23.501."]
