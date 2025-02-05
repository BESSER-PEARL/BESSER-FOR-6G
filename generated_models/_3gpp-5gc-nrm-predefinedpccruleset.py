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
TscaiInputContainer = Class(name="TscaiInputContainer")
ConditionData = Class(name="ConditionData")
SteeringMode = Class(name="SteeringMode")
UpPathChgEvent = Class(name="UpPathChgEvent")
RouteInformation = Class(name="RouteInformation")
RouteToLocation = Class(name="RouteToLocation")
RedirectInformaton = Class(name="RedirectInformaton")
TrafficControlDataInformation = Class(name="TrafficControlDataInformation")
ARP = Class(name="ARP")
QosDataInformation = Class(name="QosDataInformation")
EthFlowDescription = Class(name="EthFlowDescription")
FlowInformation = Class(name="FlowInformation")
PccRule = Class(name="PccRule")
PredefinedPccRuleSetGrp = Class(name="PredefinedPccRuleSetGrp")
PredefinedPccRuleSetSubtree = Class(name="PredefinedPccRuleSetSubtree")

# TscaiInputContainer class attributes and methods
TscaiInputContainer_periodicity: Property = Property(name="periodicity", type=IntegerType)
TscaiInputContainer_burstArrivalTime: Property = Property(name="burstArrivalTime", type=yang:date-and-time)
TscaiInputContainer.attributes={TscaiInputContainer_periodicity, TscaiInputContainer_burstArrivalTime}

# ConditionData class attributes and methods
ConditionData_condId: Property = Property(name="condId", type=StringType)
ConditionData_activationTime: Property = Property(name="activationTime", type=yang:date-and-time)
ConditionData_deactivationTime: Property = Property(name="deactivationTime", type=yang:date-and-time)
ConditionData_accessType: Property = Property(name="accessType", type=enumeration)
ConditionData_ratType: Property = Property(name="ratType", type=enumeration)
ConditionData.attributes={ConditionData_deactivationTime, ConditionData_accessType, ConditionData_ratType, ConditionData_condId, ConditionData_activationTime}

# SteeringMode class attributes and methods
SteeringMode_steerModeValue: Property = Property(name="steerModeValue", type=enumeration)
SteeringMode_active: Property = Property(name="active", type=enumeration)
SteeringMode_standby: Property = Property(name="standby", type=enumeration)
SteeringMode_threeGLoad: Property = Property(name="threeGLoad", type=IntegerType)
SteeringMode_prioAcc: Property = Property(name="prioAcc", type=enumeration)
SteeringMode.attributes={SteeringMode_active, SteeringMode_standby, SteeringMode_threeGLoad, SteeringMode_prioAcc, SteeringMode_steerModeValue}

# UpPathChgEvent class attributes and methods
UpPathChgEvent_notificationUri: Property = Property(name="notificationUri", type=StringType)
UpPathChgEvent_notifCorreId: Property = Property(name="notifCorreId", type=StringType)
UpPathChgEvent_dnaiChgType: Property = Property(name="dnaiChgType", type=enumeration)
UpPathChgEvent_afAckInd: Property = Property(name="afAckInd", type=BooleanType)
UpPathChgEvent.attributes={UpPathChgEvent_notificationUri, UpPathChgEvent_dnaiChgType, UpPathChgEvent_afAckInd, UpPathChgEvent_notifCorreId}

# RouteInformation class attributes and methods
RouteInformation_ipv4Addr: Property = Property(name="ipv4Addr", type=StringType)
RouteInformation_ipv6Addr: Property = Property(name="ipv6Addr", type=StringType)
RouteInformation_portNumber: Property = Property(name="portNumber", type=IntegerType)
RouteInformation.attributes={RouteInformation_ipv4Addr, RouteInformation_portNumber, RouteInformation_ipv6Addr}

# RouteToLocation class attributes and methods
RouteToLocation_dnai: Property = Property(name="dnai", type=StringType)
RouteToLocation_routeProfId: Property = Property(name="routeProfId", type=StringType)
RouteToLocation.attributes={RouteToLocation_dnai, RouteToLocation_routeProfId}

# RedirectInformaton class attributes and methods
RedirectInformaton_redirectEnabled: Property = Property(name="redirectEnabled", type=BooleanType)
RedirectInformaton_redirectAddressType: Property = Property(name="redirectAddressType", type=enumeration)
RedirectInformaton_redirectServerAddress: Property = Property(name="redirectServerAddress", type=StringType)
RedirectInformaton.attributes={RedirectInformaton_redirectEnabled, RedirectInformaton_redirectServerAddress, RedirectInformaton_redirectAddressType}

# TrafficControlDataInformation class attributes and methods
TrafficControlDataInformation_tcId: Property = Property(name="tcId", type=StringType)
TrafficControlDataInformation_flowStatus: Property = Property(name="flowStatus", type=enumeration)
TrafficControlDataInformation_muteNotif: Property = Property(name="muteNotif", type=BooleanType)
TrafficControlDataInformation_trafficSteeringPolIdDl: Property = Property(name="trafficSteeringPolIdDl", type=StringType)
TrafficControlDataInformation_trafficSteeringPolIdUl: Property = Property(name="trafficSteeringPolIdUl", type=StringType)
TrafficControlDataInformation_steerFun: Property = Property(name="steerFun", type=enumeration)
TrafficControlDataInformation_mulAccCtrl: Property = Property(name="mulAccCtrl", type=enumeration)
TrafficControlDataInformation.attributes={TrafficControlDataInformation_mulAccCtrl, TrafficControlDataInformation_flowStatus, TrafficControlDataInformation_muteNotif, TrafficControlDataInformation_trafficSteeringPolIdDl, TrafficControlDataInformation_trafficSteeringPolIdUl, TrafficControlDataInformation_tcId, TrafficControlDataInformation_steerFun}

