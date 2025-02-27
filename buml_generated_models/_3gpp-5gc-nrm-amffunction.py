# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
AMFFunction = Class(name="AMFFunction", synonyms=["5G Core AMF Function"])

# AMFFunction class attributes and methods
AMFFunction_commModelList: Property = Property(name="commModelList", type=list, synonyms=["Specifies a list of commModel. It can be used by NF and NF services to interact with each other in 5G Core network"])
AMFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
AMFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["A list of PLMN identifiers (Mobile Country Code and Mobile Network Code)."])
AMFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType, synonyms=["The FQDN of the registered NF instance in the service-based interface."])
AMFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list, synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
AMFFunction.attributes={AMFFunction_commModelList, AMFFunction_managedNFProfile, AMFFunction_pLMNIdList, AMFFunction_sBIFQDN, AMFFunction_sNSSAIList}

AMFFunctionGrp = Class(name="AMFFunctionGrp", synonyms=["Represents the AMFFunction IOC"])

# AMFFunctionGrp class attributes and methods
AMFFunctionGrp_commModelList: Property = Property(name="commModelList", type=list, synonyms=["Specifies a list of commModel. It can be used by NF and NF services to interact with each other in 5G Core network"])
AMFFunctionGrp_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
AMFFunctionGrp_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["A list of PLMN identifiers (Mobile Country Code and Mobile Network Code)."])
AMFFunctionGrp_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType, synonyms=["The FQDN of the registered NF instance in the service-based interface."])
AMFFunctionGrp_sNSSAIList: Property = Property(name="sNSSAIList", type=list, synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
AMFFunctionGrp.attributes={AMFFunctionGrp_commModelList, AMFFunctionGrp_managedNFProfile, AMFFunctionGrp_pLMNIdList, AMFFunctionGrp_sBIFQDN, AMFFunctionGrp_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-amffunction",
    types={AMFFunction, AMFFunctionGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["AMFFunction derived from basic ManagedFunction."]
