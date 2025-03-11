# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models.ietf_inet_types import domain_model as inet_model
from buml_generated_models._3gpp_common_top import domain_model as top3gpp_model
from buml_generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Enumerations
TjjobtypeEnum = Enumeration(name="TjjobtypeEnum")
TjjobtypeEnum_IMMEDIATE_MDT_AND_TRACE = EnumerationLiteral(name="IMMEDIATE_MDT_AND_TRACE", owner=TjjobtypeEnum)
TjjobtypeEnum_IMMEDIATE_MDT_ONLY = EnumerationLiteral(name="IMMEDIATE_MDT_ONLY", owner=TjjobtypeEnum)
TjjobtypeEnum_LOGGED_MBSFN_MDT = EnumerationLiteral(name="LOGGED_MBSFN_MDT", owner=TjjobtypeEnum)
TjjobtypeEnum_LOGGED_MDT_ONLY = EnumerationLiteral(name="LOGGED_MDT_ONLY", owner=TjjobtypeEnum)
TjjobtypeEnum_RCEF_REPORT_ONLY = EnumerationLiteral(name="RCEF_REPORT_ONLY", owner=TjjobtypeEnum)
TjjobtypeEnum_RLF_REPORT_ONLY = EnumerationLiteral(name="RLF_REPORT_ONLY", owner=TjjobtypeEnum)
TjjobtypeEnum_TRACE_ONLY = EnumerationLiteral(name="TRACE_ONLY", owner=TjjobtypeEnum)
TjjobtypeEnum.literals = {TjjobtypeEnum_IMMEDIATE_MDT_AND_TRACE, TjjobtypeEnum_IMMEDIATE_MDT_ONLY, TjjobtypeEnum_LOGGED_MBSFN_MDT, TjjobtypeEnum_LOGGED_MDT_ONLY, TjjobtypeEnum_RCEF_REPORT_ONLY, TjjobtypeEnum_RLF_REPORT_ONLY, TjjobtypeEnum_TRACE_ONLY}
TjjobtypeEnum.synonyms = ["Specifies the MDT mode and it specifies also whether the TraceJob represents only MDT, Logged MBSFN MDT, Trace or a combined Trace and MDT job. The attribute is applicable for Trace, MDT, RCEF and RLF reporting."]

TjmdtanonymizationofdataEnum = Enumeration(name="TjmdtanonymizationofdataEnum")
TjmdtanonymizationofdataEnum_NO_IDENTITY = EnumerationLiteral(name="NO_IDENTITY", owner=TjmdtanonymizationofdataEnum)
TjmdtanonymizationofdataEnum_TAC_OF_IMEI = EnumerationLiteral(name="TAC_OF_IMEI", owner=TjmdtanonymizationofdataEnum)
TjmdtanonymizationofdataEnum.literals = {TjmdtanonymizationofdataEnum_NO_IDENTITY, TjmdtanonymizationofdataEnum_TAC_OF_IMEI}
TjmdtanonymizationofdataEnum.synonyms = ["Specifies level of MDT anonymization."]

TjmdteventlistfortriggeredmeasurementEnum = Enumeration(name="TjmdteventlistfortriggeredmeasurementEnum")
TjmdteventlistfortriggeredmeasurementEnum_A2_EVENT = EnumerationLiteral(name="A2_EVENT", owner=TjmdteventlistfortriggeredmeasurementEnum)
TjmdteventlistfortriggeredmeasurementEnum_OUT_OF_COVERAGE = EnumerationLiteral(name="OUT_OF_COVERAGE", owner=TjmdteventlistfortriggeredmeasurementEnum)
TjmdteventlistfortriggeredmeasurementEnum.literals = {TjmdteventlistfortriggeredmeasurementEnum_A2_EVENT, TjmdteventlistfortriggeredmeasurementEnum_OUT_OF_COVERAGE}
TjmdteventlistfortriggeredmeasurementEnum.synonyms = ["Specifies event types for event triggered measurement in the case of logged NR MDT. Each trace session may configure at most one event. The UE shall perform logging of measurements only upon certain condition being fulfilled: - Out of coverage. - A2 event."]

