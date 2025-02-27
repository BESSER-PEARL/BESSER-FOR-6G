# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
NRCellDU = Class(name="NRCellDU", synonyms=["Represents the information of a cell known by DU."])

# NRCellDU class attributes and methods
NRCellDU_administrativeState: Property = Property(name="administrativeState", type=StringType, synonyms=["Administrative state of the NRCellDU. Indicates the permission to use or prohibition against using the cell, imposed through the OAM services."])
NRCellDU_arfcnDL: Property = Property(name="arfcnDL", type=IntegerType, synonyms=["NR Absolute Radio Frequency Channel Number (NR-ARFCN) for downlink."])
NRCellDU_arfcnSUL: Property = Property(name="arfcnSUL", type=IntegerType, synonyms=["NR Absolute Radio Frequency Channel Number (NR-ARFCN) for supplementary uplink."])
NRCellDU_arfcnUL: Property = Property(name="arfcnUL", type=IntegerType, synonyms=["NR Absolute Radio Frequency Channel Number (NR-ARFCN) for uplink."])
NRCellDU_bSChannelBwDL: Property = Property(name="bSChannelBwDL", type=IntegerType, synonyms=["Base station channel bandwidth for downlink."])
NRCellDU_bSChannelBwSUL: Property = Property(name="bSChannelBwSUL", type=IntegerType, synonyms=["Base station channel bandwidth for supplementary uplink."])
NRCellDU_bSChannelBwUL: Property = Property(name="bSChannelBwUL", type=IntegerType, synonyms=["Base station channel bandwidth for uplink."])
NRCellDU_cellLocalId: Property = Property(name="cellLocalId", type=IntegerType, synonyms=["Identifies an NR cell of a gNB. Together with the corresponding gNB identifier in forms the NR Cell Identity (NCI)."])
NRCellDU_cellState: Property = Property(name="cellState", type=StringType, synonyms=["Cell state of the NRCellDU instance. Indicates whether the cell is not currently in use (IDLE), or currently in use but not configured to carry traffic (INACTIVE), or currently in use and is configured to carry traffic (ACTIVE)."])
NRCellDU_nRPCI: Property = Property(name="nRPCI", type=IntegerType, synonyms=["The Physical Cell Identity (PCI) of the NR cell."])
NRCellDU_nRTAC: Property = Property(name="nRTAC", type=StringType, synonyms=["The common 5GS Tracking Area Code for the PLMNs."])
NRCellDU_operationalState: Property = Property(name="operationalState", type=StringType, synonyms=["Operational state of the NRCellDU instance. Indicates whether the resource is installed and partially or fully operable (ENABLED) or the resource is not installed or not operable (DISABLED)."])
NRCellDU_pLMNInfoList: Property = Property(name="pLMNInfoList", type=list, synonyms=["The PLMNInfoList is a list of PLMNInfo data type. It defines which PLMNs that can be served by the NR cell, and which S-NSSAIs that can be supported by the NR cell for corresponding PLMN in case of network slicing feature is supported. The plMNId of the first entry of the list is the PLMNId used to construct the nCGI for the NR cell."])
NRCellDU_ssbDuration: Property = Property(name="ssbDuration", type=IntegerType, synonyms=["Duration of the measurement window in which to receive SS/PBCH blocks."])
NRCellDU_ssbFrequency: Property = Property(name="ssbFrequency", type=IntegerType, synonyms=["Indicates cell defining SSB frequency domain position. Frequency (in terms of NR-ARFCN) of the cell defining SSB transmission. The frequency identifies the position of resource element RE=#0 (subcarrier #0) of resource block RB#10 of the SS block. The frequency must be positioned on the NR global frequency raster, as defined in 3GPP TS 38.101-1, and within bSChannelBwDL."])
NRCellDU_ssbOffset: Property = Property(name="ssbOffset", type=IntegerType, synonyms=["Indicates cell defining SSB time domain position. Defined as the offset of the measurement window, in which to receive SS/PBCH blocks, where allowed values depend on the ssbPeriodicity (ssbOffset < ssbPeriodicity)."])
NRCellDU_ssbPeriodicity: Property = Property(name="ssbPeriodicity", type=IntegerType, synonyms=["Indicates cell defined SSB periodicity. The SSB periodicity is used for the rate matching purpose."])
NRCellDU_ssbSubCarrierSpacing: Property = Property(name="ssbSubCarrierSpacing", type=IntegerType, synonyms=["Subcarrier spacing of SSB. Only the values 15 kHz or 30 kHz (< 6 GHz), 120 kHz or 240 kHz (> 6 GHz) are applicable."])
NRCellDU.attributes={NRCellDU_administrativeState, NRCellDU_arfcnDL, NRCellDU_arfcnSUL, NRCellDU_arfcnUL, NRCellDU_bSChannelBwDL, NRCellDU_bSChannelBwSUL, NRCellDU_bSChannelBwUL, NRCellDU_cellLocalId, NRCellDU_cellState, NRCellDU_nRPCI, NRCellDU_nRTAC, NRCellDU_operationalState, NRCellDU_pLMNInfoList, NRCellDU_ssbDuration, NRCellDU_ssbFrequency, NRCellDU_ssbOffset, NRCellDU_ssbPeriodicity, NRCellDU_ssbSubCarrierSpacing}

NRCellDUGrp = Class(name="NRCellDUGrp", synonyms=["Represents the NRCellDU IOC."])

