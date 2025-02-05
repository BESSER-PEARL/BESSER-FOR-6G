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
NFStatus: Enumeration = Enumeration(
    name="NFStatus",
    literals={
            EnumerationLiteral(name="REGISTERED"),
			EnumerationLiteral(name="SUSPENDED")
    }
)

DataSetId: Enumeration = Enumeration(
    name="DataSetId",
    literals={
            EnumerationLiteral(name="SUBSCRIPTION"),
			EnumerationLiteral(name="POLICY"),
			EnumerationLiteral(name="EXPOSURE"),
			EnumerationLiteral(name="APPLICATION")
    }
)

PduSessionType: Enumeration = Enumeration(
    name="PduSessionType",
    literals={
            EnumerationLiteral(name="IPV4"),
			EnumerationLiteral(name="IPV6"),
			EnumerationLiteral(name="IPV4V6"),
			EnumerationLiteral(name="UNSTRUCTURED"),
			EnumerationLiteral(name="ETHERNET")
    }
)

UPInterfaceType: Enumeration = Enumeration(
    name="UPInterfaceType",
    literals={
            EnumerationLiteral(name="N3"),
			EnumerationLiteral(name="N6"),
			EnumerationLiteral(name="N9")
    }
)

AccessType: Enumeration = Enumeration(
    name="AccessType",
    literals={
            EnumerationLiteral(name="3GPP_ACCESS"),
			EnumerationLiteral(name="NON_3GPP_ACCESS")
    }
)

# Classes
N2InterfaceAmfInfo = Class(name="N2InterfaceAmfInfo")
sNssaiSmfInfoItem = Class(name="sNssaiSmfInfoItem")
DnnSmfInfoItem = Class(name="DnnSmfInfoItem")
PlmnSnssai = Class(name="PlmnSnssai")
NFProfileGrp = Class(name="NFProfileGrp")
SupiRange = Class(name="SupiRange")
IdentityRange = Class(name="IdentityRange")
TacRange = Class(name="TacRange")
SnssaiUpfInfoItem = Class(name="SnssaiUpfInfoItem")
DnnUpfInfoItem = Class(name="DnnUpfInfoItem")
Snssai = Class(name="Snssai")
Guami = Class(name="Guami")
Tai = Class(name="Tai")
InterfaceUpfInfoItem = Class(name="InterfaceUpfInfoItem")
TaiRange = Class(name="TaiRange")

# N2InterfaceAmfInfo class attributes and methods
N2InterfaceAmfInfo_amfName: Property = Property(name="amfName", type=StringType)
N2InterfaceAmfInfo.attributes={N2InterfaceAmfInfo_amfName}

# sNssaiSmfInfoItem class attributes and methods
sNssaiSmfInfoItem_sNssai: Property = Property(name="sNssai", type=list)
sNssaiSmfInfoItem_dnnSmfInfoList: Property = Property(name="dnnSmfInfoList", type=list)
sNssaiSmfInfoItem.attributes={sNssaiSmfInfoItem_sNssai, sNssaiSmfInfoItem_dnnSmfInfoList}

# DnnSmfInfoItem class attributes and methods
DnnSmfInfoItem_dnn: Property = Property(name="dnn", type=StringType)
DnnSmfInfoItem.attributes={DnnSmfInfoItem_dnn}

# PlmnSnssai class attributes and methods
PlmnSnssai_plmnId: Property = Property(name="plmnId", type=list)
PlmnSnssai_sNssaiList: Property = Property(name="sNssaiList", type=list)
PlmnSnssai.attributes={PlmnSnssai_sNssaiList, PlmnSnssai_plmnId}

# NFProfileGrp class attributes and methods
NFProfileGrp_nfInstanceID: Property = Property(name="nfInstanceID", type=StringType)
NFProfileGrp_nfType: Property = Property(name="nfType", type=types3gpp:NfType)
NFProfileGrp_nfStatus: Property = Property(name="nfStatus", type=NFStatus)
NFProfileGrp_heartBeatTimer: Property = Property(name="heartBeatTimer", type=IntegerType)
NFProfileGrp_fqdn: Property = Property(name="fqdn", type=inet:domain-name)
NFProfileGrp_interPlmnFqdn: Property = Property(name="interPlmnFqdn", type=inet:domain-name)
NFProfileGrp_priority: Property = Property(name="priority", type=IntegerType)
NFProfileGrp_capacity: Property = Property(name="capacity", type=IntegerType)
NFProfileGrp_load: Property = Property(name="load", type=types3gpp:Load)
NFProfileGrp_locality: Property = Property(name="locality", type=StringType)
NFProfileGrp_customInfo: Property = Property(name="customInfo", type=StringType)
NFProfileGrp_recoveryTime: Property = Property(name="recoveryTime", type=yang:date-and-time)
NFProfileGrp_nfServicePersistence: Property = Property(name="nfServicePersistence", type=BooleanType)
NFProfileGrp_nfProfileChangesSupportInd: Property = Property(name="nfProfileChangesSupportInd", type=BooleanType)
NFProfileGrp_nfProfileChangesInd: Property = Property(name="nfProfileChangesInd", type=BooleanType)
NFProfileGrp_plmnList: Property = Property(name="plmnList", type=list)
NFProfileGrp_sNssais: Property = Property(name="sNssais", type=list)
NFProfileGrp_perPlmnSnssaiList: Property = Property(name="perPlmnSnssaiList", type=list)
NFProfileGrp_allowedPlmns: Property = Property(name="allowedPlmns", type=list)
NFProfileGrp_allowedNssais: Property = Property(name="allowedNssais", type=list)
NFProfileGrp_nrfInfo: Property = Property(name="nrfInfo", type=list)
NFProfileGrp_nfServices: Property = Property(name="nfServices", type=list)
NFProfileGrp_defaultNotificationSubscriptions: Property = Property(name="defaultNotificationSubscriptions", type=list)
NFProfileGrp.attributes={NFProfileGrp_nfType, NFProfileGrp_nfStatus, NFProfileGrp_heartBeatTimer, NFProfileGrp_fqdn, NFProfileGrp_interPlmnFqdn, NFProfileGrp_priority, NFProfileGrp_capacity, NFProfileGrp_load, NFProfileGrp_nfServices, NFProfileGrp_locality, NFProfileGrp_customInfo, NFProfileGrp_nrfInfo, NFProfileGrp_recoveryTime, NFProfileGrp_nfServicePersistence, NFProfileGrp_nfProfileChangesSupportInd, NFProfileGrp_nfProfileChangesInd, NFProfileGrp_plmnList, NFProfileGrp_sNssais, NFProfileGrp_perPlmnSnssaiList, NFProfileGrp_allowedPlmns, NFProfileGrp_defaultNotificationSubscriptions, NFProfileGrp_allowedNssais, NFProfileGrp_nfInstanceID}

