# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
AMFSet = Class(name="AMFSet", synonyms=["5G Core AMFSet IOC"])

# AMFSet class attributes and methods
AMFSet_aMFRegion: Property = Property(name="aMFRegion", type=StringType, synonyms=["The AMFRegion that the AFMSet is associated with."])
AMFSet_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
AMFSet_sNSSAIList: Property = Property(name="sNSSAIList", type=list, synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
AMFSet.attributes={AMFSet_aMFRegion, AMFSet_pLMNIdList, AMFSet_sNSSAIList}

AMFSetGrp = Class(name="AMFSetGrp", synonyms=["Represents the AMFSet IOC"])

# AMFSetGrp class attributes and methods
AMFSetGrp_aMFRegion: Property = Property(name="aMFRegion", type=StringType, synonyms=["The AMFRegion that the AFMSet is associated with."])
AMFSetGrp_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
AMFSetGrp_sNSSAIList: Property = Property(name="sNSSAIList", type=list, synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
AMFSetGrp.attributes={AMFSetGrp_aMFRegion, AMFSetGrp_pLMNIdList, AMFSetGrp_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-amfset",
    types={AMFSet, AMFSetGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the AMF Set which consists of some AMFs that serve a given area and Network Slice."]
