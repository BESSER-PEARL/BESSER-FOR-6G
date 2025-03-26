# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models.ietf_inet_types import domain_model as inet_model
from buml_generated_models._3gpp_common_yang_types import domain_model as types3gpp_model
from buml_generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
# from buml_generated_models.ietf_yang_types import domain_model as yang_model

# Enumerations
NFServiceStatus = Enumeration(name="NFServiceStatus")
NFServiceStatus_REGISTERED = EnumerationLiteral(name="REGISTERED", owner=NFServiceStatus)
NFServiceStatus_SUSPENDED = EnumerationLiteral(name="SUSPENDED", owner=NFServiceStatus)
NFServiceStatus_UNDISCOVERABLE = EnumerationLiteral(name="UNDISCOVERABLE", owner=NFServiceStatus)
NFServiceStatus.literals = {NFServiceStatus_REGISTERED, NFServiceStatus_SUSPENDED, NFServiceStatus_UNDISCOVERABLE}

ServiceName = Enumeration(name="ServiceName")
ServiceName_N5G_EIR_EIC = EnumerationLiteral(name="N5G_EIR_EIC", owner=ServiceName)
ServiceName_NAMF_COMM = EnumerationLiteral(name="NAMF_COMM", owner=ServiceName)
ServiceName_NAMF_EVTS = EnumerationLiteral(name="NAMF_EVTS", owner=ServiceName)
ServiceName_NAMF_LOC = EnumerationLiteral(name="NAMF_LOC", owner=ServiceName)
ServiceName_NAMF_MT = EnumerationLiteral(name="NAMF_MT", owner=ServiceName)
ServiceName_NAUSF_AUTH = EnumerationLiteral(name="NAUSF_AUTH", owner=ServiceName)
ServiceName_NAUSF_SORPROTECTION = EnumerationLiteral(name="NAUSF_SORPROTECTION", owner=ServiceName)
ServiceName_NBSF_MANAGEMENT = EnumerationLiteral(name="NBSF_MANAGEMENT", owner=ServiceName)
ServiceName_NCHF_CONVERGEDCHARGING = EnumerationLiteral(name="NCHF_CONVERGEDCHARGING", owner=ServiceName)
ServiceName_NCHF_SPENDINGLIMITCONTROL = EnumerationLiteral(name="NCHF_SPENDINGLIMITCONTROL", owner=ServiceName)
ServiceName_NLMF_LOC = EnumerationLiteral(name="NLMF_LOC", owner=ServiceName)
ServiceName_NNEF_PFDMANAGEMENT = EnumerationLiteral(name="NNEF_PFDMANAGEMENT", owner=ServiceName)
ServiceName_NNRF_DISC = EnumerationLiteral(name="NNRF_DISC", owner=ServiceName)
ServiceName_NNRF_NFM = EnumerationLiteral(name="NNRF_NFM", owner=ServiceName)
ServiceName_NNSSF_NSSAIAVAILABILITY = EnumerationLiteral(name="NNSSF_NSSAIAVAILABILITY", owner=ServiceName)
ServiceName_NNSSF_NSSELECTION = EnumerationLiteral(name="NNSSF_NSSELECTION", owner=ServiceName)
ServiceName_NNWDAF_ANALYTICSINFO = EnumerationLiteral(name="NNWDAF_ANALYTICSINFO", owner=ServiceName)
ServiceName_NNWDAF_EVENTSSUBSCRIPTION = EnumerationLiteral(name="NNWDAF_EVENTSSUBSCRIPTION", owner=ServiceName)
ServiceName_NPCF_AM_POLICY_CONTROL = EnumerationLiteral(name="NPCF_AM-POLICY-CONTROL", owner=ServiceName)
ServiceName_NPCF_BDTPOLICYCONTROL = EnumerationLiteral(name="NPCF_BDTPOLICYCONTROL", owner=ServiceName)
ServiceName_NPCF_EVENTEXPOSURE = EnumerationLiteral(name="NPCF_EVENTEXPOSURE", owner=ServiceName)
ServiceName_NPCF_POLICYAUTHORIZATION = EnumerationLiteral(name="NPCF_POLICYAUTHORIZATION", owner=ServiceName)
ServiceName_NPCF_SMPOLICYCONTROL = EnumerationLiteral(name="NPCF_SMPOLICYCONTROL", owner=ServiceName)
ServiceName_NPCF_UE_POLICY_CONTROL = EnumerationLiteral(name="NPCF_UE_POLICY_CONTROL", owner=ServiceName)
ServiceName_NSMF_EVENT_EXPOSURE = EnumerationLiteral(name="NSMF_EVENT-EXPOSURE", owner=ServiceName)
ServiceName_NSMF_PDUSESSION = EnumerationLiteral(name="NSMF_PDUSESSION", owner=ServiceName)
ServiceName_NSMSF_SMS = EnumerationLiteral(name="NSMSF_SMS", owner=ServiceName)
ServiceName_NUDM_EE = EnumerationLiteral(name="NUDM_EE", owner=ServiceName)
ServiceName_NUDM_PP = EnumerationLiteral(name="NUDM_PP", owner=ServiceName)
ServiceName_NUDM_SDM = EnumerationLiteral(name="NUDM_SDM", owner=ServiceName)
ServiceName_NUDM_UEAU = EnumerationLiteral(name="NUDM_UEAU", owner=ServiceName)
ServiceName_NUDM_UECM = EnumerationLiteral(name="NUDM_UECM", owner=ServiceName)
ServiceName_NUDR_DR = EnumerationLiteral(name="NUDR_DR", owner=ServiceName)
ServiceName.literals = {ServiceName_N5G_EIR_EIC, ServiceName_NAMF_COMM, ServiceName_NAMF_EVTS, ServiceName_NAMF_LOC, ServiceName_NAMF_MT, ServiceName_NAUSF_AUTH, ServiceName_NAUSF_SORPROTECTION, ServiceName_NBSF_MANAGEMENT, ServiceName_NCHF_CONVERGEDCHARGING, ServiceName_NCHF_SPENDINGLIMITCONTROL, ServiceName_NLMF_LOC, ServiceName_NNEF_PFDMANAGEMENT, ServiceName_NNRF_DISC, ServiceName_NNRF_NFM, ServiceName_NNSSF_NSSAIAVAILABILITY, ServiceName_NNSSF_NSSELECTION, ServiceName_NNWDAF_ANALYTICSINFO, ServiceName_NNWDAF_EVENTSSUBSCRIPTION, ServiceName_NPCF_AM_POLICY_CONTROL, ServiceName_NPCF_BDTPOLICYCONTROL, ServiceName_NPCF_EVENTEXPOSURE, ServiceName_NPCF_POLICYAUTHORIZATION, ServiceName_NPCF_SMPOLICYCONTROL, ServiceName_NPCF_UE_POLICY_CONTROL, ServiceName_NSMF_EVENT_EXPOSURE, ServiceName_NSMF_PDUSESSION, ServiceName_NSMSF_SMS, ServiceName_NUDM_EE, ServiceName_NUDM_PP, ServiceName_NUDM_SDM, ServiceName_NUDM_UEAU, ServiceName_NUDM_UECM, ServiceName_NUDR_DR}

