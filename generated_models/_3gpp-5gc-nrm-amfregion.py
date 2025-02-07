# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
AMFRegion = Class(name="AMFRegion")

# AMFRegion class attributes and methods
AMFRegion_aMFRegionId: Property = Property(name="aMFRegionId", type=types3gpp:AmfRegionId)
AMFRegion_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
AMFRegion_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
AMFRegion.attributes={AMFRegion_aMFRegionId, AMFRegion_pLMNIdList, AMFRegion_sNSSAIList}

