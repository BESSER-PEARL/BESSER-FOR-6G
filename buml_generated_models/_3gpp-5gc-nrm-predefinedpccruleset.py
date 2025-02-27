# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
ARP = Class(name="ARP", synonyms=["It specifies the allocation and retention priority of a QoS control policy."])

# ARP class attributes and methods
ARP_preemptCap: Property = Property(name="preemptCap", type=EnumerationType, synonyms=["It defines whether a service data flow may get resources that were already assigned to another service data flow with a lower priority level."])
ARP_preemptVuln: Property = Property(name="preemptVuln", type=EnumerationType, synonyms=["It defines whether a service data flow may lose the resources assigned to it in order to admit a service data flow with higher priority level."])
ARP_priorityLevel: Property = Property(name="priorityLevel", type=IntegerType, synonyms=["It defines the relative importance of a resource request."])
ARP.attributes={ARP_preemptCap, ARP_preemptVuln, ARP_priorityLevel}

ConditionData = Class(name="ConditionData", synonyms=["It specifies the specifies the condition data for a PCC rule."])

# ConditionData class attributes and methods
ConditionData_accessType: Property = Property(name="accessType", type=EnumerationType, synonyms=["It provides the condition of access type of the UE when the session AMBR shall be enforced."])
ConditionData_activationTime: Property = Property(name="activationTime", type=StringType, synonyms=["It indicates the time (in date-time format) when the decision data shall be activated."])
ConditionData_condId: Property = Property(name="condId", type=StringType, synonyms=["It uniquely identifies the condition data."])
ConditionData_deactivationTime: Property = Property(name="deactivationTime", type=StringType, synonyms=["It indicates the time (in date-time format) when the decision data shall be deactivated."])
ConditionData_ratType: Property = Property(name="ratType", type=EnumerationType, synonyms=["It provides the condition of RAT type of the UE when the session AMBR shall be enforced."])
ConditionData.attributes={ConditionData_accessType, ConditionData_activationTime, ConditionData_condId, ConditionData_deactivationTime, ConditionData_ratType}

EthFlowDescription = Class(name="EthFlowDescription", synonyms=["It describes an Ethernet flow."])

# EthFlowDescription class attributes and methods
EthFlowDescription_destMacAddr: Property = Property(name="destMacAddr", type=StringType, synonyms=["It specifies the destination MAC address formatted in the hexadecimal ."])
EthFlowDescription_destMacAddrEnd: Property = Property(name="destMacAddrEnd", type=StringType, synonyms=["It specifies the destination MAC address end. If this attribute is present, the destMacAddr attribute specifies the destination MAC address start."])
EthFlowDescription_ethType: Property = Property(name="ethType", type=StringType, synonyms=["A two-octet string that represents the Ethertype."])
EthFlowDescription_fDesc: Property = Property(name="fDesc", type=StringType, synonyms=["It contains the flow description for the Uplink or Downlink IP flow. It shall be present when the ethtype is IP."])
EthFlowDescription_fDir: Property = Property(name="fDir", type=EnumerationType, synonyms=["It indicates the packet filter direction."])
EthFlowDescription_sourceMacAddr: Property = Property(name="sourceMacAddr", type=StringType, synonyms=["It specifies the source MAC address formatted in the hexadecimal notation."])
EthFlowDescription_srcMacAddrEnd: Property = Property(name="srcMacAddrEnd", type=StringType, synonyms=["It specifies the source MAC address end. If this attribute is present, the sourceMacAddr attribute specifies the source MAC address start. E.g. srcMacAddrEnd with value 00-10-A4-23-3E-FE and sourceMacAddr with value 00-10-A4-23-3E-02 means all MAC addresses from 00-10-A4-23-3E-02 up to and including 00-10-A4-23-3E-FE."])
EthFlowDescription.attributes={EthFlowDescription_destMacAddr, EthFlowDescription_destMacAddrEnd, EthFlowDescription_ethType, EthFlowDescription_fDesc, EthFlowDescription_fDir, EthFlowDescription_sourceMacAddr, EthFlowDescription_srcMacAddrEnd}

FlowInformation = Class(name="FlowInformation", synonyms=["It specifies the flow information of a PCC rule."])

