# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
ThresholdInfo = Class(name="ThresholdInfo")

# ThresholdInfo class attributes and methods
ThresholdInfo_thresholdLevel: Property = Property(name="thresholdLevel", type=IntegerType)
ThresholdInfo_thresholdDirection: Property = Property(name="thresholdDirection", type=enumeration)
ThresholdInfo_thresholdValue: Property = Property(name="thresholdValue", type=union)
ThresholdInfo_hysteresis: Property = Property(name="hysteresis", type=union)
ThresholdInfo.attributes={ThresholdInfo_thresholdLevel, ThresholdInfo_thresholdDirection, ThresholdInfo_thresholdValue, ThresholdInfo_hysteresis}

SupportedPerfMetricGroup = Class(name="SupportedPerfMetricGroup")

# SupportedPerfMetricGroup class attributes and methods
SupportedPerfMetricGroup_SupportedPerfMetricGroup: Property = Property(name="SupportedPerfMetricGroup", type=list)
SupportedPerfMetricGroup.attributes={SupportedPerfMetricGroup_SupportedPerfMetricGroup}

PerfMetricJob = Class(name="PerfMetricJob")

# PerfMetricJob class attributes and methods
PerfMetricJob_administrativeState: Property = Property(name="administrativeState", type=types3gpp:AdministrativeState)
PerfMetricJob_operationalState: Property = Property(name="operationalState", type=types3gpp:OperationalState)
PerfMetricJob_jobId: Property = Property(name="jobId", type=StringType)
PerfMetricJob_granularityPeriod: Property = Property(name="granularityPeriod", type=IntegerType)
PerfMetricJob.attributes={PerfMetricJob_administrativeState, PerfMetricJob_operationalState, PerfMetricJob_jobId, PerfMetricJob_granularityPeriod}

ThresholdMonitor = Class(name="ThresholdMonitor")

# ThresholdMonitor class attributes and methods
ThresholdMonitor_administrativeState: Property = Property(name="administrativeState", type=types3gpp:AdministrativeState)
ThresholdMonitor_operationalState: Property = Property(name="operationalState", type=types3gpp:OperationalState)
ThresholdMonitor_monitorGranularityPeriod: Property = Property(name="monitorGranularityPeriod", type=IntegerType)
ThresholdMonitor_thresholdInfoList: Property = Property(name="thresholdInfoList", type=list)
ThresholdMonitor.attributes={ThresholdMonitor_administrativeState, ThresholdMonitor_operationalState, ThresholdMonitor_monitorGranularityPeriod, ThresholdMonitor_thresholdInfoList}

MeasurementSubtree = Class(name="MeasurementSubtree")

# MeasurementSubtree class attributes and methods
MeasurementSubtree_PerfMetricJob: Property = Property(name="PerfMetricJob", type=list)
MeasurementSubtree_ThresholdMonitor: Property = Property(name="ThresholdMonitor", type=list)
MeasurementSubtree.attributes={MeasurementSubtree_PerfMetricJob, MeasurementSubtree_ThresholdMonitor}

