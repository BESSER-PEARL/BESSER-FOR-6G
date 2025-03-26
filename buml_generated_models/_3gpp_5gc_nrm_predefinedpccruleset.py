# Generated B_UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models._3gpp_common_top import domain_model as top3gpp_model
# from buml_generated_models.ietf_yang_types import domain_model as yang_model

# Enumerations
AccesstypeEnum = Enumeration(name="AccesstypeEnum")
AccesstypeEnum_3GPP_ACCESS = EnumerationLiteral(name="3GPP_ACCESS", owner=AccesstypeEnum)
AccesstypeEnum_NON_3GPP_ACCESS = EnumerationLiteral(name="NON_3GPP_ACCESS", owner=AccesstypeEnum)
AccesstypeEnum.literals = {AccesstypeEnum_3GPP_ACCESS, AccesstypeEnum_NON_3GPP_ACCESS}
AccesstypeEnum.synonyms = ["It provides the condition of access type of the UE when the session AMBR shall be enforced."]

ActiveEnum = Enumeration(name="ActiveEnum")
ActiveEnum_3GPP_ACCESS = EnumerationLiteral(name="3GPP_ACCESS", owner=ActiveEnum)
ActiveEnum_NON_3GPP_ACCESS = EnumerationLiteral(name="NON_3GPP_ACCESS", owner=ActiveEnum)
ActiveEnum.literals = {ActiveEnum_3GPP_ACCESS, ActiveEnum_NON_3GPP_ACCESS}
ActiveEnum.synonyms = ["It indicates the active access, see TS 29.571."]

AfsigprotocolEnum = Enumeration(name="AfsigprotocolEnum")
AfsigprotocolEnum_NO_INFORMATION = EnumerationLiteral(name="NO_INFORMATION", owner=AfsigprotocolEnum)
AfsigprotocolEnum_SIP = EnumerationLiteral(name="SIP", owner=AfsigprotocolEnum)
AfsigprotocolEnum.literals = {AfsigprotocolEnum_NO_INFORMATION, AfsigprotocolEnum_SIP}
AfsigprotocolEnum.synonyms = ["Indicates the protocol used for signalling between the UE and the AF, the default value is NO_INFORMATION."]

DnaichgtypeEnum = Enumeration(name="DnaichgtypeEnum")
DnaichgtypeEnum_EARLY = EnumerationLiteral(name="EARLY", owner=DnaichgtypeEnum)
DnaichgtypeEnum_EARLY_LATE = EnumerationLiteral(name="EARLY_LATE", owner=DnaichgtypeEnum)
DnaichgtypeEnum_LATE = EnumerationLiteral(name="LATE", owner=DnaichgtypeEnum)
DnaichgtypeEnum.literals = {DnaichgtypeEnum_EARLY, DnaichgtypeEnum_EARLY_LATE, DnaichgtypeEnum_LATE}
DnaichgtypeEnum.synonyms = ["It indicates the type of DNAI change, see TS 29.512"]

FdirEnum = Enumeration(name="FdirEnum")
FdirEnum_DOWNLINK = EnumerationLiteral(name="DOWNLINK", owner=FdirEnum)
FdirEnum_UPLINK = EnumerationLiteral(name="UPLINK", owner=FdirEnum)
FdirEnum.literals = {FdirEnum_DOWNLINK, FdirEnum_UPLINK}
FdirEnum.synonyms = ["It indicates the packet filter direction."]

FlowdirectionEnum = Enumeration(name="FlowdirectionEnum")
FlowdirectionEnum_BIDIRECTIONAL = EnumerationLiteral(name="BIDIRECTIONAL", owner=FlowdirectionEnum)
FlowdirectionEnum_DOWNLINK = EnumerationLiteral(name="DOWNLINK", owner=FlowdirectionEnum)
FlowdirectionEnum_UNSPECIFIED = EnumerationLiteral(name="UNSPECIFIED", owner=FlowdirectionEnum)
FlowdirectionEnum_UPLINK = EnumerationLiteral(name="UPLINK", owner=FlowdirectionEnum)
FlowdirectionEnum.literals = {FlowdirectionEnum_BIDIRECTIONAL, FlowdirectionEnum_DOWNLINK, FlowdirectionEnum_UNSPECIFIED, FlowdirectionEnum_UPLINK}
FlowdirectionEnum.synonyms = ["It indicates the direction/directions that a filter is applicable."]

