# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
NRSectorCarrier = Class(name="NRSectorCarrier", synonyms=["Represents the NRSectorCarrier IOC."])

# NRSectorCarrier class attributes and methods
NRSectorCarrier_NRSectorCarrier: Property = Property(name="NRSectorCarrier", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["Represents the resources of each transmission point included in the cell."])
NRSectorCarrier_arfcnDL: Property = Property(name="arfcnDL", type=IntegerType, synonyms=["NR Absolute Radio Frequency Channel Number (NR-ARFCN) for downlink. Condition: The sector-carrier has a downlink AND the value differs from the referring cell's value of arfcnDL."])
NRSectorCarrier_arfcnUL: Property = Property(name="arfcnUL", type=IntegerType, synonyms=["NR Absolute Radio Frequency Channel Number (NR-ARFCN) for uplink. Condition: The sector-carrier has an uplink AND the value differs from the referring cell's value of arfcnUL."])
NRSectorCarrier_bSChannelBwDL: Property = Property(name="bSChannelBwDL", type=IntegerType, synonyms=["Base station channel bandwitdth for downlink. Condition: The sector-carrier has a downlink AND the value differs from the referring cell's value of bSChannelBwDL."])
NRSectorCarrier_bSChannelBwUL: Property = Property(name="bSChannelBwUL", type=IntegerType, synonyms=["Base station channel bandwitdth for uplink."])
NRSectorCarrier_configuredMaxTxEIRP: Property = Property(name="configuredMaxTxEIRP", type=IntegerType, synonyms=["The maximum emitted isotroptic radiated power (EIRP) in dBm for all downlink channels, used simultaneously in a cell, added together. Condition: the sector-carrier has a downlink and the configuration of emitted isotropic radiated power is supported"])
NRSectorCarrier_configuredMaxTxPower: Property = Property(name="configuredMaxTxPower", type=IntegerType, synonyms=["Maximum transmisssion power at the antenna port for all downlink channels, used simultaneously in a cell, added together. Condition: The sector-carrier has a downlink and the configuration of Tx power at antenna port reference point is supported."])
NRSectorCarrier_sectorEquipmentFunctionRef: Property = Property(name="sectorEquipmentFunctionRef", type=DataType('DistinguishedName'), synonyms=["Reference to corresponding SectorEquipmentFunction instance."])
NRSectorCarrier_txDirection: Property = Property(name="txDirection", type=TxDirection, synonyms=["Indicates if the transmission direction is downlink, uplink, or both downlink and uplink."])
NRSectorCarrier.attributes={NRSectorCarrier_NRSectorCarrier, NRSectorCarrier_arfcnDL, NRSectorCarrier_arfcnUL, NRSectorCarrier_bSChannelBwDL, NRSectorCarrier_bSChannelBwUL, NRSectorCarrier_configuredMaxTxEIRP, NRSectorCarrier_configuredMaxTxPower, NRSectorCarrier_sectorEquipmentFunctionRef, NRSectorCarrier_txDirection}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-nrsectorcarrier",
    types={NRSectorCarrier},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the NRSectorCarrier Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