# NRCellDUGrp class attributes and methods
NRCellDUGrp_administrativeState: Property = Property(name="administrativeState", type=StringType, synonyms=["Administrative state of the NRCellDU. Indicates the permission to use or prohibition against using the cell, imposed through the OAM services."])
NRCellDUGrp_arfcnDL: Property = Property(name="arfcnDL", type=IntegerType, synonyms=["NR Absolute Radio Frequency Channel Number (NR-ARFCN) for downlink."])
NRCellDUGrp_arfcnSUL: Property = Property(name="arfcnSUL", type=IntegerType, synonyms=["NR Absolute Radio Frequency Channel Number (NR-ARFCN) for supplementary uplink."])
NRCellDUGrp_arfcnUL: Property = Property(name="arfcnUL", type=IntegerType, synonyms=["NR Absolute Radio Frequency Channel Number (NR-ARFCN) for uplink."])
NRCellDUGrp_bSChannelBwDL: Property = Property(name="bSChannelBwDL", type=IntegerType, synonyms=["Base station channel bandwidth for downlink."])
NRCellDUGrp_bSChannelBwSUL: Property = Property(name="bSChannelBwSUL", type=IntegerType, synonyms=["Base station channel bandwidth for supplementary uplink."])
NRCellDUGrp_bSChannelBwUL: Property = Property(name="bSChannelBwUL", type=IntegerType, synonyms=["Base station channel bandwidth for uplink."])
NRCellDUGrp_cellLocalId: Property = Property(name="cellLocalId", type=IntegerType, synonyms=["Identifies an NR cell of a gNB. Together with the corresponding gNB identifier in forms the NR Cell Identity (NCI)."])
NRCellDUGrp_cellState: Property = Property(name="cellState", type=StringType, synonyms=["Cell state of the NRCellDU instance. Indicates whether the cell is not currently in use (IDLE), or currently in use but not configured to carry traffic (INACTIVE), or currently in use and is configured to carry traffic (ACTIVE)."])
NRCellDUGrp_nRPCI: Property = Property(name="nRPCI", type=IntegerType, synonyms=["The Physical Cell Identity (PCI) of the NR cell."])
NRCellDUGrp_nRTAC: Property = Property(name="nRTAC", type=StringType, synonyms=["The common 5GS Tracking Area Code for the PLMNs."])
NRCellDUGrp_operationalState: Property = Property(name="operationalState", type=StringType, synonyms=["Operational state of the NRCellDU instance. Indicates whether the resource is installed and partially or fully operable (ENABLED) or the resource is not installed or not operable (DISABLED)."])
NRCellDUGrp_pLMNInfoList: Property = Property(name="pLMNInfoList", type=list, synonyms=["The PLMNInfoList is a list of PLMNInfo data type. It defines which PLMNs that can be served by the NR cell, and which S-NSSAIs that can be supported by the NR cell for corresponding PLMN in case of network slicing feature is supported. The plMNId of the first entry of the list is the PLMNId used to construct the nCGI for the NR cell."])
NRCellDUGrp_ssbDuration: Property = Property(name="ssbDuration", type=IntegerType, synonyms=["Duration of the measurement window in which to receive SS/PBCH blocks."])
NRCellDUGrp_ssbFrequency: Property = Property(name="ssbFrequency", type=IntegerType, synonyms=["Indicates cell defining SSB frequency domain position. Frequency (in terms of NR-ARFCN) of the cell defining SSB transmission. The frequency identifies the position of resource element RE=#0 (subcarrier #0) of resource block RB#10 of the SS block. The frequency must be positioned on the NR global frequency raster, as defined in 3GPP TS 38.101-1, and within bSChannelBwDL."])
NRCellDUGrp_ssbOffset: Property = Property(name="ssbOffset", type=IntegerType, synonyms=["Indicates cell defining SSB time domain position. Defined as the offset of the measurement window, in which to receive SS/PBCH blocks, where allowed values depend on the ssbPeriodicity (ssbOffset < ssbPeriodicity)."])
NRCellDUGrp_ssbPeriodicity: Property = Property(name="ssbPeriodicity", type=IntegerType, synonyms=["Indicates cell defined SSB periodicity. The SSB periodicity is used for the rate matching purpose."])
NRCellDUGrp_ssbSubCarrierSpacing: Property = Property(name="ssbSubCarrierSpacing", type=IntegerType, synonyms=["Subcarrier spacing of SSB. Only the values 15 kHz or 30 kHz (< 6 GHz), 120 kHz or 240 kHz (> 6 GHz) are applicable."])
NRCellDUGrp.attributes={NRCellDUGrp_administrativeState, NRCellDUGrp_arfcnDL, NRCellDUGrp_arfcnSUL, NRCellDUGrp_arfcnUL, NRCellDUGrp_bSChannelBwDL, NRCellDUGrp_bSChannelBwSUL, NRCellDUGrp_bSChannelBwUL, NRCellDUGrp_cellLocalId, NRCellDUGrp_cellState, NRCellDUGrp_nRPCI, NRCellDUGrp_nRTAC, NRCellDUGrp_operationalState, NRCellDUGrp_pLMNInfoList, NRCellDUGrp_ssbDuration, NRCellDUGrp_ssbFrequency, NRCellDUGrp_ssbOffset, NRCellDUGrp_ssbPeriodicity, NRCellDUGrp_ssbSubCarrierSpacing}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-nrcelldu",
    types={NRCellDU, NRCellDUGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the NRCellDU Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
