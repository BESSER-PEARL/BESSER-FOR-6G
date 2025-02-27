# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
GtpUPathDelayThresholdsType = Class(name="GtpUPathDelayThresholdsType", synonyms=["Thresholds for reporting the packet delay for GTP-U path QoS monitoring"])

# GtpUPathDelayThresholdsType class attributes and methods
GtpUPathDelayThresholdsType_n3AveragePacketDelayThreshold: Property = Property(name="n3AveragePacketDelayThreshold", type=IntegerType)
GtpUPathDelayThresholdsType_n3MaxPacketDelayThreshold: Property = Property(name="n3MaxPacketDelayThreshold", type=IntegerType)
GtpUPathDelayThresholdsType_n3MinPacketDelayThreshold: Property = Property(name="n3MinPacketDelayThreshold", type=IntegerType)
GtpUPathDelayThresholdsType_n9AveragePacketDelayThreshold: Property = Property(name="n9AveragePacketDelayThreshold", type=IntegerType)
GtpUPathDelayThresholdsType_n9MaxPacketDelayThreshold: Property = Property(name="n9MaxPacketDelayThreshold", type=IntegerType)
GtpUPathDelayThresholdsType_n9MinPacketDelayThreshold: Property = Property(name="n9MinPacketDelayThreshold", type=IntegerType)
GtpUPathDelayThresholdsType.attributes={GtpUPathDelayThresholdsType_n3AveragePacketDelayThreshold, GtpUPathDelayThresholdsType_n3MaxPacketDelayThreshold, GtpUPathDelayThresholdsType_n3MinPacketDelayThreshold, GtpUPathDelayThresholdsType_n9AveragePacketDelayThreshold, GtpUPathDelayThresholdsType_n9MaxPacketDelayThreshold, GtpUPathDelayThresholdsType_n9MinPacketDelayThreshold}

GtpUPathQoSMonitoringControl = Class(name="GtpUPathQoSMonitoringControl", synonyms=["Specifies the capabilities and properties for control of GTP-U path QoS monitoring. For more information about the GTP-U path QoS monitoring."])

# GtpUPathQoSMonitoringControl class attributes and methods
GtpUPathQoSMonitoringControl_gtpUPathDelayThresholds: Property = Property(name="gtpUPathDelayThresholds", type=list, synonyms=["It specifies the thresholds for reporting the packet delay for the GTO-U path QoS monitoring."])
GtpUPathQoSMonitoringControl_gtpUPathMeasurementPeriod: Property = Property(name="gtpUPathMeasurementPeriod", type=IntegerType, synonyms=["It specifies the period (in seconds) for reporting the packet delay for GTP-U path QoS monitoring."])
GtpUPathQoSMonitoringControl_gtpUPathMinimumWaitTime: Property = Property(name="gtpUPathMinimumWaitTime", type=IntegerType, synonyms=["It specifies the minimum waiting time (in seconds) between two consecutive reports for event triggered GTP-U path QoS monitoring reporting."])
GtpUPathQoSMonitoringControl_gtpUPathMonitoredSNSSAIs: Property = Property(name="gtpUPathMonitoredSNSSAIs", type=list, synonyms=["The S-NSSAIs for which the the GTP-U path QoS monitoring is to be performed."])
GtpUPathQoSMonitoringControl_gtpUPathQoSMonitoringState: Property = Property(name="gtpUPathQoSMonitoringState", type=EnumerationType, synonyms=["The state of GTP-U path QoS monitoring."])
GtpUPathQoSMonitoringControl_isEventTriggeredGtpUPathMonitoringSupported: Property = Property(name="isEventTriggeredGtpUPathMonitoringSupported", type=BooleanType, synonyms=["It indicates whether the event triggered GTP-U path QoS monitoring reporting based on thresholds is supported."])
GtpUPathQoSMonitoringControl_isImmediateGtpUMonitoringSupported: Property = Property(name="isImmediateGtpUMonitoringSupported", type=BooleanType, synonyms=["It indicates whether the immediate GTP-U path QoS monitoring reporting is supported."])
GtpUPathQoSMonitoringControl_isPeriodicGtpUMonitoringSupported: Property = Property(name="isPeriodicGtpUMonitoringSupported", type=BooleanType, synonyms=["It indicates whether the periodic GTP-U path QoS monitoring reporting is supported."])
GtpUPathQoSMonitoringControl.attributes={GtpUPathQoSMonitoringControl_gtpUPathDelayThresholds, GtpUPathQoSMonitoringControl_gtpUPathMeasurementPeriod, GtpUPathQoSMonitoringControl_gtpUPathMinimumWaitTime, GtpUPathQoSMonitoringControl_gtpUPathMonitoredSNSSAIs, GtpUPathQoSMonitoringControl_gtpUPathQoSMonitoringState, GtpUPathQoSMonitoringControl_isEventTriggeredGtpUPathMonitoringSupported, GtpUPathQoSMonitoringControl_isImmediateGtpUMonitoringSupported, GtpUPathQoSMonitoringControl_isPeriodicGtpUMonitoringSupported}

