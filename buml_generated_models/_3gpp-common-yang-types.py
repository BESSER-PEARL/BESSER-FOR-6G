# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models.ietf_inet_types import domain_model as inet_model
from buml_generated_models.ietf_yang_types import domain_model as yang_model

# Enumerations
AdministrativeState = Enumeration(name="AdministrativeState")
AdministrativeState_LOCKED = EnumerationLiteral(name="LOCKED", owner=AdministrativeState, synonyms=["The resource is administratively prohibited from performing services for its users."])
AdministrativeState_SHUTTINGDOWN = EnumerationLiteral(name="SHUTTINGDOWN", owner=AdministrativeState, synonyms=["Use of the resource is administratively permitted to existing instances of use only. While the system remains in the shutting down state the manager or the managed element may at any time cause the resource to transition to the locked state."])
AdministrativeState_UNLOCKED = EnumerationLiteral(name="UNLOCKED", owner=AdministrativeState, synonyms=["The resource is administratively permitted to perform services for its users. This is independent of its inherent operability."])
AdministrativeState.literals = {AdministrativeState_LOCKED, AdministrativeState_SHUTTINGDOWN, AdministrativeState_UNLOCKED}

AvailabilityStatus = Enumeration(name="AvailabilityStatus")
AvailabilityStatus_DEGRADED = EnumerationLiteral(name="DEGRADED", owner=AvailabilityStatus)
AvailabilityStatus_DEPENDENCY = EnumerationLiteral(name="DEPENDENCY", owner=AvailabilityStatus)
AvailabilityStatus_FAILED = EnumerationLiteral(name="FAILED", owner=AvailabilityStatus)
AvailabilityStatus_IN_TEST = EnumerationLiteral(name="IN_TEST", owner=AvailabilityStatus)
AvailabilityStatus_LOG_FULL = EnumerationLiteral(name="LOG_FULL", owner=AvailabilityStatus)
AvailabilityStatus_NOT_INSTALLED = EnumerationLiteral(name="NOT_INSTALLED", owner=AvailabilityStatus)
AvailabilityStatus_OFF_DUTY = EnumerationLiteral(name="OFF_DUTY", owner=AvailabilityStatus)
AvailabilityStatus_OFF_LINE = EnumerationLiteral(name="OFF_LINE", owner=AvailabilityStatus)
AvailabilityStatus_POWER_OFF = EnumerationLiteral(name="POWER_OFF", owner=AvailabilityStatus)
AvailabilityStatus.literals = {AvailabilityStatus_DEGRADED, AvailabilityStatus_DEPENDENCY, AvailabilityStatus_FAILED, AvailabilityStatus_IN_TEST, AvailabilityStatus_LOG_FULL, AvailabilityStatus_NOT_INSTALLED, AvailabilityStatus_OFF_DUTY, AvailabilityStatus_OFF_LINE, AvailabilityStatus_POWER_OFF}

CellState = Enumeration(name="CellState")
CellState_ACTIVE = EnumerationLiteral(name="ACTIVE", owner=CellState)
CellState_IDLE = EnumerationLiteral(name="IDLE", owner=CellState)
CellState_INACTIVE = EnumerationLiteral(name="INACTIVE", owner=CellState)
CellState.literals = {CellState_ACTIVE, CellState_IDLE, CellState_INACTIVE}

N1MessageClass = Enumeration(name="N1MessageClass")
N1MessageClass_5GMM = EnumerationLiteral(name="5GMM", owner=N1MessageClass)
N1MessageClass_LPP = EnumerationLiteral(name="LPP", owner=N1MessageClass)
N1MessageClass_SM = EnumerationLiteral(name="SM", owner=N1MessageClass)
N1MessageClass_SMS = EnumerationLiteral(name="SMS", owner=N1MessageClass)
N1MessageClass.literals = {N1MessageClass_5GMM, N1MessageClass_LPP, N1MessageClass_SM, N1MessageClass_SMS}

