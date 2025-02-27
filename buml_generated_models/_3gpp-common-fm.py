# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

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

severity-level = Enumeration(name="severity-level")
severity-level_CLEARED = EnumerationLiteral(name="CLEARED", owner=severity-level)
severity-level_CRITICAL = EnumerationLiteral(name="CRITICAL", owner=severity-level)
severity-level_INDETERMINATE = EnumerationLiteral(name="INDETERMINATE", owner=severity-level)
severity-level_MAJOR = EnumerationLiteral(name="MAJOR", owner=severity-level)
severity-level_MINOR = EnumerationLiteral(name="MINOR", owner=severity-level)
severity-level_WARNING = EnumerationLiteral(name="WARNING", owner=severity-level)
severity-level.literals = {severity-level_CLEARED, severity-level_CRITICAL, severity-level_INDETERMINATE, severity-level_MAJOR, severity-level_MINOR, severity-level_WARNING}

# Classes
AlarmList = Class(name="AlarmList")

# AlarmList class attributes and methods
AlarmList_administrativeState: Property = Property(name="administrativeState", type=StringType)
AlarmList_alarmRecords: Property = Property(name="alarmRecords", type=list)
AlarmList_lastModification: Property = Property(name="lastModification", type=StringType)
AlarmList_numOfAlarmRecords: Property = Property(name="numOfAlarmRecords", type=IntegerType)
AlarmList_operationalState: Property = Property(name="operationalState", type=StringType)
AlarmList.attributes={AlarmList_administrativeState, AlarmList_alarmRecords, AlarmList_lastModification, AlarmList_numOfAlarmRecords, AlarmList_operationalState}

AlarmRecord = Class(name="AlarmRecord")

# AlarmRecord class attributes and methods
AlarmRecord_ackState: Property = Property(name="ackState", type=EnumerationType)
AlarmRecord_ackSystemId: Property = Property(name="ackSystemId", type=StringType)
AlarmRecord_ackTime: Property = Property(name="ackTime", type=StringType)
AlarmRecord_ackUserId: Property = Property(name="ackUserId", type=StringType)
AlarmRecord_additionalInformation: Property = Property(name="additionalInformation", type=StringType)
AlarmRecord_additionalText: Property = Property(name="additionalText", type=StringType)
AlarmRecord_alarmChangedTime: Property = Property(name="alarmChangedTime", type=StringType)
AlarmRecord_alarmClearedTime: Property = Property(name="alarmClearedTime", type=StringType)
AlarmRecord_alarmId: Property = Property(name="alarmId", type=StringType)
AlarmRecord_alarmRaisedTime: Property = Property(name="alarmRaisedTime", type=StringType)
AlarmRecord_alarmType: Property = Property(name="alarmType", type=StringType)
AlarmRecord_backUpObject: Property = Property(name="backUpObject", type=StringType)
AlarmRecord_backedUpStatus: Property = Property(name="backedUpStatus", type=StringType)
AlarmRecord_clearSystemId: Property = Property(name="clearSystemId", type=StringType)
AlarmRecord_clearUserId: Property = Property(name="clearUserId", type=StringType)
AlarmRecord_monitoredAttributes: Property = Property(name="monitoredAttributes", type=StringType)
AlarmRecord_notificationId: Property = Property(name="notificationId", type=StringType)
AlarmRecord_objectInstance: Property = Property(name="objectInstance", type=StringType)
AlarmRecord_perceivedSeverity: Property = Property(name="perceivedSeverity", type=StringType)
AlarmRecord_probableCause: Property = Property(name="probableCause", type=StringType)
AlarmRecord_proposedRepairActions: Property = Property(name="proposedRepairActions", type=StringType)
AlarmRecord_rootCauseIndicator: Property = Property(name="rootCauseIndicator", type=EnumerationType)
AlarmRecord_securityAlarmDetector: Property = Property(name="securityAlarmDetector", type=StringType)
AlarmRecord_serviceProvider: Property = Property(name="serviceProvider", type=StringType)
AlarmRecord_serviceUser: Property = Property(name="serviceUser", type=StringType)
AlarmRecord_specificProblem: Property = Property(name="specificProblem", type=StringType)
AlarmRecord_stateChangeDefinition: Property = Property(name="stateChangeDefinition", type=StringType)
AlarmRecord_thresholdInfo: Property = Property(name="thresholdInfo", type=list)
AlarmRecord_trendIndication: Property = Property(name="trendIndication", type=StringType)
AlarmRecord.attributes={AlarmRecord_ackState, AlarmRecord_ackSystemId, AlarmRecord_ackTime, AlarmRecord_ackUserId, AlarmRecord_additionalInformation, AlarmRecord_additionalText, AlarmRecord_alarmChangedTime, AlarmRecord_alarmClearedTime, AlarmRecord_alarmId, AlarmRecord_alarmRaisedTime, AlarmRecord_alarmType, AlarmRecord_backUpObject, AlarmRecord_backedUpStatus, AlarmRecord_clearSystemId, AlarmRecord_clearUserId, AlarmRecord_monitoredAttributes, AlarmRecord_notificationId, AlarmRecord_objectInstance, AlarmRecord_perceivedSeverity, AlarmRecord_probableCause, AlarmRecord_proposedRepairActions, AlarmRecord_rootCauseIndicator, AlarmRecord_securityAlarmDetector, AlarmRecord_serviceProvider, AlarmRecord_serviceUser, AlarmRecord_specificProblem, AlarmRecord_stateChangeDefinition, AlarmRecord_thresholdInfo, AlarmRecord_trendIndication}

FmSubtree = Class(name="FmSubtree")

# FmSubtree class attributes and methods
FmSubtree_AlarmList: Property = Property(name="AlarmList", type=list)
FmSubtree.attributes={FmSubtree_AlarmList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-common-fm",
    types={AlarmList, AlarmRecord, FmSubtree, eventType, severity-level},
    associations={},
    generalizations={}
)
