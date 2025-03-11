# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model

# Enumerations
QfqosmonitoringstateEnum = Enumeration(name="QfqosmonitoringstateEnum")
QfqosmonitoringstateEnum_DISABLED = EnumerationLiteral(name="DISABLED", owner=QfqosmonitoringstateEnum)
QfqosmonitoringstateEnum_ENABLED = EnumerationLiteral(name="ENABLED", owner=QfqosmonitoringstateEnum)
QfqosmonitoringstateEnum.literals = {QfqosmonitoringstateEnum_DISABLED, QfqosmonitoringstateEnum_ENABLED}
QfqosmonitoringstateEnum.synonyms = ["The state of QoS monitoring per QoS flow per UE."]

# Classes
QFPacketDelayThresholdsType = Class(name="QFPacketDelayThresholdsType", synonyms=["Represents the QFPacketDelayThresholdsType"])

# QFPacketDelayThresholdsType class attributes and methods
QFPacketDelayThresholdsType_thresholdDl: Property = Property(name="thresholdDl", type=IntegerType, synonyms=["Downlink threshold"])
QFPacketDelayThresholdsType_thresholdRtt: Property = Property(name="thresholdRtt", type=IntegerType, synonyms=["Round trip threshold"])
QFPacketDelayThresholdsType_thresholdUl: Property = Property(name="thresholdUl", type=IntegerType, synonyms=["Uplink threshold"])
QFPacketDelayThresholdsType.attributes={QFPacketDelayThresholdsType_thresholdDl, QFPacketDelayThresholdsType_thresholdRtt, QFPacketDelayThresholdsType_thresholdUl}

QFQoSMonitoringControl = Class(name="QFQoSMonitoringControl", synonyms=["Represents the QFQoSMonitoringControl IOC."])

# QFQoSMonitoringControl class attributes and methods
QFQoSMonitoringControl_isEventTriggeredQFMonitoringSupported: Property = Property(name="isEventTriggeredQFMonitoringSupported", type=BooleanType, synonyms=["It indicates whether the event based QoS monitoring reporting per QoS flow per UE is supported."])
QFQoSMonitoringControl_isPeriodicQFMonitoringSupported: Property = Property(name="isPeriodicQFMonitoringSupported", type=BooleanType, synonyms=["It indicates whether the periodic QoS monitoring reporting per QoS flow per UE is supported."])
QFQoSMonitoringControl_isSessionReleasedQFMonitoringSupported: Property = Property(name="isSessionReleasedQFMonitoringSupported", type=BooleanType, synonyms=["It indicates whether the session release based QoS monitoring reporting per QoS flow per UE is supported."])
QFQoSMonitoringControl_qFMeasurementPeriod: Property = Property(name="qFMeasurementPeriod", type=IntegerType, synonyms=["It specifies the period (in seconds) for reporting the packet delay for QoS monitoring per QoS flow per UE."])
QFQoSMonitoringControl_qFMinimumWaitTime: Property = Property(name="qFMinimumWaitTime", type=IntegerType, synonyms=["It specifies the minimum waiting time (in seconds) between two consecutive reports for event triggered QoS monitoring reporting per QoS flow per UE."])
QFQoSMonitoringControl_qFMonitoredSNSSAIs: Property = Property(name="qFMonitoredSNSSAIs", type=types5g3gpp_model.get_type_by_name('SNssai'), multiplicity=Multiplicity(0, "*"), synonyms=["The S-NSSAIs for which the QoS monitoring per QoS flow per UE is to be performed."])
QFQoSMonitoringControl_qFPacketDelayThresholds: Property = Property(name="qFPacketDelayThresholds", type=list, multiplicity=Multiplicity(1, "*"), synonyms=["It specifies the thresholds for reporting the packet delay between PSA and UE for QoS monitoring per QoS flow per UE."])
QFQoSMonitoringControl_qFQoSMonitoringState: Property = Property(name="qFQoSMonitoringState", type=QfqosmonitoringstateEnum, synonyms=["The state of QoS monitoring per QoS flow per UE."])
QFQoSMonitoringControl.attributes={QFQoSMonitoringControl_isEventTriggeredQFMonitoringSupported, QFQoSMonitoringControl_isPeriodicQFMonitoringSupported, QFQoSMonitoringControl_isSessionReleasedQFMonitoringSupported, QFQoSMonitoringControl_qFMeasurementPeriod, QFQoSMonitoringControl_qFMinimumWaitTime, QFQoSMonitoringControl_qFMonitoredSNSSAIs, QFQoSMonitoringControl_qFPacketDelayThresholds, QFQoSMonitoringControl_qFQoSMonitoringState}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-QFQoSMonitoringControl",
    types={QFPacketDelayThresholdsType, QFQoSMonitoringControl, QfqosmonitoringstateEnum},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the capabilities and properties for control of QoS monitoring per QoS flow per UE for URLLC service defined in 3GPP TS 23.501."]
