# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
NWDAFFunction = Class(name="NWDAFFunction")

# NWDAFFunction class attributes and methods
NWDAFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=inet:domain-name)
NWDAFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
NWDAFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
NWDAFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
NWDAFFunction_commModelList: Property = Property(name="commModelList", type=list)
NWDAFFunction.attributes={NWDAFFunction_sBIFQDN, NWDAFFunction_pLMNIdList, NWDAFFunction_sNSSAIList, NWDAFFunction_managedNFProfile, NWDAFFunction_commModelList}