# SupiRange class attributes and methods
SupiRange_start: Property = Property(name="start", type=StringType)
SupiRange_end: Property = Property(name="end", type=StringType)
SupiRange_pattern: Property = Property(name="pattern", type=StringType)
SupiRange.attributes={SupiRange_pattern, SupiRange_start, SupiRange_end}

# IdentityRange class attributes and methods
IdentityRange_start: Property = Property(name="start", type=StringType)
IdentityRange_end: Property = Property(name="end", type=StringType)
IdentityRange_pattern: Property = Property(name="pattern", type=StringType)
IdentityRange.attributes={IdentityRange_start, IdentityRange_end, IdentityRange_pattern}

# TacRange class attributes and methods
TacRange_start: Property = Property(name="start", type=StringType)
TacRange_end: Property = Property(name="end", type=StringType)
TacRange_pattern: Property = Property(name="pattern", type=StringType)
TacRange.attributes={TacRange_end, TacRange_start, TacRange_pattern}

# SnssaiUpfInfoItem class attributes and methods
SnssaiUpfInfoItem_sNssai: Property = Property(name="sNssai", type=list)
SnssaiUpfInfoItem_dnnUpfInfoList: Property = Property(name="dnnUpfInfoList", type=list)
SnssaiUpfInfoItem.attributes={SnssaiUpfInfoItem_sNssai, SnssaiUpfInfoItem_dnnUpfInfoList}

# DnnUpfInfoItem class attributes and methods
DnnUpfInfoItem_dnn: Property = Property(name="dnn", type=StringType)
DnnUpfInfoItem.attributes={DnnUpfInfoItem_dnn}

# Snssai class attributes and methods
Snssai_sst: Property = Property(name="sst", type=IntegerType)
Snssai_sd: Property = Property(name="sd", type=StringType)
Snssai.attributes={Snssai_sd, Snssai_sst}

# Guami class attributes and methods
Guami_plmnId: Property = Property(name="plmnId", type=list)
Guami_amfId: Property = Property(name="amfId", type=list)
Guami.attributes={Guami_plmnId, Guami_amfId}

# Tai class attributes and methods
Tai_tac: Property = Property(name="tac", type=types3gpp:Tac)
Tai_plmnId: Property = Property(name="plmnId", type=list)
Tai.attributes={Tai_tac, Tai_plmnId}

# InterfaceUpfInfoItem class attributes and methods
InterfaceUpfInfoItem_interfaceType: Property = Property(name="interfaceType", type=UPInterfaceType)
InterfaceUpfInfoItem_networkInstance: Property = Property(name="networkInstance", type=StringType)
InterfaceUpfInfoItem.attributes={InterfaceUpfInfoItem_networkInstance, InterfaceUpfInfoItem_interfaceType}

# TaiRange class attributes and methods
TaiRange_plmnId: Property = Property(name="plmnId", type=list)
TaiRange_tacRangeList: Property = Property(name="tacRangeList", type=list)
TaiRange.attributes={TaiRange_tacRangeList, TaiRange_plmnId}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-nfprofile",
    types={N2InterfaceAmfInfo, sNssaiSmfInfoItem, DnnSmfInfoItem, PlmnSnssai, NFProfileGrp, SupiRange, IdentityRange, TacRange, SnssaiUpfInfoItem, DnnUpfInfoItem, Snssai, Guami, Tai, InterfaceUpfInfoItem, TaiRange, NFStatus, DataSetId, PduSessionType, UPInterfaceType, AccessType, types3gpp_model, mf3gpp_model, me3gpp_model, top3gpp_model, types5g3gpp_model, inet_model, subnet3gpp_model, Conf5QIs3gpp_model, eprp3gpp_model, af3gpp_model, amf3gpp_model, ausf3gpp_model, dn3gpp_model, lmf3gpp_model, n3iwf3gpp_model, ngeir3gpp_model, nrf3gpp_model, nssf3gpp_model, pcf3gpp_model, sepp3gpp_model, smf3gpp_model, smsf3gpp_model, udm3gpp_model, upf3gpp_model, yang_model, nfs3gpp_model},
    associations={},
    generalizations={}
)
