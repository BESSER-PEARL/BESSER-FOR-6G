# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
NRCellDU = Class(name="NRCellDU")

# NRCellDU class attributes and methods
NRCellDU_cellLocalId: Property = Property(name="cellLocalId", type=IntegerType)
NRCellDU_operationalState: Property = Property(name="operationalState", type=types3gpp:OperationalState)
NRCellDU_administrativeState: Property = Property(name="administrativeState", type=types3gpp:AdministrativeState)
NRCellDU_cellState: Property = Property(name="cellState", type=types3gpp:CellState)
NRCellDU_nRPCI: Property = Property(name="nRPCI", type=IntegerType)
NRCellDU_nRTAC: Property = Property(name="nRTAC", type=types3gpp:Tac)
NRCellDU_arfcnDL: Property = Property(name="arfcnDL", type=IntegerType)
NRCellDU_arfcnUL: Property = Property(name="arfcnUL", type=IntegerType)
NRCellDU_arfcnSUL: Property = Property(name="arfcnSUL", type=IntegerType)
NRCellDU_bSChannelBwDL: Property = Property(name="bSChannelBwDL", type=IntegerType)
NRCellDU_bSChannelBwUL: Property = Property(name="bSChannelBwUL", type=IntegerType)
NRCellDU_bSChannelBwSUL: Property = Property(name="bSChannelBwSUL", type=IntegerType)
NRCellDU_ssbFrequency: Property = Property(name="ssbFrequency", type=IntegerType)
NRCellDU_ssbPeriodicity: Property = Property(name="ssbPeriodicity", type=IntegerType)
NRCellDU_ssbSubCarrierSpacing: Property = Property(name="ssbSubCarrierSpacing", type=IntegerType)
NRCellDU_ssbOffset: Property = Property(name="ssbOffset", type=IntegerType)
NRCellDU_ssbDuration: Property = Property(name="ssbDuration", type=IntegerType)
NRCellDU_pLMNInfoList: Property = Property(name="pLMNInfoList", type=list)
NRCellDU.attributes={NRCellDU_cellLocalId, NRCellDU_operationalState, NRCellDU_administrativeState, NRCellDU_cellState, NRCellDU_nRPCI, NRCellDU_nRTAC, NRCellDU_arfcnDL, NRCellDU_arfcnUL, NRCellDU_arfcnSUL, NRCellDU_bSChannelBwDL, NRCellDU_bSChannelBwUL, NRCellDU_bSChannelBwSUL, NRCellDU_ssbFrequency, NRCellDU_ssbPeriodicity, NRCellDU_ssbSubCarrierSpacing, NRCellDU_ssbOffset, NRCellDU_ssbDuration, NRCellDU_pLMNInfoList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-nrcelldu",
    types={NRCellDU},
    associations={},
    generalizations={}
)
