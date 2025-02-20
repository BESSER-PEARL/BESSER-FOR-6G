# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
GtpUPathDelayThresholdsType = Class(name="GtpUPathDelayThresholdsType")

# GtpUPathDelayThresholdsType class attributes and methods
GtpUPathDelayThresholdsType_n3AveragePacketDelayThreshold: Property = Property(name="n3AveragePacketDelayThreshold", type=IntegerType)
GtpUPathDelayThresholdsType_n3MaxPacketDelayThreshold: Property = Property(name="n3MaxPacketDelayThreshold", type=IntegerType)
GtpUPathDelayThresholdsType_n3MinPacketDelayThreshold: Property = Property(name="n3MinPacketDelayThreshold", type=IntegerType)
GtpUPathDelayThresholdsType_n9AveragePacketDelayThreshold: Property = Property(name="n9AveragePacketDelayThreshold", type=IntegerType)
GtpUPathDelayThresholdsType_n9MaxPacketDelayThreshold: Property = Property(name="n9MaxPacketDelayThreshold", type=IntegerType)
GtpUPathDelayThresholdsType_n9MinPacketDelayThreshold: Property = Property(name="n9MinPacketDelayThreshold", type=IntegerType)
GtpUPathDelayThresholdsType.attributes={GtpUPathDelayThresholdsType_n3AveragePacketDelayThreshold, GtpUPathDelayThresholdsType_n3MaxPacketDelayThreshold, GtpUPathDelayThresholdsType_n3MinPacketDelayThreshold, GtpUPathDelayThresholdsType_n9AveragePacketDelayThreshold, GtpUPathDelayThresholdsType_n9MaxPacketDelayThreshold, GtpUPathDelayThresholdsType_n9MinPacketDelayThreshold}

GtpUPathQoSMonitoringControl = Class(name="GtpUPathQoSMonitoringControl")

# GtpUPathQoSMonitoringControl class attributes and methods
GtpUPathQoSMonitoringControl_gtpUPathDelayThresholds: Property = Property(name="gtpUPathDelayThresholds", type=list)
GtpUPathQoSMonitoringControl_gtpUPathMeasurementPeriod: Property = Property(name="gtpUPathMeasurementPeriod", type=IntegerType)
GtpUPathQoSMonitoringControl_gtpUPathMinimumWaitTime: Property = Property(name="gtpUPathMinimumWaitTime", type=IntegerType)
GtpUPathQoSMonitoringControl_gtpUPathMonitoredSNSSAIs: Property = Property(name="gtpUPathMonitoredSNSSAIs", type=list)
GtpUPathQoSMonitoringControl_gtpUPathQoSMonitoringState: Property = Property(name="gtpUPathQoSMonitoringState", type=EnumerationType)
GtpUPathQoSMonitoringControl_isEventTriggeredGtpUPathMonitoringSupported: Property = Property(name="isEventTriggeredGtpUPathMonitoringSupported", type=BooleanType)
GtpUPathQoSMonitoringControl_isImmediateGtpUMonitoringSupported: Property = Property(name="isImmediateGtpUMonitoringSupported", type=BooleanType)
GtpUPathQoSMonitoringControl_isPeriodicGtpUMonitoringSupported: Property = Property(name="isPeriodicGtpUMonitoringSupported", type=BooleanType)
GtpUPathQoSMonitoringControl.attributes={GtpUPathQoSMonitoringControl_gtpUPathDelayThresholds, GtpUPathQoSMonitoringControl_gtpUPathMeasurementPeriod, GtpUPathQoSMonitoringControl_gtpUPathMinimumWaitTime, GtpUPathQoSMonitoringControl_gtpUPathMonitoredSNSSAIs, GtpUPathQoSMonitoringControl_gtpUPathQoSMonitoringState, GtpUPathQoSMonitoringControl_isEventTriggeredGtpUPathMonitoringSupported, GtpUPathQoSMonitoringControl_isImmediateGtpUMonitoringSupported, GtpUPathQoSMonitoringControl_isPeriodicGtpUMonitoringSupported}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-GtpUPathQoSMonitoringControl",
    types={GtpUPathDelayThresholdsType, GtpUPathQoSMonitoringControl},
    associations={},
    generalizations={}
)
