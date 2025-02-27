# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
ARP = Class(name="ARP")

# ARP class attributes and methods
ARP_preemptCap: Property = Property(name="preemptCap", type=EnumerationType)
ARP_preemptVuln: Property = Property(name="preemptVuln", type=EnumerationType)
ARP_priorityLevel: Property = Property(name="priorityLevel", type=IntegerType)
ARP.attributes={ARP_preemptCap, ARP_preemptVuln, ARP_priorityLevel}

ConditionData = Class(name="ConditionData")

# ConditionData class attributes and methods
ConditionData_accessType: Property = Property(name="accessType", type=EnumerationType)
ConditionData_activationTime: Property = Property(name="activationTime", type=StringType)
ConditionData_condId: Property = Property(name="condId", type=StringType)
ConditionData_deactivationTime: Property = Property(name="deactivationTime", type=StringType)
ConditionData_ratType: Property = Property(name="ratType", type=EnumerationType)
ConditionData.attributes={ConditionData_accessType, ConditionData_activationTime, ConditionData_condId, ConditionData_deactivationTime, ConditionData_ratType}

EthFlowDescription = Class(name="EthFlowDescription")

# EthFlowDescription class attributes and methods
EthFlowDescription_destMacAddr: Property = Property(name="destMacAddr", type=StringType)
EthFlowDescription_destMacAddrEnd: Property = Property(name="destMacAddrEnd", type=StringType)
EthFlowDescription_ethType: Property = Property(name="ethType", type=StringType)
EthFlowDescription_fDesc: Property = Property(name="fDesc", type=StringType)
EthFlowDescription_fDir: Property = Property(name="fDir", type=EnumerationType)
EthFlowDescription_sourceMacAddr: Property = Property(name="sourceMacAddr", type=StringType)
EthFlowDescription_srcMacAddrEnd: Property = Property(name="srcMacAddrEnd", type=StringType)
EthFlowDescription.attributes={EthFlowDescription_destMacAddr, EthFlowDescription_destMacAddrEnd, EthFlowDescription_ethType, EthFlowDescription_fDesc, EthFlowDescription_fDir, EthFlowDescription_sourceMacAddr, EthFlowDescription_srcMacAddrEnd}

FlowInformation = Class(name="FlowInformation")

# FlowInformation class attributes and methods
FlowInformation_flowDescription: Property = Property(name="flowDescription", type=StringType)
FlowInformation_flowDirection: Property = Property(name="flowDirection", type=EnumerationType)
FlowInformation_flowLabel: Property = Property(name="flowLabel", type=StringType)
FlowInformation_packFiltId: Property = Property(name="packFiltId", type=StringType)
FlowInformation_packetFilterUsage: Property = Property(name="packetFilterUsage", type=BooleanType)
FlowInformation_spi: Property = Property(name="spi", type=StringType)
FlowInformation_tosTrafficClass: Property = Property(name="tosTrafficClass", type=StringType)
FlowInformation.attributes={FlowInformation_flowDescription, FlowInformation_flowDirection, FlowInformation_flowLabel, FlowInformation_packFiltId, FlowInformation_packetFilterUsage, FlowInformation_spi, FlowInformation_tosTrafficClass}

PccRule = Class(name="PccRule")

# PccRule class attributes and methods
PccRule_afSigProtocol: Property = Property(name="afSigProtocol", type=EnumerationType)
PccRule_appDescriptor: Property = Property(name="appDescriptor", type=StringType)
PccRule_applicationId: Property = Property(name="applicationId", type=StringType)
PccRule_contentVersion: Property = Property(name="contentVersion", type=IntegerType)
PccRule_isAppRelocatable: Property = Property(name="isAppRelocatable", type=BooleanType)
PccRule_isUeAddrPreserved: Property = Property(name="isUeAddrPreserved", type=BooleanType)
PccRule_pccRuleId: Property = Property(name="pccRuleId", type=StringType)
PccRule_precedence: Property = Property(name="precedence", type=IntegerType)
PccRule.attributes={PccRule_afSigProtocol, PccRule_appDescriptor, PccRule_applicationId, PccRule_contentVersion, PccRule_isAppRelocatable, PccRule_isUeAddrPreserved, PccRule_pccRuleId, PccRule_precedence}