TjmdtpositioningmethodEnum = Enumeration(name="TjmdtpositioningmethodEnum")
TjmdtpositioningmethodEnum_E_CELL_ID = EnumerationLiteral(name="E_CELL_ID", owner=TjmdtpositioningmethodEnum)
TjmdtpositioningmethodEnum_GNSS = EnumerationLiteral(name="GNSS", owner=TjmdtpositioningmethodEnum)
TjmdtpositioningmethodEnum.literals = {TjmdtpositioningmethodEnum_E_CELL_ID, TjmdtpositioningmethodEnum_GNSS}
TjmdtpositioningmethodEnum.synonyms = ["It specifies what positioning method should be used in the MDT job."]

TjmdtreportingtriggerEnum = Enumeration(name="TjmdtreportingtriggerEnum")
TjmdtreportingtriggerEnum_1F_FOR_UMTS = EnumerationLiteral(name="1F_FOR_UMTS", owner=TjmdtreportingtriggerEnum)
TjmdtreportingtriggerEnum_1I_FOR_UMTS_MCPS_TDD = EnumerationLiteral(name="1I_FOR_UMTS_MCPS_TDD", owner=TjmdtreportingtriggerEnum)
TjmdtreportingtriggerEnum_A2_FOR_LTE = EnumerationLiteral(name="A2_FOR_LTE", owner=TjmdtreportingtriggerEnum)
TjmdtreportingtriggerEnum_A2_TRIGGERED_PERIODIC_FOR_LTE = EnumerationLiteral(name="A2_TRIGGERED_PERIODIC_FOR_LTE", owner=TjmdtreportingtriggerEnum)
TjmdtreportingtriggerEnum_ALL_CONFIGURED_RRM_FOR_LTE = EnumerationLiteral(name="ALL_CONFIGURED_RRM_FOR_LTE", owner=TjmdtreportingtriggerEnum)
TjmdtreportingtriggerEnum_ALL_CONFIGURED_RRM_FOR_UMTS = EnumerationLiteral(name="ALL_CONFIGURED_RRM_FOR_UMTS", owner=TjmdtreportingtriggerEnum)
TjmdtreportingtriggerEnum_PERIODICAL = EnumerationLiteral(name="PERIODICAL", owner=TjmdtreportingtriggerEnum)
TjmdtreportingtriggerEnum.literals = {TjmdtreportingtriggerEnum_1F_FOR_UMTS, TjmdtreportingtriggerEnum_1I_FOR_UMTS_MCPS_TDD, TjmdtreportingtriggerEnum_A2_FOR_LTE, TjmdtreportingtriggerEnum_A2_TRIGGERED_PERIODIC_FOR_LTE, TjmdtreportingtriggerEnum_ALL_CONFIGURED_RRM_FOR_LTE, TjmdtreportingtriggerEnum_ALL_CONFIGURED_RRM_FOR_UMTS, TjmdtreportingtriggerEnum_PERIODICAL}
TjmdtreportingtriggerEnum.synonyms = ["It specifies whether periodic or event based measurements should be collected. The attribute is applicable only for Immediate MDT and when the tjMDTListOfMeasurements is configured for M1 (for both UMTS and LTE) or M2 (only for UMTS). In case this attribute is not used, it carries a null semantic."]

TjmdtreporttypeEnum = Enumeration(name="TjmdtreporttypeEnum")
TjmdtreporttypeEnum_EVENT_TRIGGERED = EnumerationLiteral(name="EVENT_TRIGGERED", owner=TjmdtreporttypeEnum)
TjmdtreporttypeEnum_PERIODICAL = EnumerationLiteral(name="PERIODICAL", owner=TjmdtreporttypeEnum)
TjmdtreporttypeEnum.literals = {TjmdtreporttypeEnum_EVENT_TRIGGERED, TjmdtreporttypeEnum_PERIODICAL}
TjmdtreporttypeEnum.synonyms = ["It specifies report type for logged NR MDT"]

