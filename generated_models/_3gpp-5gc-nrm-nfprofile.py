# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

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
DnnSmfInfoItem_dnn: Property = Property(name="dnn", type=StringType)
DnnSmfInfoItem.attributes={DnnSmfInfoItem_dnn}

DnnUpfInfoItem = Class(name="DnnUpfInfoItem")

# DnnUpfInfoItem class attributes and methods
DnnUpfInfoItem_dnn: Property = Property(name="dnn", type=StringType)
DnnUpfInfoItem.attributes={DnnUpfInfoItem_dnn}

Guami = Class(name="Guami")

# Guami class attributes and methods
Guami_amfId: Property = Property(name="amfId", type=list)
Guami_plmnId: Property = Property(name="plmnId", type=list)
Guami.attributes={Guami_amfId, Guami_plmnId}

IdentityRange = Class(name="IdentityRange")

# IdentityRange class attributes and methods
IdentityRange_end: Property = Property(name="end", type=StringType)
IdentityRange_pattern: Property = Property(name="pattern", type=StringType)
IdentityRange_start: Property = Property(name="start", type=StringType)
IdentityRange.attributes={IdentityRange_end, IdentityRange_pattern, IdentityRange_start}

InterfaceUpfInfoItem = Class(name="InterfaceUpfInfoItem")

# InterfaceUpfInfoItem class attributes and methods
InterfaceUpfInfoItem_interfaceType: Property = Property(name="interfaceType", type=StringType)
InterfaceUpfInfoItem_networkInstance: Property = Property(name="networkInstance", type=StringType)
InterfaceUpfInfoItem.attributes={InterfaceUpfInfoItem_interfaceType, InterfaceUpfInfoItem_networkInstance}

N2InterfaceAmfInfo = Class(name="N2InterfaceAmfInfo")

# N2InterfaceAmfInfo class attributes and methods
N2InterfaceAmfInfo_amfName: Property = Property(name="amfName", type=StringType)
N2InterfaceAmfInfo.attributes={N2InterfaceAmfInfo_amfName}

NFProfile = Class(name="NFProfile")

# NFProfile class attributes and methods
NFProfile_allowedNssais: Property = Property(name="allowedNssais", type=list)
NFProfile_allowedPlmns: Property = Property(name="allowedPlmns", type=list)
NFProfile_capacity: Property = Property(name="capacity", type=IntegerType)
NFProfile_customInfo: Property = Property(name="customInfo", type=StringType)
NFProfile_defaultNotificationSubscriptions: Property = Property(name="defaultNotificationSubscriptions", type=list)
NFProfile_fqdn: Property = Property(name="fqdn", type=StringType)
NFProfile_heartBeatTimer: Property = Property(name="heartBeatTimer", type=IntegerType)
NFProfile_interPlmnFqdn: Property = Property(name="interPlmnFqdn", type=StringType)
NFProfile_load: Property = Property(name="load", type=StringType)
NFProfile_locality: Property = Property(name="locality", type=StringType)
NFProfile_nfInstanceID: Property = Property(name="nfInstanceID", type=StringType)
NFProfile_nfProfileChangesInd: Property = Property(name="nfProfileChangesInd", type=BooleanType)
NFProfile_nfProfileChangesSupportInd: Property = Property(name="nfProfileChangesSupportInd", type=BooleanType)
NFProfile_nfServicePersistence: Property = Property(name="nfServicePersistence", type=BooleanType)
NFProfile_nfServices: Property = Property(name="nfServices", type=list)
NFProfile_nfStatus: Property = Property(name="nfStatus", type=StringType)
NFProfile_nfType: Property = Property(name="nfType", type=StringType)
NFProfile_nrfInfo: Property = Property(name="nrfInfo", type=list)
NFProfile_perPlmnSnssaiList: Property = Property(name="perPlmnSnssaiList", type=list)
NFProfile_plmnList: Property = Property(name="plmnList", type=list)
NFProfile_priority: Property = Property(name="priority", type=IntegerType)
NFProfile_recoveryTime: Property = Property(name="recoveryTime", type=StringType)
NFProfile_sNssais: Property = Property(name="sNssais", type=list)
NFProfile.attributes={NFProfile_allowedNssais, NFProfile_allowedPlmns, NFProfile_capacity, NFProfile_customInfo, NFProfile_defaultNotificationSubscriptions, NFProfile_fqdn, NFProfile_heartBeatTimer, NFProfile_interPlmnFqdn, NFProfile_load, NFProfile_locality, NFProfile_nfInstanceID, NFProfile_nfProfileChangesInd, NFProfile_nfProfileChangesSupportInd, NFProfile_nfServicePersistence, NFProfile_nfServices, NFProfile_nfStatus, NFProfile_nfType, NFProfile_nrfInfo, NFProfile_perPlmnSnssaiList, NFProfile_plmnList, NFProfile_priority, NFProfile_recoveryTime, NFProfile_sNssais}

