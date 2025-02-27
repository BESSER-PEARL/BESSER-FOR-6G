# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models._3gpp_common_top import domain_model as top3gpp_model
from buml_generated_models._3gpp_common_yang_types import domain_model as types3gpp_model
from buml_generated_models.ietf_yang_types import domain_model as yang_model

# Enumerations
eventType = Enumeration(name="eventType")
eventType_COMMUNICATIONS_ALARM = EnumerationLiteral(name="COMMUNICATIONS_ALARM", owner=eventType)
eventType_ENVIRONMENTAL_ALARM = EnumerationLiteral(name="ENVIRONMENTAL_ALARM", owner=eventType)
eventType_EQUIPMENT_ALARM = EnumerationLiteral(name="EQUIPMENT_ALARM", owner=eventType)
eventType_INTEGRITY_VIOLATION = EnumerationLiteral(name="INTEGRITY_VIOLATION", owner=eventType)
eventType_OPERATIONAL_VIOLATION = EnumerationLiteral(name="OPERATIONAL_VIOLATION", owner=eventType)
eventType_PHYSICAL_VIOLATIONu = EnumerationLiteral(name="PHYSICAL_VIOLATIONu", owner=eventType)
eventType_PROCESSING_ERROR_ALARM = EnumerationLiteral(name="PROCESSING_ERROR_ALARM", owner=eventType)
eventType_QUALITY_OF_SERVICE_ALARM = EnumerationLiteral(name="QUALITY_OF_SERVICE_ALARM", owner=eventType)
eventType_SECURITY_SERVICE_OR_MECHANISM_VIOLATION = EnumerationLiteral(name="SECURITY_SERVICE_OR_MECHANISM_VIOLATION", owner=eventType)
eventType_TIME_DOMAIN_VIOLATION = EnumerationLiteral(name="TIME_DOMAIN_VIOLATION", owner=eventType)
eventType.literals = {eventType_COMMUNICATIONS_ALARM, eventType_ENVIRONMENTAL_ALARM, eventType_EQUIPMENT_ALARM, eventType_INTEGRITY_VIOLATION, eventType_OPERATIONAL_VIOLATION, eventType_PHYSICAL_VIOLATIONu, eventType_PROCESSING_ERROR_ALARM, eventType_QUALITY_OF_SERVICE_ALARM, eventType_SECURITY_SERVICE_OR_MECHANISM_VIOLATION, eventType_TIME_DOMAIN_VIOLATION}
eventType.synonyms = ["General category for the alarm."]

severity_level = Enumeration(name="severity_level")
severity_level_CLEARED = EnumerationLiteral(name="CLEARED", owner=severity_level)
severity_level_CRITICAL = EnumerationLiteral(name="CRITICAL", owner=severity_level)
severity_level_INDETERMINATE = EnumerationLiteral(name="INDETERMINATE", owner=severity_level)
severity_level_MAJOR = EnumerationLiteral(name="MAJOR", owner=severity_level)
severity_level_MINOR = EnumerationLiteral(name="MINOR", owner=severity_level)
severity_level_WARNING = EnumerationLiteral(name="WARNING", owner=severity_level)
severity_level.literals = {severity_level_CLEARED, severity_level_CRITICAL, severity_level_INDETERMINATE, severity_level_MAJOR, severity_level_MINOR, severity_level_WARNING}
severity_level.synonyms = ["The possible alarm serverities. 	Aligned with ERICSSON-ALARM-MIB."]

# Classes
AlarmList = Class(name="AlarmList", synonyms=["Represents the AlarmList IOC."])

