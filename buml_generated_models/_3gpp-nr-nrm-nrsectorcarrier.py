# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
NRSectorCarrier = Class(name="NRSectorCarrier", synonyms=["Represents the resources of each transmission point included in the cell."])

# NRSectorCarrier class attributes and methods
NRSectorCarrier_arfcnDL: Property = Property(name="arfcnDL", type=IntegerType, synonyms=["NR Absolute Radio Frequency Channel Number (NR-ARFCN) for downlink. Condition: The sector-carrier has a downlink AND the value differs from the referring cell's value of arfcnDL."])
NRSectorCarrier_arfcnUL: Property = Property(name="arfcnUL", type=IntegerType, synonyms=["NR Absolute Radio Frequency Channel Number (NR-ARFCN) for uplink. Condition: The sector-carrier has an uplink AND the value differs from the referring cell's value of arfcnUL."])
NRSectorCarrier_bSChannelBwDL: Property = Property(name="bSChannelBwDL", type=IntegerType, synonyms=["Base station channel bandwitdth for downlink. Condition: The sector-carrier has a downlink AND the value differs from the referring cell's value of bSChannelBwDL."])
NRSectorCarrier_bSChannelBwUL: Property = Property(name="bSChannelBwUL", type=IntegerType, synonyms=["Base station channel bandwitdth for uplink."])
NRSectorCarrier_configuredMaxTxEIRP: Property = Property(name="configuredMaxTxEIRP", type=IntegerType, synonyms=["The maximum emitted isotroptic radiated power (EIRP) in dBm for all downlink channels, used simultaneously in a cell, added together. Condition: the sector-carrier has a downlink and the configuration of emitted isotropic radiated power is supported"])
NRSectorCarrier_configuredMaxTxPower: Property = Property(name="configuredMaxTxPower", type=IntegerType, synonyms=["Maximum transmisssion power at the antenna port for all downlink channels, used simultaneously in a cell, added together. Condition: The sector-carrier has a downlink and the configuration of Tx power at antenna port reference point is supported."])
NRSectorCarrier_sectorEquipmentFunctionRef: Property = Property(name="sectorEquipmentFunctionRef", type=StringType, synonyms=["Reference to corresponding SectorEquipmentFunction instance."])
NRSectorCarrier_txDirection: Property = Property(name="txDirection", type=StringType, synonyms=["Indicates if the transmission direction is downlink, uplink, or both downlink and uplink."])
NRSectorCarrier.attributes={NRSectorCarrier_arfcnDL, NRSectorCarrier_arfcnUL, NRSectorCarrier_bSChannelBwDL, NRSectorCarrier_bSChannelBwUL, NRSectorCarrier_configuredMaxTxEIRP, NRSectorCarrier_configuredMaxTxPower, NRSectorCarrier_sectorEquipmentFunctionRef, NRSectorCarrier_txDirection}

NRSectorCarrierGrp = Class(name="NRSectorCarrierGrp", synonyms=["Represents the NRSectorCarrier IOC."])

# NRSectorCarrierGrp class attributes and methods
NRSectorCarrierGrp_arfcnDL: Property = Property(name="arfcnDL", type=IntegerType, synonyms=["NR Absolute Radio Frequency Channel Number (NR-ARFCN) for downlink. Condition: The sector-carrier has a downlink AND the value differs from the referring cell's value of arfcnDL."])
NRSectorCarrierGrp_arfcnUL: Property = Property(name="arfcnUL", type=IntegerType, synonyms=["NR Absolute Radio Frequency Channel Number (NR-ARFCN) for uplink. Condition: The sector-carrier has an uplink AND the value differs from the referring cell's value of arfcnUL."])
NRSectorCarrierGrp_bSChannelBwDL: Property = Property(name="bSChannelBwDL", type=IntegerType, synonyms=["Base station channel bandwitdth for downlink. Condition: The sector-carrier has a downlink AND the value differs from the referring cell's value of bSChannelBwDL."])
NRSectorCarrierGrp_bSChannelBwUL: Property = Property(name="bSChannelBwUL", type=IntegerType, synonyms=["Base station channel bandwitdth for uplink."])
NRSectorCarrierGrp_configuredMaxTxEIRP: Property = Property(name="configuredMaxTxEIRP", type=IntegerType, synonyms=["The maximum emitted isotroptic radiated power (EIRP) in dBm for all downlink channels, used simultaneously in a cell, added together. Condition: the sector-carrier has a downlink and the configuration of emitted isotropic radiated power is supported"])
NRSectorCarrierGrp_configuredMaxTxPower: Property = Property(name="configuredMaxTxPower", type=IntegerType, synonyms=["Maximum transmisssion power at the antenna port for all downlink channels, used simultaneously in a cell, added together. Condition: The sector-carrier has a downlink and the configuration of Tx power at antenna port reference point is supported."])
NRSectorCarrierGrp_sectorEquipmentFunctionRef: Property = Property(name="sectorEquipmentFunctionRef", type=StringType, synonyms=["Reference to corresponding SectorEquipmentFunction instance."])
NRSectorCarrierGrp_txDirection: Property = Property(name="txDirection", type=StringType, synonyms=["Indicates if the transmission direction is downlink, uplink, or both downlink and uplink."])
NRSectorCarrierGrp.attributes={NRSectorCarrierGrp_arfcnDL, NRSectorCarrierGrp_arfcnUL, NRSectorCarrierGrp_bSChannelBwDL, NRSectorCarrierGrp_bSChannelBwUL, NRSectorCarrierGrp_configuredMaxTxEIRP, NRSectorCarrierGrp_configuredMaxTxPower, NRSectorCarrierGrp_sectorEquipmentFunctionRef, NRSectorCarrierGrp_txDirection}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-nrsectorcarrier",
    types={NRSectorCarrier, NRSectorCarrierGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the NRSectorCarrier Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
