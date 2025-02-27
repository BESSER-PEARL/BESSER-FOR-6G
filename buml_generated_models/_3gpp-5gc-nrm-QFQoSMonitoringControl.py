# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
QFPacketDelayThresholdsTypeGrp = Class(name="QFPacketDelayThresholdsTypeGrp", synonyms=["Represents the QFPacketDelayThresholdsType"])

# QFPacketDelayThresholdsTypeGrp class attributes and methods
QFPacketDelayThresholdsTypeGrp_thresholdDl: Property = Property(name="thresholdDl", type=IntegerType, synonyms=["Downlink threshold"])
QFPacketDelayThresholdsTypeGrp_thresholdRtt: Property = Property(name="thresholdRtt", type=IntegerType, synonyms=["Round trip threshold"])
QFPacketDelayThresholdsTypeGrp_thresholdUl: Property = Property(name="thresholdUl", type=IntegerType, synonyms=["Uplink threshold"])
QFPacketDelayThresholdsTypeGrp.attributes={QFPacketDelayThresholdsTypeGrp_thresholdDl, QFPacketDelayThresholdsTypeGrp_thresholdRtt, QFPacketDelayThresholdsTypeGrp_thresholdUl}

QFQoSMonitoringControl = Class(name="QFQoSMonitoringControl", synonyms=["Represents the QFQoSMonitoringControl IOC."])

# QFQoSMonitoringControl class attributes and methods
QFQoSMonitoringControl_isEventTriggeredQFMonitoringSupported: Property = Property(name="isEventTriggeredQFMonitoringSupported", type=BooleanType, synonyms=["It indicates whether the event based QoS monitoring reporting per QoS flow per UE is supported."])
QFQoSMonitoringControl_isPeriodicQFMonitoringSupported: Property = Property(name="isPeriodicQFMonitoringSupported", type=BooleanType, synonyms=["It indicates whether the periodic QoS monitoring reporting per QoS flow per UE is supported."])
QFQoSMonitoringControl_isSessionReleasedQFMonitoringSupported: Property = Property(name="isSessionReleasedQFMonitoringSupported", type=BooleanType, synonyms=["It indicates whether the session release based QoS monitoring reporting per QoS flow per UE is supported."])
QFQoSMonitoringControl_qFMeasurementPeriod: Property = Property(name="qFMeasurementPeriod", type=IntegerType, synonyms=["It specifies the period (in seconds) for reporting the packet delay for QoS monitoring per QoS flow per UE."])
QFQoSMonitoringControl_qFMinimumWaitTime: Property = Property(name="qFMinimumWaitTime", type=IntegerType, synonyms=["It specifies the minimum waiting time (in seconds) between two consecutive reports for event triggered QoS monitoring reporting per QoS flow per UE."])
QFQoSMonitoringControl_qFMonitoredSNSSAIs: Property = Property(name="qFMonitoredSNSSAIs", type=list, synonyms=["The S-NSSAIs for which the QoS monitoring per QoS flow per UE is to be performed."])
QFQoSMonitoringControl_qFPacketDelayThresholds: Property = Property(name="qFPacketDelayThresholds", type=list, synonyms=["It specifies the thresholds for reporting the packet delay between PSA and UE for QoS monitoring per QoS flow per UE."])
QFQoSMonitoringControl_qFQoSMonitoringState: Property = Property(name="qFQoSMonitoringState", type=EnumerationType, synonyms=["The state of QoS monitoring per QoS flow per UE."])
QFQoSMonitoringControl.attributes={QFQoSMonitoringControl_isEventTriggeredQFMonitoringSupported, QFQoSMonitoringControl_isPeriodicQFMonitoringSupported, QFQoSMonitoringControl_isSessionReleasedQFMonitoringSupported, QFQoSMonitoringControl_qFMeasurementPeriod, QFQoSMonitoringControl_qFMinimumWaitTime, QFQoSMonitoringControl_qFMonitoredSNSSAIs, QFQoSMonitoringControl_qFPacketDelayThresholds, QFQoSMonitoringControl_qFQoSMonitoringState}

QFQoSMonitoringControlGrp = Class(name="QFQoSMonitoringControlGrp", synonyms=["Represents the QFQoSMonitoringControl IOC."])

# QFQoSMonitoringControlGrp class attributes and methods
QFQoSMonitoringControlGrp_isEventTriggeredQFMonitoringSupported: Property = Property(name="isEventTriggeredQFMonitoringSupported", type=BooleanType, synonyms=["It indicates whether the event based QoS monitoring reporting per QoS flow per UE is supported."])
QFQoSMonitoringControlGrp_isPeriodicQFMonitoringSupported: Property = Property(name="isPeriodicQFMonitoringSupported", type=BooleanType, synonyms=["It indicates whether the periodic QoS monitoring reporting per QoS flow per UE is supported."])
QFQoSMonitoringControlGrp_isSessionReleasedQFMonitoringSupported: Property = Property(name="isSessionReleasedQFMonitoringSupported", type=BooleanType, synonyms=["It indicates whether the session release based QoS monitoring reporting per QoS flow per UE is supported."])
QFQoSMonitoringControlGrp_qFMeasurementPeriod: Property = Property(name="qFMeasurementPeriod", type=IntegerType, synonyms=["It specifies the period (in seconds) for reporting the packet delay for QoS monitoring per QoS flow per UE."])
QFQoSMonitoringControlGrp_qFMinimumWaitTime: Property = Property(name="qFMinimumWaitTime", type=IntegerType, synonyms=["It specifies the minimum waiting time (in seconds) between two consecutive reports for event triggered QoS monitoring reporting per QoS flow per UE."])
QFQoSMonitoringControlGrp_qFMonitoredSNSSAIs: Property = Property(name="qFMonitoredSNSSAIs", type=list, synonyms=["The S-NSSAIs for which the QoS monitoring per QoS flow per UE is to be performed."])
QFQoSMonitoringControlGrp_qFPacketDelayThresholds: Property = Property(name="qFPacketDelayThresholds", type=list, synonyms=["It specifies the thresholds for reporting the packet delay between PSA and UE for QoS monitoring per QoS flow per UE."])
QFQoSMonitoringControlGrp_qFQoSMonitoringState: Property = Property(name="qFQoSMonitoringState", type=EnumerationType, synonyms=["The state of QoS monitoring per QoS flow per UE."])
QFQoSMonitoringControlGrp.attributes={QFQoSMonitoringControlGrp_isEventTriggeredQFMonitoringSupported, QFQoSMonitoringControlGrp_isPeriodicQFMonitoringSupported, QFQoSMonitoringControlGrp_isSessionReleasedQFMonitoringSupported, QFQoSMonitoringControlGrp_qFMeasurementPeriod, QFQoSMonitoringControlGrp_qFMinimumWaitTime, QFQoSMonitoringControlGrp_qFMonitoredSNSSAIs, QFQoSMonitoringControlGrp_qFPacketDelayThresholds, QFQoSMonitoringControlGrp_qFQoSMonitoringState}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-QFQoSMonitoringControl",
    types={QFPacketDelayThresholdsTypeGrp, QFQoSMonitoringControl, QFQoSMonitoringControlGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the capabilities and properties for control of QoS monitoring per QoS flow per UE for URLLC service defined in 3GPP TS 23.501."]
