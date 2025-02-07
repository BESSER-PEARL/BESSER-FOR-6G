# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
NetworkSlice = Class(name="NetworkSlice")

# NetworkSlice class attributes and methods
NetworkSlice_operationalState: Property = Property(name="operationalState", type=types3gpp:OperationalState)
NetworkSlice_administrativeState: Property = Property(name="administrativeState", type=types3gpp:AdministrativeState)
NetworkSlice_networkSliceSubnetRef: Property = Property(name="networkSliceSubnetRef", type=leafref)
NetworkSlice_serviceProfileList: Property = Property(name="serviceProfileList", type=list)
NetworkSlice_NetworkSlice: Property = Property(name="NetworkSlice", type=list)
NetworkSlice.attributes={NetworkSlice_operationalState, NetworkSlice_administrativeState, NetworkSlice_networkSliceSubnetRef, NetworkSlice_serviceProfileList, NetworkSlice_NetworkSlice}

