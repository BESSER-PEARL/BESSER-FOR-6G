# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
NRSectorCarrier = Class(name="NRSectorCarrier")

# NRSectorCarrier class attributes and methods
NRSectorCarrier_txDirection: Property = Property(name="txDirection", type=types3gpp:TxDirection)
NRSectorCarrier_configuredMaxTxPower: Property = Property(name="configuredMaxTxPower", type=IntegerType)
NRSectorCarrier_configuredMaxTxEIRP: Property = Property(name="configuredMaxTxEIRP", type=IntegerType)
NRSectorCarrier_arfcnDL: Property = Property(name="arfcnDL", type=IntegerType)
NRSectorCarrier_arfcnUL: Property = Property(name="arfcnUL", type=IntegerType)
NRSectorCarrier_bSChannelBwDL: Property = Property(name="bSChannelBwDL", type=IntegerType)
NRSectorCarrier_bSChannelBwUL: Property = Property(name="bSChannelBwUL", type=IntegerType)
NRSectorCarrier_sectorEquipmentFunctionRef: Property = Property(name="sectorEquipmentFunctionRef", type=types3gpp:DistinguishedName)
NRSectorCarrier.attributes={NRSectorCarrier_txDirection, NRSectorCarrier_configuredMaxTxPower, NRSectorCarrier_configuredMaxTxEIRP, NRSectorCarrier_arfcnDL, NRSectorCarrier_arfcnUL, NRSectorCarrier_bSChannelBwDL, NRSectorCarrier_bSChannelBwUL, NRSectorCarrier_sectorEquipmentFunctionRef}

