# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
SMFFunction = Class(name="SMFFunction")

# SMFFunction class attributes and methods
SMFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=inet:domain-name)
SMFFunction_configurable5QISetRef: Property = Property(name="configurable5QISetRef", type=types3gpp:DistinguishedName)
SMFFunction_dynamic5QISetRef: Property = Property(name="dynamic5QISetRef", type=types3gpp:DistinguishedName)
SMFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
SMFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
SMFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
SMFFunction_commModelList: Property = Property(name="commModelList", type=list)
SMFFunction.attributes={SMFFunction_sBIFQDN, SMFFunction_configurable5QISetRef, SMFFunction_dynamic5QISetRef, SMFFunction_pLMNIdList, SMFFunction_sNSSAIList, SMFFunction_managedNFProfile, SMFFunction_commModelList}

