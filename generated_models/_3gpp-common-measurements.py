# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    Constraint
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_5gc_nrm_affunction import domain_model as af3gpp_model
from generated_models._3gpp_5gc_nrm_amffunction import domain_model as amf3gpp_model
from generated_models._3gpp_5gc_nrm_ausffunction import domain_model as ausf3gpp_model
from generated_models._3gpp_5gc_nrm_configurable5qiset import domain_model as Conf5QIs3gpp_model
from generated_models._3gpp_5gc_nrm_dnfunction import domain_model as dn3gpp_model
from generated_models._3gpp_5gc_nrm_lmffunction import domain_model as lmf3gpp_model
from generated_models._3gpp_5gc_nrm_n3iwffunction import domain_model as n3iwf3gpp_model
from generated_models._3gpp_5gc_nrm_nfprofile import domain_model as nfp3gpp_model
from generated_models._3gpp_5gc_nrm_nfservice import domain_model as nfs3gpp_model
from generated_models._3gpp_5gc_nrm_ngeirfunction import domain_model as ngeir3gpp_model
from generated_models._3gpp_5gc_nrm_nrffunction import domain_model as nrf3gpp_model
from generated_models._3gpp_5gc_nrm_nssffunction import domain_model as nssf3gpp_model
from generated_models._3gpp_5gc_nrm_pcffunction import domain_model as pcf3gpp_model
from generated_models._3gpp_5gc_nrm_seppfunction import domain_model as sepp3gpp_model
from generated_models._3gpp_5gc_nrm_smffunction import domain_model as smf3gpp_model
from generated_models._3gpp_5gc_nrm_smsffunction import domain_model as smsf3gpp_model
from generated_models._3gpp_5gc_nrm_udmfunction import domain_model as udm3gpp_model
from generated_models._3gpp_5gc_nrm_upffunction import domain_model as upf3gpp_model
from generated_models._3gpp_common_ep_rp import domain_model as eprp3gpp_model
from generated_models._3gpp_common_fm import domain_model as fm3gpp_model
from generated_models._3gpp_common_managed_element import domain_model as me3gpp_model
from generated_models._3gpp_common_managed_function import domain_model as mf3gpp_model
from generated_models._3gpp_common_measurements import domain_model as meas3gpp_model
from generated_models._3gpp_common_subnetwork import domain_model as subnet3gpp_model
from generated_models._3gpp_common_subscription_control import domain_model as subscr3gpp_model
from generated_models._3gpp_common_top import domain_model as top3gpp_model
from generated_models._3gpp_common_trace import domain_model as trace3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Enumerations
# Classes
ThresholdInfoGrp = Class(name="ThresholdInfoGrp")
SupportedPerfMetricGroupGrp = Class(name="SupportedPerfMetricGroupGrp")
PerfMetricJobGrp = Class(name="PerfMetricJobGrp")
ThresholdMonitorGrp = Class(name="ThresholdMonitorGrp")
MeasurementSubtree = Class(name="MeasurementSubtree")

# ThresholdInfoGrp class attributes and methods
ThresholdInfoGrp_thresholdLevel: Property = Property(name="thresholdLevel", type=IntegerType)
ThresholdInfoGrp_thresholdDirection: Property = Property(name="thresholdDirection", type=enumeration)
ThresholdInfoGrp_thresholdValue: Property = Property(name="thresholdValue", type=union)
ThresholdInfoGrp_hysteresis: Property = Property(name="hysteresis", type=union)
ThresholdInfoGrp.attributes={ThresholdInfoGrp_thresholdLevel, ThresholdInfoGrp_thresholdDirection, ThresholdInfoGrp_hysteresis, ThresholdInfoGrp_thresholdValue}

# SupportedPerfMetricGroupGrp class attributes and methods
SupportedPerfMetricGroupGrp_SupportedPerfMetricGroup: Property = Property(name="SupportedPerfMetricGroup", type=list)
SupportedPerfMetricGroupGrp.attributes={SupportedPerfMetricGroupGrp_SupportedPerfMetricGroup}

# PerfMetricJobGrp class attributes and methods
PerfMetricJobGrp_administrativeState: Property = Property(name="administrativeState", type=types3gpp:AdministrativeState)
PerfMetricJobGrp_operationalState: Property = Property(name="operationalState", type=types3gpp:OperationalState)
PerfMetricJobGrp_jobId: Property = Property(name="jobId", type=StringType)
PerfMetricJobGrp_granularityPeriod: Property = Property(name="granularityPeriod", type=IntegerType)
PerfMetricJobGrp.attributes={PerfMetricJobGrp_granularityPeriod, PerfMetricJobGrp_jobId, PerfMetricJobGrp_operationalState, PerfMetricJobGrp_administrativeState}

# ThresholdMonitorGrp class attributes and methods
ThresholdMonitorGrp_administrativeState: Property = Property(name="administrativeState", type=types3gpp:AdministrativeState)
ThresholdMonitorGrp_operationalState: Property = Property(name="operationalState", type=types3gpp:OperationalState)
ThresholdMonitorGrp_monitorGranularityPeriod: Property = Property(name="monitorGranularityPeriod", type=IntegerType)
ThresholdMonitorGrp_thresholdInfoList: Property = Property(name="thresholdInfoList", type=list)
ThresholdMonitorGrp.attributes={ThresholdMonitorGrp_thresholdInfoList, ThresholdMonitorGrp_operationalState, ThresholdMonitorGrp_administrativeState, ThresholdMonitorGrp_monitorGranularityPeriod}

# MeasurementSubtree class attributes and methods
MeasurementSubtree_PerfMetricJob: Property = Property(name="PerfMetricJob", type=list)
MeasurementSubtree_ThresholdMonitor: Property = Property(name="ThresholdMonitor", type=list)
MeasurementSubtree.attributes={MeasurementSubtree_PerfMetricJob, MeasurementSubtree_ThresholdMonitor}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-common-measurements",
    types={ThresholdInfoGrp, SupportedPerfMetricGroupGrp, PerfMetricJobGrp, ThresholdMonitorGrp, MeasurementSubtree, types3gpp_model, mf3gpp_model, me3gpp_model, top3gpp_model, types5g3gpp_model, inet_model, subnet3gpp_model, Conf5QIs3gpp_model, eprp3gpp_model, af3gpp_model, amf3gpp_model, ausf3gpp_model, dn3gpp_model, lmf3gpp_model, n3iwf3gpp_model, ngeir3gpp_model, nrf3gpp_model, nssf3gpp_model, pcf3gpp_model, sepp3gpp_model, smf3gpp_model, smsf3gpp_model, udm3gpp_model, upf3gpp_model, yang_model, nfs3gpp_model, nfp3gpp_model, meas3gpp_model, subscr3gpp_model, fm3gpp_model, trace3gpp_model},
    associations={},
    generalizations={}
)
