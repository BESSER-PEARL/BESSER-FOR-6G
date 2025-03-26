# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Classes
EPTransport = Class(name="EPTransport")

# EPTransport class attributes and methods
EPTransport_ipAddress: Property = Property(name="ipAddress", type=StringType, synonyms=["This parameter specifies the IP address assigned to a logical transport interface/endpoint. It can be an IPv4 address (See RFC 791) or an IPv6 address (See RFC 2373)."])
EPTransport_logicInterfaceId: Property = Property(name="logicInterfaceId", type=StringType, synonyms=["This parameter specifies the identify of a logical transport interface. It could be VLAN ID (See IEEE 802.1Q), MPLS Tag or Segment ID."])
EPTransport.attributes={EPTransport_ipAddress, EPTransport_logicInterfaceId}

NetworkSliceSubnet = Class(name="NetworkSliceSubnet")

# NetworkSliceSubnet class attributes and methods
NetworkSliceSubnet_NetworkSliceSubnet: Property = Property(name="NetworkSliceSubnet", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["Represents the properties of a network slice subnet instance in a 5G network."])
NetworkSliceSubnet_administrativeState: Property = Property(name="administrativeState", type=AdministrativeState, synonyms=["The administrative state of the network slice instance. It describes the permission to use or prohibition against using the instance, imposed through the OAM services."])
NetworkSliceSubnet_managedFunctionRef: Property = Property(name="managedFunctionRef", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["The managed functions that the NetworkSliceSubnet is associated with."])
NetworkSliceSubnet_nsInfo: Property = Property(name="nsInfo", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["This list represents the properties of network service information corresponding to the network slice subnet instance."])
NetworkSliceSubnet_operationalState: Property = Property(name="operationalState", type=OperationalState, synonyms=["The operational state of the network slice instance. It describes whether or not the resource is physically installed and working."])
NetworkSliceSubnet_sliceProfileList: Property = Property(name="sliceProfileList", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["List of SliceProfiles supported by the network slice subnet instance"])
NetworkSliceSubnet.attributes={NetworkSliceSubnet_NetworkSliceSubnet, NetworkSliceSubnet_administrativeState, NetworkSliceSubnet_managedFunctionRef, NetworkSliceSubnet_nsInfo, NetworkSliceSubnet_operationalState, NetworkSliceSubnet_sliceProfileList}

NsInfo = Class(name="NsInfo", synonyms=["The NsInfo of the NS instance corresponding to the network slice subnet instance."])

# NsInfo class attributes and methods
NsInfo_description: Property = Property(name="description", type=StringType, synonyms=["Human readable description of the NS instance."])
NsInfo_nSInstanceId: Property = Property(name="nSInstanceId", type=StringType, synonyms=["Uniquely identifies the NS instance."])
NsInfo_nsName: Property = Property(name="nsName", type=StringType, synonyms=["Human readable name of the NS instance."])
NsInfo.attributes={NsInfo_description, NsInfo_nSInstanceId, NsInfo_nsName}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-ns-nrm-networkslicesubnet",
    types={EPTransport, NetworkSliceSubnet, NsInfo},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the properties of a network slice subnet instance in a 5G network."]