FlowstatusEnum = Enumeration(name="FlowstatusEnum")
FlowstatusEnum_DISABLED = EnumerationLiteral(name="DISABLED", owner=FlowstatusEnum)
FlowstatusEnum_ENABLED = EnumerationLiteral(name="ENABLED", owner=FlowstatusEnum)
FlowstatusEnum_ENABLED_DOWNLINK = EnumerationLiteral(name="ENABLED_DOWNLINK", owner=FlowstatusEnum)
FlowstatusEnum_ENABLED_UPLINK = EnumerationLiteral(name="ENABLED_UPLINK", owner=FlowstatusEnum)
FlowstatusEnum_REMOVED = EnumerationLiteral(name="REMOVED", owner=FlowstatusEnum)
FlowstatusEnum.literals = {FlowstatusEnum_DISABLED, FlowstatusEnum_ENABLED, FlowstatusEnum_ENABLED_DOWNLINK, FlowstatusEnum_ENABLED_UPLINK, FlowstatusEnum_REMOVED}
FlowstatusEnum.synonyms = ["It represents whether the service data flow(s) are enabled or disabled."]

MulaccctrlEnum = Enumeration(name="MulaccctrlEnum")
MulaccctrlEnum_ALLOWED = EnumerationLiteral(name="ALLOWED", owner=MulaccctrlEnum)
MulaccctrlEnum_NOT_ALLOWED = EnumerationLiteral(name="NOT_ALLOWED", owner=MulaccctrlEnum)
MulaccctrlEnum.literals = {MulaccctrlEnum_ALLOWED, MulaccctrlEnum_NOT_ALLOWED}
MulaccctrlEnum.synonyms = ["It indicates whether the service data flow, corresponding to the service data flow template, is allowed or not allowed."]

PreemptcapEnum = Enumeration(name="PreemptcapEnum")
PreemptcapEnum_MAY_PREEMPT = EnumerationLiteral(name="MAY_PREEMPT", owner=PreemptcapEnum)
PreemptcapEnum_NOT_PREEMPT = EnumerationLiteral(name="NOT_PREEMPT", owner=PreemptcapEnum)
PreemptcapEnum.literals = {PreemptcapEnum_MAY_PREEMPT, PreemptcapEnum_NOT_PREEMPT}
PreemptcapEnum.synonyms = ["It defines whether a service data flow may get resources that were already assigned to another service data flow with a lower priority level."]

PreemptvulnEnum = Enumeration(name="PreemptvulnEnum")
PreemptvulnEnum_NOT_PREEMPTABLE = EnumerationLiteral(name="NOT_PREEMPTABLE", owner=PreemptvulnEnum)
PreemptvulnEnum_PREEMPTABLE = EnumerationLiteral(name="PREEMPTABLE", owner=PreemptvulnEnum)
PreemptvulnEnum.literals = {PreemptvulnEnum_NOT_PREEMPTABLE, PreemptvulnEnum_PREEMPTABLE}
PreemptvulnEnum.synonyms = ["It defines whether a service data flow may lose the resources assigned to it in order to admit a service data flow with higher priority level."]

PrioaccEnum = Enumeration(name="PrioaccEnum")
PrioaccEnum_3GPP_ACCESS = EnumerationLiteral(name="3GPP_ACCESS", owner=PrioaccEnum)
PrioaccEnum_NON_3GPP_ACCESS = EnumerationLiteral(name="NON_3GPP_ACCESS", owner=PrioaccEnum)
PrioaccEnum.literals = {PrioaccEnum_3GPP_ACCESS, PrioaccEnum_NON_3GPP_ACCESS}
PrioaccEnum.synonyms = ["It indicates the high priority access."]

