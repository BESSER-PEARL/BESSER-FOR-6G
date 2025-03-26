# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models._3gpp_common_top import domain_model as top3gpp_model

# Classes
NetworkSlice = Class(name="NetworkSlice")

# NetworkSlice class attributes and methods
NetworkSlice_NetworkSlice: Property = Property(name="NetworkSlice", type=DataType('Top_Grp'), multiplicity=Multiplicity(0, "*"), synonyms=["Represents the properties of a network slice instance in a 5G network."])
NetworkSlice_administrativeState: Property = Property(name="administrativeState", type=AdministrativeState, synonyms=["The administrative state of the network slice instance. It describes the permission to use or prohibition against using the instance, imposed through the OAM services."])
NetworkSlice_networkSliceSubnetRef: Property = Property(name="networkSliceSubnetRef", type=StringType, synonyms=["The NetworkSliceSubnet that the NetworkSlice is associated with."])
NetworkSlice_operationalState: Property = Property(name="operationalState", type=OperationalState, synonyms=["The operational state of the network slice instance. It describes whether or not the resource is physically installed and working."])
NetworkSlice_serviceProfileList: Property = Property(name="serviceProfileList", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["A list of service profiles supported by the network slice instance."])
NetworkSlice.attributes={NetworkSlice_NetworkSlice, NetworkSlice_administrativeState, NetworkSlice_networkSliceSubnetRef, NetworkSlice_operationalState, NetworkSlice_serviceProfileList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-ns-nrm-networkslice",
    types={NetworkSlice},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["A network slice instance in a 5G network."]
