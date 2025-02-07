# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
QFPacketDelayThresholdsType = Class(name="QFPacketDelayThresholdsType")

# QFPacketDelayThresholdsType class attributes and methods
QFPacketDelayThresholdsType_thresholdDl: Property = Property(name="thresholdDl", type=IntegerType)
QFPacketDelayThresholdsType_thresholdUl: Property = Property(name="thresholdUl", type=IntegerType)
QFPacketDelayThresholdsType_thresholdRtt: Property = Property(name="thresholdRtt", type=IntegerType)
QFPacketDelayThresholdsType.attributes={QFPacketDelayThresholdsType_thresholdDl, QFPacketDelayThresholdsType_thresholdUl, QFPacketDelayThresholdsType_thresholdRtt}

QFQoSMonitoringControl = Class(name="QFQoSMonitoringControl")

# QFQoSMonitoringControl class attributes and methods
QFQoSMonitoringControl_isSessionReleasedQFMonitoringSupported: Property = Property(name="isSessionReleasedQFMonitoringSupported", type=BooleanType)
QFQoSMonitoringControl_qFMinimumWaitTime: Property = Property(name="qFMinimumWaitTime", type=IntegerType)
QFQoSMonitoringControl_qFMeasurementPeriod: Property = Property(name="qFMeasurementPeriod", type=IntegerType)
QFQoSMonitoringControl_qFMonitoredSNSSAIs: Property = Property(name="qFMonitoredSNSSAIs", type=list)
QFQoSMonitoringControl_qFPacketDelayThresholds: Property = Property(name="qFPacketDelayThresholds", type=list)
QFQoSMonitoringControl_qFQoSMonitoringState: Property = Property(name="qFQoSMonitoringState", type=enumeration)
QFQoSMonitoringControl_isEventTriggeredQFMonitoringSupported: Property = Property(name="isEventTriggeredQFMonitoringSupported", type=BooleanType)
QFQoSMonitoringControl_isPeriodicQFMonitoringSupported: Property = Property(name="isPeriodicQFMonitoringSupported", type=BooleanType)
QFQoSMonitoringControl.attributes={QFQoSMonitoringControl_isSessionReleasedQFMonitoringSupported, QFQoSMonitoringControl_qFMinimumWaitTime, QFQoSMonitoringControl_qFMeasurementPeriod, QFQoSMonitoringControl_qFMonitoredSNSSAIs, QFQoSMonitoringControl_qFPacketDelayThresholds, QFQoSMonitoringControl_qFQoSMonitoringState, QFQoSMonitoringControl_isEventTriggeredQFMonitoringSupported, QFQoSMonitoringControl_isPeriodicQFMonitoringSupported}