TransportProtocol = Enumeration(name="TransportProtocol")
TransportProtocol_STCP = EnumerationLiteral(name="STCP", owner=TransportProtocol)
TransportProtocol_TCP = EnumerationLiteral(name="TCP", owner=TransportProtocol)
TransportProtocol_UDP = EnumerationLiteral(name="UDP", owner=TransportProtocol)
TransportProtocol.literals = {TransportProtocol_STCP, TransportProtocol_TCP, TransportProtocol_UDP}

UriScheme = Enumeration(name="UriScheme")
UriScheme_HTTP = EnumerationLiteral(name="HTTP", owner=UriScheme)
UriScheme_HTTPS = EnumerationLiteral(name="HTTPS", owner=UriScheme)
UriScheme.literals = {UriScheme_HTTP, UriScheme_HTTPS}

# Classes
ChfServiceInfo = Class(name="ChfServiceInfo")

# ChfServiceInfo class attributes and methods
ChfServiceInfo_primaryChfServiceInstance: Property = Property(name="primaryChfServiceInstance", type=StringType, synonyms=["Shall be present if the CHF service instance serves as a secondary CHF instance of another primary CHF service instance."])
ChfServiceInfo_secondaryChfServiceInstance: Property = Property(name="secondaryChfServiceInstance", type=StringType, synonyms=["Shall be present if the CHF service instance serves as a primary CHF instance of another secondary CHF service instance."])
ChfServiceInfo.attributes={ChfServiceInfo_primaryChfServiceInstance, ChfServiceInfo_secondaryChfServiceInstance}

NFService = Class(name="NFService", synonyms=["Represents the NFService IOC"])

