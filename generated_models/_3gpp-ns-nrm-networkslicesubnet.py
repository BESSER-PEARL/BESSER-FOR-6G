# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
EPTransport = Class(name="EPTransport")

# EPTransport class attributes and methods
EPTransport_ipAddress: Property = Property(name="ipAddress", type=StringType)
EPTransport_logicInterfaceId: Property = Property(name="logicInterfaceId", type=StringType)
EPTransport.attributes={EPTransport_ipAddress, EPTransport_logicInterfaceId}

NsInfo = Class(name="NsInfo")

# NsInfo class attributes and methods
NsInfo_nSInstanceId: Property = Property(name="nSInstanceId", type=ETSI-GS-NFV-Identifier)
NsInfo_nsName: Property = Property(name="nsName", type=StringType)
NsInfo_description: Property = Property(name="description", type=StringType)
NsInfo.attributes={NsInfo_nSInstanceId, NsInfo_nsName, NsInfo_description}

NetworkSliceSubnet = Class(name="NetworkSliceSubnet")

# NetworkSliceSubnet class attributes and methods
NetworkSliceSubnet_operationalState: Property = Property(name="operationalState", type=types3gpp:OperationalState)
NetworkSliceSubnet_administrativeState: Property = Property(name="administrativeState", type=types3gpp:AdministrativeState)
NetworkSliceSubnet_nsInfo: Property = Property(name="nsInfo", type=list)
NetworkSliceSubnet_sliceProfileList: Property = Property(name="sliceProfileList", type=list)
NetworkSliceSubnet_managedFunctionRef: Property = Property(name="managedFunctionRef", type=list)
NetworkSliceSubnet_NetworkSliceSubnet: Property = Property(name="NetworkSliceSubnet", type=list)
NetworkSliceSubnet.attributes={NetworkSliceSubnet_operationalState, NetworkSliceSubnet_administrativeState, NetworkSliceSubnet_nsInfo, NetworkSliceSubnet_sliceProfileList, NetworkSliceSubnet_managedFunctionRef, NetworkSliceSubnet_NetworkSliceSubnet}

