# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
PCFFuntion = Class(name="PCFFuntion")

# PCFFuntion class attributes and methods
PCFFuntion_commModelList: Property = Property(name="commModelList", type=list)
PCFFuntion_sBIFQDN: Property = Property(name="sBIFQDN", type=inet:domain-name)
PCFFuntion_dynamic5QISetRef: Property = Property(name="dynamic5QISetRef", type=types3gpp:DistinguishedName)
PCFFuntion_configurable5QISetRef: Property = Property(name="configurable5QISetRef", type=types3gpp:DistinguishedName)
PCFFuntion_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
PCFFuntion_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
PCFFuntion_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
PCFFuntion.attributes={PCFFuntion_commModelList, PCFFuntion_sBIFQDN, PCFFuntion_dynamic5QISetRef, PCFFuntion_configurable5QISetRef, PCFFuntion_pLMNIdList, PCFFuntion_sNSSAIList, PCFFuntion_managedNFProfile}

