# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models._3gpp_common_yang_types import domain_model as types3gpp_model
from buml_generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model

# Classes
AMFSet = Class(name="AMFSet", synonyms=["Represents the AMFSet IOC"])

# AMFSet class attributes and methods
AMFSet_AMFSet: Property = Property(name="AMFSet", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["5G Core AMFSet IOC"])
AMFSet_aMFRegion: Property = Property(name="aMFRegion", type=StringType, synonyms=["The AMFRegion that the AFMSet is associated with."])
AMFSet_pLMNIdList: Property = Property(name="pLMNIdList", type=DataType('PLMNId'), multiplicity=Multiplicity(1, "*"), synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
AMFSet_sNSSAIList: Property = Property(name="sNSSAIList", type=DataType('SNssai'), multiplicity=Multiplicity(0, "*"), synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
AMFSet.attributes={AMFSet_AMFSet, AMFSet_aMFRegion, AMFSet_pLMNIdList, AMFSet_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-amfset",
    types={AMFSet},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the AMF Set which consists of some AMFs that serve a given area and Network Slice."]
