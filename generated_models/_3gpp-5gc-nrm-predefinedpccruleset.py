# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
TscaiInputContainer = Class(name="TscaiInputContainer")

# TscaiInputContainer class attributes and methods
TscaiInputContainer_periodicity: Property = Property(name="periodicity", type=IntegerType)
TscaiInputContainer_burstArrivalTime: Property = Property(name="burstArrivalTime", type=yang:date-and-time)
TscaiInputContainer.attributes={TscaiInputContainer_periodicity, TscaiInputContainer_burstArrivalTime}

ConditionData = Class(name="ConditionData")

# ConditionData class attributes and methods
ConditionData_condId: Property = Property(name="condId", type=StringType)
ConditionData_activationTime: Property = Property(name="activationTime", type=yang:date-and-time)
ConditionData_deactivationTime: Property = Property(name="deactivationTime", type=yang:date-and-time)
ConditionData_accessType: Property = Property(name="accessType", type=enumeration)
ConditionData_ratType: Property = Property(name="ratType", type=enumeration)
ConditionData.attributes={ConditionData_condId, ConditionData_activationTime, ConditionData_deactivationTime, ConditionData_accessType, ConditionData_ratType}

SteeringMode = Class(name="SteeringMode")

# SteeringMode class attributes and methods
SteeringMode_steerModeValue: Property = Property(name="steerModeValue", type=enumeration)
SteeringMode_active: Property = Property(name="active", type=enumeration)
SteeringMode_standby: Property = Property(name="standby", type=enumeration)
SteeringMode_threeGLoad: Property = Property(name="threeGLoad", type=IntegerType)
SteeringMode_prioAcc: Property = Property(name="prioAcc", type=enumeration)
SteeringMode.attributes={SteeringMode_steerModeValue, SteeringMode_active, SteeringMode_standby, SteeringMode_threeGLoad, SteeringMode_prioAcc}

UpPathChgEvent = Class(name="UpPathChgEvent")

# UpPathChgEvent class attributes and methods
UpPathChgEvent_notificationUri: Property = Property(name="notificationUri", type=StringType)
UpPathChgEvent_notifCorreId: Property = Property(name="notifCorreId", type=StringType)
UpPathChgEvent_dnaiChgType: Property = Property(name="dnaiChgType", type=enumeration)
UpPathChgEvent_afAckInd: Property = Property(name="afAckInd", type=BooleanType)
UpPathChgEvent.attributes={UpPathChgEvent_notificationUri, UpPathChgEvent_notifCorreId, UpPathChgEvent_dnaiChgType, UpPathChgEvent_afAckInd}

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

RedirectInformaton = Class(name="RedirectInformaton")

# RedirectInformaton class attributes and methods
RedirectInformaton_redirectEnabled: Property = Property(name="redirectEnabled", type=BooleanType)
RedirectInformaton_redirectAddressType: Property = Property(name="redirectAddressType", type=enumeration)
RedirectInformaton_redirectServerAddress: Property = Property(name="redirectServerAddress", type=StringType)
RedirectInformaton.attributes={RedirectInformaton_redirectEnabled, RedirectInformaton_redirectAddressType, RedirectInformaton_redirectServerAddress}

TrafficControlDataInformation = Class(name="TrafficControlDataInformation")

# TrafficControlDataInformation class attributes and methods
TrafficControlDataInformation_tcId: Property = Property(name="tcId", type=StringType)
TrafficControlDataInformation_flowStatus: Property = Property(name="flowStatus", type=enumeration)
TrafficControlDataInformation_muteNotif: Property = Property(name="muteNotif", type=BooleanType)
TrafficControlDataInformation_trafficSteeringPolIdDl: Property = Property(name="trafficSteeringPolIdDl", type=StringType)
TrafficControlDataInformation_trafficSteeringPolIdUl: Property = Property(name="trafficSteeringPolIdUl", type=StringType)
TrafficControlDataInformation_steerFun: Property = Property(name="steerFun", type=enumeration)
TrafficControlDataInformation_mulAccCtrl: Property = Property(name="mulAccCtrl", type=enumeration)
TrafficControlDataInformation.attributes={TrafficControlDataInformation_tcId, TrafficControlDataInformation_flowStatus, TrafficControlDataInformation_muteNotif, TrafficControlDataInformation_trafficSteeringPolIdDl, TrafficControlDataInformation_trafficSteeringPolIdUl, TrafficControlDataInformation_steerFun, TrafficControlDataInformation_mulAccCtrl}

ARP = Class(name="ARP")

# ARP class attributes and methods
ARP_priorityLevel: Property = Property(name="priorityLevel", type=IntegerType)
ARP_preemptCap: Property = Property(name="preemptCap", type=enumeration)
ARP_preemptVuln: Property = Property(name="preemptVuln", type=enumeration)
ARP.attributes={ARP_priorityLevel, ARP_preemptCap, ARP_preemptVuln}

QosDataInformation = Class(name="QosDataInformation")