# AlarmList class attributes and methods
AlarmList_administrativeState: Property = Property(name="administrativeState", type=types3gpp_model.get_type_by_name('AdministrativeState'), synonyms=["When set to UNLOCKED, the alarm list is updated. When the set to LOCKED, the existing alarm records are not updated, and new alarm records are not added to the alarm list."])
AlarmList_alarmRecords: Property = Property(name="alarmRecords", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["List of alarmRecords"])
AlarmList_lastModification: Property = Property(name="lastModification", type=yang_model.get_type_by_name('date_and_time'), synonyms=["The last time when an alarm record was modified"])
AlarmList_numOfAlarmRecords: Property = Property(name="numOfAlarmRecords", type=IntegerType, synonyms=["The number of alarm records in the AlarmList"])
AlarmList_operationalState: Property = Property(name="operationalState", type=types3gpp_model.get_type_by_name('OperationalState'), synonyms=["The producer sets this attribute to ENABLED, indicating that it has the resource and ability to record alarm in AlarmList else, it sets the attribute to DISABLED."])
AlarmList.attributes={AlarmList_administrativeState, AlarmList_alarmRecords, AlarmList_lastModification, AlarmList_numOfAlarmRecords, AlarmList_operationalState}

AlarmRecord = Class(name="AlarmRecord", synonyms=["Contains alarm information of an alarmed object instance. A new record is created in the alarm list when an alarmed object instance generates an alarm and no alarm record exists with the same values for objectInstance, alarmType, probableCause and specificProblem. When a new record is created the MnS producer creates an alarmId, that unambiguously identifies an alarm record in the AlarmList. Alarm records are maintained only for active alarms. Inactive alarms are automatically deleted by the MnS producer from the AlarmList. Active alarms are alarms whose a)	perceivedSeverity is not CLEARED, or whose b)	perceivedSeverity is CLEARED and its ackState is not ACKNOWLEDED."])

