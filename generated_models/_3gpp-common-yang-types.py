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
from generated_models._3gpp_common_fm import domain_model as fm3gpp_model
from generated_models._3gpp_common_managed_element import domain_model as me3gpp_model
from generated_models._3gpp_common_managed_function import domain_model as mf3gpp_model
from generated_models._3gpp_common_measurements import domain_model as meas3gpp_model
from generated_models._3gpp_common_subnetwork import domain_model as subnet3gpp_model
from generated_models._3gpp_common_subscription_control import domain_model as subscr3gpp_model
from generated_models._3gpp_common_top import domain_model as top3gpp_model
from generated_models._3gpp_common_trace import domain_model as trace3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Enumerations
usageState: Enumeration = Enumeration(
    name="usageState",
    literals={
            EnumerationLiteral(name="IDLE"),
			EnumerationLiteral(name="ACTIVE"),
			EnumerationLiteral(name="BUSY")
    }
)

OperationalState: Enumeration = Enumeration(
    name="OperationalState",
    literals={
            EnumerationLiteral(name="DISABLED"),
			EnumerationLiteral(name="ENABLED")
    }
)

AdministrativeState: Enumeration = Enumeration(
    name="AdministrativeState",
    literals={
            EnumerationLiteral(name="LOCKED"),
			EnumerationLiteral(name="UNLOCKED"),
			EnumerationLiteral(name="SHUTTINGDOWN")
    }
)

AvailabilityStatus: Enumeration = Enumeration(
    name="AvailabilityStatus",
    literals={
            EnumerationLiteral(name="IN_TEST"),
			EnumerationLiteral(name="FAILED"),
			EnumerationLiteral(name="POWER_OFF"),
			EnumerationLiteral(name="OFF_LINE"),
			EnumerationLiteral(name="OFF_DUTY"),
			EnumerationLiteral(name="DEPENDENCY"),
			EnumerationLiteral(name="DEGRADED"),
			EnumerationLiteral(name="NOT_INSTALLED"),
			EnumerationLiteral(name="LOG_FULL")
    }
)

CellState: Enumeration = Enumeration(
    name="CellState",
    literals={
            EnumerationLiteral(name="IDLE"),
			EnumerationLiteral(name="INACTIVE"),
			EnumerationLiteral(name="ACTIVE")
    }
)

NfType: Enumeration = Enumeration(
    name="NfType",
    literals={
            EnumerationLiteral(name="NRF"),
			EnumerationLiteral(name="UDM"),
			EnumerationLiteral(name="AMF"),
			EnumerationLiteral(name="SMF"),
			EnumerationLiteral(name="AUSF"),
			EnumerationLiteral(name="NEF"),
			EnumerationLiteral(name="PCF"),
			EnumerationLiteral(name="SMSF"),
			EnumerationLiteral(name="NSSF"),
			EnumerationLiteral(name="UDR"),
			EnumerationLiteral(name="LMF"),
			EnumerationLiteral(name="GMLC"),
			EnumerationLiteral(name="5G_EIR"),
			EnumerationLiteral(name="SEPP"),
			EnumerationLiteral(name="UPF"),
			EnumerationLiteral(name="N3IWF"),
			EnumerationLiteral(name="AF"),
			EnumerationLiteral(name="UDSF"),
			EnumerationLiteral(name="BSF"),
			EnumerationLiteral(name="CHF")
    }
)

NotificationType: Enumeration = Enumeration(
    name="NotificationType",
    literals={
            EnumerationLiteral(name="N1_MESSAGES"),
			EnumerationLiteral(name="N2_INFORMATION"),
			EnumerationLiteral(name="LOCATION_NOTIFICATION")
    }
)

N1MessageClass: Enumeration = Enumeration(
    name="N1MessageClass",
    literals={
            EnumerationLiteral(name="5GMM"),
			EnumerationLiteral(name="SM"),
			EnumerationLiteral(name="LPP"),
			EnumerationLiteral(name="SMS")
    }
)

N2InformationClass: Enumeration = Enumeration(
    name="N2InformationClass",
    literals={
            EnumerationLiteral(name="SM"),
			EnumerationLiteral(name="NRPPA"),
			EnumerationLiteral(name="PWS"),
			EnumerationLiteral(name="PWS_BCAL"),
			EnumerationLiteral(name="PWS_RF")
    }
)

UeMobilityLevel: Enumeration = Enumeration(
    name="UeMobilityLevel",
    literals={
            EnumerationLiteral(name="STATIONARY"),
			EnumerationLiteral(name="NOMADIC"),
			EnumerationLiteral(name="RESTRICTED_MOBILITY"),
			EnumerationLiteral(name="FULLY_MOBILITY")
    }
)

ResourceSharingLevel: Enumeration = Enumeration(
    name="ResourceSharingLevel",
    literals={
            EnumerationLiteral(name="SHARED"),
			EnumerationLiteral(name="NOT_SHARED")
    }
)

TxDirection: Enumeration = Enumeration(
    name="TxDirection",
    literals={
            EnumerationLiteral(name="DL"),
			EnumerationLiteral(name="UL"),
			EnumerationLiteral(name="DL_AND_UL")
    }
)

