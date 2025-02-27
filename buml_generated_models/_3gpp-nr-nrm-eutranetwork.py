# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
EUtraNetwork = Class(name="EUtraNetwork", synonyms=["Represents the EUtraNetwork IOC."])

# EUtraNetwork class attributes and methods
EUtraNetwork_EUtraNetwork: Property = Property(name="EUtraNetwork", type=list, synonyms=["A subnetwork containing gNB external E-UTRAN entities."])
EUtraNetwork.attributes={EUtraNetwork_EUtraNetwork}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-eutranetwork",
    types={EUtraNetwork},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the EUtraNetwork Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
