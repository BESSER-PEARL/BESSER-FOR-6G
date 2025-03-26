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
# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-ep",
    types={EP_E1Grp, EP_F1CGrp, EP_F1UGrp, EP_NgCGrp, EP_NgUGrp, EP_S1UGrp, EP_X2CGrp, EP_X2UGrp, EP_XnCGrp, EP_XnUGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the NR related endpoint Information Object Classes (IOCs) that are part of the NR Network Resource Model (NRM)."]
