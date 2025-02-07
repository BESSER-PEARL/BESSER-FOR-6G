# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
NFProfile = Class(name="NFProfile")

# NFProfile class attributes and methods
NFProfile_nfInstanceID: Property = Property(name="nfInstanceID", type=StringType)
NFProfile_nfType: Property = Property(name="nfType", type=types3gpp:NfType)
NFProfile_nfStatus: Property = Property(name="nfStatus", type=NFStatus)
NFProfile_heartBeatTimer: Property = Property(name="heartBeatTimer", type=IntegerType)
NFProfile_fqdn: Property = Property(name="fqdn", type=inet:domain-name)
NFProfile_interPlmnFqdn: Property = Property(name="interPlmnFqdn", type=inet:domain-name)
NFProfile_priority: Property = Property(name="priority", type=IntegerType)
NFProfile_capacity: Property = Property(name="capacity", type=IntegerType)
NFProfile_load: Property = Property(name="load", type=types3gpp:Load)
NFProfile_locality: Property = Property(name="locality", type=StringType)
NFProfile_customInfo: Property = Property(name="customInfo", type=StringType)
NFProfile_recoveryTime: Property = Property(name="recoveryTime", type=yang:date-and-time)
NFProfile_nfServicePersistence: Property = Property(name="nfServicePersistence", type=BooleanType)
NFProfile_nfProfileChangesSupportInd: Property = Property(name="nfProfileChangesSupportInd", type=BooleanType)
NFProfile_nfProfileChangesInd: Property = Property(name="nfProfileChangesInd", type=BooleanType)
NFProfile_plmnList: Property = Property(name="plmnList", type=list)
NFProfile_sNssais: Property = Property(name="sNssais", type=list)
NFProfile_perPlmnSnssaiList: Property = Property(name="perPlmnSnssaiList", type=list)
NFProfile_allowedPlmns: Property = Property(name="allowedPlmns", type=list)
NFProfile_allowedNssais: Property = Property(name="allowedNssais", type=list)
NFProfile_nrfInfo: Property = Property(name="nrfInfo", type=list)
NFProfile_nfServices: Property = Property(name="nfServices", type=list)
NFProfile_defaultNotificationSubscriptions: Property = Property(name="defaultNotificationSubscriptions", type=list)
NFProfile.attributes={NFProfile_nfInstanceID, NFProfile_nfType, NFProfile_nfStatus, NFProfile_heartBeatTimer, NFProfile_fqdn, NFProfile_interPlmnFqdn, NFProfile_priority, NFProfile_capacity, NFProfile_load, NFProfile_locality, NFProfile_customInfo, NFProfile_recoveryTime, NFProfile_nfServicePersistence, NFProfile_nfProfileChangesSupportInd, NFProfile_nfProfileChangesInd, NFProfile_plmnList, NFProfile_sNssais, NFProfile_perPlmnSnssaiList, NFProfile_allowedPlmns, NFProfile_allowedNssais, NFProfile_nrfInfo, NFProfile_nfServices, NFProfile_defaultNotificationSubscriptions}

N2InterfaceAmfInfo = Class(name="N2InterfaceAmfInfo")

# N2InterfaceAmfInfo class attributes and methods
N2InterfaceAmfInfo_amfName: Property = Property(name="amfName", type=StringType)
N2InterfaceAmfInfo.attributes={N2InterfaceAmfInfo_amfName}

sNssaiSmfInfoItem = Class(name="sNssaiSmfInfoItem")

# sNssaiSmfInfoItem class attributes and methods
sNssaiSmfInfoItem_sNssai: Property = Property(name="sNssai", type=list)
sNssaiSmfInfoItem_dnnSmfInfoList: Property = Property(name="dnnSmfInfoList", type=list)
sNssaiSmfInfoItem.attributes={sNssaiSmfInfoItem_sNssai, sNssaiSmfInfoItem_dnnSmfInfoList}

DnnSmfInfoItem = Class(name="DnnSmfInfoItem")

