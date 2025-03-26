# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models.ietf_inet_types import domain_model as inet_model
from buml_generated_models._3gpp_5gc_nrm_nfservice import domain_model as nfs3gpp_model
from buml_generated_models._3gpp_common_yang_types import domain_model as types3gpp_model
# from buml_generated_models.ietf_yang_types import domain_model as yang_model

# Enumerations
AccessType = Enumeration(name="AccessType")
AccessType_3GPP_ACCESS = EnumerationLiteral(name="3GPP_ACCESS", owner=AccessType)
AccessType_NON_3GPP_ACCESS = EnumerationLiteral(name="NON_3GPP_ACCESS", owner=AccessType)
AccessType.literals = {AccessType_3GPP_ACCESS, AccessType_NON_3GPP_ACCESS}

DataSetId = Enumeration(name="DataSetId")
DataSetId_APPLICATION = EnumerationLiteral(name="APPLICATION", owner=DataSetId)
DataSetId_EXPOSURE = EnumerationLiteral(name="EXPOSURE", owner=DataSetId)
DataSetId_POLICY = EnumerationLiteral(name="POLICY", owner=DataSetId)
DataSetId_SUBSCRIPTION = EnumerationLiteral(name="SUBSCRIPTION", owner=DataSetId)
DataSetId.literals = {DataSetId_APPLICATION, DataSetId_EXPOSURE, DataSetId_POLICY, DataSetId_SUBSCRIPTION}

NFStatus = Enumeration(name="NFStatus")
NFStatus_REGISTERED = EnumerationLiteral(name="REGISTERED", owner=NFStatus)
NFStatus_SUSPENDED = EnumerationLiteral(name="SUSPENDED", owner=NFStatus)
NFStatus.literals = {NFStatus_REGISTERED, NFStatus_SUSPENDED}

PduSessionType = Enumeration(name="PduSessionType")
PduSessionType_ETHERNET = EnumerationLiteral(name="ETHERNET", owner=PduSessionType)
PduSessionType_IPV4 = EnumerationLiteral(name="IPV4", owner=PduSessionType)
PduSessionType_IPV4V6 = EnumerationLiteral(name="IPV4V6", owner=PduSessionType)
PduSessionType_IPV6 = EnumerationLiteral(name="IPV6", owner=PduSessionType)
PduSessionType_UNSTRUCTURED = EnumerationLiteral(name="UNSTRUCTURED", owner=PduSessionType)
PduSessionType.literals = {PduSessionType_ETHERNET, PduSessionType_IPV4, PduSessionType_IPV4V6, PduSessionType_IPV6, PduSessionType_UNSTRUCTURED}

UPInterfaceType = Enumeration(name="UPInterfaceType")
UPInterfaceType_N3 = EnumerationLiteral(name="N3", owner=UPInterfaceType)
UPInterfaceType_N6 = EnumerationLiteral(name="N6", owner=UPInterfaceType)
UPInterfaceType_N9 = EnumerationLiteral(name="N9", owner=UPInterfaceType)
UPInterfaceType.literals = {UPInterfaceType_N3, UPInterfaceType_N6, UPInterfaceType_N9}

# Classes
DnnSmfInfoItem = Class(name="DnnSmfInfoItem")

# DnnSmfInfoItem class attributes and methods
DnnSmfInfoItem_dnn: Property = Property(name="dnn", type=StringType, synonyms=["Supported DNN."])
DnnSmfInfoItem.attributes={DnnSmfInfoItem_dnn}

DnnUpfInfoItem = Class(name="DnnUpfInfoItem")

# DnnUpfInfoItem class attributes and methods
DnnUpfInfoItem_dnn: Property = Property(name="dnn", type=StringType, synonyms=["String representing a Data Network."])
DnnUpfInfoItem.attributes={DnnUpfInfoItem_dnn}

Guami = Class(name="Guami")

# Guami class attributes and methods
Guami_amfId: Property = Property(name="amfId", type=DataType('AmfIdentifier'), multiplicity=Multiplicity(1, "*"), synonyms=["AMF Identity."])
Guami_plmnId: Property = Property(name="plmnId", type=DataType('PLMNId'), multiplicity=Multiplicity(1, "*"), synonyms=["PLMN Identity."])
Guami.attributes={Guami_amfId, Guami_plmnId}

IdentityRange = Class(name="IdentityRange")