# Classes
ManagedNFProfile = Class(name="ManagedNFProfile")
SAP = Class(name="SAP")
PLMNId = Class(name="PLMNId")
AmfIdentifier = Class(name="AmfIdentifier")
DefaultNotificationSubscription = Class(name="DefaultNotificationSubscription")
Ipv4AddressRange = Class(name="Ipv4AddressRange")
Ipv6PrefixRange = Class(name="Ipv6PrefixRange")
AddressWithVlan = Class(name="AddressWithVlan")

# ManagedNFProfile class attributes and methods
ManagedNFProfile_idx: Property = Property(name="idx", type=IntegerType)
ManagedNFProfile_nfInstanceID: Property = Property(name="nfInstanceID", type=yang:uuid)
ManagedNFProfile_hostAddr: Property = Property(name="hostAddr", type=inet:host)
ManagedNFProfile_authzInfo: Property = Property(name="authzInfo", type=StringType)
ManagedNFProfile_location: Property = Property(name="location", type=StringType)
ManagedNFProfile_capacity: Property = Property(name="capacity", type=IntegerType)
ManagedNFProfile_nFSrvGroupId: Property = Property(name="nFSrvGroupId", type=StringType)
ManagedNFProfile_priority: Property = Property(name="priority", type=IntegerType)
ManagedNFProfile.attributes={ManagedNFProfile_nfInstanceID, ManagedNFProfile_authzInfo, ManagedNFProfile_hostAddr, ManagedNFProfile_capacity, ManagedNFProfile_nFSrvGroupId, ManagedNFProfile_location, ManagedNFProfile_idx, ManagedNFProfile_priority}

# SAP class attributes and methods
SAP_host: Property = Property(name="host", type=inet:host)
SAP_port: Property = Property(name="port", type=inet:port-number)
SAP.attributes={SAP_host, SAP_port}

# PLMNId class attributes and methods
PLMNId_mcc: Property = Property(name="mcc", type=Mcc)
PLMNId_mnc: Property = Property(name="mnc", type=Mnc)
PLMNId.attributes={PLMNId_mcc, PLMNId_mnc}

# AmfIdentifier class attributes and methods
AmfIdentifier_amfRegionId: Property = Property(name="amfRegionId", type=AmfRegionId)
AmfIdentifier_amfSetId: Property = Property(name="amfSetId", type=AmfSetId)
AmfIdentifier_amfPointer: Property = Property(name="amfPointer", type=AmfPointer)
AmfIdentifier.attributes={AmfIdentifier_amfSetId, AmfIdentifier_amfRegionId, AmfIdentifier_amfPointer}

# DefaultNotificationSubscription class attributes and methods
DefaultNotificationSubscription_notificationType: Property = Property(name="notificationType", type=NotificationType)
DefaultNotificationSubscription_callbackUri: Property = Property(name="callbackUri", type=inet:uri)
DefaultNotificationSubscription_n1MessageClass: Property = Property(name="n1MessageClass", type=N1MessageClass)
DefaultNotificationSubscription_n2InformationClass: Property = Property(name="n2InformationClass", type=N2InformationClass)
DefaultNotificationSubscription.attributes={DefaultNotificationSubscription_n2InformationClass, DefaultNotificationSubscription_n1MessageClass, DefaultNotificationSubscription_callbackUri, DefaultNotificationSubscription_notificationType}

# Ipv4AddressRange class attributes and methods
Ipv4AddressRange_start: Property = Property(name="start", type=inet:ipv4-address)
Ipv4AddressRange_end: Property = Property(name="end", type=inet:ipv4-address)
Ipv4AddressRange.attributes={Ipv4AddressRange_start, Ipv4AddressRange_end}

# Ipv6PrefixRange class attributes and methods
Ipv6PrefixRange_start: Property = Property(name="start", type=inet:ipv6-prefix)
Ipv6PrefixRange_end: Property = Property(name="end", type=inet:ipv6-prefix)
Ipv6PrefixRange.attributes={Ipv6PrefixRange_end, Ipv6PrefixRange_start}

# AddressWithVlan class attributes and methods
AddressWithVlan_ipAddress: Property = Property(name="ipAddress", type=inet:ip-address)
AddressWithVlan_vlanId: Property = Property(name="vlanId", type=IntegerType)
AddressWithVlan.attributes={AddressWithVlan_vlanId, AddressWithVlan_ipAddress}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-common-yang-types",
    types={ManagedNFProfile, SAP, PLMNId, AmfIdentifier, DefaultNotificationSubscription, Ipv4AddressRange, Ipv6PrefixRange, AddressWithVlan, usageState, OperationalState, AdministrativeState, AvailabilityStatus, CellState, NfType, NotificationType, N1MessageClass, N2InformationClass, UeMobilityLevel, ResourceSharingLevel, TxDirection, types3gpp_model, mf3gpp_model, me3gpp_model, top3gpp_model, types5g3gpp_model, inet_model, subnet3gpp_model, Conf5QIs3gpp_model, eprp3gpp_model, af3gpp_model, amf3gpp_model, ausf3gpp_model, dn3gpp_model, lmf3gpp_model, n3iwf3gpp_model, ngeir3gpp_model, nrf3gpp_model, nssf3gpp_model, pcf3gpp_model, sepp3gpp_model, smf3gpp_model, smsf3gpp_model, udm3gpp_model, upf3gpp_model, yang_model, nfs3gpp_model, nfp3gpp_model, meas3gpp_model, subscr3gpp_model, fm3gpp_model, trace3gpp_model, yangmnt_model},
    associations={},
    generalizations={}
)