# AlarmRecord class attributes and methods
AlarmRecord_ackState: Property = Property(name="ackState", type=EnumerationType)
AlarmRecord_ackSystemId: Property = Property(name="ackSystemId", type=StringType, synonyms=["It identifies the system (Management System) that last changed the ackState of an alarm, i.e. acknowledged or unacknowledged the alarm."])
AlarmRecord_ackTime: Property = Property(name="ackTime", type=yang_model.get_type_by_name('date_and_time'), synonyms=["It identifies the time when the alarm has been acknowledged or unacknowledged the last time, i.e. it registers the time when ackState changes."])
AlarmRecord_ackUserId: Property = Property(name="ackUserId", type=StringType, synonyms=["It identifies the last user who has changed the Acknowledgement State."])
AlarmRecord_additionalInformation: Property = Property(name="additionalInformation", type=StringType)
AlarmRecord_additionalText: Property = Property(name="additionalText", type=StringType)
AlarmRecord_alarmChangedTime: Property = Property(name="alarmChangedTime", type=yang_model.get_type_by_name('date_and_time'), synonyms=["not applicable if related alarm has not changed"])
AlarmRecord_alarmClearedTime: Property = Property(name="alarmClearedTime", type=yang_model.get_type_by_name('date_and_time'), synonyms=["not applicable if related alarm was not cleared"])
AlarmRecord_alarmId: Property = Property(name="alarmId", type=StringType, synonyms=["Identifies the alarmRecord"])
AlarmRecord_alarmRaisedTime: Property = Property(name="alarmRaisedTime", type=yang_model.get_type_by_name('date_and_time'))
AlarmRecord_alarmType: Property = Property(name="alarmType", type=StringType, synonyms=["General category for the alarm."])
AlarmRecord_backUpObject: Property = Property(name="backUpObject", type=StringType)
AlarmRecord_backedUpStatus: Property = Property(name="backedUpStatus", type=StringType, synonyms=["Indicates if an object (the MonitoredEntity) has a back up. See definition in ITU-T Recommendation X.733 clause 8.1.2.4."])
AlarmRecord_clearSystemId: Property = Property(name="clearSystemId", type=StringType)
AlarmRecord_clearUserId: Property = Property(name="clearUserId", type=StringType, synonyms=["Carries the identity of the user who invokes the clearAlarms operation."])
AlarmRecord_monitoredAttributes: Property = Property(name="monitoredAttributes", type=StringType, synonyms=["Indicates MO attributes whose value changes are being monitored. See definition in ITU-T Recommendation X.733 clause 8.1.2.11."])
AlarmRecord_notificationId: Property = Property(name="notificationId", type=StringType)
AlarmRecord_objectInstance: Property = Property(name="objectInstance", type=StringType)
AlarmRecord_perceivedSeverity: Property = Property(name="perceivedSeverity", type=StringType, synonyms=["This is Writable only if producer supports consumer to set perceivedSeverity to CLEARED"])
AlarmRecord_probableCause: Property = Property(name="probableCause", type=StringType)
AlarmRecord_proposedRepairActions: Property = Property(name="proposedRepairActions", type=StringType, synonyms=["Indicates proposed repair actions. See definition in ITU-T Recommendation X.733 clause 8.1.2.12."])
AlarmRecord_rootCauseIndicator: Property = Property(name="rootCauseIndicator", type=EnumerationType, synonyms=["It indicates that this AlarmInformation is the root cause of the events captured by the notifications whose identifiers are in the related CorrelatedNotification instances."])
AlarmRecord_securityAlarmDetector: Property = Property(name="securityAlarmDetector", type=StringType)
AlarmRecord_serviceProvider: Property = Property(name="serviceProvider", type=StringType, synonyms=["It identifies the service-provider whose service is requested by the serviceUser and the service request provokes the generation of the security alarm."])
AlarmRecord_serviceUser: Property = Property(name="serviceUser", type=StringType, synonyms=["It identifies the service-user whose request for service provided by the serviceProvider led to the generation of the security alarm."])
AlarmRecord_specificProblem: Property = Property(name="specificProblem", type=StringType)
AlarmRecord_stateChangeDefinition: Property = Property(name="stateChangeDefinition", type=StringType, synonyms=["Indicates MO attribute value changes. See definition in ITU-T Recommendation X.733 clause 8.1.2.11."])
AlarmRecord_thresholdInfo: Property = Property(name="thresholdInfo", type=list, multiplicity=Multiplicity(0, "*"))
AlarmRecord_trendIndication: Property = Property(name="trendIndication", type=StringType, synonyms=["Indicates if some observed condition is getting better, worse, or not changing."])
AlarmRecord.attributes={AlarmRecord_ackState, AlarmRecord_ackSystemId, AlarmRecord_ackTime, AlarmRecord_ackUserId, AlarmRecord_additionalInformation, AlarmRecord_additionalText, AlarmRecord_alarmChangedTime, AlarmRecord_alarmClearedTime, AlarmRecord_alarmId, AlarmRecord_alarmRaisedTime, AlarmRecord_alarmType, AlarmRecord_backUpObject, AlarmRecord_backedUpStatus, AlarmRecord_clearSystemId, AlarmRecord_clearUserId, AlarmRecord_monitoredAttributes, AlarmRecord_notificationId, AlarmRecord_objectInstance, AlarmRecord_perceivedSeverity, AlarmRecord_probableCause, AlarmRecord_proposedRepairActions, AlarmRecord_rootCauseIndicator, AlarmRecord_securityAlarmDetector, AlarmRecord_serviceProvider, AlarmRecord_serviceUser, AlarmRecord_specificProblem, AlarmRecord_stateChangeDefinition, AlarmRecord_thresholdInfo, AlarmRecord_trendIndication}

FmSubtree = Class(name="FmSubtree", synonyms=["Contains FM related classes. Should be used in all classes (or classes inheriting from) - SubNetwork - ManagedElement If some YAM wants to augment these classes/list/groupings they must augment all user classes!"])

# FmSubtree class attributes and methods
FmSubtree_AlarmList: Property = Property(name="AlarmList", type=top3gpp_model.get_type_by_name('Top_Grp'), multiplicity=Multiplicity(0, "*"), synonyms=["The AlarmList represents the capability to store and manage alarm records. The management scope of an AlarmList is defined by all descendant objects of the base managed object, which is the object name-containing the AlarmList, and the base object itself. AlarmList instances are created by the system or are pre-installed. They cannot be created nor deleted by MnS consumers. When the alarm list is locked or disabled, the existing alarm records are not updated, and new alarm records are not added to the alarm list"])
FmSubtree.attributes={FmSubtree_AlarmList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-common-fm",
    types={AlarmList, AlarmRecord, FmSubtree, eventType, severity_level},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines a Fault Management model"]
