# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
NRCellDU = Class(name="NRCellDU")

# NRCellDU class attributes and methods
NRCellDU_administrativeState: Property = Property(name="administrativeState", type=StringType)
NRCellDU_arfcnDL: Property = Property(name="arfcnDL", type=IntegerType)
NRCellDU_arfcnSUL: Property = Property(name="arfcnSUL", type=IntegerType)
NRCellDU_arfcnUL: Property = Property(name="arfcnUL", type=IntegerType)
NRCellDU_bSChannelBwDL: Property = Property(name="bSChannelBwDL", type=IntegerType)
NRCellDU_bSChannelBwSUL: Property = Property(name="bSChannelBwSUL", type=IntegerType)
NRCellDU_bSChannelBwUL: Property = Property(name="bSChannelBwUL", type=IntegerType)
NRCellDU_cellLocalId: Property = Property(name="cellLocalId", type=IntegerType)
NRCellDU_cellState: Property = Property(name="cellState", type=StringType)
NRCellDU_nRPCI: Property = Property(name="nRPCI", type=IntegerType)
NRCellDU_nRTAC: Property = Property(name="nRTAC", type=StringType)
NRCellDU_operationalState: Property = Property(name="operationalState", type=StringType)
NRCellDU_pLMNInfoList: Property = Property(name="pLMNInfoList", type=list)
NRCellDU_ssbDuration: Property = Property(name="ssbDuration", type=IntegerType)
NRCellDU_ssbFrequency: Property = Property(name="ssbFrequency", type=IntegerType)
NRCellDU_ssbOffset: Property = Property(name="ssbOffset", type=IntegerType)
NRCellDU_ssbPeriodicity: Property = Property(name="ssbPeriodicity", type=IntegerType)
NRCellDU_ssbSubCarrierSpacing: Property = Property(name="ssbSubCarrierSpacing", type=IntegerType)
NRCellDU.attributes={NRCellDU_administrativeState, NRCellDU_arfcnDL, NRCellDU_arfcnSUL, NRCellDU_arfcnUL, NRCellDU_bSChannelBwDL, NRCellDU_bSChannelBwSUL, NRCellDU_bSChannelBwUL, NRCellDU_cellLocalId, NRCellDU_cellState, NRCellDU_nRPCI, NRCellDU_nRTAC, NRCellDU_operationalState, NRCellDU_pLMNInfoList, NRCellDU_ssbDuration, NRCellDU_ssbFrequency, NRCellDU_ssbOffset, NRCellDU_ssbPeriodicity, NRCellDU_ssbSubCarrierSpacing}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-nrcelldu",
    types={NRCellDU},
    associations={},
    generalizations={}
)
