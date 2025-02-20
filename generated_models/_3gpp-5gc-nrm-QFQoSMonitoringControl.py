# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
QFPacketDelayThresholdsType = Class(name="QFPacketDelayThresholdsType")

# QFPacketDelayThresholdsType class attributes and methods
QFPacketDelayThresholdsType_thresholdDl: Property = Property(name="thresholdDl", type=IntegerType)
QFPacketDelayThresholdsType_thresholdRtt: Property = Property(name="thresholdRtt", type=IntegerType)
QFPacketDelayThresholdsType_thresholdUl: Property = Property(name="thresholdUl", type=IntegerType)
QFPacketDelayThresholdsType.attributes={QFPacketDelayThresholdsType_thresholdDl, QFPacketDelayThresholdsType_thresholdRtt, QFPacketDelayThresholdsType_thresholdUl}

QFQoSMonitoringControl = Class(name="QFQoSMonitoringControl")

# QFQoSMonitoringControl class attributes and methods
QFQoSMonitoringControl_isEventTriggeredQFMonitoringSupported: Property = Property(name="isEventTriggeredQFMonitoringSupported", type=BooleanType)
QFQoSMonitoringControl_isPeriodicQFMonitoringSupported: Property = Property(name="isPeriodicQFMonitoringSupported", type=BooleanType)
QFQoSMonitoringControl_isSessionReleasedQFMonitoringSupported: Property = Property(name="isSessionReleasedQFMonitoringSupported", type=BooleanType)
QFQoSMonitoringControl_qFMeasurementPeriod: Property = Property(name="qFMeasurementPeriod", type=IntegerType)
QFQoSMonitoringControl_qFMinimumWaitTime: Property = Property(name="qFMinimumWaitTime", type=IntegerType)
QFQoSMonitoringControl_qFMonitoredSNSSAIs: Property = Property(name="qFMonitoredSNSSAIs", type=list)
QFQoSMonitoringControl_qFPacketDelayThresholds: Property = Property(name="qFPacketDelayThresholds", type=list)
QFQoSMonitoringControl_qFQoSMonitoringState: Property = Property(name="qFQoSMonitoringState", type=EnumerationType)
QFQoSMonitoringControl.attributes={QFQoSMonitoringControl_isEventTriggeredQFMonitoringSupported, QFQoSMonitoringControl_isPeriodicQFMonitoringSupported, QFQoSMonitoringControl_isSessionReleasedQFMonitoringSupported, QFQoSMonitoringControl_qFMeasurementPeriod, QFQoSMonitoringControl_qFMinimumWaitTime, QFQoSMonitoringControl_qFMonitoredSNSSAIs, QFQoSMonitoringControl_qFPacketDelayThresholds, QFQoSMonitoringControl_qFQoSMonitoringState}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-QFQoSMonitoringControl",
    types={QFPacketDelayThresholdsType, QFQoSMonitoringControl},
    associations={},
    generalizations={}
)
