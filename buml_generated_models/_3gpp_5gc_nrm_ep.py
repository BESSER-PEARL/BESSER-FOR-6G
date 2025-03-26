# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models.ietf_inet_types import domain_model as inet_model
from buml_generated_models._3gpp_common_top import domain_model as top3gpp_model

# Classes
# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-ep",
    types={EP_MAP_SMSCGrp, EP_N10Grp, EP_N11Grp, EP_N12Grp, EP_N13Grp, EP_N14Grp, EP_N15Grp, EP_N16Grp, EP_N17Grp, EP_N20Grp, EP_N21Grp, EP_N22Grp, EP_N26Grp, EP_N27Grp, EP_N2Grp, EP_N31Grp, EP_N32Grp, EP_N3Grp, EP_N4Grp, EP_N5Grp, EP_N6Grp, EP_N7Grp, EP_N8Grp, EP_N9Grp, EP_NLGGrp, EP_NLSGrp, EP_RxGrp, EP_S5CGrp, EP_S5UGrp, EP_SBI_IPXGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the 5GC related endpoint Information Object Classes (IOCs) that are part of the 5G Core Network Resource Model."]
