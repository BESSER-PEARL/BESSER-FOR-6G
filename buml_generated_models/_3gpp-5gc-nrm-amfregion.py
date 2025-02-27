# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
AMFRegion = Class(name="AMFRegion", synonyms=["5G Core AMFRegion IOC"])

# AMFRegion class attributes and methods
AMFRegion_aMFRegionId: Property = Property(name="aMFRegionId", type=StringType, synonyms=["Represents the AMF Region ID, which identifies the region."])
AMFRegion_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
AMFRegion_sNSSAIList: Property = Property(name="sNSSAIList", type=list, synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
AMFRegion.attributes={AMFRegion_aMFRegionId, AMFRegion_pLMNIdList, AMFRegion_sNSSAIList}

AMFRegionGrp = Class(name="AMFRegionGrp", synonyms=["Represents the AMFRegion IOC"])

# AMFRegionGrp class attributes and methods
AMFRegionGrp_aMFRegionId: Property = Property(name="aMFRegionId", type=StringType, synonyms=["Represents the AMF Region ID, which identifies the region."])
AMFRegionGrp_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
AMFRegionGrp_sNSSAIList: Property = Property(name="sNSSAIList", type=list, synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
AMFRegionGrp.attributes={AMFRegionGrp_aMFRegionId, AMFRegionGrp_pLMNIdList, AMFRegionGrp_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-amfregion",
    types={AMFRegion, AMFRegionGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the AMF Region which consists one or multiple AMF Sets."]
