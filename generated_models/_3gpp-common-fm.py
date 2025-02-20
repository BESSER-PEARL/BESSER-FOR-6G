# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
AlarmRecord = Class(name="AlarmRecord")

# AlarmRecord class attributes and methods
AlarmRecord_alarmId: Property = Property(name="alarmId", type=StringType)
AlarmRecord_objectInstance: Property = Property(name="objectInstance", type=StringType)
AlarmRecord_notificationId: Property = Property(name="notificationId", type=StringType)
AlarmRecord_alarmRaisedTime: Property = Property(name="alarmRaisedTime", type=yang:date-and-time)
AlarmRecord_alarmChangedTime: Property = Property(name="alarmChangedTime", type=yang:date-and-time)
AlarmRecord_alarmClearedTime: Property = Property(name="alarmClearedTime", type=yang:date-and-time)
AlarmRecord_alarmType: Property = Property(name="alarmType", type=eventType)
AlarmRecord_probableCause: Property = Property(name="probableCause", type=StringType)
AlarmRecord_specificProblem: Property = Property(name="specificProblem", type=StringType)
AlarmRecord_perceivedSeverity: Property = Property(name="perceivedSeverity", type=severity-level)
AlarmRecord_backedUpStatus: Property = Property(name="backedUpStatus", type=StringType)
AlarmRecord_backUpObject: Property = Property(name="backUpObject", type=StringType)
AlarmRecord_trendIndication: Property = Property(name="trendIndication", type=StringType)
AlarmRecord_stateChangeDefinition: Property = Property(name="stateChangeDefinition", type=StringType)
AlarmRecord_monitoredAttributes: Property = Property(name="monitoredAttributes", type=StringType)
AlarmRecord_proposedRepairActions: Property = Property(name="proposedRepairActions", type=StringType)
AlarmRecord_additionalText: Property = Property(name="additionalText", type=StringType)
AlarmRecord_additionalInformation: Property = Property(name="additionalInformation", type=StringType)
AlarmRecord_rootCauseIndicator: Property = Property(name="rootCauseIndicator", type=enumeration)
AlarmRecord_ackTime: Property = Property(name="ackTime", type=yang:date-and-time)
AlarmRecord_ackUserId: Property = Property(name="ackUserId", type=StringType)
AlarmRecord_ackSystemId: Property = Property(name="ackSystemId", type=StringType)
AlarmRecord_ackState: Property = Property(name="ackState", type=enumeration)
AlarmRecord_clearUserId: Property = Property(name="clearUserId", type=StringType)
AlarmRecord_clearSystemId: Property = Property(name="clearSystemId", type=StringType)
AlarmRecord_serviceUser: Property = Property(name="serviceUser", type=StringType)
AlarmRecord_serviceProvider: Property = Property(name="serviceProvider", type=StringType)
AlarmRecord_securityAlarmDetector: Property = Property(name="securityAlarmDetector", type=StringType)
AlarmRecord_thresholdInfo: Property = Property(name="thresholdInfo", type=list)
AlarmRecord.attributes={AlarmRecord_alarmId, AlarmRecord_objectInstance, AlarmRecord_notificationId, AlarmRecord_alarmRaisedTime, AlarmRecord_alarmChangedTime, AlarmRecord_alarmClearedTime, AlarmRecord_alarmType, AlarmRecord_probableCause, AlarmRecord_specificProblem, AlarmRecord_perceivedSeverity, AlarmRecord_backedUpStatus, AlarmRecord_backUpObject, AlarmRecord_trendIndication, AlarmRecord_stateChangeDefinition, AlarmRecord_monitoredAttributes, AlarmRecord_proposedRepairActions, AlarmRecord_additionalText, AlarmRecord_additionalInformation, AlarmRecord_rootCauseIndicator, AlarmRecord_ackTime, AlarmRecord_ackUserId, AlarmRecord_ackSystemId, AlarmRecord_ackState, AlarmRecord_clearUserId, AlarmRecord_clearSystemId, AlarmRecord_serviceUser, AlarmRecord_serviceProvider, AlarmRecord_securityAlarmDetector, AlarmRecord_thresholdInfo}

AlarmList = Class(name="AlarmList")

# AlarmList class attributes and methods
AlarmList_administrativeState: Property = Property(name="administrativeState", type=types3gpp:AdministrativeState)
AlarmList_operationalState: Property = Property(name="operationalState", type=types3gpp:OperationalState)
AlarmList_numOfAlarmRecords: Property = Property(name="numOfAlarmRecords", type=IntegerType)
AlarmList_lastModification: Property = Property(name="lastModification", type=yang:date-and-time)
AlarmList_alarmRecords: Property = Property(name="alarmRecords", type=list)
AlarmList.attributes={AlarmList_administrativeState, AlarmList_operationalState, AlarmList_numOfAlarmRecords, AlarmList_lastModification, AlarmList_alarmRecords}

FmSubtree = Class(name="FmSubtree")

# FmSubtree class attributes and methods
FmSubtree_AlarmList: Property = Property(name="AlarmList", type=list)
FmSubtree.attributes={FmSubtree_AlarmList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-common-fm",
    types={AlarmRecord, AlarmList, FmSubtree},
    associations={},
    generalizations={}
)