N2InformationClass = Enumeration(name="N2InformationClass")
N2InformationClass_NRPPA = EnumerationLiteral(name="NRPPA", owner=N2InformationClass)
N2InformationClass_PWS = EnumerationLiteral(name="PWS", owner=N2InformationClass)
N2InformationClass_PWS_BCAL = EnumerationLiteral(name="PWS_BCAL", owner=N2InformationClass)
N2InformationClass_PWS_RF = EnumerationLiteral(name="PWS_RF", owner=N2InformationClass)
N2InformationClass_SM = EnumerationLiteral(name="SM", owner=N2InformationClass)
N2InformationClass.literals = {N2InformationClass_NRPPA, N2InformationClass_PWS, N2InformationClass_PWS_BCAL, N2InformationClass_PWS_RF, N2InformationClass_SM}

NfType = Enumeration(name="NfType")
NfType_5G_EIR = EnumerationLiteral(name="5G_EIR", owner=NfType)
NfType_AF = EnumerationLiteral(name="AF", owner=NfType)
NfType_AMF = EnumerationLiteral(name="AMF", owner=NfType)
NfType_AUSF = EnumerationLiteral(name="AUSF", owner=NfType)
NfType_BSF = EnumerationLiteral(name="BSF", owner=NfType)
NfType_CHF = EnumerationLiteral(name="CHF", owner=NfType)
NfType_GMLC = EnumerationLiteral(name="GMLC", owner=NfType)
NfType_LMF = EnumerationLiteral(name="LMF", owner=NfType)
NfType_N3IWF = EnumerationLiteral(name="N3IWF", owner=NfType)
NfType_NEF = EnumerationLiteral(name="NEF", owner=NfType)
NfType_NRF = EnumerationLiteral(name="NRF", owner=NfType)
NfType_NSSF = EnumerationLiteral(name="NSSF", owner=NfType)
NfType_PCF = EnumerationLiteral(name="PCF", owner=NfType)
NfType_SEPP = EnumerationLiteral(name="SEPP", owner=NfType)
NfType_SMF = EnumerationLiteral(name="SMF", owner=NfType)
NfType_SMSF = EnumerationLiteral(name="SMSF", owner=NfType)
NfType_UDM = EnumerationLiteral(name="UDM", owner=NfType)
NfType_UDR = EnumerationLiteral(name="UDR", owner=NfType)
NfType_UDSF = EnumerationLiteral(name="UDSF", owner=NfType)
NfType_UPF = EnumerationLiteral(name="UPF", owner=NfType)
NfType.literals = {NfType_5G_EIR, NfType_AF, NfType_AMF, NfType_AUSF, NfType_BSF, NfType_CHF, NfType_GMLC, NfType_LMF, NfType_N3IWF, NfType_NEF, NfType_NRF, NfType_NSSF, NfType_PCF, NfType_SEPP, NfType_SMF, NfType_SMSF, NfType_UDM, NfType_UDR, NfType_UDSF, NfType_UPF}

NotificationType = Enumeration(name="NotificationType")
NotificationType_LOCATION_NOTIFICATION = EnumerationLiteral(name="LOCATION_NOTIFICATION", owner=NotificationType)
NotificationType_N1_MESSAGES = EnumerationLiteral(name="N1_MESSAGES", owner=NotificationType)
NotificationType_N2_INFORMATION = EnumerationLiteral(name="N2_INFORMATION", owner=NotificationType)
NotificationType.literals = {NotificationType_LOCATION_NOTIFICATION, NotificationType_N1_MESSAGES, NotificationType_N2_INFORMATION}

OperationalState = Enumeration(name="OperationalState")
OperationalState_DISABLED = EnumerationLiteral(name="DISABLED", owner=OperationalState, synonyms=["The resource is totally inoperable."])
OperationalState_ENABLED = EnumerationLiteral(name="ENABLED", owner=OperationalState, synonyms=["The resource is partially or fully operable."])
OperationalState.literals = {OperationalState_DISABLED, OperationalState_ENABLED}

ResourceSharingLevel = Enumeration(name="ResourceSharingLevel")
ResourceSharingLevel_NOT_SHARED = EnumerationLiteral(name="NOT_SHARED", owner=ResourceSharingLevel)
ResourceSharingLevel_SHARED = EnumerationLiteral(name="SHARED", owner=ResourceSharingLevel)
ResourceSharingLevel.literals = {ResourceSharingLevel_NOT_SHARED, ResourceSharingLevel_SHARED}

