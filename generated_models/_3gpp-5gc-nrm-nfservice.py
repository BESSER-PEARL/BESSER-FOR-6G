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
TransportProtocol: Enumeration = Enumeration(
    name="TransportProtocol",
    literals={
            EnumerationLiteral(name="TCP"),
			EnumerationLiteral(name="STCP"),
			EnumerationLiteral(name="UDP")
    }
)

ServiceName: Enumeration = Enumeration(
    name="ServiceName",
    literals={
            EnumerationLiteral(name="NNRF_NFM"),
			EnumerationLiteral(name="NNRF_DISC"),
			EnumerationLiteral(name="NUDM_SDM"),
			EnumerationLiteral(name="NUDM_UECM"),
			EnumerationLiteral(name="NUDM_UEAU"),
			EnumerationLiteral(name="NUDM_EE"),
			EnumerationLiteral(name="NUDM_PP"),
			EnumerationLiteral(name="NAMF_COMM"),
			EnumerationLiteral(name="NAMF_EVTS"),
			EnumerationLiteral(name="NAMF_MT"),
			EnumerationLiteral(name="NAMF_LOC"),
			EnumerationLiteral(name="NSMF_PDUSESSION"),
			EnumerationLiteral(name="NSMF_EVENT-EXPOSURE"),
			EnumerationLiteral(name="NAUSF_AUTH"),
			EnumerationLiteral(name="NAUSF_SORPROTECTION"),
			EnumerationLiteral(name="NNEF_PFDMANAGEMENT"),
			EnumerationLiteral(name="NPCF_AM-POLICY-CONTROL"),
			EnumerationLiteral(name="NPCF_SMPOLICYCONTROL"),
			EnumerationLiteral(name="NPCF_POLICYAUTHORIZATION"),
			EnumerationLiteral(name="NPCF_BDTPOLICYCONTROL"),
			EnumerationLiteral(name="NPCF_EVENTEXPOSURE"),
			EnumerationLiteral(name="NPCF_UE_POLICY_CONTROL"),
			EnumerationLiteral(name="NSMSF_SMS"),
			EnumerationLiteral(name="NNSSF_NSSELECTION"),
			EnumerationLiteral(name="NNSSF_NSSAIAVAILABILITY"),
			EnumerationLiteral(name="NUDR_DR"),
			EnumerationLiteral(name="NLMF_LOC"),
			EnumerationLiteral(name="N5G_EIR_EIC"),
			EnumerationLiteral(name="NBSF_MANAGEMENT"),
			EnumerationLiteral(name="NCHF_SPENDINGLIMITCONTROL"),
			EnumerationLiteral(name="NCHF_CONVERGEDCHARGING"),
			EnumerationLiteral(name="NNWDAF_EVENTSSUBSCRIPTION"),
			EnumerationLiteral(name="NNWDAF_ANALYTICSINFO")
    }
)

UriScheme: Enumeration = Enumeration(
    name="UriScheme",
    literals={
            EnumerationLiteral(name="HTTP"),
			EnumerationLiteral(name="HTTPS")
    }
)

NFServiceStatus: Enumeration = Enumeration(
    name="NFServiceStatus",
    literals={
            EnumerationLiteral(name="REGISTERED"),
			EnumerationLiteral(name="SUSPENDED"),
			EnumerationLiteral(name="UNDISCOVERABLE")
    }
)

# Classes
NFServiceGrp = Class(name="NFServiceGrp")
ipEndPoint = Class(name="ipEndPoint")
NFServiceVersion = Class(name="NFServiceVersion")
ChfServiceInfo = Class(name="ChfServiceInfo")