# QosDataInformation class attributes and methods
QosDataInformation_qosId: Property = Property(name="qosId", type=StringType)
QosDataInformation_fiveQIValue: Property = Property(name="fiveQIValue", type=IntegerType)
QosDataInformation_maxbrUl: Property = Property(name="maxbrUl", type=StringType)
QosDataInformation_maxbrDl: Property = Property(name="maxbrDl", type=StringType)
QosDataInformation_gbrUl: Property = Property(name="gbrUl", type=StringType)
QosDataInformation_gbrDl: Property = Property(name="gbrDl", type=StringType)
QosDataInformation_qosNotificationControl: Property = Property(name="qosNotificationControl", type=BooleanType)
QosDataInformation_reflectiveQos: Property = Property(name="reflectiveQos", type=BooleanType)
QosDataInformation_sharingKeyDl: Property = Property(name="sharingKeyDl", type=StringType)
QosDataInformation_sharingKeyUl: Property = Property(name="sharingKeyUl", type=StringType)
QosDataInformation_maxPacketLossRateDl: Property = Property(name="maxPacketLossRateDl", type=IntegerType)
QosDataInformation_maxPacketLossRateUl: Property = Property(name="maxPacketLossRateUl", type=IntegerType)
QosDataInformation_extMaxDataBurstVol: Property = Property(name="extMaxDataBurstVol", type=IntegerType)
QosDataInformation.attributes={QosDataInformation_qosId, QosDataInformation_fiveQIValue, QosDataInformation_maxbrUl, QosDataInformation_maxbrDl, QosDataInformation_gbrUl, QosDataInformation_gbrDl, QosDataInformation_qosNotificationControl, QosDataInformation_reflectiveQos, QosDataInformation_sharingKeyDl, QosDataInformation_sharingKeyUl, QosDataInformation_maxPacketLossRateDl, QosDataInformation_maxPacketLossRateUl, QosDataInformation_extMaxDataBurstVol}

EthFlowDescription = Class(name="EthFlowDescription")

# EthFlowDescription class attributes and methods
EthFlowDescription_destMacAddr: Property = Property(name="destMacAddr", type=StringType)
EthFlowDescription_ethType: Property = Property(name="ethType", type=StringType)
EthFlowDescription_fDesc: Property = Property(name="fDesc", type=StringType)
EthFlowDescription_fDir: Property = Property(name="fDir", type=enumeration)
EthFlowDescription_sourceMacAddr: Property = Property(name="sourceMacAddr", type=StringType)
EthFlowDescription_srcMacAddrEnd: Property = Property(name="srcMacAddrEnd", type=StringType)
EthFlowDescription_destMacAddrEnd: Property = Property(name="destMacAddrEnd", type=StringType)
EthFlowDescription.attributes={EthFlowDescription_destMacAddr, EthFlowDescription_ethType, EthFlowDescription_fDesc, EthFlowDescription_fDir, EthFlowDescription_sourceMacAddr, EthFlowDescription_srcMacAddrEnd, EthFlowDescription_destMacAddrEnd}

FlowInformation = Class(name="FlowInformation")

# FlowInformation class attributes and methods
FlowInformation_flowDescription: Property = Property(name="flowDescription", type=StringType)
FlowInformation_packFiltId: Property = Property(name="packFiltId", type=StringType)
FlowInformation_packetFilterUsage: Property = Property(name="packetFilterUsage", type=BooleanType)
FlowInformation_tosTrafficClass: Property = Property(name="tosTrafficClass", type=StringType)
FlowInformation_spi: Property = Property(name="spi", type=StringType)
FlowInformation_flowLabel: Property = Property(name="flowLabel", type=StringType)
FlowInformation_flowDirection: Property = Property(name="flowDirection", type=enumeration)
FlowInformation.attributes={FlowInformation_flowDescription, FlowInformation_packFiltId, FlowInformation_packetFilterUsage, FlowInformation_tosTrafficClass, FlowInformation_spi, FlowInformation_flowLabel, FlowInformation_flowDirection}

PccRule = Class(name="PccRule")

# PccRule class attributes and methods
PccRule_pccRuleId: Property = Property(name="pccRuleId", type=StringType)
PccRule_applicationId: Property = Property(name="applicationId", type=StringType)
PccRule_appDescriptor: Property = Property(name="appDescriptor", type=StringType)
PccRule_contentVersion: Property = Property(name="contentVersion", type=IntegerType)
PccRule_precedence: Property = Property(name="precedence", type=IntegerType)
PccRule_afSigProtocol: Property = Property(name="afSigProtocol", type=enumeration)
PccRule_isAppRelocatable: Property = Property(name="isAppRelocatable", type=BooleanType)
PccRule_isUeAddrPreserved: Property = Property(name="isUeAddrPreserved", type=BooleanType)
PccRule.attributes={PccRule_pccRuleId, PccRule_applicationId, PccRule_appDescriptor, PccRule_contentVersion, PccRule_precedence, PccRule_afSigProtocol, PccRule_isAppRelocatable, PccRule_isUeAddrPreserved}

PredefinedPccRuleSet = Class(name="PredefinedPccRuleSet")

# PredefinedPccRuleSet class attributes and methods
PredefinedPccRuleSet_PredefinedPccRules: Property = Property(name="PredefinedPccRules", type=list)
PredefinedPccRuleSet.attributes={PredefinedPccRuleSet_PredefinedPccRules}

PredefinedPccRuleSetSubtree = Class(name="PredefinedPccRuleSetSubtree")

# PredefinedPccRuleSetSubtree class attributes and methods
PredefinedPccRuleSetSubtree_PredefinedPccRuleSet: Property = Property(name="PredefinedPccRuleSet", type=list)
PredefinedPccRuleSetSubtree.attributes={PredefinedPccRuleSetSubtree_PredefinedPccRuleSet}