RattypeEnum = Enumeration(name="RattypeEnum")
RattypeEnum_EUTRA = EnumerationLiteral(name="EUTRA", owner=RattypeEnum)
RattypeEnum_EUTRA_U = EnumerationLiteral(name="EUTRA_U", owner=RattypeEnum)
RattypeEnum_GERA = EnumerationLiteral(name="GERA", owner=RattypeEnum)
RattypeEnum_LTE_M = EnumerationLiteral(name="LTE_M", owner=RattypeEnum)
RattypeEnum_NBIOT = EnumerationLiteral(name="NBIOT", owner=RattypeEnum)
RattypeEnum_NR = EnumerationLiteral(name="NR", owner=RattypeEnum)
RattypeEnum_NR_U = EnumerationLiteral(name="NR_U", owner=RattypeEnum)
RattypeEnum_TRUSTED_N3GA = EnumerationLiteral(name="TRUSTED_N3GA", owner=RattypeEnum)
RattypeEnum_TRUSTED_WLAN = EnumerationLiteral(name="TRUSTED_WLAN", owner=RattypeEnum)
RattypeEnum_UTRA = EnumerationLiteral(name="UTRA", owner=RattypeEnum)
RattypeEnum_VIRTUAL = EnumerationLiteral(name="VIRTUAL", owner=RattypeEnum)
RattypeEnum_WIRELINE = EnumerationLiteral(name="WIRELINE", owner=RattypeEnum)
RattypeEnum_WIRELINE_BBF = EnumerationLiteral(name="WIRELINE_BBF", owner=RattypeEnum)
RattypeEnum_WIRELINE_CABLE = EnumerationLiteral(name="WIRELINE_CABLE", owner=RattypeEnum)
RattypeEnum_WLAN = EnumerationLiteral(name="WLAN", owner=RattypeEnum)
RattypeEnum.literals = {RattypeEnum_EUTRA, RattypeEnum_EUTRA_U, RattypeEnum_GERA, RattypeEnum_LTE_M, RattypeEnum_NBIOT, RattypeEnum_NR, RattypeEnum_NR_U, RattypeEnum_TRUSTED_N3GA, RattypeEnum_TRUSTED_WLAN, RattypeEnum_UTRA, RattypeEnum_VIRTUAL, RattypeEnum_WIRELINE, RattypeEnum_WIRELINE_BBF, RattypeEnum_WIRELINE_CABLE, RattypeEnum_WLAN}
RattypeEnum.synonyms = ["It provides the condition of RAT type of the UE when the session AMBR shall be enforced."]

RedirectaddresstypeEnum = Enumeration(name="RedirectaddresstypeEnum")
RedirectaddresstypeEnum_IPV4_ADDR = EnumerationLiteral(name="IPV4_ADDR", owner=RedirectaddresstypeEnum)
RedirectaddresstypeEnum_IPV6_ADDR = EnumerationLiteral(name="IPV6_ADDR", owner=RedirectaddresstypeEnum)
RedirectaddresstypeEnum_SIP_URI = EnumerationLiteral(name="SIP_URI", owner=RedirectaddresstypeEnum)
RedirectaddresstypeEnum_URL = EnumerationLiteral(name="URL", owner=RedirectaddresstypeEnum)
RedirectaddresstypeEnum.literals = {RedirectaddresstypeEnum_IPV4_ADDR, RedirectaddresstypeEnum_IPV6_ADDR, RedirectaddresstypeEnum_SIP_URI, RedirectaddresstypeEnum_URL}
RedirectaddresstypeEnum.synonyms = ["It indicates the type of redirect address."]

StandbyEnum = Enumeration(name="StandbyEnum")
StandbyEnum_3GPP_ACCESS = EnumerationLiteral(name="3GPP_ACCESS", owner=StandbyEnum)
StandbyEnum_NON_3GPP_ACCESS = EnumerationLiteral(name="NON_3GPP_ACCESS", owner=StandbyEnum)
StandbyEnum.literals = {StandbyEnum_3GPP_ACCESS, StandbyEnum_NON_3GPP_ACCESS}
StandbyEnum.synonyms = ["It indicates the Standby access, see TS 29.571."]

SteerfunEnum = Enumeration(name="SteerfunEnum")
SteerfunEnum_ATSSS_LL = EnumerationLiteral(name="ATSSS_LL", owner=SteerfunEnum)
SteerfunEnum_MPTCP = EnumerationLiteral(name="MPTCP", owner=SteerfunEnum)
SteerfunEnum.literals = {SteerfunEnum_ATSSS_LL, SteerfunEnum_MPTCP}
SteerfunEnum.synonyms = ["It indicates the applicable traffic steering functionality."]