PredefinedPccRuleSet = Class(name="PredefinedPccRuleSet")

# PredefinedPccRuleSet class attributes and methods
PredefinedPccRuleSet_PredefinedPccRules: Property = Property(name="PredefinedPccRules", type=list)
PredefinedPccRuleSet.attributes={PredefinedPccRuleSet_PredefinedPccRules}

PredefinedPccRuleSetSubtree = Class(name="PredefinedPccRuleSetSubtree")

# PredefinedPccRuleSetSubtree class attributes and methods
PredefinedPccRuleSetSubtree_PredefinedPccRuleSet: Property = Property(name="PredefinedPccRuleSet", type=list)
PredefinedPccRuleSetSubtree.attributes={PredefinedPccRuleSetSubtree_PredefinedPccRuleSet}

QosDataInformation = Class(name="QosDataInformation")

# QosDataInformation class attributes and methods
QosDataInformation_extMaxDataBurstVol: Property = Property(name="extMaxDataBurstVol", type=IntegerType)
QosDataInformation_fiveQIValue: Property = Property(name="fiveQIValue", type=IntegerType)
QosDataInformation_gbrDl: Property = Property(name="gbrDl", type=StringType)
QosDataInformation_gbrUl: Property = Property(name="gbrUl", type=StringType)
QosDataInformation_maxPacketLossRateDl: Property = Property(name="maxPacketLossRateDl", type=IntegerType)
QosDataInformation_maxPacketLossRateUl: Property = Property(name="maxPacketLossRateUl", type=IntegerType)
QosDataInformation_maxbrDl: Property = Property(name="maxbrDl", type=StringType)
QosDataInformation_maxbrUl: Property = Property(name="maxbrUl", type=StringType)
QosDataInformation_qosId: Property = Property(name="qosId", type=StringType)
QosDataInformation_qosNotificationControl: Property = Property(name="qosNotificationControl", type=BooleanType)
QosDataInformation_reflectiveQos: Property = Property(name="reflectiveQos", type=BooleanType)
QosDataInformation_sharingKeyDl: Property = Property(name="sharingKeyDl", type=StringType)
QosDataInformation_sharingKeyUl: Property = Property(name="sharingKeyUl", type=StringType)
QosDataInformation.attributes={QosDataInformation_extMaxDataBurstVol, QosDataInformation_fiveQIValue, QosDataInformation_gbrDl, QosDataInformation_gbrUl, QosDataInformation_maxPacketLossRateDl, QosDataInformation_maxPacketLossRateUl, QosDataInformation_maxbrDl, QosDataInformation_maxbrUl, QosDataInformation_qosId, QosDataInformation_qosNotificationControl, QosDataInformation_reflectiveQos, QosDataInformation_sharingKeyDl, QosDataInformation_sharingKeyUl}

RedirectInformaton = Class(name="RedirectInformaton")

# RedirectInformaton class attributes and methods
RedirectInformaton_redirectAddressType: Property = Property(name="redirectAddressType", type=EnumerationType)
RedirectInformaton_redirectEnabled: Property = Property(name="redirectEnabled", type=BooleanType)
RedirectInformaton_redirectServerAddress: Property = Property(name="redirectServerAddress", type=StringType)
RedirectInformaton.attributes={RedirectInformaton_redirectAddressType, RedirectInformaton_redirectEnabled, RedirectInformaton_redirectServerAddress}

RouteInformation = Class(name="RouteInformation")

# RouteInformation class attributes and methods
RouteInformation_ipv4Addr: Property = Property(name="ipv4Addr", type=StringType)
RouteInformation_ipv6Addr: Property = Property(name="ipv6Addr", type=StringType)
RouteInformation_portNumber: Property = Property(name="portNumber", type=IntegerType)
RouteInformation.attributes={RouteInformation_ipv4Addr, RouteInformation_ipv6Addr, RouteInformation_portNumber}