# IdentityRange class attributes and methods
IdentityRange_end: Property = Property(name="end", type=StringType, synonyms=["Last value identifying the end of an identity range. To be used when the range of identities can be represented as a numeric range (e.g. MSISDN ranges)."])
IdentityRange_pattern: Property = Property(name="pattern", type=StringType, synonyms=["Pattern representing the set of identities belonging to this range. An identity value is considered part of the range if and only if the identity string fully matches the regular expression."])
IdentityRange_start: Property = Property(name="start", type=StringType, synonyms=["First value identifying the start of an identity range. To be used when the range of identities can be represented as a numeric range (e.g., MSISDN ranges)."])
IdentityRange.attributes={IdentityRange_end, IdentityRange_pattern, IdentityRange_start}

InterfaceUpfInfoItem = Class(name="InterfaceUpfInfoItem")

# InterfaceUpfInfoItem class attributes and methods
InterfaceUpfInfoItem_interfaceType: Property = Property(name="interfaceType", type=StringType, synonyms=["User Plane interface type."])
InterfaceUpfInfoItem_networkInstance: Property = Property(name="networkInstance", type=StringType, synonyms=["Network Instance associated to the User Plane interface."])
InterfaceUpfInfoItem.attributes={InterfaceUpfInfoItem_interfaceType, InterfaceUpfInfoItem_networkInstance}

N2InterfaceAmfInfo = Class(name="N2InterfaceAmfInfo")

# N2InterfaceAmfInfo class attributes and methods
N2InterfaceAmfInfo_amfName: Property = Property(name="amfName", type=StringType, synonyms=["AMF name."])
N2InterfaceAmfInfo.attributes={N2InterfaceAmfInfo_amfName}

NFProfile = Class(name="NFProfile")