TjtracedepthEnum = Enumeration(name="TjtracedepthEnum")
TjtracedepthEnum_MAXIMUM = EnumerationLiteral(name="MAXIMUM", owner=TjtracedepthEnum)
TjtracedepthEnum_MEDIUM = EnumerationLiteral(name="MEDIUM", owner=TjtracedepthEnum)
TjtracedepthEnum_MINIMUM = EnumerationLiteral(name="MINIMUM", owner=TjtracedepthEnum)
TjtracedepthEnum_VENDORMAXIMUM = EnumerationLiteral(name="VENDORMAXIMUM", owner=TjtracedepthEnum)
TjtracedepthEnum_VENDORMEDIUM = EnumerationLiteral(name="VENDORMEDIUM", owner=TjtracedepthEnum)
TjtracedepthEnum_VENDORMINIMUM = EnumerationLiteral(name="VENDORMINIMUM", owner=TjtracedepthEnum)
TjtracedepthEnum.literals = {TjtracedepthEnum_MAXIMUM, TjtracedepthEnum_MEDIUM, TjtracedepthEnum_MINIMUM, TjtracedepthEnum_VENDORMAXIMUM, TjtracedepthEnum_VENDORMEDIUM, TjtracedepthEnum_VENDORMINIMUM}
TjtracedepthEnum.synonyms = ["Specifies how detailed information should be recorded in the Network Element. The Trace Depth is a paremeter for Trace Session level, i.e., the Trace Depth is the same for all of the NEs to be traced in the same Trace Session. The attribute is applicable only for Trace, otherwise it carries a null semantic."]

TjtracereportingformatEnum = Enumeration(name="TjtracereportingformatEnum")
TjtracereportingformatEnum_FILE_BASED = EnumerationLiteral(name="FILE_BASED", owner=TjtracereportingformatEnum)
TjtracereportingformatEnum_STREAMING = EnumerationLiteral(name="STREAMING", owner=TjtracereportingformatEnum)
TjtracereportingformatEnum.literals = {TjtracereportingformatEnum_FILE_BASED, TjtracereportingformatEnum_STREAMING}
TjtracereportingformatEnum.synonyms = ["Specifies the trace reporting format - streaming trace reporting or file-based trace reporting"]

# Classes
TraceJob = Class(name="TraceJob")

