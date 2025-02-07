# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
NRFFunction = Class(name="NRFFunction")

# NRFFunction class attributes and methods
NRFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=inet:domain-name)
NRFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
NRFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
NRFFunction_nFProfileList: Property = Property(name="nFProfileList", type=list)
NRFFunction.attributes={NRFFunction_sBIFQDN, NRFFunction_pLMNIdList, NRFFunction_sNSSAIList, NRFFunction_nFProfileList}

