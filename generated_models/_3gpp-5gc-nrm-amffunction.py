# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
AMFFunction = Class(name="AMFFunction")

# AMFFunction class attributes and methods
AMFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=inet:domain-name)
AMFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
AMFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
AMFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
AMFFunction_commModelList: Property = Property(name="commModelList", type=list)
AMFFunction.attributes={AMFFunction_sBIFQDN, AMFFunction_pLMNIdList, AMFFunction_sNSSAIList, AMFFunction_managedNFProfile, AMFFunction_commModelList}

