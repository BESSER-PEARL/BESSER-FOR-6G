# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
NRCellCU = Class(name="NRCellCU")

# NRCellCU class attributes and methods
NRCellCU_cellLocalId: Property = Property(name="cellLocalId", type=IntegerType)
NRCellCU_nRFrequencyRef: Property = Property(name="nRFrequencyRef", type=types3gpp:DistinguishedName)
NRCellCU_pLMNInfoList: Property = Property(name="pLMNInfoList", type=list)
NRCellCU.attributes={NRCellCU_cellLocalId, NRCellCU_nRFrequencyRef, NRCellCU_pLMNInfoList}

