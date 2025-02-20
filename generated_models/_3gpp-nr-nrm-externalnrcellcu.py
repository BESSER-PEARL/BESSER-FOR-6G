# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
ExternalNRCellCU = Class(name="ExternalNRCellCU")

# ExternalNRCellCU class attributes and methods
ExternalNRCellCU_cellLocalId: Property = Property(name="cellLocalId", type=IntegerType)
ExternalNRCellCU_nRPCI: Property = Property(name="nRPCI", type=IntegerType)
ExternalNRCellCU_nRFrequencyRef: Property = Property(name="nRFrequencyRef", type=StringType)
ExternalNRCellCU_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
ExternalNRCellCU.attributes={ExternalNRCellCU_cellLocalId, ExternalNRCellCU_nRPCI, ExternalNRCellCU_nRFrequencyRef, ExternalNRCellCU_pLMNIdList}

ExternalNRCellCUWrapper = Class(name="ExternalNRCellCUWrapper")

# ExternalNRCellCUWrapper class attributes and methods
ExternalNRCellCUWrapper_ExternalNRCellCU: Property = Property(name="ExternalNRCellCU", type=list)
ExternalNRCellCUWrapper.attributes={ExternalNRCellCUWrapper_ExternalNRCellCU}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-externalnrcellcu",
    types={ExternalNRCellCU, ExternalNRCellCUWrapper},
    associations={},
    generalizations={}
)
