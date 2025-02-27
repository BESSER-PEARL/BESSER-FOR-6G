# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
NRNetwork = Class(name="NRNetwork", synonyms=["Represents the NRNetwork IOC."])

# NRNetwork class attributes and methods
NRNetwork_NRNetwork: Property = Property(name="NRNetwork", type=list, synonyms=["A subnetwork containing gNB external NR entities."])
NRNetwork.attributes={NRNetwork_NRNetwork}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-nrnetwork",
    types={NRNetwork},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the NRNetwork Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
