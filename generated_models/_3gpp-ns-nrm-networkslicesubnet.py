# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
EPTransport = Class(name="EPTransport")

# EPTransport class attributes and methods
EPTransport_ipAddress: Property = Property(name="ipAddress", type=StringType)
EPTransport_logicInterfaceId: Property = Property(name="logicInterfaceId", type=StringType)
EPTransport.attributes={EPTransport_ipAddress, EPTransport_logicInterfaceId}

NetworkSliceSubnet = Class(name="NetworkSliceSubnet")

# NetworkSliceSubnet class attributes and methods
NetworkSliceSubnet_NetworkSliceSubnet: Property = Property(name="NetworkSliceSubnet", type=list)
NetworkSliceSubnet_administrativeState: Property = Property(name="administrativeState", type=StringType)
NetworkSliceSubnet_managedFunctionRef: Property = Property(name="managedFunctionRef", type=list)
NetworkSliceSubnet_nsInfo: Property = Property(name="nsInfo", type=list)
NetworkSliceSubnet_operationalState: Property = Property(name="operationalState", type=StringType)
NetworkSliceSubnet_sliceProfileList: Property = Property(name="sliceProfileList", type=list)
NetworkSliceSubnet.attributes={NetworkSliceSubnet_NetworkSliceSubnet, NetworkSliceSubnet_administrativeState, NetworkSliceSubnet_managedFunctionRef, NetworkSliceSubnet_nsInfo, NetworkSliceSubnet_operationalState, NetworkSliceSubnet_sliceProfileList}

NsInfo = Class(name="NsInfo")

# NsInfo class attributes and methods
NsInfo_description: Property = Property(name="description", type=StringType)
NsInfo_nSInstanceId: Property = Property(name="nSInstanceId", type=StringType)
NsInfo_nsName: Property = Property(name="nsName", type=StringType)
NsInfo.attributes={NsInfo_description, NsInfo_nSInstanceId, NsInfo_nsName}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-ns-nrm-networkslicesubnet",
    types={EPTransport, NetworkSliceSubnet, NsInfo},
    associations={},
    generalizations={}
)
