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
from generated_models._3gpp_common_measurements import domain_model as meas3gpp_model
from generated_models._3gpp_common_subnetwork import domain_model as subnet3gpp_model
from generated_models._3gpp_common_top import domain_model as top3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Enumerations
eventType: Enumeration = Enumeration(
    name="eventType",
    literals={
            EnumerationLiteral(name="COMMUNICATIONS_ALARM"),
			EnumerationLiteral(name="QUALITY_OF_SERVICE_ALARM"),
			EnumerationLiteral(name="PROCESSING_ERROR_ALARM"),
			EnumerationLiteral(name="EQUIPMENT_ALARM"),
			EnumerationLiteral(name="ENVIRONMENTAL_ALARM"),
			EnumerationLiteral(name="INTEGRITY_VIOLATION"),
			EnumerationLiteral(name="OPERATIONAL_VIOLATION"),
			EnumerationLiteral(name="PHYSICAL_VIOLATIONu"),
			EnumerationLiteral(name="SECURITY_SERVICE_OR_MECHANISM_VIOLATION"),
			EnumerationLiteral(name="TIME_DOMAIN_VIOLATION")
    }
)

severity-level: Enumeration = Enumeration(
    name="severity-level",
    literals={
            EnumerationLiteral(name="CRITICAL"),
			EnumerationLiteral(name="MAJOR"),
			EnumerationLiteral(name="MINOR"),
			EnumerationLiteral(name="WARNING"),
			EnumerationLiteral(name="INDETERMINATE"),
			EnumerationLiteral(name="CLEARED")
    }
)

# Classes
AlarmRecordGrp = Class(name="AlarmRecordGrp")
AlarmListGrp = Class(name="AlarmListGrp")
FmSubtree = Class(name="FmSubtree")

# AlarmRecordGrp class attributes and methods
AlarmRecordGrp_alarmId: Property = Property(name="alarmId", type=StringType)
AlarmRecordGrp_objectInstance: Property = Property(name="objectInstance", type=StringType)
AlarmRecordGrp_notificationId: Property = Property(name="notificationId", type=StringType)
AlarmRecordGrp_alarmRaisedTime: Property = Property(name="alarmRaisedTime", type=yang:date-and-time)
AlarmRecordGrp_alarmChangedTime: Property = Property(name="alarmChangedTime", type=yang:date-and-time)
AlarmRecordGrp_alarmClearedTime: Property = Property(name="alarmClearedTime", type=yang:date-and-time)
AlarmRecordGrp_alarmType: Property = Property(name="alarmType", type=eventType)
AlarmRecordGrp_probableCause: Property = Property(name="probableCause", type=StringType)
AlarmRecordGrp_specificProblem: Property = Property(name="specificProblem", type=StringType)
AlarmRecordGrp_perceivedSeverity: Property = Property(name="perceivedSeverity", type=severity-level)
AlarmRecordGrp_backedUpStatus: Property = Property(name="backedUpStatus", type=StringType)
AlarmRecordGrp_backUpObject: Property = Property(name="backUpObject", type=StringType)
AlarmRecordGrp_trendIndication: Property = Property(name="trendIndication", type=StringType)
AlarmRecordGrp_stateChangeDefinition: Property = Property(name="stateChangeDefinition", type=StringType)
AlarmRecordGrp_monitoredAttributes: Property = Property(name="monitoredAttributes", type=StringType)
AlarmRecordGrp_proposedRepairActions: Property = Property(name="proposedRepairActions", type=StringType)
AlarmRecordGrp_additionalText: Property = Property(name="additionalText", type=StringType)
AlarmRecordGrp_additionalInformation: Property = Property(name="additionalInformation", type=StringType)
AlarmRecordGrp_rootCauseIndicator: Property = Property(name="rootCauseIndicator", type=enumeration)
AlarmRecordGrp_ackTime: Property = Property(name="ackTime", type=yang:date-and-time)
AlarmRecordGrp_ackUserId: Property = Property(name="ackUserId", type=StringType)
AlarmRecordGrp_ackSystemId: Property = Property(name="ackSystemId", type=StringType)
AlarmRecordGrp_ackState: Property = Property(name="ackState", type=enumeration)
AlarmRecordGrp_clearUserId: Property = Property(name="clearUserId", type=StringType)
AlarmRecordGrp_clearSystemId: Property = Property(name="clearSystemId", type=StringType)
AlarmRecordGrp_serviceUser: Property = Property(name="serviceUser", type=StringType)
AlarmRecordGrp_serviceProvider: Property = Property(name="serviceProvider", type=StringType)
AlarmRecordGrp_securityAlarmDetector: Property = Property(name="securityAlarmDetector", type=StringType)
AlarmRecordGrp_thresholdInfo: Property = Property(name="thresholdInfo", type=list)
AlarmRecordGrp.attributes={AlarmRecordGrp_thresholdInfo, AlarmRecordGrp_probableCause, AlarmRecordGrp_specificProblem, AlarmRecordGrp_perceivedSeverity, AlarmRecordGrp_backedUpStatus, AlarmRecordGrp_backUpObject, AlarmRecordGrp_trendIndication, AlarmRecordGrp_stateChangeDefinition, AlarmRecordGrp_monitoredAttributes, AlarmRecordGrp_proposedRepairActions, AlarmRecordGrp_additionalText, AlarmRecordGrp_additionalInformation, AlarmRecordGrp_rootCauseIndicator, AlarmRecordGrp_ackTime, AlarmRecordGrp_ackUserId, AlarmRecordGrp_alarmId, AlarmRecordGrp_ackSystemId, AlarmRecordGrp_ackState, AlarmRecordGrp_objectInstance, AlarmRecordGrp_clearUserId, AlarmRecordGrp_notificationId, AlarmRecordGrp_clearSystemId, AlarmRecordGrp_alarmRaisedTime, AlarmRecordGrp_serviceUser, AlarmRecordGrp_alarmChangedTime, AlarmRecordGrp_serviceProvider, AlarmRecordGrp_alarmClearedTime, AlarmRecordGrp_securityAlarmDetector, AlarmRecordGrp_alarmType}

