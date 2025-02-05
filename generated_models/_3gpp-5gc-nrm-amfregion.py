# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    Constraint
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_managed_element import domain_model as me3gpp_model
from generated_models._3gpp_common_managed_function import domain_model as mf3gpp_model
from generated_models._3gpp_common_subnetwork import domain_model as subnet3gpp_model
from generated_models._3gpp_common_top import domain_model as top3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Enumerations
# Classes
AMFRegionGrp = Class(name="AMFRegionGrp")
AMFRegion = Class(name="AMFRegion")

# AMFRegionGrp class attributes and methods
AMFRegionGrp_aMFRegionId: Property = Property(name="aMFRegionId", type=types3gpp:AmfRegionId)
AMFRegionGrp_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
AMFRegionGrp_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
AMFRegionGrp.attributes={AMFRegionGrp_aMFRegionId, AMFRegionGrp_sNSSAIList, AMFRegionGrp_pLMNIdList}

# AMFRegion class attributes and methods
AMFRegion_aMFRegionId: Property = Property(name="aMFRegionId", type=types3gpp:AmfRegionId)
AMFRegion_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
AMFRegion_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
AMFRegion.attributes={AMFRegion_aMFRegionId, AMFRegion_sNSSAIList, AMFRegion_pLMNIdList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-amfregion",
    types={AMFRegionGrp, AMFRegion, types3gpp_model, mf3gpp_model, me3gpp_model, top3gpp_model, types5g3gpp_model, inet_model, subnet3gpp_model},
    associations={},
    generalizations={}
)
