# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
NRSectorCarrier = Class(name="NRSectorCarrier")

# NRSectorCarrier class attributes and methods
NRSectorCarrier_arfcnDL: Property = Property(name="arfcnDL", type=IntegerType)
NRSectorCarrier_arfcnUL: Property = Property(name="arfcnUL", type=IntegerType)
NRSectorCarrier_bSChannelBwDL: Property = Property(name="bSChannelBwDL", type=IntegerType)
NRSectorCarrier_bSChannelBwUL: Property = Property(name="bSChannelBwUL", type=IntegerType)
NRSectorCarrier_configuredMaxTxEIRP: Property = Property(name="configuredMaxTxEIRP", type=IntegerType)
NRSectorCarrier_configuredMaxTxPower: Property = Property(name="configuredMaxTxPower", type=IntegerType)
NRSectorCarrier_sectorEquipmentFunctionRef: Property = Property(name="sectorEquipmentFunctionRef", type=StringType)
NRSectorCarrier_txDirection: Property = Property(name="txDirection", type=StringType)
NRSectorCarrier.attributes={NRSectorCarrier_arfcnDL, NRSectorCarrier_arfcnUL, NRSectorCarrier_bSChannelBwDL, NRSectorCarrier_bSChannelBwUL, NRSectorCarrier_configuredMaxTxEIRP, NRSectorCarrier_configuredMaxTxPower, NRSectorCarrier_sectorEquipmentFunctionRef, NRSectorCarrier_txDirection}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-nrsectorcarrier",
    types={NRSectorCarrier},
    associations={},
    generalizations={}
)