SteermodevalueEnum = Enumeration(name="SteermodevalueEnum")
SteermodevalueEnum_ACTIVE_STANDBY = EnumerationLiteral(name="ACTIVE_STANDBY", owner=SteermodevalueEnum)
SteermodevalueEnum_LOAD_BALANCING = EnumerationLiteral(name="LOAD_BALANCING", owner=SteermodevalueEnum)
SteermodevalueEnum_PRIORITY_BASED = EnumerationLiteral(name="PRIORITY_BASED", owner=SteermodevalueEnum)
SteermodevalueEnum_SMALLEST_DELAY = EnumerationLiteral(name="SMALLEST_DELAY", owner=SteermodevalueEnum)
SteermodevalueEnum.literals = {SteermodevalueEnum_ACTIVE_STANDBY, SteermodevalueEnum_LOAD_BALANCING, SteermodevalueEnum_PRIORITY_BASED, SteermodevalueEnum_SMALLEST_DELAY}
SteermodevalueEnum.synonyms = ["It indicates the value of the steering mode, see TS 29.512."]

# Classes
ARP = Class(name="ARP", synonyms=["It specifies the allocation and retention priority of a QoS control policy."])

# ARP class attributes and methods
ARP_preemptCap: Property = Property(name="preemptCap", type=PreemptcapEnum, synonyms=["It defines whether a service data flow may get resources that were already assigned to another service data flow with a lower priority level."])
ARP_preemptVuln: Property = Property(name="preemptVuln", type=PreemptvulnEnum, synonyms=["It defines whether a service data flow may lose the resources assigned to it in order to admit a service data flow with higher priority level."])
ARP_priorityLevel: Property = Property(name="priorityLevel", type=IntegerType, synonyms=["It defines the relative importance of a resource request."])
ARP.attributes={ARP_preemptCap, ARP_preemptVuln, ARP_priorityLevel}

ConditionData = Class(name="ConditionData", synonyms=["It specifies the specifies the condition data for a PCC rule."])

# ConditionData class attributes and methods
ConditionData_accessType: Property = Property(name="accessType", type=AccesstypeEnum, synonyms=["It provides the condition of access type of the UE when the session AMBR shall be enforced."])
ConditionData_activationTime: Property = Property(name="activationTime", type=DataType('date_and_time'), synonyms=["It indicates the time (in date_time format) when the decision data shall be activated."])
ConditionData_condId: Property = Property(name="condId", type=StringType, synonyms=["It uniquely identifies the condition data."])
ConditionData_deactivationTime: Property = Property(name="deactivationTime", type=DataType('date_and_time'), synonyms=["It indicates the time (in date_time format) when the decision data shall be deactivated."])
ConditionData_ratType: Property = Property(name="ratType", type=RattypeEnum, synonyms=["It provides the condition of RAT type of the UE when the session AMBR shall be enforced."])
ConditionData.attributes={ConditionData_accessType, ConditionData_activationTime, ConditionData_condId, ConditionData_deactivationTime, ConditionData_ratType}

EthFlowDescription = Class(name="EthFlowDescription", synonyms=["It describes an Ethernet flow."])

# EthFlowDescription class attributes and methods
EthFlowDescription_destMacAddr: Property = Property(name="destMacAddr", type=StringType, synonyms=["It specifies the destination MAC address formatted in the hexadecimal ."])
EthFlowDescription_destMacAddrEnd: Property = Property(name="destMacAddrEnd", type=StringType, synonyms=["It specifies the destination MAC address end. If this attribute is present, the destMacAddr attribute specifies the destination MAC address start."])
EthFlowDescription_ethType: Property = Property(name="ethType", type=StringType, synonyms=["A two_octet string that represents the Ethertype."])
EthFlowDescription_fDesc: Property = Property(name="fDesc", type=StringType, synonyms=["It contains the flow description for the Uplink or Downlink IP flow. It shall be present when the ethtype is IP."])
EthFlowDescription_fDir: Property = Property(name="fDir", type=FdirEnum, synonyms=["It indicates the packet filter direction."])
EthFlowDescription_sourceMacAddr: Property = Property(name="sourceMacAddr", type=StringType, synonyms=["It specifies the source MAC address formatted in the hexadecimal notation."])
EthFlowDescription_srcMacAddrEnd: Property = Property(name="srcMacAddrEnd", type=StringType, synonyms=["It specifies the source MAC address end. If this attribute is present, the sourceMacAddr attribute specifies the source MAC address start. E.g. srcMacAddrEnd with value 00_10_A4_23_3E_FE and sourceMacAddr with value 00_10_A4_23_3E_02 means all MAC addresses from 00_10_A4_23_3E_02 up to and including 00_10_A4_23_3E_FE."])
EthFlowDescription.attributes={EthFlowDescription_destMacAddr, EthFlowDescription_destMacAddrEnd, EthFlowDescription_ethType, EthFlowDescription_fDesc, EthFlowDescription_fDir, EthFlowDescription_sourceMacAddr, EthFlowDescription_srcMacAddrEnd}

