# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
AUSFFuntion = Class(name="AUSFFuntion")

# AUSFFuntion class attributes and methods
AUSFFuntion_sBIFQDN: Property = Property(name="sBIFQDN", type=inet:domain-name)
AUSFFuntion_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
AUSFFuntion_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
AUSFFuntion_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
AUSFFuntion_commModelList: Property = Property(name="commModelList", type=list)
AUSFFuntion.attributes={AUSFFuntion_sBIFQDN, AUSFFuntion_pLMNIdList, AUSFFuntion_sNSSAIList, AUSFFuntion_managedNFProfile, AUSFFuntion_commModelList}

