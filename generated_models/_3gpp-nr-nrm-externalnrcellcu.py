# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
ExternalNRCellCU = Class(name="ExternalNRCellCU")

# ExternalNRCellCU class attributes and methods
ExternalNRCellCU_cellLocalId: Property = Property(name="cellLocalId", type=IntegerType)
ExternalNRCellCU_nRPCI: Property = Property(name="nRPCI", type=IntegerType)
ExternalNRCellCU_nRFrequencyRef: Property = Property(name="nRFrequencyRef", type=types3gpp:DistinguishedName)
ExternalNRCellCU_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
ExternalNRCellCU.attributes={ExternalNRCellCU_cellLocalId, ExternalNRCellCU_nRPCI, ExternalNRCellCU_nRFrequencyRef, ExternalNRCellCU_pLMNIdList}

ExternalNRCellCUWrapper = Class(name="ExternalNRCellCUWrapper")

# ExternalNRCellCUWrapper class attributes and methods
ExternalNRCellCUWrapper_ExternalNRCellCU: Property = Property(name="ExternalNRCellCU", type=list)
ExternalNRCellCUWrapper.attributes={ExternalNRCellCUWrapper_ExternalNRCellCU}

