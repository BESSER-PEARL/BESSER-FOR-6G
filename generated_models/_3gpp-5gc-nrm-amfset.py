# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
AMFSet = Class(name="AMFSet")

# AMFSet class attributes and methods
AMFSet_aMFRegion: Property = Property(name="aMFRegion", type=instance-identifier)
AMFSet_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
AMFSet_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
AMFSet.attributes={AMFSet_aMFRegion, AMFSet_pLMNIdList, AMFSet_sNSSAIList}