# NFServiceGrp class attributes and methods
NFServiceGrp_serviceInstanceID: Property = Property(name="serviceInstanceID", type=StringType)
NFServiceGrp_serviceName: Property = Property(name="serviceName", type=ServiceName)
NFServiceGrp_scheme: Property = Property(name="scheme", type=UriScheme)
NFServiceGrp_nfServiceStatus: Property = Property(name="nfServiceStatus", type=NFServiceStatus)
NFServiceGrp_fqdn: Property = Property(name="fqdn", type=inet:domain-name)
NFServiceGrp_interPlmnFqdn: Property = Property(name="interPlmnFqdn", type=inet:domain-name)
NFServiceGrp_apiPrefix: Property = Property(name="apiPrefix", type=StringType)
NFServiceGrp_priority: Property = Property(name="priority", type=IntegerType)
NFServiceGrp_capacity: Property = Property(name="capacity", type=IntegerType)
NFServiceGrp_load: Property = Property(name="load", type=types3gpp:Load)
NFServiceGrp_recoveryTime: Property = Property(name="recoveryTime", type=yang:date-and-time)
NFServiceGrp_supportedFeatures: Property = Property(name="supportedFeatures", type=SupportedFeatures)
NFServiceGrp_versions: Property = Property(name="versions", type=list)
NFServiceGrp_ipEndPoints: Property = Property(name="ipEndPoints", type=list)
NFServiceGrp_defaultNotificationSubscriptions: Property = Property(name="defaultNotificationSubscriptions", type=list)
NFServiceGrp_allowedPlmns: Property = Property(name="allowedPlmns", type=list)
NFServiceGrp_allowedNssais: Property = Property(name="allowedNssais", type=list)
NFServiceGrp_chfServiceInfo: Property = Property(name="chfServiceInfo", type=list)
NFServiceGrp.attributes={NFServiceGrp_serviceName, NFServiceGrp_nfServiceStatus, NFServiceGrp_versions, NFServiceGrp_fqdn, NFServiceGrp_capacity, NFServiceGrp_serviceInstanceID, NFServiceGrp_load, NFServiceGrp_defaultNotificationSubscriptions, NFServiceGrp_interPlmnFqdn, NFServiceGrp_allowedPlmns, NFServiceGrp_allowedNssais, NFServiceGrp_recoveryTime, NFServiceGrp_supportedFeatures, NFServiceGrp_ipEndPoints, NFServiceGrp_chfServiceInfo, NFServiceGrp_priority, NFServiceGrp_scheme, NFServiceGrp_apiPrefix}

# ipEndPoint class attributes and methods
ipEndPoint_transport: Property = Property(name="transport", type=TransportProtocol)
ipEndPoint_port: Property = Property(name="port", type=IntegerType)
ipEndPoint.attributes={ipEndPoint_port, ipEndPoint_transport}

# NFServiceVersion class attributes and methods
NFServiceVersion_apiVersionInUri: Property = Property(name="apiVersionInUri", type=StringType)
NFServiceVersion_apiFullVersion: Property = Property(name="apiFullVersion", type=StringType)
NFServiceVersion_expiry: Property = Property(name="expiry", type=yang:date-and-time)
NFServiceVersion.attributes={NFServiceVersion_expiry, NFServiceVersion_apiFullVersion, NFServiceVersion_apiVersionInUri}

# ChfServiceInfo class attributes and methods
ChfServiceInfo_primaryChfServiceInstance: Property = Property(name="primaryChfServiceInstance", type=StringType)
ChfServiceInfo_secondaryChfServiceInstance: Property = Property(name="secondaryChfServiceInstance", type=StringType)
ChfServiceInfo.attributes={ChfServiceInfo_secondaryChfServiceInstance, ChfServiceInfo_primaryChfServiceInstance}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-nfservice",
    types={NFServiceGrp, ipEndPoint, NFServiceVersion, ChfServiceInfo, TransportProtocol, ServiceName, UriScheme, NFServiceStatus, types3gpp_model, mf3gpp_model, me3gpp_model, top3gpp_model, types5g3gpp_model, inet_model, subnet3gpp_model, Conf5QIs3gpp_model, eprp3gpp_model, af3gpp_model, amf3gpp_model, ausf3gpp_model, dn3gpp_model, lmf3gpp_model, n3iwf3gpp_model, ngeir3gpp_model, nrf3gpp_model, nssf3gpp_model, pcf3gpp_model, sepp3gpp_model, smf3gpp_model, smsf3gpp_model, udm3gpp_model, upf3gpp_model, yang_model, nfs3gpp_model},
    associations={},
    generalizations={}
)
