# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models._3gpp_common_top import domain_model as top3gpp_model

# Classes
EUtraNetwork = Class(name="EUtraNetwork", synonyms=["Represents the EUtraNetwork IOC."])

# EUtraNetwork class attributes and methods
EUtraNetwork_EUtraNetwork: Property = Property(name="EUtraNetwork", type=top3gpp_model.get_type_by_name('Top_Grp'), multiplicity=Multiplicity(0, "*"), synonyms=["A subnetwork containing gNB external E-UTRAN entities."])
EUtraNetwork.attributes={EUtraNetwork_EUtraNetwork}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-eutranetwork",
    types={EUtraNetwork},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the EUtraNetwork Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