PlmnSnssai = Class(name="PlmnSnssai")

# PlmnSnssai class attributes and methods
PlmnSnssai_plmnId: Property = Property(name="plmnId", type=list)
PlmnSnssai_sNssaiList: Property = Property(name="sNssaiList", type=list)
PlmnSnssai.attributes={PlmnSnssai_plmnId, PlmnSnssai_sNssaiList}

Snssai = Class(name="Snssai")

# Snssai class attributes and methods
Snssai_sd: Property = Property(name="sd", type=StringType)
Snssai_sst: Property = Property(name="sst", type=IntegerType)
Snssai.attributes={Snssai_sd, Snssai_sst}

SnssaiUpfInfoItem = Class(name="SnssaiUpfInfoItem")

# SnssaiUpfInfoItem class attributes and methods
SnssaiUpfInfoItem_dnnUpfInfoList: Property = Property(name="dnnUpfInfoList", type=list)
SnssaiUpfInfoItem_sNssai: Property = Property(name="sNssai", type=list)
SnssaiUpfInfoItem.attributes={SnssaiUpfInfoItem_dnnUpfInfoList, SnssaiUpfInfoItem_sNssai}

SupiRange = Class(name="SupiRange")

# SupiRange class attributes and methods
SupiRange_end: Property = Property(name="end", type=StringType)
SupiRange_pattern: Property = Property(name="pattern", type=StringType)
SupiRange_start: Property = Property(name="start", type=StringType)
SupiRange.attributes={SupiRange_end, SupiRange_pattern, SupiRange_start}

TacRange = Class(name="TacRange")

# TacRange class attributes and methods
TacRange_end: Property = Property(name="end", type=StringType)
TacRange_pattern: Property = Property(name="pattern", type=StringType)
TacRange_start: Property = Property(name="start", type=StringType)
TacRange.attributes={TacRange_end, TacRange_pattern, TacRange_start}

Tai = Class(name="Tai")

# Tai class attributes and methods
Tai_plmnId: Property = Property(name="plmnId", type=list)
Tai_tac: Property = Property(name="tac", type=StringType)
Tai.attributes={Tai_plmnId, Tai_tac}

TaiRange = Class(name="TaiRange")

# TaiRange class attributes and methods
TaiRange_plmnId: Property = Property(name="plmnId", type=list)
TaiRange_tacRangeList: Property = Property(name="tacRangeList", type=list)
TaiRange.attributes={TaiRange_plmnId, TaiRange_tacRangeList}

sNssaiSmfInfoItem = Class(name="sNssaiSmfInfoItem")

# sNssaiSmfInfoItem class attributes and methods
sNssaiSmfInfoItem_dnnSmfInfoList: Property = Property(name="dnnSmfInfoList", type=list)
sNssaiSmfInfoItem_sNssai: Property = Property(name="sNssai", type=list)
sNssaiSmfInfoItem.attributes={sNssaiSmfInfoItem_dnnSmfInfoList, sNssaiSmfInfoItem_sNssai}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-nfprofile",
    types={AccessType, DataSetId, DnnSmfInfoItem, DnnUpfInfoItem, Guami, IdentityRange, InterfaceUpfInfoItem, N2InterfaceAmfInfo, NFProfile, NFStatus, PduSessionType, PlmnSnssai, Snssai, SnssaiUpfInfoItem, SupiRange, TacRange, Tai, TaiRange, UPInterfaceType, sNssaiSmfInfoItem},
    associations={},
    generalizations={}
)