FlowInformation = Class(name="FlowInformation", synonyms=["It specifies the flow information of a PCC rule."])

# FlowInformation class attributes and methods
FlowInformation_flowDescription: Property = Property(name="flowDescription", type=StringType, synonyms=["It defines a packet filter for an IP flow."])
FlowInformation_flowDirection: Property = Property(name="flowDirection", type=FlowdirectionEnum, synonyms=["It indicates the direction/directions that a filter is applicable."])
FlowInformation_flowLabel: Property = Property(name="flowLabel", type=StringType, synonyms=["It specifies the Ipv6 flow label header field."])
FlowInformation_packFiltId: Property = Property(name="packFiltId", type=StringType, synonyms=["It is the identifier of the packet filter."])
FlowInformation_packetFilterUsage: Property = Property(name="packetFilterUsage", type=BooleanType, synonyms=["It indicates if the packet shall be sent to the UE."])
FlowInformation_spi: Property = Property(name="spi", type=StringType, synonyms=["It is the security parameter index of the IPSec packet."])
FlowInformation_tosTrafficClass: Property = Property(name="tosTrafficClass", type=StringType, synonyms=["It contains the Ipv4 Type_of_Service and mask field or the Ipv6 Traffic_Class field and mask field."])
FlowInformation.attributes={FlowInformation_flowDescription, FlowInformation_flowDirection, FlowInformation_flowLabel, FlowInformation_packFiltId, FlowInformation_packetFilterUsage, FlowInformation_spi, FlowInformation_tosTrafficClass}

PccRule = Class(name="PccRule", synonyms=["It specifies the PCC rule, see TS 29.512"])

# PccRule class attributes and methods
PccRule_afSigProtocol: Property = Property(name="afSigProtocol", type=AfsigprotocolEnum, synonyms=["Indicates the protocol used for signalling between the UE and the AF, the default value is NO_INFORMATION."])
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
PredefinedPccRuleSet_PredefinedPccRules: Property = Property(name="PredefinedPccRules", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["The list of predefined PCC rules."])
PredefinedPccRuleSet.attributes={PredefinedPccRuleSet_PredefinedPccRules}

PredefinedPccRuleSetSubtree = Class(name="PredefinedPccRuleSetSubtree", synonyms=["It specifies the PredefinedPccRuleSet IOC with inherited attributes."])

# PredefinedPccRuleSetSubtree class attributes and methods
PredefinedPccRuleSetSubtree_PredefinedPccRuleSet: Property = Property(name="PredefinedPccRuleSet", type=DataType('Top_Grp'), multiplicity=Multiplicity(0, "*"), synonyms=["Specifies the predefined PCC rules."])
PredefinedPccRuleSetSubtree.attributes={PredefinedPccRuleSetSubtree_PredefinedPccRuleSet}

QosDataInformation = Class(name="QosDataInformation", synonyms=["It specifies the QoS control policy data for a service flow of a PCC rule."])

