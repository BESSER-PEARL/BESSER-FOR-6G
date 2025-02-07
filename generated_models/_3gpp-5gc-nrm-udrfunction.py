# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
UDRFuntion = Class(name="UDRFuntion")

# UDRFuntion class attributes and methods
UDRFuntion_sBIFQDN: Property = Property(name="sBIFQDN", type=inet:domain-name)
UDRFuntion_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
UDRFuntion_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
UDRFuntion_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
UDRFuntion.attributes={UDRFuntion_sBIFQDN, UDRFuntion_pLMNIdList, UDRFuntion_sNSSAIList, UDRFuntion_managedNFProfile}

