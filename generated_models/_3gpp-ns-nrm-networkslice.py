# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
NetworkSlice = Class(name="NetworkSlice")

# NetworkSlice class attributes and methods
NetworkSlice_operationalState: Property = Property(name="operationalState", type=types3gpp:OperationalState)
NetworkSlice_administrativeState: Property = Property(name="administrativeState", type=types3gpp:AdministrativeState)
NetworkSlice_networkSliceSubnetRef: Property = Property(name="networkSliceSubnetRef", type=leafref)
NetworkSlice_serviceProfileList: Property = Property(name="serviceProfileList", type=list)
NetworkSlice_NetworkSlice: Property = Property(name="NetworkSlice", type=list)
NetworkSlice.attributes={NetworkSlice_operationalState, NetworkSlice_administrativeState, NetworkSlice_networkSliceSubnetRef, NetworkSlice_serviceProfileList, NetworkSlice_NetworkSlice}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-ns-nrm-networkslice",
    types={NetworkSlice},
    associations={},
    generalizations={}
)