# QosDataInformation class attributes and methods
QosDataInformation_extMaxDataBurstVol: Property = Property(name="extMaxDataBurstVol", type=IntegerType, synonyms=["It denotes the largest amount of data that is required to be transferred within a period of 5G_AN PDB, see TS 29.512"])
QosDataInformation_fiveQIValue: Property = Property(name="fiveQIValue", type=IntegerType, synonyms=["It indicates the 5QI value."])
QosDataInformation_gbrDl: Property = Property(name="gbrDl", type=StringType, synonyms=["It represents the guaranteed downlink bandwidth."])
QosDataInformation_gbrUl: Property = Property(name="gbrUl", type=StringType, synonyms=["It represents the guaranteed uplink bandwidth."])
QosDataInformation_maxPacketLossRateDl: Property = Property(name="maxPacketLossRateDl", type=IntegerType, synonyms=["It indicates the downlink maximum rate for lost packets that can be tolerated for the service data flow."])
QosDataInformation_maxPacketLossRateUl: Property = Property(name="maxPacketLossRateUl", type=IntegerType, synonyms=["It indicates the uplink maximum rate for lost packets that can be tolerated for the service data flow."])
QosDataInformation_maxbrDl: Property = Property(name="maxbrDl", type=StringType, synonyms=["It represents the maximum downlink bandwidth."])
QosDataInformation_maxbrUl: Property = Property(name="maxbrUl", type=StringType, synonyms=["It represents the maximum uplink bandwidth."])
QosDataInformation_qosId: Property = Property(name="qosId", type=StringType, synonyms=["It identifies the QoS control policy data for a PCC rule."])
QosDataInformation_qosNotificationControl: Property = Property(name="qosNotificationControl", type=BooleanType, synonyms=["It indicates whether notifications are requested from 3GPP NG_RAN when the GFBR can no longer (or again) be guaranteed for a QoS Flow during the lifetime of the QoS Flow."])
QosDataInformation_reflectiveQos: Property = Property(name="reflectiveQos", type=BooleanType, synonyms=["Indicates whether the QoS information is reflective for the corresponding non_GBR service data flow"])
QosDataInformation_sharingKeyDl: Property = Property(name="sharingKeyDl", type=StringType, synonyms=["It indicates, by containing the same value, what PCC rules may share resource in downlink direction."])
QosDataInformation_sharingKeyUl: Property = Property(name="sharingKeyUl", type=StringType, synonyms=["It indicates, by containing the same value, what PCC rules may share resource in uplink direction."])
QosDataInformation.attributes={QosDataInformation_extMaxDataBurstVol, QosDataInformation_fiveQIValue, QosDataInformation_gbrDl, QosDataInformation_gbrUl, QosDataInformation_maxPacketLossRateDl, QosDataInformation_maxPacketLossRateUl, QosDataInformation_maxbrDl, QosDataInformation_maxbrUl, QosDataInformation_qosId, QosDataInformation_qosNotificationControl, QosDataInformation_reflectiveQos, QosDataInformation_sharingKeyDl, QosDataInformation_sharingKeyUl}

RedirectInformaton = Class(name="RedirectInformaton", synonyms=["It specifies the redirect information for traffic control in the PCC rule."])

# RedirectInformaton class attributes and methods
RedirectInformaton_redirectAddressType: Property = Property(name="redirectAddressType", type=RedirectaddresstypeEnum, synonyms=["It indicates the type of redirect address."])
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
SteeringMode_active: Property = Property(name="active", type=ActiveEnum, synonyms=["It indicates the active access, see TS 29.571."])
SteeringMode_prioAcc: Property = Property(name="prioAcc", type=PrioaccEnum, synonyms=["It indicates the high priority access."])
SteeringMode_standby: Property = Property(name="standby", type=StandbyEnum, synonyms=["It indicates the Standby access, see TS 29.571."])
SteeringMode_steerModeValue: Property = Property(name="steerModeValue", type=SteermodevalueEnum, synonyms=["It indicates the value of the steering mode, see TS 29.512."])
SteeringMode_threeGLoad: Property = Property(name="threeGLoad", type=IntegerType, synonyms=["It indicates the traffic load to steer to the 3GPP Access expressed in one percent."])
SteeringMode.attributes={SteeringMode_active, SteeringMode_prioAcc, SteeringMode_standby, SteeringMode_steerModeValue, SteeringMode_threeGLoad}

TrafficControlDataInformation = Class(name="TrafficControlDataInformation", synonyms=["It specifies the traffic control data for a service flow of a PCC rule."])

