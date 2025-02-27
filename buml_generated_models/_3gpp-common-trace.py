# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
TraceJob = Class(name="TraceJob")

# TraceJob class attributes and methods
TraceJob_tjJobType: Property = Property(name="tjJobType", type=EnumerationType)
TraceJob_tjListOfInterfaces: Property = Property(name="tjListOfInterfaces", type=list)
TraceJob_tjMDTAnonymizationOfData: Property = Property(name="tjMDTAnonymizationOfData", type=EnumerationType)
TraceJob_tjMDTAreaConfigurationForNeighCell: Property = Property(name="tjMDTAreaConfigurationForNeighCell", type=list)
TraceJob_tjMDTCollectionPeriodRrmLte: Property = Property(name="tjMDTCollectionPeriodRrmLte", type=IntegerType)
TraceJob_tjMDTCollectionPeriodRrmNR: Property = Property(name="tjMDTCollectionPeriodRrmNR", type=IntegerType)
TraceJob_tjMDTCollectionPeriodRrmUmts: Property = Property(name="tjMDTCollectionPeriodRrmUmts", type=IntegerType)
TraceJob_tjMDTEventListForTriggeredMeasurement: Property = Property(name="tjMDTEventListForTriggeredMeasurement", type=EnumerationType)
TraceJob_tjMDTEventThreshold: Property = Property(name="tjMDTEventThreshold", type=IntegerType)
TraceJob_tjMDTListOfMeasurements: Property = Property(name="tjMDTListOfMeasurements", type=IntegerType)
TraceJob_tjMDTLoggingDuration: Property = Property(name="tjMDTLoggingDuration", type=IntegerType)
TraceJob_tjMDTLoggingInterval: Property = Property(name="tjMDTLoggingInterval", type=IntegerType)
TraceJob_tjMDTMeasurementPeriodLTE: Property = Property(name="tjMDTMeasurementPeriodLTE", type=IntegerType)
TraceJob_tjMDTMeasurementPeriodUMTS: Property = Property(name="tjMDTMeasurementPeriodUMTS", type=IntegerType)
TraceJob_tjMDTMeasurementQuantity: Property = Property(name="tjMDTMeasurementQuantity", type=IntegerType)
TraceJob_tjMDTPLMList: Property = Property(name="tjMDTPLMList", type=list)
TraceJob_tjMDTPositioningMethod: Property = Property(name="tjMDTPositioningMethod", type=EnumerationType)
TraceJob_tjMDTReportAmount: Property = Property(name="tjMDTReportAmount", type=StringType)
TraceJob_tjMDTReportInterval: Property = Property(name="tjMDTReportInterval", type=IntegerType)
TraceJob_tjMDTReportType: Property = Property(name="tjMDTReportType", type=EnumerationType)
TraceJob_tjMDTReportingTrigger: Property = Property(name="tjMDTReportingTrigger", type=EnumerationType)
TraceJob_tjMDTSensorInformation: Property = Property(name="tjMDTSensorInformation", type=StringType)
TraceJob_tjMDTTraceCollectionEntityID: Property = Property(name="tjMDTTraceCollectionEntityID", type=IntegerType)
TraceJob_tjPLMNTarget: Property = Property(name="tjPLMNTarget", type=StringType)
TraceJob_tjStreamingTraceConsumerURI: Property = Property(name="tjStreamingTraceConsumerURI", type=StringType)
TraceJob_tjTraceCollectionEntityAddress: Property = Property(name="tjTraceCollectionEntityAddress", type=StringType)
TraceJob_tjTraceDepth: Property = Property(name="tjTraceDepth", type=EnumerationType)
TraceJob_tjTraceReference: Property = Property(name="tjTraceReference", type=IntegerType)
TraceJob_tjTraceReportingFormat: Property = Property(name="tjTraceReportingFormat", type=EnumerationType)
TraceJob_tjTraceTarget: Property = Property(name="tjTraceTarget", type=list)
TraceJob_tjTriggeringEvent: Property = Property(name="tjTriggeringEvent", type=StringType)
TraceJob.attributes={TraceJob_tjJobType, TraceJob_tjListOfInterfaces, TraceJob_tjMDTAnonymizationOfData, TraceJob_tjMDTAreaConfigurationForNeighCell, TraceJob_tjMDTCollectionPeriodRrmLte, TraceJob_tjMDTCollectionPeriodRrmNR, TraceJob_tjMDTCollectionPeriodRrmUmts, TraceJob_tjMDTEventListForTriggeredMeasurement, TraceJob_tjMDTEventThreshold, TraceJob_tjMDTListOfMeasurements, TraceJob_tjMDTLoggingDuration, TraceJob_tjMDTLoggingInterval, TraceJob_tjMDTMeasurementPeriodLTE, TraceJob_tjMDTMeasurementPeriodUMTS, TraceJob_tjMDTMeasurementQuantity, TraceJob_tjMDTPLMList, TraceJob_tjMDTPositioningMethod, TraceJob_tjMDTReportAmount, TraceJob_tjMDTReportInterval, TraceJob_tjMDTReportType, TraceJob_tjMDTReportingTrigger, TraceJob_tjMDTSensorInformation, TraceJob_tjMDTTraceCollectionEntityID, TraceJob_tjPLMNTarget, TraceJob_tjStreamingTraceConsumerURI, TraceJob_tjTraceCollectionEntityAddress, TraceJob_tjTraceDepth, TraceJob_tjTraceReference, TraceJob_tjTraceReportingFormat, TraceJob_tjTraceTarget, TraceJob_tjTriggeringEvent}

TraceSubtree = Class(name="TraceSubtree")

# TraceSubtree class attributes and methods
TraceSubtree_TraceJob: Property = Property(name="TraceJob", type=list)
TraceSubtree.attributes={TraceSubtree_TraceJob}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-common-trace",
    types={TraceJob, TraceSubtree},
    associations={},
    generalizations={}
)
