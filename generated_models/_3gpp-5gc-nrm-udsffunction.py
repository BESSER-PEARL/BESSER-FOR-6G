# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
UDSFFuntion = Class(name="UDSFFuntion")

# UDSFFuntion class attributes and methods
UDSFFuntion_sBIFQDN: Property = Property(name="sBIFQDN", type=inet:domain-name)
UDSFFuntion_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
UDSFFuntion_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
UDSFFuntion_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
UDSFFuntion.attributes={UDSFFuntion_sBIFQDN, UDSFFuntion_pLMNIdList, UDSFFuntion_sNSSAIList, UDSFFuntion_managedNFProfile}

