# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
SMFFunction = Class(name="SMFFunction", synonyms=["5G Core SMF Function"])

# SMFFunction class attributes and methods
SMFFunction_commModelList: Property = Property(name="commModelList", type=list, synonyms=["Specifies a list of commModel. It can be used by NF and NF services to interact with each other in 5G Core network"])
SMFFunction_configurable5QISetRef: Property = Property(name="configurable5QISetRef", type=StringType, synonyms=["DN of the Configurable5QISet that the SMFFunction supports (is associated to)."])
SMFFunction_dynamic5QISetRef: Property = Property(name="dynamic5QISetRef", type=StringType, synonyms=["DN of the Dynamic5QISet that the SMFFunction supports (is associated to)."])
SMFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
SMFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["A list of PLMN identifiers (Mobile Country Code and Mobile Network Code)."])
SMFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType, synonyms=["The FQDN of the registered NF instance in the service-based interface."])
SMFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list, synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
SMFFunction.attributes={SMFFunction_commModelList, SMFFunction_configurable5QISetRef, SMFFunction_dynamic5QISetRef, SMFFunction_managedNFProfile, SMFFunction_pLMNIdList, SMFFunction_sBIFQDN, SMFFunction_sNSSAIList}

SMFFunctionGrp = Class(name="SMFFunctionGrp", synonyms=["Represents the SMFFuntion IOC"])

# SMFFunctionGrp class attributes and methods
SMFFunctionGrp_commModelList: Property = Property(name="commModelList", type=list, synonyms=["Specifies a list of commModel. It can be used by NF and NF services to interact with each other in 5G Core network"])
SMFFunctionGrp_configurable5QISetRef: Property = Property(name="configurable5QISetRef", type=StringType, synonyms=["DN of the Configurable5QISet that the SMFFunction supports (is associated to)."])
SMFFunctionGrp_dynamic5QISetRef: Property = Property(name="dynamic5QISetRef", type=StringType, synonyms=["DN of the Dynamic5QISet that the SMFFunction supports (is associated to)."])
SMFFunctionGrp_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
SMFFunctionGrp_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["A list of PLMN identifiers (Mobile Country Code and Mobile Network Code)."])
SMFFunctionGrp_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType, synonyms=["The FQDN of the registered NF instance in the service-based interface."])
SMFFunctionGrp_sNSSAIList: Property = Property(name="sNSSAIList", type=list, synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
SMFFunctionGrp.attributes={SMFFunctionGrp_commModelList, SMFFunctionGrp_configurable5QISetRef, SMFFunctionGrp_dynamic5QISetRef, SMFFunctionGrp_managedNFProfile, SMFFunctionGrp_pLMNIdList, SMFFunctionGrp_sBIFQDN, SMFFunctionGrp_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-smffunction",
    types={SMFFunction, SMFFunctionGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["SMFFunction derived from basic ManagedFunction."]