RouteToLocation = Class(name="RouteToLocation")

# RouteToLocation class attributes and methods
RouteToLocation_dnai: Property = Property(name="dnai", type=StringType)
RouteToLocation_routeProfId: Property = Property(name="routeProfId", type=StringType)
RouteToLocation.attributes={RouteToLocation_dnai, RouteToLocation_routeProfId}

SteeringMode = Class(name="SteeringMode")

# SteeringMode class attributes and methods
SteeringMode_active: Property = Property(name="active", type=EnumerationType)
SteeringMode_prioAcc: Property = Property(name="prioAcc", type=EnumerationType)
SteeringMode_standby: Property = Property(name="standby", type=EnumerationType)
SteeringMode_steerModeValue: Property = Property(name="steerModeValue", type=EnumerationType)
SteeringMode_threeGLoad: Property = Property(name="threeGLoad", type=IntegerType)
SteeringMode.attributes={SteeringMode_active, SteeringMode_prioAcc, SteeringMode_standby, SteeringMode_steerModeValue, SteeringMode_threeGLoad}

TrafficControlDataInformation = Class(name="TrafficControlDataInformation")

# TrafficControlDataInformation class attributes and methods
TrafficControlDataInformation_flowStatus: Property = Property(name="flowStatus", type=EnumerationType)
TrafficControlDataInformation_mulAccCtrl: Property = Property(name="mulAccCtrl", type=EnumerationType)
TrafficControlDataInformation_muteNotif: Property = Property(name="muteNotif", type=BooleanType)
TrafficControlDataInformation_steerFun: Property = Property(name="steerFun", type=EnumerationType)
TrafficControlDataInformation_tcId: Property = Property(name="tcId", type=StringType)
TrafficControlDataInformation_trafficSteeringPolIdDl: Property = Property(name="trafficSteeringPolIdDl", type=StringType)
TrafficControlDataInformation_trafficSteeringPolIdUl: Property = Property(name="trafficSteeringPolIdUl", type=StringType)
TrafficControlDataInformation.attributes={TrafficControlDataInformation_flowStatus, TrafficControlDataInformation_mulAccCtrl, TrafficControlDataInformation_muteNotif, TrafficControlDataInformation_steerFun, TrafficControlDataInformation_tcId, TrafficControlDataInformation_trafficSteeringPolIdDl, TrafficControlDataInformation_trafficSteeringPolIdUl}

TscaiInputContainer = Class(name="TscaiInputContainer")

# TscaiInputContainer class attributes and methods
TscaiInputContainer_burstArrivalTime: Property = Property(name="burstArrivalTime", type=StringType)
TscaiInputContainer_periodicity: Property = Property(name="periodicity", type=IntegerType)
TscaiInputContainer.attributes={TscaiInputContainer_burstArrivalTime, TscaiInputContainer_periodicity}

UpPathChgEvent = Class(name="UpPathChgEvent")

# UpPathChgEvent class attributes and methods
UpPathChgEvent_afAckInd: Property = Property(name="afAckInd", type=BooleanType)
UpPathChgEvent_dnaiChgType: Property = Property(name="dnaiChgType", type=EnumerationType)
UpPathChgEvent_notifCorreId: Property = Property(name="notifCorreId", type=StringType)
UpPathChgEvent_notificationUri: Property = Property(name="notificationUri", type=StringType)
UpPathChgEvent.attributes={UpPathChgEvent_afAckInd, UpPathChgEvent_dnaiChgType, UpPathChgEvent_notifCorreId, UpPathChgEvent_notificationUri}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-predefinedpccruleset",
    types={ARP, ConditionData, EthFlowDescription, FlowInformation, PccRule, PredefinedPccRuleSet, PredefinedPccRuleSetSubtree, QosDataInformation, RedirectInformaton, RouteInformation, RouteToLocation, SteeringMode, TrafficControlDataInformation, TscaiInputContainer, UpPathChgEvent},
    associations={},
    generalizations={}
)