# FlowInformation class attributes and methods
FlowInformation_flowDescription: Property = Property(name="flowDescription", type=StringType, synonyms=["It defines a packet filter for an IP flow."])
FlowInformation_flowDirection: Property = Property(name="flowDirection", type=EnumerationType, synonyms=["It indicates the direction/directions that a filter is applicable."])
FlowInformation_flowLabel: Property = Property(name="flowLabel", type=StringType, synonyms=["It specifies the Ipv6 flow label header field."])
FlowInformation_packFiltId: Property = Property(name="packFiltId", type=StringType, synonyms=["It is the identifier of the packet filter."])
FlowInformation_packetFilterUsage: Property = Property(name="packetFilterUsage", type=BooleanType, synonyms=["It indicates if the packet shall be sent to the UE."])
FlowInformation_spi: Property = Property(name="spi", type=StringType, synonyms=["It is the security parameter index of the IPSec packet."])
FlowInformation_tosTrafficClass: Property = Property(name="tosTrafficClass", type=StringType, synonyms=["It contains the Ipv4 Type-of-Service and mask field or the Ipv6 Traffic-Class field and mask field."])
FlowInformation.attributes={FlowInformation_flowDescription, FlowInformation_flowDirection, FlowInformation_flowLabel, FlowInformation_packFiltId, FlowInformation_packetFilterUsage, FlowInformation_spi, FlowInformation_tosTrafficClass}

PccRule = Class(name="PccRule", synonyms=["It specifies the PCC rule, see TS 29.512"])

# PccRule class attributes and methods
PccRule_afSigProtocol: Property = Property(name="afSigProtocol", type=EnumerationType, synonyms=["Indicates the protocol used for signalling between the UE and the AF, the default value is NO_INFORMATION."])
PccRule_appDescriptor: Property = Property(name="appDescriptor", type=StringType, synonyms=["It is the ATSSS rule application descriptor."])
PccRule_applicationId: Property = Property(name="applicationId", type=StringType, synonyms=["A reference to the application detection filter configured at the UPF."])
PccRule_contentVersion: Property = Property(name="contentVersion", type=IntegerType, synonyms=["Indicates the content version of the PCC rule."])
PccRule_isAppRelocatable: Property = Property(name="isAppRelocatable", type=BooleanType, synonyms=["It indicates the application relocation possibility, the default value is NO_INFORMATION."])
PccRule_isUeAddrPreserved: Property = Property(name="isUeAddrPreserved", type=BooleanType, synonyms=["It Indicates whether UE IP address should be preserved."])
PccRule_pccRuleId: Property = Property(name="pccRuleId", type=StringType, synonyms=["It identifies the PCC rule."])
PccRule_precedence: Property = Property(name="precedence", type=IntegerType, synonyms=["It indicates the order in which this PCC rule is applied relative to other PCC rules within the same PDU session."])
PccRule.attributes={PccRule_afSigProtocol, PccRule_appDescriptor, PccRule_applicationId, PccRule_contentVersion, PccRule_isAppRelocatable, PccRule_isUeAddrPreserved, PccRule_pccRuleId, PccRule_precedence}

PredefinedPccRuleSet = Class(name="PredefinedPccRuleSet", synonyms=["Represents the PredefinedPccRuleSet IOC."])

# PredefinedPccRuleSet class attributes and methods
PredefinedPccRuleSet_PredefinedPccRules: Property = Property(name="PredefinedPccRules", type=list, synonyms=["The list of predefined PCC rules."])
PredefinedPccRuleSet.attributes={PredefinedPccRuleSet_PredefinedPccRules}

PredefinedPccRuleSetSubtree = Class(name="PredefinedPccRuleSetSubtree", synonyms=["It specifies the PredefinedPccRuleSet IOC with inherited attributes."])

# PredefinedPccRuleSetSubtree class attributes and methods
PredefinedPccRuleSetSubtree_PredefinedPccRuleSet: Property = Property(name="PredefinedPccRuleSet", type=list, synonyms=["Specifies the predefined PCC rules."])
PredefinedPccRuleSetSubtree.attributes={PredefinedPccRuleSetSubtree_PredefinedPccRuleSet}

QosDataInformation = Class(name="QosDataInformation", synonyms=["It specifies the QoS control policy data for a service flow of a PCC rule."])