# ARP class attributes and methods
ARP_priorityLevel: Property = Property(name="priorityLevel", type=IntegerType)
ARP_preemptCap: Property = Property(name="preemptCap", type=enumeration)
ARP_preemptVuln: Property = Property(name="preemptVuln", type=enumeration)
ARP.attributes={ARP_priorityLevel, ARP_preemptVuln, ARP_preemptCap}

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
QosDataInformation.attributes={QosDataInformation_gbrUl, QosDataInformation_qosId, QosDataInformation_maxPacketLossRateDl, QosDataInformation_gbrDl, QosDataInformation_maxPacketLossRateUl, QosDataInformation_qosNotificationControl, QosDataInformation_fiveQIValue, QosDataInformation_extMaxDataBurstVol, QosDataInformation_reflectiveQos, QosDataInformation_maxbrUl, QosDataInformation_sharingKeyDl, QosDataInformation_maxbrDl, QosDataInformation_sharingKeyUl}

# EthFlowDescription class attributes and methods
EthFlowDescription_destMacAddr: Property = Property(name="destMacAddr", type=StringType)
EthFlowDescription_ethType: Property = Property(name="ethType", type=StringType)
EthFlowDescription_fDesc: Property = Property(name="fDesc", type=StringType)
EthFlowDescription_fDir: Property = Property(name="fDir", type=enumeration)
EthFlowDescription_sourceMacAddr: Property = Property(name="sourceMacAddr", type=StringType)
EthFlowDescription_srcMacAddrEnd: Property = Property(name="srcMacAddrEnd", type=StringType)
EthFlowDescription_destMacAddrEnd: Property = Property(name="destMacAddrEnd", type=StringType)
EthFlowDescription.attributes={EthFlowDescription_ethType, EthFlowDescription_destMacAddrEnd, EthFlowDescription_fDesc, EthFlowDescription_fDir, EthFlowDescription_sourceMacAddr, EthFlowDescription_destMacAddr, EthFlowDescription_srcMacAddrEnd}

# FlowInformation class attributes and methods
FlowInformation_flowDescription: Property = Property(name="flowDescription", type=StringType)
FlowInformation_packFiltId: Property = Property(name="packFiltId", type=StringType)
FlowInformation_packetFilterUsage: Property = Property(name="packetFilterUsage", type=BooleanType)
FlowInformation_tosTrafficClass: Property = Property(name="tosTrafficClass", type=StringType)
FlowInformation_spi: Property = Property(name="spi", type=StringType)
FlowInformation_flowLabel: Property = Property(name="flowLabel", type=StringType)
FlowInformation_flowDirection: Property = Property(name="flowDirection", type=enumeration)
FlowInformation.attributes={FlowInformation_tosTrafficClass, FlowInformation_spi, FlowInformation_flowDescription, FlowInformation_flowLabel, FlowInformation_flowDirection, FlowInformation_packFiltId, FlowInformation_packetFilterUsage}

# PccRule class attributes and methods
PccRule_pccRuleId: Property = Property(name="pccRuleId", type=StringType)
PccRule_applicationId: Property = Property(name="applicationId", type=StringType)
PccRule_appDescriptor: Property = Property(name="appDescriptor", type=StringType)
PccRule_contentVersion: Property = Property(name="contentVersion", type=IntegerType)
PccRule_precedence: Property = Property(name="precedence", type=IntegerType)
PccRule_afSigProtocol: Property = Property(name="afSigProtocol", type=enumeration)
PccRule_isAppRelocatable: Property = Property(name="isAppRelocatable", type=BooleanType)
PccRule_isUeAddrPreserved: Property = Property(name="isUeAddrPreserved", type=BooleanType)
PccRule.attributes={PccRule_isAppRelocatable, PccRule_applicationId, PccRule_isUeAddrPreserved, PccRule_appDescriptor, PccRule_contentVersion, PccRule_precedence, PccRule_pccRuleId, PccRule_afSigProtocol}

# PredefinedPccRuleSetGrp class attributes and methods
PredefinedPccRuleSetGrp_PredefinedPccRules: Property = Property(name="PredefinedPccRules", type=list)
PredefinedPccRuleSetGrp.attributes={PredefinedPccRuleSetGrp_PredefinedPccRules}

# PredefinedPccRuleSetSubtree class attributes and methods
PredefinedPccRuleSetSubtree_PredefinedPccRuleSet: Property = Property(name="PredefinedPccRuleSet", type=list)
PredefinedPccRuleSetSubtree.attributes={PredefinedPccRuleSetSubtree_PredefinedPccRuleSet}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-predefinedpccruleset",
    types={TscaiInputContainer, ConditionData, SteeringMode, UpPathChgEvent, RouteInformation, RouteToLocation, RedirectInformaton, TrafficControlDataInformation, ARP, QosDataInformation, EthFlowDescription, FlowInformation, PccRule, PredefinedPccRuleSetGrp, PredefinedPccRuleSetSubtree, types3gpp_model, mf3gpp_model, me3gpp_model, top3gpp_model, types5g3gpp_model, inet_model, subnet3gpp_model, Conf5QIs3gpp_model, eprp3gpp_model, af3gpp_model, amf3gpp_model, ausf3gpp_model, dn3gpp_model, lmf3gpp_model, n3iwf3gpp_model, ngeir3gpp_model, nrf3gpp_model, nssf3gpp_model, pcf3gpp_model, sepp3gpp_model, smf3gpp_model, smsf3gpp_model, udm3gpp_model, upf3gpp_model, yang_model, nfs3gpp_model, nfp3gpp_model},
    associations={},
    generalizations={}
)
