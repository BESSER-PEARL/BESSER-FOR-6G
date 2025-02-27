# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
MeasurementSubtree = Class(name="MeasurementSubtree")

# MeasurementSubtree class attributes and methods
MeasurementSubtree_PerfMetricJob: Property = Property(name="PerfMetricJob", type=list)
MeasurementSubtree_ThresholdMonitor: Property = Property(name="ThresholdMonitor", type=list)
MeasurementSubtree.attributes={MeasurementSubtree_PerfMetricJob, MeasurementSubtree_ThresholdMonitor}

PerfMetricJob = Class(name="PerfMetricJob")

# PerfMetricJob class attributes and methods
PerfMetricJob_administrativeState: Property = Property(name="administrativeState", type=StringType)
PerfMetricJob_granularityPeriod: Property = Property(name="granularityPeriod", type=IntegerType)
PerfMetricJob_jobId: Property = Property(name="jobId", type=StringType)
PerfMetricJob_operationalState: Property = Property(name="operationalState", type=StringType)
PerfMetricJob.attributes={PerfMetricJob_administrativeState, PerfMetricJob_granularityPeriod, PerfMetricJob_jobId, PerfMetricJob_operationalState}

SupportedPerfMetricGroup = Class(name="SupportedPerfMetricGroup")

# SupportedPerfMetricGroup class attributes and methods
SupportedPerfMetricGroup_SupportedPerfMetricGroup: Property = Property(name="SupportedPerfMetricGroup", type=list)
SupportedPerfMetricGroup.attributes={SupportedPerfMetricGroup_SupportedPerfMetricGroup}

ThresholdInfo = Class(name="ThresholdInfo")

# ThresholdInfo class attributes and methods
ThresholdInfo_hysteresis: Property = Property(name="hysteresis", type=StringType)
ThresholdInfo_thresholdDirection: Property = Property(name="thresholdDirection", type=EnumerationType)
ThresholdInfo_thresholdLevel: Property = Property(name="thresholdLevel", type=IntegerType)
ThresholdInfo_thresholdValue: Property = Property(name="thresholdValue", type=StringType)
ThresholdInfo.attributes={ThresholdInfo_hysteresis, ThresholdInfo_thresholdDirection, ThresholdInfo_thresholdLevel, ThresholdInfo_thresholdValue}

ThresholdMonitor = Class(name="ThresholdMonitor")

# ThresholdMonitor class attributes and methods
ThresholdMonitor_administrativeState: Property = Property(name="administrativeState", type=StringType)
ThresholdMonitor_monitorGranularityPeriod: Property = Property(name="monitorGranularityPeriod", type=IntegerType)
ThresholdMonitor_operationalState: Property = Property(name="operationalState", type=StringType)
ThresholdMonitor_thresholdInfoList: Property = Property(name="thresholdInfoList", type=list)
ThresholdMonitor.attributes={ThresholdMonitor_administrativeState, ThresholdMonitor_monitorGranularityPeriod, ThresholdMonitor_operationalState, ThresholdMonitor_thresholdInfoList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-common-measurements",
    types={MeasurementSubtree, PerfMetricJob, SupportedPerfMetricGroup, ThresholdInfo, ThresholdMonitor},
    associations={},
    generalizations={}
)
