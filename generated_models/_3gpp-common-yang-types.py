# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
ManagedNFProfile = Class(name="ManagedNFProfile")

# ManagedNFProfile class attributes and methods
ManagedNFProfile_idx: Property = Property(name="idx", type=IntegerType)
ManagedNFProfile_nfInstanceID: Property = Property(name="nfInstanceID", type=yang:uuid)
ManagedNFProfile_hostAddr: Property = Property(name="hostAddr", type=inet:host)
ManagedNFProfile_authzInfo: Property = Property(name="authzInfo", type=StringType)
ManagedNFProfile_location: Property = Property(name="location", type=StringType)
ManagedNFProfile_capacity: Property = Property(name="capacity", type=IntegerType)
ManagedNFProfile_nFSrvGroupId: Property = Property(name="nFSrvGroupId", type=StringType)
ManagedNFProfile_priority: Property = Property(name="priority", type=IntegerType)
ManagedNFProfile.attributes={ManagedNFProfile_idx, ManagedNFProfile_nfInstanceID, ManagedNFProfile_hostAddr, ManagedNFProfile_authzInfo, ManagedNFProfile_location, ManagedNFProfile_capacity, ManagedNFProfile_nFSrvGroupId, ManagedNFProfile_priority}

SAP = Class(name="SAP")

# SAP class attributes and methods
SAP_host: Property = Property(name="host", type=inet:host)
SAP_port: Property = Property(name="port", type=inet:port-number)
SAP.attributes={SAP_host, SAP_port}

PLMNId = Class(name="PLMNId")

# PLMNId class attributes and methods
PLMNId_mcc: Property = Property(name="mcc", type=Mcc)
PLMNId_mnc: Property = Property(name="mnc", type=Mnc)
PLMNId.attributes={PLMNId_mcc, PLMNId_mnc}

AmfIdentifier = Class(name="AmfIdentifier")

# AmfIdentifier class attributes and methods
AmfIdentifier_amfRegionId: Property = Property(name="amfRegionId", type=AmfRegionId)
AmfIdentifier_amfSetId: Property = Property(name="amfSetId", type=AmfSetId)
AmfIdentifier_amfPointer: Property = Property(name="amfPointer", type=AmfPointer)
AmfIdentifier.attributes={AmfIdentifier_amfRegionId, AmfIdentifier_amfSetId, AmfIdentifier_amfPointer}

DefaultNotificationSubscription = Class(name="DefaultNotificationSubscription")

# DefaultNotificationSubscription class attributes and methods
DefaultNotificationSubscription_notificationType: Property = Property(name="notificationType", type=NotificationType)
DefaultNotificationSubscription_callbackUri: Property = Property(name="callbackUri", type=inet:uri)
DefaultNotificationSubscription_n1MessageClass: Property = Property(name="n1MessageClass", type=N1MessageClass)
DefaultNotificationSubscription_n2InformationClass: Property = Property(name="n2InformationClass", type=N2InformationClass)
DefaultNotificationSubscription.attributes={DefaultNotificationSubscription_notificationType, DefaultNotificationSubscription_callbackUri, DefaultNotificationSubscription_n1MessageClass, DefaultNotificationSubscription_n2InformationClass}

Ipv4AddressRange = Class(name="Ipv4AddressRange")

# Ipv4AddressRange class attributes and methods
Ipv4AddressRange_start: Property = Property(name="start", type=inet:ipv4-address)
Ipv4AddressRange_end: Property = Property(name="end", type=inet:ipv4-address)
Ipv4AddressRange.attributes={Ipv4AddressRange_start, Ipv4AddressRange_end}

Ipv6PrefixRange = Class(name="Ipv6PrefixRange")

# Ipv6PrefixRange class attributes and methods
Ipv6PrefixRange_start: Property = Property(name="start", type=inet:ipv6-prefix)
Ipv6PrefixRange_end: Property = Property(name="end", type=inet:ipv6-prefix)
Ipv6PrefixRange.attributes={Ipv6PrefixRange_start, Ipv6PrefixRange_end}

AddressWithVlan = Class(name="AddressWithVlan")

# AddressWithVlan class attributes and methods
AddressWithVlan_ipAddress: Property = Property(name="ipAddress", type=inet:ip-address)
AddressWithVlan_vlanId: Property = Property(name="vlanId", type=IntegerType)
AddressWithVlan.attributes={AddressWithVlan_ipAddress, AddressWithVlan_vlanId}

