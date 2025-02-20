# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
NetworkSlice = Class(name="NetworkSlice")

# NetworkSlice class attributes and methods
NetworkSlice_NetworkSlice: Property = Property(name="NetworkSlice", type=list)
NetworkSlice_administrativeState: Property = Property(name="administrativeState", type=StringType)
NetworkSlice_networkSliceSubnetRef: Property = Property(name="networkSliceSubnetRef", type=StringType)
NetworkSlice_operationalState: Property = Property(name="operationalState", type=StringType)
NetworkSlice_serviceProfileList: Property = Property(name="serviceProfileList", type=list)
NetworkSlice.attributes={NetworkSlice_NetworkSlice, NetworkSlice_administrativeState, NetworkSlice_networkSliceSubnetRef, NetworkSlice_operationalState, NetworkSlice_serviceProfileList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-ns-nrm-networkslice",
    types={NetworkSlice},
    associations={},
    generalizations={}
)