# DnnSmfInfoItem class attributes and methods
DnnSmfInfoItem_dnn: Property = Property(name="dnn", type=StringType)
DnnSmfInfoItem.attributes={DnnSmfInfoItem_dnn}

PlmnSnssai = Class(name="PlmnSnssai")

# PlmnSnssai class attributes and methods
PlmnSnssai_plmnId: Property = Property(name="plmnId", type=list)
PlmnSnssai_sNssaiList: Property = Property(name="sNssaiList", type=list)
PlmnSnssai.attributes={PlmnSnssai_plmnId, PlmnSnssai_sNssaiList}

SupiRange = Class(name="SupiRange")

# SupiRange class attributes and methods
SupiRange_start: Property = Property(name="start", type=StringType)
SupiRange_end: Property = Property(name="end", type=StringType)
SupiRange_pattern: Property = Property(name="pattern", type=StringType)
SupiRange.attributes={SupiRange_start, SupiRange_end, SupiRange_pattern}

IdentityRange = Class(name="IdentityRange")

# IdentityRange class attributes and methods
IdentityRange_start: Property = Property(name="start", type=StringType)
IdentityRange_end: Property = Property(name="end", type=StringType)
IdentityRange_pattern: Property = Property(name="pattern", type=StringType)
IdentityRange.attributes={IdentityRange_start, IdentityRange_end, IdentityRange_pattern}

TacRange = Class(name="TacRange")

# TacRange class attributes and methods
TacRange_start: Property = Property(name="start", type=StringType)
TacRange_end: Property = Property(name="end", type=StringType)
TacRange_pattern: Property = Property(name="pattern", type=StringType)
TacRange.attributes={TacRange_start, TacRange_end, TacRange_pattern}

SnssaiUpfInfoItem = Class(name="SnssaiUpfInfoItem")

# SnssaiUpfInfoItem class attributes and methods
SnssaiUpfInfoItem_sNssai: Property = Property(name="sNssai", type=list)
SnssaiUpfInfoItem_dnnUpfInfoList: Property = Property(name="dnnUpfInfoList", type=list)
SnssaiUpfInfoItem.attributes={SnssaiUpfInfoItem_sNssai, SnssaiUpfInfoItem_dnnUpfInfoList}

DnnUpfInfoItem = Class(name="DnnUpfInfoItem")

# DnnUpfInfoItem class attributes and methods
DnnUpfInfoItem_dnn: Property = Property(name="dnn", type=StringType)
DnnUpfInfoItem.attributes={DnnUpfInfoItem_dnn}

Snssai = Class(name="Snssai")

# Snssai class attributes and methods
Snssai_sst: Property = Property(name="sst", type=IntegerType)
Snssai_sd: Property = Property(name="sd", type=StringType)
Snssai.attributes={Snssai_sst, Snssai_sd}

Guami = Class(name="Guami")

# Guami class attributes and methods
Guami_plmnId: Property = Property(name="plmnId", type=list)
Guami_amfId: Property = Property(name="amfId", type=list)
Guami.attributes={Guami_plmnId, Guami_amfId}

Tai = Class(name="Tai")

# Tai class attributes and methods
Tai_tac: Property = Property(name="tac", type=types3gpp:Tac)
Tai_plmnId: Property = Property(name="plmnId", type=list)
Tai.attributes={Tai_tac, Tai_plmnId}

InterfaceUpfInfoItem = Class(name="InterfaceUpfInfoItem")

# InterfaceUpfInfoItem class attributes and methods
InterfaceUpfInfoItem_interfaceType: Property = Property(name="interfaceType", type=UPInterfaceType)
InterfaceUpfInfoItem_networkInstance: Property = Property(name="networkInstance", type=StringType)
InterfaceUpfInfoItem.attributes={InterfaceUpfInfoItem_interfaceType, InterfaceUpfInfoItem_networkInstance}

TaiRange = Class(name="TaiRange")

# TaiRange class attributes and methods
TaiRange_plmnId: Property = Property(name="plmnId", type=list)
TaiRange_tacRangeList: Property = Property(name="tacRangeList", type=list)
TaiRange.attributes={TaiRange_plmnId, TaiRange_tacRangeList}