# TrafficControlDataInformation class attributes and methods
TrafficControlDataInformation_flowStatus: Property = Property(name="flowStatus", type=FlowstatusEnum, synonyms=["It represents whether the service data flow(s) are enabled or disabled."])
TrafficControlDataInformation_mulAccCtrl: Property = Property(name="mulAccCtrl", type=MulaccctrlEnum, synonyms=["It indicates whether the service data flow, corresponding to the service data flow template, is allowed or not allowed."])
TrafficControlDataInformation_muteNotif: Property = Property(name="muteNotif", type=BooleanType, synonyms=["It indicates whether applicat'on's start or stop notification is to be muted."])
TrafficControlDataInformation_steerFun: Property = Property(name="steerFun", type=SteerfunEnum, synonyms=["It indicates the applicable traffic steering functionality."])
TrafficControlDataInformation_tcId: Property = Property(name="tcId", type=StringType, synonyms=["It univocally identifies the traffic control policy data within a PDU session."])
TrafficControlDataInformation_trafficSteeringPolIdDl: Property = Property(name="trafficSteeringPolIdDl", type=StringType, synonyms=["It references to a pre_configured traffic steering policy for downlink traffic at the SMF, see TS 29.512"])
TrafficControlDataInformation_trafficSteeringPolIdUl: Property = Property(name="trafficSteeringPolIdUl", type=StringType, synonyms=["It references to a pre_configured traffic steering policy for uplink traffic at the SMF, see TS 29.512"])
TrafficControlDataInformation.attributes={TrafficControlDataInformation_flowStatus, TrafficControlDataInformation_mulAccCtrl, TrafficControlDataInformation_muteNotif, TrafficControlDataInformation_steerFun, TrafficControlDataInformation_tcId, TrafficControlDataInformation_trafficSteeringPolIdDl, TrafficControlDataInformation_trafficSteeringPolIdUl}

TscaiInputContainer = Class(name="TscaiInputContainer", synonyms=["It specifies the transports TSCAI input parameters for TSC traffic at the ingress interface of the DS_TT/UE for a PCC rule."])

# TscaiInputContainer class attributes and methods
TscaiInputContainer_burstArrivalTime: Property = Property(name="burstArrivalTime", type=DataType('date_and_time'), synonyms=["It Indicates the arrival time (in date_time format) of the data burst in reference to the TSN GM."])
TscaiInputContainer_periodicity: Property = Property(name="periodicity", type=IntegerType, synonyms=["It identifies the time period between the start of two bursts in reference to the TSN GM."])
TscaiInputContainer.attributes={TscaiInputContainer_burstArrivalTime, TscaiInputContainer_periodicity}

UpPathChgEvent = Class(name="UpPathChgEvent", synonyms=["It specifies the information about the AF subscriptions of the UP path change."])

# UpPathChgEvent class attributes and methods
UpPathChgEvent_afAckInd: Property = Property(name="afAckInd", type=BooleanType, synonyms=["It identifies whether the AF acknowledgement of UP path event notification is expected."])
UpPathChgEvent_dnaiChgType: Property = Property(name="dnaiChgType", type=DnaichgtypeEnum, synonyms=["It indicates the type of DNAI change, see TS 29.512"])
UpPathChgEvent_notifCorreId: Property = Property(name="notifCorreId", type=StringType, synonyms=["It is used to set the value of Notification Correlation ID in the notification sent by the SMF, see TS 29.512"])
UpPathChgEvent_notificationUri: Property = Property(name="notificationUri", type=StringType, synonyms=["It provides notification address (Uri) of AF receiving the event notification."])
UpPathChgEvent.attributes={UpPathChgEvent_afAckInd, UpPathChgEvent_dnaiChgType, UpPathChgEvent_notifCorreId, UpPathChgEvent_notificationUri}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp_5gc_nrm_predefinedpccruleset",
    types={ARP, AccesstypeEnum, ActiveEnum, AfsigprotocolEnum, ConditionData, DnaichgtypeEnum, EthFlowDescription, FdirEnum, FlowInformation, FlowdirectionEnum, FlowstatusEnum, MulaccctrlEnum, PccRule, PredefinedPccRuleSet, PredefinedPccRuleSetSubtree, PreemptcapEnum, PreemptvulnEnum, PrioaccEnum, QosDataInformation, RattypeEnum, RedirectInformaton, RedirectaddresstypeEnum, RouteInformation, RouteToLocation, StandbyEnum, SteerfunEnum, SteeringMode, SteermodevalueEnum, TrafficControlDataInformation, TscaiInputContainer, UpPathChgEvent},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the predefined PCC rules, which are configured to SMF and referenced by PCF."]
