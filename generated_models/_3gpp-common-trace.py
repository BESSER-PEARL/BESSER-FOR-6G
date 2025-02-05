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
TraceJobGrp = Class(name="TraceJobGrp")
TraceSubtree = Class(name="TraceSubtree")

# TraceJobGrp class attributes and methods
TraceJobGrp_tjJobType: Property = Property(name="tjJobType", type=enumeration)
TraceJobGrp_tjPLMNTarget: Property = Property(name="tjPLMNTarget", type=StringType)
TraceJobGrp_tjStreamingTraceConsumerURI: Property = Property(name="tjStreamingTraceConsumerURI", type=inet:uri)
TraceJobGrp_tjTraceCollectionEntityAddress: Property = Property(name="tjTraceCollectionEntityAddress", type=union)
TraceJobGrp_tjTraceDepth: Property = Property(name="tjTraceDepth", type=enumeration)
TraceJobGrp_tjTraceReference: Property = Property(name="tjTraceReference", type=IntegerType)
TraceJobGrp_tjTraceReportingFormat: Property = Property(name="tjTraceReportingFormat", type=enumeration)
TraceJobGrp_tjTriggeringEvent: Property = Property(name="tjTriggeringEvent", type=StringType)
TraceJobGrp_tjMDTAnonymizationOfData: Property = Property(name="tjMDTAnonymizationOfData", type=enumeration)
TraceJobGrp_tjMDTCollectionPeriodRrmLte: Property = Property(name="tjMDTCollectionPeriodRrmLte", type=IntegerType)
TraceJobGrp_tjMDTCollectionPeriodRrmUmts: Property = Property(name="tjMDTCollectionPeriodRrmUmts", type=IntegerType)
TraceJobGrp_tjMDTCollectionPeriodRrmNR: Property = Property(name="tjMDTCollectionPeriodRrmNR", type=IntegerType)
TraceJobGrp_tjMDTEventListForTriggeredMeasurement: Property = Property(name="tjMDTEventListForTriggeredMeasurement", type=enumeration)
TraceJobGrp_tjMDTEventThreshold: Property = Property(name="tjMDTEventThreshold", type=IntegerType)
TraceJobGrp_tjMDTListOfMeasurements: Property = Property(name="tjMDTListOfMeasurements", type=IntegerType)
TraceJobGrp_tjMDTLoggingDuration: Property = Property(name="tjMDTLoggingDuration", type=IntegerType)
TraceJobGrp_tjMDTLoggingInterval: Property = Property(name="tjMDTLoggingInterval", type=IntegerType)
TraceJobGrp_tjMDTMeasurementPeriodLTE: Property = Property(name="tjMDTMeasurementPeriodLTE", type=IntegerType)
TraceJobGrp_tjMDTMeasurementPeriodUMTS: Property = Property(name="tjMDTMeasurementPeriodUMTS", type=IntegerType)
TraceJobGrp_tjMDTMeasurementQuantity: Property = Property(name="tjMDTMeasurementQuantity", type=IntegerType)
TraceJobGrp_tjMDTPositioningMethod: Property = Property(name="tjMDTPositioningMethod", type=enumeration)
TraceJobGrp_tjMDTReportAmount: Property = Property(name="tjMDTReportAmount", type=union)
TraceJobGrp_tjMDTReportingTrigger: Property = Property(name="tjMDTReportingTrigger", type=enumeration)
TraceJobGrp_tjMDTReportInterval: Property = Property(name="tjMDTReportInterval", type=IntegerType)
TraceJobGrp_tjMDTReportType: Property = Property(name="tjMDTReportType", type=enumeration)
TraceJobGrp_tjMDTSensorInformation: Property = Property(name="tjMDTSensorInformation", type=bits)
TraceJobGrp_tjMDTTraceCollectionEntityID: Property = Property(name="tjMDTTraceCollectionEntityID", type=IntegerType)
TraceJobGrp_tjListOfInterfaces: Property = Property(name="tjListOfInterfaces", type=list)
TraceJobGrp_tjTraceTarget: Property = Property(name="tjTraceTarget", type=list)
TraceJobGrp_tjMDTAreaConfigurationForNeighCell: Property = Property(name="tjMDTAreaConfigurationForNeighCell", type=list)
TraceJobGrp_tjMDTPLMList: Property = Property(name="tjMDTPLMList", type=list)
TraceJobGrp.attributes={TraceJobGrp_tjMDTAreaConfigurationForNeighCell, TraceJobGrp_tjMDTReportType, TraceJobGrp_tjMDTReportingTrigger, TraceJobGrp_tjMDTSensorInformation, TraceJobGrp_tjMDTTraceCollectionEntityID, TraceJobGrp_tjJobType, TraceJobGrp_tjTraceReference, TraceJobGrp_tjMDTMeasurementQuantity, TraceJobGrp_tjTraceReportingFormat, TraceJobGrp_tjMDTCollectionPeriodRrmNR, TraceJobGrp_tjMDTAnonymizationOfData, TraceJobGrp_tjListOfInterfaces, TraceJobGrp_tjMDTEventThreshold, TraceJobGrp_tjStreamingTraceConsumerURI, TraceJobGrp_tjMDTPositioningMethod, TraceJobGrp_tjMDTMeasurementPeriodLTE, TraceJobGrp_tjMDTMeasurementPeriodUMTS, TraceJobGrp_tjMDTReportAmount, TraceJobGrp_tjMDTLoggingInterval, TraceJobGrp_tjMDTEventListForTriggeredMeasurement, TraceJobGrp_tjMDTListOfMeasurements, TraceJobGrp_tjMDTCollectionPeriodRrmUmts, TraceJobGrp_tjTraceCollectionEntityAddress, TraceJobGrp_tjMDTLoggingDuration, TraceJobGrp_tjTraceDepth, TraceJobGrp_tjMDTPLMList, TraceJobGrp_tjTriggeringEvent, TraceJobGrp_tjTraceTarget, TraceJobGrp_tjPLMNTarget, TraceJobGrp_tjMDTCollectionPeriodRrmLte, TraceJobGrp_tjMDTReportInterval}

# TraceSubtree class attributes and methods
TraceSubtree_TraceJob: Property = Property(name="TraceJob", type=list)
TraceSubtree.attributes={TraceSubtree_TraceJob}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-common-trace",
    types={TraceJobGrp, TraceSubtree, types3gpp_model, mf3gpp_model, me3gpp_model, top3gpp_model, types5g3gpp_model, inet_model, subnet3gpp_model, Conf5QIs3gpp_model, eprp3gpp_model, af3gpp_model, amf3gpp_model, ausf3gpp_model, dn3gpp_model, lmf3gpp_model, n3iwf3gpp_model, ngeir3gpp_model, nrf3gpp_model, nssf3gpp_model, pcf3gpp_model, sepp3gpp_model, smf3gpp_model, smsf3gpp_model, udm3gpp_model, upf3gpp_model, yang_model, nfs3gpp_model, nfp3gpp_model, meas3gpp_model, subscr3gpp_model, fm3gpp_model, trace3gpp_model, yangmnt_model},
    associations={},
    generalizations={}
)