# NFProfile class attributes and methods
NFProfile_allowedNssais: Property = Property(name="allowedNssais", type=list, multiplicity=Multiplicity(1, "*"), synonyms=["S-NSSAI of the allowed slices to access the NF instance. If not provided, any slice is allowed to access the NF."])
NFProfile_allowedPlmns: Property = Property(name="allowedPlmns", type=DataType('PLMNId'), multiplicity=Multiplicity(1, "*"), synonyms=["PLMNs allowed to access the NF instance. If not provided, any PLMN is allowed to access the NF."])
NFProfile_capacity: Property = Property(name="capacity", type=IntegerType, synonyms=["Static capacity information in the range of 0-65535, expressed as a weight relative to other NF instances of the same type; if capacity is also present in the nfServiceList parameters, those will have precedence over this value."])
NFProfile_customInfo: Property = Property(name="customInfo", type=StringType, synonyms=["Specific data for custom Network Functions."])
NFProfile_defaultNotificationSubscriptions: Property = Property(name="defaultNotificationSubscriptions", type=DataType('DefaultNotificationSubscription'), multiplicity=Multiplicity(1, "*"), synonyms=["Notification endpoints for different notification types."])
NFProfile_fqdn: Property = Property(name="fqdn", type=DataType('domain_name'), synonyms=["FQDN of the Network Function. For AMF, the FQDN registered with the NRF shall be that of the AMF Name."])
NFProfile_heartBeatTimer: Property = Property(name="heartBeatTimer", type=IntegerType, synonyms=["Time in seconds expected between 2 consecutive heart-beat messages from an NF Instance to the NRF. It may be included in the registration request. When present in the request it shall contain the heartbeat time proposed by the NF service consumer."])
NFProfile_interPlmnFqdn: Property = Property(name="interPlmnFqdn", type=DataType('domain_name'), synonyms=["If the NF needs to be discoverable by other NFs in a different PLMN, then an FQDN that is used for inter-PLMN routing is specified."])
NFProfile_load: Property = Property(name="load", type=DataType('Load'), synonyms=["Dynamic load information, ranged from 0 to 100, indicates the current load percentage of the NF."])
NFProfile_locality: Property = Property(name="locality", type=StringType, synonyms=["Operator defined information about the location of the NF instance (e.g. geographic location, data center)."])
NFProfile_nfInstanceID: Property = Property(name="nfInstanceID", type=StringType, synonyms=["String uniquely identifying a NF instance."])
NFProfile_nfProfileChangesInd: Property = Property(name="nfProfileChangesInd", type=BooleanType, synonyms=["NF Profile Changes Indicator. This IE shall be absent in the request to the NRF and may be included by the NRF in NFRegister or NFUpdate (NF Profile Complete Replacement) response. true: the NF Profile contains NF Profile changes. false (default): complete NF Profile."])
NFProfile_nfProfileChangesSupportInd: Property = Property(name="nfProfileChangesSupportInd", type=BooleanType, synonyms=["NF Profile Changes Support Indicator. This IE may be present in the NFRegister or NFUpdate (NF Profile Complete Replacement) request and shall be absent in the response. true: the NF Service Consumer supports receiving NF Profile Changes in the response. false (default): the NF Service Consumer does not support receiving NF Profile Changes in the response."])
NFProfile_nfServicePersistence: Property = Property(name="nfServicePersistence", type=BooleanType, synonyms=["If present, and set to true, it indicates that the different service instances of a same NF Service in this NF instance, supporting a same API version, are capable to persist their resource state in shared storage and therefore these resources are available after a new NF service instance supporting the same API version is selected by a NF Service Consumer (see 3GPP TS 23.527). Otherwise, it indicates that the NF Service Instances of a same NF Service are not capable to share resource state inside the NF Instance."])
NFProfile_nfServices: Property = Property(name="nfServices", type=DataType('NFServiceGrp'), multiplicity=Multiplicity(1, "*"), synonyms=["List of NF Service Instances. It shall include the services produced by the NF that can be discovered by other NFs."])
NFProfile_nfStatus: Property = Property(name="nfStatus", type=StringType, synonyms=["Status of the NF Instance."])
NFProfile_nfType: Property = Property(name="nfType", type=DataType("NfType"), synonyms=["Type of Network Function."])
NFProfile_nrfInfo: Property = Property(name="nrfInfo", type=list, multiplicity=Multiplicity(0, "*"))
NFProfile_perPlmnSnssaiList: Property = Property(name="perPlmnSnssaiList", type=list, multiplicity=Multiplicity(1, "*"), synonyms=["This IE may be included when the list of S-NSSAIs supported by the NF for each PLMN it is supporting is different. When present, this IE shall include the S-NSSAIs supported by the Network Function for each PLMN supported by the Network Function. When present, this IE shall override sNssais IE."])
NFProfile_plmnList: Property = Property(name="plmnList", type=DataType('PLMNId'), multiplicity=Multiplicity(1, "*"), synonyms=["PLMN(s) of the Network Function. This IE shall be present if this information is available for the NF. If not provided, PLMN ID(s) of the PLMN of the NRF are assumed for the NF."])
NFProfile_priority: Property = Property(name="priority", type=IntegerType, synonyms=["Priority (relative to other NFs of the same type) in the range of 0-65535, to be used for NF selection; lower values indicate a higher priority. If priority is also present in the nfServiceList parameters, those will have precedence over this value. The NRF may overwrite the received priority value when exposing an NFProfile with the Nnrf_NFDiscovery service."])
NFProfile_recoveryTime: Property = Property(name="recoveryTime", type=DataType('date_and_time'), synonyms=["Timestamp when the NF was (re)started."])
NFProfile_sNssais: Property = Property(name="sNssais", type=list, multiplicity=Multiplicity(1, "*"), synonyms=["S-NSSAIs of the Network Function. If not provided, the NF can serve any S-NSSAI. When present this IE represents the list of S-NSSAIs supported in all the PLMNs listed in the plmnList IE."])
NFProfile.attributes={NFProfile_allowedNssais, NFProfile_allowedPlmns, NFProfile_capacity, NFProfile_customInfo, NFProfile_defaultNotificationSubscriptions, NFProfile_fqdn, NFProfile_heartBeatTimer, NFProfile_interPlmnFqdn, NFProfile_load, NFProfile_locality, NFProfile_nfInstanceID, NFProfile_nfProfileChangesInd, NFProfile_nfProfileChangesSupportInd, NFProfile_nfServicePersistence, NFProfile_nfServices, NFProfile_nfStatus, NFProfile_nfType, NFProfile_nrfInfo, NFProfile_perPlmnSnssaiList, NFProfile_plmnList, NFProfile_priority, NFProfile_recoveryTime, NFProfile_sNssais}

PlmnSnssai = Class(name="PlmnSnssai")

# PlmnSnssai class attributes and methods
PlmnSnssai_plmnId: Property = Property(name="plmnId", type=DataType('PLMNId'), multiplicity=Multiplicity(1, "*"), synonyms=["PLMN ID for which list of supported S-NSSAI(s) is provided."])
PlmnSnssai_sNssaiList: Property = Property(name="sNssaiList", type=list, multiplicity=Multiplicity(1, "*"), synonyms=["The specific list of S-NSSAIs supported by the given PLMN."])
PlmnSnssai.attributes={PlmnSnssai_plmnId, PlmnSnssai_sNssaiList}

Snssai = Class(name="Snssai")

