# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
NFService = Class(name="NFService")

# NFService class attributes and methods
NFService_serviceInstanceID: Property = Property(name="serviceInstanceID", type=StringType)
NFService_serviceName: Property = Property(name="serviceName", type=ServiceName)
NFService_scheme: Property = Property(name="scheme", type=UriScheme)
NFService_nfServiceStatus: Property = Property(name="nfServiceStatus", type=NFServiceStatus)
NFService_fqdn: Property = Property(name="fqdn", type=inet:domain-name)
NFService_interPlmnFqdn: Property = Property(name="interPlmnFqdn", type=inet:domain-name)
NFService_apiPrefix: Property = Property(name="apiPrefix", type=StringType)
NFService_priority: Property = Property(name="priority", type=IntegerType)
NFService_capacity: Property = Property(name="capacity", type=IntegerType)
NFService_load: Property = Property(name="load", type=types3gpp:Load)
NFService_recoveryTime: Property = Property(name="recoveryTime", type=yang:date-and-time)
NFService_supportedFeatures: Property = Property(name="supportedFeatures", type=SupportedFeatures)
NFService_versions: Property = Property(name="versions", type=list)
NFService_ipEndPoints: Property = Property(name="ipEndPoints", type=list)
NFService_defaultNotificationSubscriptions: Property = Property(name="defaultNotificationSubscriptions", type=list)
NFService_allowedPlmns: Property = Property(name="allowedPlmns", type=list)
NFService_allowedNssais: Property = Property(name="allowedNssais", type=list)
NFService_chfServiceInfo: Property = Property(name="chfServiceInfo", type=list)
NFService.attributes={NFService_serviceInstanceID, NFService_serviceName, NFService_scheme, NFService_nfServiceStatus, NFService_fqdn, NFService_interPlmnFqdn, NFService_apiPrefix, NFService_priority, NFService_capacity, NFService_load, NFService_recoveryTime, NFService_supportedFeatures, NFService_versions, NFService_ipEndPoints, NFService_defaultNotificationSubscriptions, NFService_allowedPlmns, NFService_allowedNssais, NFService_chfServiceInfo}

ipEndPoint = Class(name="ipEndPoint")

# ipEndPoint class attributes and methods
ipEndPoint_transport: Property = Property(name="transport", type=TransportProtocol)
ipEndPoint_port: Property = Property(name="port", type=IntegerType)
ipEndPoint.attributes={ipEndPoint_transport, ipEndPoint_port}

NFServiceVersion = Class(name="NFServiceVersion")

# NFServiceVersion class attributes and methods
NFServiceVersion_apiVersionInUri: Property = Property(name="apiVersionInUri", type=StringType)
NFServiceVersion_apiFullVersion: Property = Property(name="apiFullVersion", type=StringType)
NFServiceVersion_expiry: Property = Property(name="expiry", type=yang:date-and-time)
NFServiceVersion.attributes={NFServiceVersion_apiVersionInUri, NFServiceVersion_apiFullVersion, NFServiceVersion_expiry}

ChfServiceInfo = Class(name="ChfServiceInfo")

# ChfServiceInfo class attributes and methods
ChfServiceInfo_primaryChfServiceInstance: Property = Property(name="primaryChfServiceInstance", type=StringType)
ChfServiceInfo_secondaryChfServiceInstance: Property = Property(name="secondaryChfServiceInstance", type=StringType)
ChfServiceInfo.attributes={ChfServiceInfo_primaryChfServiceInstance, ChfServiceInfo_secondaryChfServiceInstance}