GtpUPathQoSMonitoringControlGrp = Class(name="GtpUPathQoSMonitoringControlGrp", synonyms=["Represents the GtpUPathQoSMonitoringControl IOC."])

# GtpUPathQoSMonitoringControlGrp class attributes and methods
GtpUPathQoSMonitoringControlGrp_gtpUPathDelayThresholds: Property = Property(name="gtpUPathDelayThresholds", type=list, synonyms=["It specifies the thresholds for reporting the packet delay for the GTO-U path QoS monitoring."])
GtpUPathQoSMonitoringControlGrp_gtpUPathMeasurementPeriod: Property = Property(name="gtpUPathMeasurementPeriod", type=IntegerType, synonyms=["It specifies the period (in seconds) for reporting the packet delay for GTP-U path QoS monitoring."])
GtpUPathQoSMonitoringControlGrp_gtpUPathMinimumWaitTime: Property = Property(name="gtpUPathMinimumWaitTime", type=IntegerType, synonyms=["It specifies the minimum waiting time (in seconds) between two consecutive reports for event triggered GTP-U path QoS monitoring reporting."])
GtpUPathQoSMonitoringControlGrp_gtpUPathMonitoredSNSSAIs: Property = Property(name="gtpUPathMonitoredSNSSAIs", type=list, synonyms=["The S-NSSAIs for which the the GTP-U path QoS monitoring is to be performed."])
GtpUPathQoSMonitoringControlGrp_gtpUPathQoSMonitoringState: Property = Property(name="gtpUPathQoSMonitoringState", type=EnumerationType, synonyms=["The state of GTP-U path QoS monitoring."])
GtpUPathQoSMonitoringControlGrp_isEventTriggeredGtpUPathMonitoringSupported: Property = Property(name="isEventTriggeredGtpUPathMonitoringSupported", type=BooleanType, synonyms=["It indicates whether the event triggered GTP-U path QoS monitoring reporting based on thresholds is supported."])
GtpUPathQoSMonitoringControlGrp_isImmediateGtpUMonitoringSupported: Property = Property(name="isImmediateGtpUMonitoringSupported", type=BooleanType, synonyms=["It indicates whether the immediate GTP-U path QoS monitoring reporting is supported."])
GtpUPathQoSMonitoringControlGrp_isPeriodicGtpUMonitoringSupported: Property = Property(name="isPeriodicGtpUMonitoringSupported", type=BooleanType, synonyms=["It indicates whether the periodic GTP-U path QoS monitoring reporting is supported."])
GtpUPathQoSMonitoringControlGrp.attributes={GtpUPathQoSMonitoringControlGrp_gtpUPathDelayThresholds, GtpUPathQoSMonitoringControlGrp_gtpUPathMeasurementPeriod, GtpUPathQoSMonitoringControlGrp_gtpUPathMinimumWaitTime, GtpUPathQoSMonitoringControlGrp_gtpUPathMonitoredSNSSAIs, GtpUPathQoSMonitoringControlGrp_gtpUPathQoSMonitoringState, GtpUPathQoSMonitoringControlGrp_isEventTriggeredGtpUPathMonitoringSupported, GtpUPathQoSMonitoringControlGrp_isImmediateGtpUMonitoringSupported, GtpUPathQoSMonitoringControlGrp_isPeriodicGtpUMonitoringSupported}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-GtpUPathQoSMonitoringControl",
    types={GtpUPathDelayThresholdsType, GtpUPathQoSMonitoringControl, GtpUPathQoSMonitoringControlGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the capabilities and properties for control of GTP-U path QoS monitoring defined in 3GPP TS 23.501."]