TxDirection = Enumeration(name="TxDirection")
TxDirection_DL = EnumerationLiteral(name="DL", owner=TxDirection)
TxDirection_DL_AND_UL = EnumerationLiteral(name="DL_AND_UL", owner=TxDirection)
TxDirection_UL = EnumerationLiteral(name="UL", owner=TxDirection)
TxDirection.literals = {TxDirection_DL, TxDirection_DL_AND_UL, TxDirection_UL}

UeMobilityLevel = Enumeration(name="UeMobilityLevel")
UeMobilityLevel_FULLY_MOBILITY = EnumerationLiteral(name="FULLY_MOBILITY", owner=UeMobilityLevel)
UeMobilityLevel_NOMADIC = EnumerationLiteral(name="NOMADIC", owner=UeMobilityLevel)
UeMobilityLevel_RESTRICTED_MOBILITY = EnumerationLiteral(name="RESTRICTED_MOBILITY", owner=UeMobilityLevel)
UeMobilityLevel_STATIONARY = EnumerationLiteral(name="STATIONARY", owner=UeMobilityLevel)
UeMobilityLevel.literals = {UeMobilityLevel_FULLY_MOBILITY, UeMobilityLevel_NOMADIC, UeMobilityLevel_RESTRICTED_MOBILITY, UeMobilityLevel_STATIONARY}

usageState = Enumeration(name="usageState")
usageState_ACTIVE = EnumerationLiteral(name="ACTIVE", owner=usageState)
usageState_BUSY = EnumerationLiteral(name="BUSY", owner=usageState)
usageState_IDLE = EnumerationLiteral(name="IDLE", owner=usageState)
usageState.literals = {usageState_ACTIVE, usageState_BUSY, usageState_IDLE}
usageState.synonyms = ["It describes whether or not the resource is actively in use at a specific instant, and if so, whether or not it has spare capacity for additional users at that instant. The value is READ-ONLY."]

# Classes
AddressWithVlan = Class(name="AddressWithVlan")

# AddressWithVlan class attributes and methods
AddressWithVlan_ipAddress: Property = Property(name="ipAddress", type=inet_model.get_type_by_name('ip_address'))
AddressWithVlan_vlanId: Property = Property(name="vlanId", type=IntegerType)
AddressWithVlan.attributes={AddressWithVlan_ipAddress, AddressWithVlan_vlanId}

AmfIdentifier = Class(name="AmfIdentifier", synonyms=["The AMFI is constructed from an AMF Region ID, an AMF Set ID and an AMF Pointer. The AMF Region ID identifies the region, the AMF Set ID uniquely identifies the AMF Set within the AMF Region, and the AMF Pointer uniquely identifies the AMF within the AMF Set."])

# AmfIdentifier class attributes and methods
AmfIdentifier_amfPointer: Property = Property(name="amfPointer", type=StringType)
AmfIdentifier_amfRegionId: Property = Property(name="amfRegionId", type=StringType)
AmfIdentifier_amfSetId: Property = Property(name="amfSetId", type=StringType)
AmfIdentifier.attributes={AmfIdentifier_amfPointer, AmfIdentifier_amfRegionId, AmfIdentifier_amfSetId}

DefaultNotificationSubscription = Class(name="DefaultNotificationSubscription")

# DefaultNotificationSubscription class attributes and methods
DefaultNotificationSubscription_callbackUri: Property = Property(name="callbackUri", type=inet_model.get_type_by_name('uri'))
DefaultNotificationSubscription_n1MessageClass: Property = Property(name="n1MessageClass", type=StringType)
DefaultNotificationSubscription_n2InformationClass: Property = Property(name="n2InformationClass", type=StringType)
DefaultNotificationSubscription_notificationType: Property = Property(name="notificationType", type=StringType)
DefaultNotificationSubscription.attributes={DefaultNotificationSubscription_callbackUri, DefaultNotificationSubscription_n1MessageClass, DefaultNotificationSubscription_n2InformationClass, DefaultNotificationSubscription_notificationType}

Ipv4AddressRange = Class(name="Ipv4AddressRange")

# Ipv4AddressRange class attributes and methods
Ipv4AddressRange_end: Property = Property(name="end", type=inet_model.get_type_by_name('ipv4_address'))
Ipv4AddressRange_start: Property = Property(name="start", type=inet_model.get_type_by_name('ipv4_address'))
Ipv4AddressRange.attributes={Ipv4AddressRange_end, Ipv4AddressRange_start}