# AlarmListGrp class attributes and methods
AlarmListGrp_administrativeState: Property = Property(name="administrativeState", type=types3gpp:AdministrativeState)
AlarmListGrp_operationalState: Property = Property(name="operationalState", type=types3gpp:OperationalState)
AlarmListGrp_numOfAlarmRecords: Property = Property(name="numOfAlarmRecords", type=IntegerType)
AlarmListGrp_lastModification: Property = Property(name="lastModification", type=yang:date-and-time)
AlarmListGrp_alarmRecords: Property = Property(name="alarmRecords", type=list)
AlarmListGrp.attributes={AlarmListGrp_alarmRecords, AlarmListGrp_administrativeState, AlarmListGrp_operationalState, AlarmListGrp_numOfAlarmRecords, AlarmListGrp_lastModification}

# FmSubtree class attributes and methods
FmSubtree_AlarmList: Property = Property(name="AlarmList", type=list)
FmSubtree.attributes={FmSubtree_AlarmList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-common-fm",
    types={AlarmRecordGrp, AlarmListGrp, FmSubtree, eventType, severity-level, types3gpp_model, mf3gpp_model, me3gpp_model, top3gpp_model, types5g3gpp_model, inet_model, subnet3gpp_model, Conf5QIs3gpp_model, eprp3gpp_model, af3gpp_model, amf3gpp_model, ausf3gpp_model, dn3gpp_model, lmf3gpp_model, n3iwf3gpp_model, ngeir3gpp_model, nrf3gpp_model, nssf3gpp_model, pcf3gpp_model, sepp3gpp_model, smf3gpp_model, smsf3gpp_model, udm3gpp_model, upf3gpp_model, yang_model, nfs3gpp_model, nfp3gpp_model, meas3gpp_model},
    associations={},
    generalizations={}
)
