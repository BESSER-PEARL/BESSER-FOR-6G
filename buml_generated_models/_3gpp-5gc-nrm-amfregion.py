# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models._3gpp_common_yang_types import domain_model as types3gpp_model
from buml_generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model

# Classes
AMFRegion = Class(name="AMFRegion", synonyms=["5G Core AMFRegion IOC"])

# AMFRegion class attributes and methods
AMFRegion_aMFRegionId: Property = Property(name="aMFRegionId", type=types3gpp_model.get_type_by_name('AmfRegionId'), synonyms=["Represents the AMF Region ID, which identifies the region."])
AMFRegion_pLMNIdList: Property = Property(name="pLMNIdList", type=types3gpp_model.get_type_by_name('PLMNId'), multiplicity=Multiplicity(1, "*"), synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
AMFRegion_sNSSAIList: Property = Property(name="sNSSAIList", type=types5g3gpp_model.get_type_by_name('SNssai'), multiplicity=Multiplicity(0, "*"), synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
AMFRegion.attributes={AMFRegion_aMFRegionId, AMFRegion_pLMNIdList, AMFRegion_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-amfregion",
    types={AMFRegion},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the AMF Region which consists one or multiple AMF Sets."]