# NFService class attributes and methods
NFService_allowedNssais: Property = Property(name="allowedNssais", type=DataType('SNssai'), multiplicity=Multiplicity(1, "*"), synonyms=["S-NSSAI of the allowed slices to access the service instance. The absence of this attribute indicates that any slice is allowed to access the service instance."])
NFService_allowedPlmns: Property = Property(name="allowedPlmns", type=DataType('PLMNId'), multiplicity=Multiplicity(1, "*"), synonyms=["PLMNs allowed to access the service instance. The absence of this attribute indicates that any PLMN is allowed to access the service instance."])
NFService_apiPrefix: Property = Property(name="apiPrefix", type=StringType, synonyms=["Optional path segment(s) used to construct the {apiRoot} variable of the different API URIs."])
NFService_capacity: Property = Property(name="capacity", type=IntegerType, synonyms=["Static capacity information in the range of 0-65535, expressed as a weight relative to other services of the same type."])
NFService_chfServiceInfo: Property = Property(name="chfServiceInfo", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["Specific data for a CHF service instance."])
NFService_defaultNotificationSubscriptions: Property = Property(name="defaultNotificationSubscriptions", type=DataType('DefaultNotificationSubscription'), multiplicity=Multiplicity(1, "*"), synonyms=["Notification endpoints for different notification types."])
NFService_fqdn: Property = Property(name="fqdn", type=DataType('domain_name'), synonyms=["FQDN of the NF Service Instance."])
NFService_interPlmnFqdn: Property = Property(name="interPlmnFqdn", type=DataType('domain_name'), synonyms=["If the NF service needs to be discoverable by other NFs in a different PLMN, then an FQDN that is used for inter PLMN routing."])
NFService_ipEndPoints: Property = Property(name="ipEndPoints", type=list, multiplicity=Multiplicity(1, "*"), synonyms=["IP address(es) and port information of the Network Function (including IPv4 and/or IPv6 address)where the service is listening for incoming service requests."])
NFService_load: Property = Property(name="load", type=DataType('Load'), synonyms=["Dynamic load information, ranged from 0 to 100, indicates the current load percentage of the NF Service."])
NFService_nfServiceStatus: Property = Property(name="nfServiceStatus", type=StringType, synonyms=["Status of the NF Service Instance."])
NFService_priority: Property = Property(name="priority", type=IntegerType, synonyms=["Priority (relative to other services of the same type) in the range of 0-65535, to be used for NF Service selection; lower values indicate a higher priority."])
NFService_recoveryTime: Property = Property(name="recoveryTime", type=DataType('date_and_time'), synonyms=["Timestamp when the NF was (re)started."])
NFService_scheme: Property = Property(name="scheme", type=StringType, synonyms=["URI scheme (e.g. 'http', 'https')."])
NFService_serviceInstanceID: Property = Property(name="serviceInstanceID", type=StringType, synonyms=["Unique ID of the service instance within a given NF Instance."])
NFService_serviceName: Property = Property(name="serviceName", type=StringType, synonyms=["Name of the service instance (e.g. 'nudm-sdm')."])
NFService_supportedFeatures: Property = Property(name="supportedFeatures", type=StringType, synonyms=["Supported Features of the NF Service instance."])
NFService_versions: Property = Property(name="versions", type=list, multiplicity=Multiplicity(1, "*"), synonyms=["API versions supported by the NF Service and if available, the corresponding retirement date of the NF Service."])
NFService.attributes={NFService_allowedNssais, NFService_allowedPlmns, NFService_apiPrefix, NFService_capacity, NFService_chfServiceInfo, NFService_defaultNotificationSubscriptions, NFService_fqdn, NFService_interPlmnFqdn, NFService_ipEndPoints, NFService_load, NFService_nfServiceStatus, NFService_priority, NFService_recoveryTime, NFService_scheme, NFService_serviceInstanceID, NFService_serviceName, NFService_supportedFeatures, NFService_versions}

NFServiceVersion = Class(name="NFServiceVersion")

# NFServiceVersion class attributes and methods
NFServiceVersion_apiFullVersion: Property = Property(name="apiFullVersion", type=StringType)
NFServiceVersion_apiVersionInUri: Property = Property(name="apiVersionInUri", type=StringType)
NFServiceVersion_expiry: Property = Property(name="expiry", type=DataType('date_and_time'))
NFServiceVersion.attributes={NFServiceVersion_apiFullVersion, NFServiceVersion_apiVersionInUri, NFServiceVersion_expiry}

ipEndPoint = Class(name="ipEndPoint")

# ipEndPoint class attributes and methods
ipEndPoint_port: Property = Property(name="port", type=IntegerType)
ipEndPoint_transport: Property = Property(name="transport", type=StringType)
ipEndPoint.attributes={ipEndPoint_port, ipEndPoint_transport}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-nfservice",
    types={ChfServiceInfo, NFService, NFServiceStatus, NFServiceVersion, ServiceName, TransportProtocol, UriScheme, ipEndPoint},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["NF service class."]
