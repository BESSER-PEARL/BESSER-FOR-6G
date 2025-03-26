# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models._3gpp_common_top import domain_model as top3gpp_model
from buml_generated_models._3gpp_common_ep_rp import EP_Common

# Classes
EP_E1Grp = Class(
    name="EP_E1Grp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_E1Grp.synonyms = ["Represents the EP_E1 IOC."]

EP_F1CGrp = Class(
    name="EP_F1CGrp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_F1CGrp.synonyms = ["Represents the EP_F1C IOC."]

EP_F1UGrp = Class(
    name="EP_F1UGrp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_F1UGrp.synonyms = ["Represents the EP_F1U IOC."]

EP_XnCGrp = Class(
    name="EP_XnCGrp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_XnCGrp.synonyms = ["Represents the EP_XnC IOC."]

EP_XnUGrp = Class(
    name="EP_XnUGrp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_XnUGrp.synonyms = ["Represents the EP_XnU IOC."]

EP_NgCGrp = Class(
    name="EP_NgCGrp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_NgCGrp.synonyms = ["Represents the EP_NgC IOC."]

EP_NgUGrp = Class(
    name="EP_NgUGrp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_NgUGrp.synonyms = ["Represents the EP_NgU IOC."]

EP_X2CGrp = Class(
    name="EP_X2CGrp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_X2CGrp.synonyms = ["Represents the EP_X2C IOC."]

EP_X2UGrp = Class(
    name="EP_X2UGrp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_X2UGrp.synonyms = ["Represents the EP_X2U IOC."]

EP_S1UGrp = Class(
    name="EP_S1UGrp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_S1UGrp.synonyms = ["Represents the EP_S1U IOC."]

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-ep",
    types={EP_E1Grp, EP_F1CGrp, EP_F1UGrp, EP_NgCGrp, EP_NgUGrp, EP_S1UGrp, EP_X2CGrp, EP_X2UGrp, EP_XnCGrp, EP_XnUGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the NR related endpoint Information Object Classes (IOCs) that are part of the NR Network Resource Model (NRM)."]