# QosDataInformation class attributes and methods
QosDataInformation_extMaxDataBurstVol: Property = Property(name="extMaxDataBurstVol", type=IntegerType, synonyms=["It denotes the largest amount of data that is required to be transferred within a period of 5G-AN PDB, see TS 29.512"])
QosDataInformation_fiveQIValue: Property = Property(name="fiveQIValue", type=IntegerType, synonyms=["It indicates the 5QI value."])
QosDataInformation_gbrDl: Property = Property(name="gbrDl", type=StringType, synonyms=["It represents the guaranteed downlink bandwidth."])
QosDataInformation_gbrUl: Property = Property(name="gbrUl", type=StringType, synonyms=["It represents the guaranteed uplink bandwidth."])
QosDataInformation_maxPacketLossRateDl: Property = Property(name="maxPacketLossRateDl", type=IntegerType, synonyms=["It indicates the downlink maximum rate for lost packets that can be tolerated for the service data flow."])
QosDataInformation_maxPacketLossRateUl: Property = Property(name="maxPacketLossRateUl", type=IntegerType, synonyms=["It indicates the uplink maximum rate for lost packets that can be tolerated for the service data flow."])
QosDataInformation_maxbrDl: Property = Property(name="maxbrDl", type=StringType, synonyms=["It represents the maximum downlink bandwidth."])
QosDataInformation_maxbrUl: Property = Property(name="maxbrUl", type=StringType, synonyms=["It represents the maximum uplink bandwidth."])
QosDataInformation_qosId: Property = Property(name="qosId", type=StringType, synonyms=["It identifies the QoS control policy data for a PCC rule."])
QosDataInformation_qosNotificationControl: Property = Property(name="qosNotificationControl", type=BooleanType, synonyms=["It indicates whether notifications are requested from 3GPP NG-RAN when the GFBR can no longer (or again) be guaranteed for a QoS Flow during the lifetime of the QoS Flow."])
QosDataInformation_reflectiveQos: Property = Property(name="reflectiveQos", type=BooleanType, synonyms=["Indicates whether the QoS information is reflective for the corresponding non-GBR service data flow"])
QosDataInformation_sharingKeyDl: Property = Property(name="sharingKeyDl", type=StringType, synonyms=["It indicates, by containing the same value, what PCC rules may share resource in downlink direction."])
QosDataInformation_sharingKeyUl: Property = Property(name="sharingKeyUl", type=StringType, synonyms=["It indicates, by containing the same value, what PCC rules may share resource in uplink direction."])
QosDataInformation.attributes={QosDataInformation_extMaxDataBurstVol, QosDataInformation_fiveQIValue, QosDataInformation_gbrDl, QosDataInformation_gbrUl, QosDataInformation_maxPacketLossRateDl, QosDataInformation_maxPacketLossRateUl, QosDataInformation_maxbrDl, QosDataInformation_maxbrUl, QosDataInformation_qosId, QosDataInformation_qosNotificationControl, QosDataInformation_reflectiveQos, QosDataInformation_sharingKeyDl, QosDataInformation_sharingKeyUl}

RedirectInformaton = Class(name="RedirectInformaton", synonyms=["It specifies the redirect information for traffic control in the PCC rule."])

# RedirectInformaton class attributes and methods
RedirectInformaton_redirectAddressType: Property = Property(name="redirectAddressType", type=EnumerationType, synonyms=["It indicates the type of redirect address."])
RedirectInformaton_redirectEnabled: Property = Property(name="redirectEnabled", type=BooleanType, synonyms=["It indicates whether the redirect instruction is enabled."])
RedirectInformaton_redirectServerAddress: Property = Property(name="redirectServerAddress", type=StringType, synonyms=["It indicates the address of the redirect server."])
RedirectInformaton.attributes={RedirectInformaton_redirectAddressType, RedirectInformaton_redirectEnabled, RedirectInformaton_redirectServerAddress}

RouteInformation = Class(name="RouteInformation", synonyms=["It specifies the traffic routing information."])

# RouteInformation class attributes and methods
RouteInformation_ipv4Addr: Property = Property(name="ipv4Addr", type=StringType, synonyms=["It defines the Ipv4 address of the tunnel end point in the data network, formatted in the dotted decimal notation."])
RouteInformation_ipv6Addr: Property = Property(name="ipv6Addr", type=StringType, synonyms=["It defines the Ipv6 address of the tunnel end point in the data network."])
RouteInformation_portNumber: Property = Property(name="portNumber", type=IntegerType, synonyms=["It defines the UDP port number of the tunnel end point in the data network, see TS 29.571"])
RouteInformation.attributes={RouteInformation_ipv4Addr, RouteInformation_ipv6Addr, RouteInformation_portNumber}

RouteToLocation = Class(name="RouteToLocation", synonyms=["It specifies a list of location which the traffic shall be routed to for the AF request."])

# RouteToLocation class attributes and methods
RouteToLocation_dnai: Property = Property(name="dnai", type=StringType, synonyms=["It represents the DNAI (Data network access identifier)."])
RouteToLocation_routeProfId: Property = Property(name="routeProfId", type=StringType, synonyms=["It identifies the routing profile."])
RouteToLocation.attributes={RouteToLocation_dnai, RouteToLocation_routeProfId}

SteeringMode = Class(name="SteeringMode", synonyms=["It specifies the traffic distribution rule, see TS 29.512."])

# SteeringMode class attributes and methods
SteeringMode_active: Property = Property(name="active", type=EnumerationType, synonyms=["It indicates the active access, see TS 29.571."])
SteeringMode_prioAcc: Property = Property(name="prioAcc", type=EnumerationType, synonyms=["It indicates the high priority access."])
SteeringMode_standby: Property = Property(name="standby", type=EnumerationType, synonyms=["It indicates the Standby access, see TS 29.571."])
SteeringMode_steerModeValue: Property = Property(name="steerModeValue", type=EnumerationType, synonyms=["It indicates the value of the steering mode, see TS 29.512."])
SteeringMode_threeGLoad: Property = Property(name="threeGLoad", type=IntegerType, synonyms=["It indicates the traffic load to steer to the 3GPP Access expressed in one percent."])
SteeringMode.attributes={SteeringMode_active, SteeringMode_prioAcc, SteeringMode_standby, SteeringMode_steerModeValue, SteeringMode_threeGLoad}