# TraceJob class attributes and methods
TraceJob_tjJobType: Property = Property(name="tjJobType", type=TjjobtypeEnum, synonyms=["Specifies the MDT mode and it specifies also whether the TraceJob represents only MDT, Logged MBSFN MDT, Trace or a combined Trace and MDT job. The attribute is applicable for Trace, MDT, RCEF and RLF reporting."])
TraceJob_tjListOfInterfaces: Property = Property(name="tjListOfInterfaces", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["Specifies the interfaces that need to be traced in the given ManagedEntityFunction.The attribute is applicable only for Trace. In case this attribute is not used, it carries a null semantic."])
TraceJob_tjMDTAnonymizationOfData: Property = Property(name="tjMDTAnonymizationOfData", type=TjmdtanonymizationofdataEnum, synonyms=["Specifies level of MDT anonymization."])
TraceJob_tjMDTAreaConfigurationForNeighCell: Property = Property(name="tjMDTAreaConfigurationForNeighCell", type=list, multiplicity=Multiplicity(1, "*"), synonyms=["It specifies the area for which UE is requested to perform measurement logging for neighbour cells which have list of frequencies. If it is not configured, the UE shall perform measurement logging for all the neighbour cells. Applicable only to NR Logged MDT."])
TraceJob_tjMDTCollectionPeriodRrmLte: Property = Property(name="tjMDTCollectionPeriodRrmLte", type=IntegerType, synonyms=["Specifies the collection period for collecting RRM configured measurement samples for M2, M3 in LTE. The attribute is applicable only for Immediate MDT. In case this attribute is not used, it carries a null semantic."])
TraceJob_tjMDTCollectionPeriodRrmNR: Property = Property(name="tjMDTCollectionPeriodRrmNR", type=IntegerType, synonyms=["Specifies the collection period for collecting RRM configured measurement samples for M4, M5 in NR. The attribute is applicable only for Immediate MDT. In case this attribute is not used, it carries a null semantic."])
TraceJob_tjMDTCollectionPeriodRrmUmts: Property = Property(name="tjMDTCollectionPeriodRrmUmts", type=IntegerType, synonyms=["Specifies the collection period for collecting RRM configured measurement samples for M3, M4, M5 in UMTS. The attribute is applicable only for Immediate MDT. In case this attribute is not used, it carries a null semantic"])
TraceJob_tjMDTEventListForTriggeredMeasurement: Property = Property(name="tjMDTEventListForTriggeredMeasurement", type=TjmdteventlistfortriggeredmeasurementEnum, synonyms=["Specifies event types for event triggered measurement in the case of logged NR MDT. Each trace session may configure at most one event. The UE shall perform logging of measurements only upon certain condition being fulfilled: - Out of coverage. - A2 event."])
TraceJob_tjMDTEventThreshold: Property = Property(name="tjMDTEventThreshold", type=IntegerType, synonyms=["Specifies the threshold which should trigger the reporting in case A2 event reporting in LTE or 1F/1l event in UMTS. The attribute is applicable only for Immediate MDT and when reportingTrigger is configured for A2 event in LTE or 1F event or 1l event in UMTS. In case this attribute is not used, it carries a null semantic."])
TraceJob_tjMDTListOfMeasurements: Property = Property(name="tjMDTListOfMeasurements", type=IntegerType, synonyms=["It specifies the UE measurements that shall be collected in an Immediate MDT job. The attribute is applicable only for Immediate MDT. In case this attribute is not used, it carries a null semantic."])
TraceJob_tjMDTLoggingDuration: Property = Property(name="tjMDTLoggingDuration", type=IntegerType, synonyms=["Specifies how long the MDT configuration is valid at the UE in case of Logged MDT. The attribute is applicable only for Logged MDT and Logged MBSFN MDT. In case this attribute is not used, it carries a null semantic."])
TraceJob_tjMDTLoggingInterval: Property = Property(name="tjMDTLoggingInterval", type=IntegerType, synonyms=["Specifies the periodicty for Logged MDT. The attribute is applicable only for Logged MDT and Logged MBSFN MDT. In case this attribute is not used, it carries a null semantic"])
TraceJob_tjMDTMeasurementPeriodLTE: Property = Property(name="tjMDTMeasurementPeriodLTE", type=IntegerType, synonyms=["It specifies the measurement period for the Data Volume and Scheduled IP throughput measurements for MDT taken by the eNB. The attribute is applicable only for Immediate MDT. In case this attribute is not used, it carries a null semantic."])
TraceJob_tjMDTMeasurementPeriodUMTS: Property = Property(name="tjMDTMeasurementPeriodUMTS", type=IntegerType, synonyms=["It specifies the measurement period for the Data Volume and Throughput measurements for MDT taken by RNC. The attribute is applicable only for Immediate MDT. In case this attribute is not used, it carries a null semantic."])
TraceJob_tjMDTMeasurementQuantity: Property = Property(name="tjMDTMeasurementQuantity", type=IntegerType, synonyms=["It specifies the measurements that are collected in an MDT job for a UMTS MDT configured for event triggered reporting."])
TraceJob_tjMDTPLMList: Property = Property(name="tjMDTPLMList", type=types3gpp_model.get_type_by_name('PLMNId'), multiplicity=Multiplicity(1, "*"), synonyms=["It indicates the PLMNs where measurement collection, status indication and log reporting is allowed."])
TraceJob_tjMDTPositioningMethod: Property = Property(name="tjMDTPositioningMethod", type=TjmdtpositioningmethodEnum, synonyms=["It specifies what positioning method should be used in the MDT job."])
TraceJob_tjMDTReportAmount: Property = Property(name="tjMDTReportAmount", type=StringType, synonyms=["It specifies the number of measurement reports that shall be taken for periodic reporting while the UE is in connected. The attribute is applicable only for Immediate MDT and when tjMDTReportingTrigger is configured for periodical measurements. In case this attribute is not used, it carries a null semantic."])
TraceJob_tjMDTReportInterval: Property = Property(name="tjMDTReportInterval", type=IntegerType, synonyms=["It specifies the interval between the periodical measurements that shall be taken when the UE is in connected mode. The attribute is applicable only for Immediate MDT and when tjMDTReportingTrigger is configured for periodical measurements. In case this attribute is not used, it carries a null semantic."])
TraceJob_tjMDTReportType: Property = Property(name="tjMDTReportType", type=TjmdtreporttypeEnum, synonyms=["It specifies report type for logged NR MDT"])
TraceJob_tjMDTReportingTrigger: Property = Property(name="tjMDTReportingTrigger", type=TjmdtreportingtriggerEnum, synonyms=["It specifies whether periodic or event based measurements should be collected. The attribute is applicable only for Immediate MDT and when the tjMDTListOfMeasurements is configured for M1 (for both UMTS and LTE) or M2 (only for UMTS). In case this attribute is not used, it carries a null semantic."])
TraceJob_tjMDTSensorInformation: Property = Property(name="tjMDTSensorInformation", type=StringType, synonyms=["It specifies which sensor information shall be included in logged NR MDT and immediate NR MDT measurement if they are available. The following sensor measurement can be included or excluded for the UE."])
TraceJob_tjMDTTraceCollectionEntityID: Property = Property(name="tjMDTTraceCollectionEntityID", type=IntegerType, synonyms=["It specifies the TCE Id which is sent to the UE in Logged MDT."])
TraceJob_tjPLMNTarget: Property = Property(name="tjPLMNTarget", type=StringType, synonyms=["Specifies which PLMN that the subscriber of the session to be recorded uses as selected PLMN. PLMN Target might differ from the PLMN specified in the Trace Reference"])
TraceJob_tjStreamingTraceConsumerURI: Property = Property(name="tjStreamingTraceConsumerURI", type=inet_model.get_type_by_name('uri'), synonyms=["URI of the Streaming Trace data reporting MnS consumer (a.k.a. streaming target). This attribute shall be present if file based trace data reporting is supported and tjTraceReportingFormat set to 'file based' or when tjJobType is set to Logged MDT or Logged MBSFN MDT."])
TraceJob_tjTraceCollectionEntityAddress: Property = Property(name="tjTraceCollectionEntityAddress", type=StringType, synonyms=["Specifies the address of the Trace Collection Entity when the attribute tjTraceReportingFormat is configured for the file-based reporting. The attribute is applicable for both Trace and MDT."])
TraceJob_tjTraceDepth: Property = Property(name="tjTraceDepth", type=TjtracedepthEnum, synonyms=["Specifies how detailed information should be recorded in the Network Element. The Trace Depth is a paremeter for Trace Session level, i.e., the Trace Depth is the same for all of the NEs to be traced in the same Trace Session. The attribute is applicable only for Trace, otherwise it carries a null semantic."])
TraceJob_tjTraceReference: Property = Property(name="tjTraceReference", type=IntegerType, synonyms=["A globally unique identifier, which uniquely identifies the Trace Session that is created by the TraceJob. In case of shared network, it is the MCC and MNC of the Participating Operator that request the trace session that shall be provided. The attribute is applicable for both Trace and MDT."])
TraceJob_tjTraceReportingFormat: Property = Property(name="tjTraceReportingFormat", type=TjtracereportingformatEnum, synonyms=["Specifies the trace reporting format - streaming trace reporting or file-based trace reporting"])
TraceJob_tjTraceTarget: Property = Property(name="tjTraceTarget", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["Specifies the target object of the Trace and MDT. The attribute is applicable for both Trace and MDT. This attribute includes the ID type of the target as an enumeration and the ID value. The tjTraceTarget shall be public ID in case of a Management Based Activation is done to an ScscfFunction. The tjTraceTarget shall be cell only in case of the UTRAN cell traffic trace function. The tjTraceTarget shall be E-UtranCell only in case of E-UTRAN cell traffic trace function.The tjTraceTarget shall be either IMSI or IMEI(SV) if the Trace Session is activated to any of the following ManagedEntity(ies): -	HssFunction -	MscServerFunction -	SgsnFunction -	GgsnFunction -	BmscFunction -	RncFunction -	MmeFunction The tjTraceTarget shall be IMSI if the Trace Session is activated to a ManagedEntity playing a role of ServinGWFunction. In case of signaling based Trace/MDT, the tjTraceTarget attribute shall be able to carry (IMSI or IMEI(SV)or SUPI), the tjMDTAreaScope attribute shall be able to carry a list of (cell or E-UtranCell or NRCellDU or TA/LA/RA). In case of management based Immediate MDT, the tjTraceTarget attribute shall be null value, the tjMDTAreaScope attribute shall carry a list of (Utrancell or E-UtranCell or NRCellDU). In case of management based Logged MDT, the tjTraceTarget attribute shall carry an eBs or a RNC or gNBs. The Logged MDT should be initiated on the specified eNB or RNC or gNB in tjTraceTarget. The tjMDTAreaScope attribute shall carry a list of (Utrancell or E-UtranCell or NRCellDU or TA/LA/RA). In case of RLF reporting, or RCEF reporting, the tjTraceTarget attribute shall be null value, the tjMDTAreaScope attribute shall carry one or list of eNBs/gNBs"])
TraceJob_tjTriggeringEvent: Property = Property(name="tjTriggeringEvent", type=StringType, synonyms=["Specifies the triggering event parameter of the trace session. The attribute is applicable only for Trace. In case this attribute is not used, it carries a null semantic."])
TraceJob.attributes={TraceJob_tjJobType, TraceJob_tjListOfInterfaces, TraceJob_tjMDTAnonymizationOfData, TraceJob_tjMDTAreaConfigurationForNeighCell, TraceJob_tjMDTCollectionPeriodRrmLte, TraceJob_tjMDTCollectionPeriodRrmNR, TraceJob_tjMDTCollectionPeriodRrmUmts, TraceJob_tjMDTEventListForTriggeredMeasurement, TraceJob_tjMDTEventThreshold, TraceJob_tjMDTListOfMeasurements, TraceJob_tjMDTLoggingDuration, TraceJob_tjMDTLoggingInterval, TraceJob_tjMDTMeasurementPeriodLTE, TraceJob_tjMDTMeasurementPeriodUMTS, TraceJob_tjMDTMeasurementQuantity, TraceJob_tjMDTPLMList, TraceJob_tjMDTPositioningMethod, TraceJob_tjMDTReportAmount, TraceJob_tjMDTReportInterval, TraceJob_tjMDTReportType, TraceJob_tjMDTReportingTrigger, TraceJob_tjMDTSensorInformation, TraceJob_tjMDTTraceCollectionEntityID, TraceJob_tjPLMNTarget, TraceJob_tjStreamingTraceConsumerURI, TraceJob_tjTraceCollectionEntityAddress, TraceJob_tjTraceDepth, TraceJob_tjTraceReference, TraceJob_tjTraceReportingFormat, TraceJob_tjTraceTarget, TraceJob_tjTriggeringEvent}

