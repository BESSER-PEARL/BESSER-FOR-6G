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
from generated_models._3gpp_common_managed_element import domain_model as me3gpp_model
from generated_models._3gpp_common_managed_function import domain_model as mf3gpp_model
from generated_models._3gpp_common_subnetwork import domain_model as subnet3gpp_model
from generated_models._3gpp_common_top import domain_model as top3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Enumerations
# Classes
QFPacketDelayThresholdsTypeGrp = Class(name="QFPacketDelayThresholdsTypeGrp")
QFQoSMonitoringControlGrp = Class(name="QFQoSMonitoringControlGrp")
QFQoSMonitoringControl = Class(name="QFQoSMonitoringControl")

# QFPacketDelayThresholdsTypeGrp class attributes and methods
QFPacketDelayThresholdsTypeGrp_thresholdDl: Property = Property(name="thresholdDl", type=IntegerType)
QFPacketDelayThresholdsTypeGrp_thresholdUl: Property = Property(name="thresholdUl", type=IntegerType)
QFPacketDelayThresholdsTypeGrp_thresholdRtt: Property = Property(name="thresholdRtt", type=IntegerType)
QFPacketDelayThresholdsTypeGrp.attributes={QFPacketDelayThresholdsTypeGrp_thresholdRtt, QFPacketDelayThresholdsTypeGrp_thresholdUl, QFPacketDelayThresholdsTypeGrp_thresholdDl}

# QFQoSMonitoringControlGrp class attributes and methods
QFQoSMonitoringControlGrp_qFQoSMonitoringState: Property = Property(name="qFQoSMonitoringState", type=enumeration)
QFQoSMonitoringControlGrp_isEventTriggeredQFMonitoringSupported: Property = Property(name="isEventTriggeredQFMonitoringSupported", type=BooleanType)
QFQoSMonitoringControlGrp_isPeriodicQFMonitoringSupported: Property = Property(name="isPeriodicQFMonitoringSupported", type=BooleanType)
QFQoSMonitoringControlGrp_isSessionReleasedQFMonitoringSupported: Property = Property(name="isSessionReleasedQFMonitoringSupported", type=BooleanType)
QFQoSMonitoringControlGrp_qFMinimumWaitTime: Property = Property(name="qFMinimumWaitTime", type=IntegerType)
QFQoSMonitoringControlGrp_qFMeasurementPeriod: Property = Property(name="qFMeasurementPeriod", type=IntegerType)
QFQoSMonitoringControlGrp_qFMonitoredSNSSAIs: Property = Property(name="qFMonitoredSNSSAIs", type=list)
QFQoSMonitoringControlGrp_qFPacketDelayThresholds: Property = Property(name="qFPacketDelayThresholds", type=list)
QFQoSMonitoringControlGrp.attributes={QFQoSMonitoringControlGrp_isEventTriggeredQFMonitoringSupported, QFQoSMonitoringControlGrp_qFPacketDelayThresholds, QFQoSMonitoringControlGrp_isSessionReleasedQFMonitoringSupported, QFQoSMonitoringControlGrp_qFQoSMonitoringState, QFQoSMonitoringControlGrp_isPeriodicQFMonitoringSupported, QFQoSMonitoringControlGrp_qFMinimumWaitTime, QFQoSMonitoringControlGrp_qFMonitoredSNSSAIs, QFQoSMonitoringControlGrp_qFMeasurementPeriod}

# QFQoSMonitoringControl class attributes and methods
QFQoSMonitoringControl_qFQoSMonitoringState: Property = Property(name="qFQoSMonitoringState", type=enumeration)
QFQoSMonitoringControl_isEventTriggeredQFMonitoringSupported: Property = Property(name="isEventTriggeredQFMonitoringSupported", type=BooleanType)
QFQoSMonitoringControl_isPeriodicQFMonitoringSupported: Property = Property(name="isPeriodicQFMonitoringSupported", type=BooleanType)
QFQoSMonitoringControl_isSessionReleasedQFMonitoringSupported: Property = Property(name="isSessionReleasedQFMonitoringSupported", type=BooleanType)
QFQoSMonitoringControl_qFMinimumWaitTime: Property = Property(name="qFMinimumWaitTime", type=IntegerType)
QFQoSMonitoringControl_qFMeasurementPeriod: Property = Property(name="qFMeasurementPeriod", type=IntegerType)
QFQoSMonitoringControl_qFMonitoredSNSSAIs: Property = Property(name="qFMonitoredSNSSAIs", type=list)
QFQoSMonitoringControl_qFPacketDelayThresholds: Property = Property(name="qFPacketDelayThresholds", type=list)
QFQoSMonitoringControl.attributes={QFQoSMonitoringControl_isEventTriggeredQFMonitoringSupported, QFQoSMonitoringControl_qFPacketDelayThresholds, QFQoSMonitoringControl_isSessionReleasedQFMonitoringSupported, QFQoSMonitoringControl_qFQoSMonitoringState, QFQoSMonitoringControl_isPeriodicQFMonitoringSupported, QFQoSMonitoringControl_qFMinimumWaitTime, QFQoSMonitoringControl_qFMonitoredSNSSAIs, QFQoSMonitoringControl_qFMeasurementPeriod}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-QFQoSMonitoringControl",
    types={QFPacketDelayThresholdsTypeGrp, QFQoSMonitoringControlGrp, QFQoSMonitoringControl, types3gpp_model, mf3gpp_model, me3gpp_model, top3gpp_model, types5g3gpp_model, inet_model, subnet3gpp_model, Conf5QIs3gpp_model, eprp3gpp_model, af3gpp_model, amf3gpp_model, ausf3gpp_model, dn3gpp_model, lmf3gpp_model, n3iwf3gpp_model, ngeir3gpp_model, nrf3gpp_model, nssf3gpp_model, pcf3gpp_model, sepp3gpp_model, smf3gpp_model, smsf3gpp_model, udm3gpp_model, upf3gpp_model, yang_model, nfs3gpp_model, nfp3gpp_model},
    associations={},
    generalizations={}
)
