# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
UDMFuntion = Class(name="UDMFuntion")

# UDMFuntion class attributes and methods
UDMFuntion_sBIFQDN: Property = Property(name="sBIFQDN", type=inet:domain-name)
UDMFuntion_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
UDMFuntion_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
UDMFuntion_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
UDMFuntion_commModelList: Property = Property(name="commModelList", type=list)
UDMFuntion.attributes={UDMFuntion_sBIFQDN, UDMFuntion_pLMNIdList, UDMFuntion_sNSSAIList, UDMFuntion_managedNFProfile, UDMFuntion_commModelList}

