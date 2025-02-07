# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
NEFFunction = Class(name="NEFFunction")

# NEFFunction class attributes and methods
NEFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=inet:domain-name)
NEFFunction_isINEF: Property = Property(name="isINEF", type=BooleanType)
NEFFunction_isCAPIFSup: Property = Property(name="isCAPIFSup", type=BooleanType)
NEFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
NEFFunction.attributes={NEFFunction_sBIFQDN, NEFFunction_isINEF, NEFFunction_isCAPIFSup, NEFFunction_sNSSAIList}