TraceSubtree = Class(name="TraceSubtree", synonyms=["Contains classes that manage Tracing. Should be used in all classes (or classes inheriting from) - SubNnetwork - ManagedElement - ManagedFunction If a YANG module wants to augment these classes/list/groupings they must augment all user classes!"])

# TraceSubtree class attributes and methods
TraceSubtree_TraceJob: Property = Property(name="TraceJob", type=top3gpp_model.get_type_by_name('Top_Grp'), multiplicity=Multiplicity(0, "*"), synonyms=["Represents the Trace Control and Configuration parameters of a particular Trace Job (see TS 32.421 and TS 32.422 for details). To activate Trace Jobs, a MnS consumer has to create TraceJob object instances on the MnS producer. A MnS consumer can activate a Trace Job for another MnS consumer since it is not required the value of tjTraceCollectionEntityAddress or tjStreamingTraceConsumerUri to be his own. When a MnS consumer wishes to deactivate a Trace Job, the MnS consumer shall delete the corresponding TraceJob instance. For details of management Trace Job activation/deactivation see clause 4.1.1.1.2 of TS 32.422. Creation and deletion of TraceJob instances by MnS consumers is optional; when not supported, the TraceJob instances may be created and deleted by the system or be pre-installed."])
TraceSubtree.attributes={TraceSubtree_TraceJob}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-common-trace",
    types={TjjobtypeEnum, TjmdtanonymizationofdataEnum, TjmdteventlistfortriggeredmeasurementEnum, TjmdtpositioningmethodEnum, TjmdtreportingtriggerEnum, TjmdtreporttypeEnum, TjtracedepthEnum, TjtracereportingformatEnum, TraceJob, TraceSubtree},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Trace handling"]