TrafficControlDataInformation = Class(name="TrafficControlDataInformation", synonyms=["It specifies the traffic control data for a service flow of a PCC rule."])

# TrafficControlDataInformation class attributes and methods
TrafficControlDataInformation_flowStatus: Property = Property(name="flowStatus", type=EnumerationType, synonyms=["It represents whether the service data flow(s) are enabled or disabled."])
TrafficControlDataInformation_mulAccCtrl: Property = Property(name="mulAccCtrl", type=EnumerationType, synonyms=["It indicates whether the service data flow, corresponding to the service data flow template, is allowed or not allowed."])
TrafficControlDataInformation_muteNotif: Property = Property(name="muteNotif", type=BooleanType, synonyms=["It indicates whether applicat'on's start or stop notification is to be muted."])
TrafficControlDataInformation_steerFun: Property = Property(name="steerFun", type=EnumerationType, synonyms=["It indicates the applicable traffic steering functionality."])
TrafficControlDataInformation_tcId: Property = Property(name="tcId", type=StringType, synonyms=["It univocally identifies the traffic control policy data within a PDU session."])
TrafficControlDataInformation_trafficSteeringPolIdDl: Property = Property(name="trafficSteeringPolIdDl", type=StringType, synonyms=["It references to a pre-configured traffic steering policy for downlink traffic at the SMF, see TS 29.512"])
TrafficControlDataInformation_trafficSteeringPolIdUl: Property = Property(name="trafficSteeringPolIdUl", type=StringType, synonyms=["It references to a pre-configured traffic steering policy for uplink traffic at the SMF, see TS 29.512"])
TrafficControlDataInformation.attributes={TrafficControlDataInformation_flowStatus, TrafficControlDataInformation_mulAccCtrl, TrafficControlDataInformation_muteNotif, TrafficControlDataInformation_steerFun, TrafficControlDataInformation_tcId, TrafficControlDataInformation_trafficSteeringPolIdDl, TrafficControlDataInformation_trafficSteeringPolIdUl}

TscaiInputContainer = Class(name="TscaiInputContainer", synonyms=["It specifies the transports TSCAI input parameters for TSC traffic at the ingress interface of the DS-TT/UE for a PCC rule."])

# TscaiInputContainer class attributes and methods
TscaiInputContainer_burstArrivalTime: Property = Property(name="burstArrivalTime", type=StringType, synonyms=["It Indicates the arrival time (in date-time format) of the data burst in reference to the TSN GM."])
TscaiInputContainer_periodicity: Property = Property(name="periodicity", type=IntegerType, synonyms=["It identifies the time period between the start of two bursts in reference to the TSN GM."])
TscaiInputContainer.attributes={TscaiInputContainer_burstArrivalTime, TscaiInputContainer_periodicity}

UpPathChgEvent = Class(name="UpPathChgEvent", synonyms=["It specifies the information about the AF subscriptions of the UP path change."])

# UpPathChgEvent class attributes and methods
UpPathChgEvent_afAckInd: Property = Property(name="afAckInd", type=BooleanType, synonyms=["It identifies whether the AF acknowledgement of UP path event notification is expected."])
UpPathChgEvent_dnaiChgType: Property = Property(name="dnaiChgType", type=EnumerationType, synonyms=["It indicates the type of DNAI change, see TS 29.512"])
UpPathChgEvent_notifCorreId: Property = Property(name="notifCorreId", type=StringType, synonyms=["It is used to set the value of Notification Correlation ID in the notification sent by the SMF, see TS 29.512"])
UpPathChgEvent_notificationUri: Property = Property(name="notificationUri", type=StringType, synonyms=["It provides notification address (Uri) of AF receiving the event notification."])
UpPathChgEvent.attributes={UpPathChgEvent_afAckInd, UpPathChgEvent_dnaiChgType, UpPathChgEvent_notifCorreId, UpPathChgEvent_notificationUri}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-predefinedpccruleset",
    types={ARP, ConditionData, EthFlowDescription, FlowInformation, PccRule, PredefinedPccRuleSet, PredefinedPccRuleSetSubtree, QosDataInformation, RedirectInformaton, RouteInformation, RouteToLocation, SteeringMode, TrafficControlDataInformation, TscaiInputContainer, UpPathChgEvent},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the predefined PCC rules, which are configured to SMF and referenced by PCF."]