Ipv6PrefixRange = Class(name="Ipv6PrefixRange")

# Ipv6PrefixRange class attributes and methods
Ipv6PrefixRange_end: Property = Property(name="end", type=inet_model.get_type_by_name('ipv6_prefix'))
Ipv6PrefixRange_start: Property = Property(name="start", type=inet_model.get_type_by_name('ipv6_prefix'))
Ipv6PrefixRange.attributes={Ipv6PrefixRange_end, Ipv6PrefixRange_start}

ManagedNFProfile = Class(name="ManagedNFProfile", synonyms=["Defines profile for managed NF"])

# ManagedNFProfile class attributes and methods
ManagedNFProfile_authzInfo: Property = Property(name="authzInfo", type=StringType, synonyms=["This parameter defines NF Specific Service authorization information. It shall include the NF type (s) and NF realms/origins allowed to consume NF Service(s) of NF Service Producer."])
ManagedNFProfile_capacity: Property = Property(name="capacity", type=IntegerType, synonyms=["This parameter defines static capacity information in the range of 0-65535, expressed as a weight relative to other NF instances of the same type; if capacity is also present in the nfServiceList parameters, those will have precedence over this value."])
ManagedNFProfile_hostAddr: Property = Property(name="hostAddr", type=inet_model.get_type_by_name('host'), synonyms=["Host address of a NF"])
ManagedNFProfile_idx: Property = Property(name="idx", type=IntegerType)
ManagedNFProfile_location: Property = Property(name="location", type=StringType, synonyms=["Information about the location of the NF instance (e.g. geographic location, data center) defined by operator"])
ManagedNFProfile_nFSrvGroupId: Property = Property(name="nFSrvGroupId", type=StringType, synonyms=["This parameter defines identity of the group that is served by the NF instance. May be config false or true depending on the ManagedFunction. Config=true for Udrinfo. Config=false for UdmInfo and AusfInfo. Shall be present if ../nfType = UDM or AUSF or UDR."])
ManagedNFProfile_nfInstanceID: Property = Property(name="nfInstanceID", type=yang_model.get_type_by_name('uuid'), synonyms=["This parameter defines profile for managed NF. The format of the NF Instance ID shall be a Universally Unique Identifier (UUID) version 4, as described in IETF RFC 4122"])
ManagedNFProfile_priority: Property = Property(name="priority", type=IntegerType, synonyms=["This parameter defines Priority (relative to other NFs of the same type) in the range of 0-65535, to be used for NF selection; lower values indicate a higher priority. If priority is also present in the nfServiceList parameters, those will have precedence over this value. Shall be present if ../nfType = AMF"])
ManagedNFProfile.attributes={ManagedNFProfile_authzInfo, ManagedNFProfile_capacity, ManagedNFProfile_hostAddr, ManagedNFProfile_idx, ManagedNFProfile_location, ManagedNFProfile_nFSrvGroupId, ManagedNFProfile_nfInstanceID, ManagedNFProfile_priority}

PLMNId = Class(name="PLMNId")

# PLMNId class attributes and methods
PLMNId_mcc: Property = Property(name="mcc", type=StringType)
PLMNId_mnc: Property = Property(name="mnc", type=StringType)
PLMNId.attributes={PLMNId_mcc, PLMNId_mnc}

SAP = Class(name="SAP", synonyms=["Service access point."])

# SAP class attributes and methods
SAP_host: Property = Property(name="host", type=inet_model.get_type_by_name('host'))
SAP_port: Property = Property(name="port", type=inet_model.get_type_by_name('port_number'))
SAP.attributes={SAP_host, SAP_port}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-common-yang-types",
    types={AddressWithVlan, AdministrativeState, AmfIdentifier, AvailabilityStatus, CellState, DefaultNotificationSubscription, Ipv4AddressRange, Ipv6PrefixRange, ManagedNFProfile, N1MessageClass, N2InformationClass, NfType, NotificationType, OperationalState, PLMNId, ResourceSharingLevel, SAP, TxDirection, UeMobilityLevel, usageState},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["The model defines a YANG mapping of the top level information classes used for management of 5G networks and network slicing."]