# Snssai class attributes and methods
Snssai_sd: Property = Property(name="sd", type=StringType, synonyms=["3-octet string, representing the Slice Differentiator, in hexadecimal representation."])
Snssai_sst: Property = Property(name="sst", type=IntegerType, synonyms=["Unsigned integer, within the range 0 to 255, representing the Slice/Service Type. It indicates the expected Network Slice behaviour in terms of features and services."])
Snssai.attributes={Snssai_sd, Snssai_sst}

SnssaiUpfInfoItem = Class(name="SnssaiUpfInfoItem")

# SnssaiUpfInfoItem class attributes and methods
SnssaiUpfInfoItem_dnnUpfInfoList: Property = Property(name="dnnUpfInfoList", type=list, multiplicity=Multiplicity(1, "*"), synonyms=["List of parameters supported by the UPF per DNN."])
SnssaiUpfInfoItem_sNssai: Property = Property(name="sNssai", type=list, multiplicity=Multiplicity(1, "*"), synonyms=["Supported S-NSSAI."])
SnssaiUpfInfoItem.attributes={SnssaiUpfInfoItem_dnnUpfInfoList, SnssaiUpfInfoItem_sNssai}

SupiRange = Class(name="SupiRange")

# SupiRange class attributes and methods
SupiRange_end: Property = Property(name="end", type=StringType, synonyms=["Last value identifying the end of a SUPI range. To be used when the range of SUPI's can be represented as a numeric range (e.g. IMSI ranges)."])
SupiRange_pattern: Property = Property(name="pattern", type=StringType, synonyms=["Pattern representing the set of SUPI's belonging to this range. A SUPI value is considered part of the range if and only if the SUPI string fully matches the regular expression."])
SupiRange_start: Property = Property(name="start", type=StringType, synonyms=["First value identifying the start of a SUPI range. To be used when the range of SUPI's can be represented as a numeric range (e.g., IMSI ranges)."])
SupiRange.attributes={SupiRange_end, SupiRange_pattern, SupiRange_start}

TacRange = Class(name="TacRange")

# TacRange class attributes and methods
TacRange_end: Property = Property(name="end", type=StringType, synonyms=["Last value identifying the end of a TAC range, to be used when the range of TAC's can be represented as a hexadecimal range (e.g. TAC ranges)."])
TacRange_pattern: Property = Property(name="pattern", type=StringType, synonyms=["Pattern representing the set of TAC's belonging to this range."])
TacRange_start: Property = Property(name="start", type=StringType, synonyms=["First value identifying the start of a TAC range, to be used when the range of TAC's can be represented as a hexadecimal range (e.g., TAC ranges)."])
TacRange.attributes={TacRange_end, TacRange_pattern, TacRange_start}

Tai = Class(name="Tai")

# Tai class attributes and methods
Tai_plmnId: Property = Property(name="plmnId", type=DataType('PLMNId'), multiplicity=Multiplicity(1, "*"), synonyms=["PLMN Identity."])
Tai_tac: Property = Property(name="tac", type=DataType('Tac'))
Tai.attributes={Tai_plmnId, Tai_tac}

TaiRange = Class(name="TaiRange")

# TaiRange class attributes and methods
TaiRange_plmnId: Property = Property(name="plmnId", type=DataType('PLMNId'), multiplicity=Multiplicity(1, "*"), synonyms=["PLMN ID related to the TacRange."])
TaiRange_tacRangeList: Property = Property(name="tacRangeList", type=list, multiplicity=Multiplicity(1, "*"), synonyms=["The range of the TACs."])
TaiRange.attributes={TaiRange_plmnId, TaiRange_tacRangeList}

sNssaiSmfInfoItem = Class(name="sNssaiSmfInfoItem")

# sNssaiSmfInfoItem class attributes and methods
sNssaiSmfInfoItem_dnnSmfInfoList: Property = Property(name="dnnSmfInfoList", type=list, multiplicity=Multiplicity(1, "*"), synonyms=["List of parameters supported by the SMF per DNN."])
sNssaiSmfInfoItem_sNssai: Property = Property(name="sNssai", type=list, multiplicity=Multiplicity(1, "*"), synonyms=["Supported S-NSSAI."])
sNssaiSmfInfoItem.attributes={sNssaiSmfInfoItem_dnnSmfInfoList, sNssaiSmfInfoItem_sNssai}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-nfprofile",
    types={AccessType, DataSetId, DnnSmfInfoItem, DnnUpfInfoItem, Guami, IdentityRange, InterfaceUpfInfoItem, N2InterfaceAmfInfo, NFProfile, NFStatus, PduSessionType, PlmnSnssai, Snssai, SnssaiUpfInfoItem, SupiRange, TacRange, Tai, TaiRange, UPInterfaceType, sNssaiSmfInfoItem},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["NF profile class."]
