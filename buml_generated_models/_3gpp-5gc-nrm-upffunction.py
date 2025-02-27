# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
UPFFunction = Class(name="UPFFunction", synonyms=["5G Core UPF Function"])

# UPFFunction class attributes and methods
UPFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
UPFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["A list of PLMN identifiers (Mobile Country Code and Mobile Network Code)."])
UPFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list, synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
UPFFunction.attributes={UPFFunction_managedNFProfile, UPFFunction_pLMNIdList, UPFFunction_sNSSAIList}

UPFFunctionGrp = Class(name="UPFFunctionGrp", synonyms=["Represents the UPFFunction IOC"])

# UPFFunctionGrp class attributes and methods
UPFFunctionGrp_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
UPFFunctionGrp_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["A list of PLMN identifiers (Mobile Country Code and Mobile Network Code)."])
UPFFunctionGrp_sNSSAIList: Property = Property(name="sNSSAIList", type=list, synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
UPFFunctionGrp.attributes={UPFFunctionGrp_managedNFProfile, UPFFunctionGrp_pLMNIdList, UPFFunctionGrp_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-upffunction",
    types={UPFFunction, UPFFunctionGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["UPFFunction derived from basic ManagedFunction."]
