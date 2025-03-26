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
from buml_generated_models._3gpp_common_ep_rp import EP_Common

# Classes
EP_N2Grp = Class(
    name="EP_N2Grp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_N2Grp.synonyms = ["Represents the EP_N2 IOC."]

EP_N3Grp = Class(
    name="EP_N3Grp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_N3Grp.synonyms = ["Represents the EP_N3 IOC."]

EP_N4Grp = Class(
    name="EP_N4Grp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_N4Grp.synonyms = ["Represents the EP_N4 IOC."]

EP_N5Grp = Class(
    name="EP_N5Grp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_N5Grp.synonyms = ["Represents the EP_N5 IOC."]

EP_N6Grp = Class(
    name="EP_N6Grp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_N6Grp.synonyms = ["Represents the EP_N6 IOC."]

EP_N7Grp = Class(
    name="EP_N7Grp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_N7Grp.synonyms = ["Represents the EP_N7 IOC."]

EP_N8Grp = Class(
    name="EP_N8Grp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_N8Grp.synonyms = ["Represents the EP_N8 IOC."]

EP_N9Grp = Class(
    name="EP_N9Grp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_N9Grp.synonyms = ["Represents the EP_N9 IOC."]

EP_N10Grp = Class(
    name="EP_N10Grp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_N10Grp.synonyms = ["Represents the EP_N10 IOC."]

EP_N11Grp = Class(
    name="EP_N11Grp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_N11Grp.synonyms = ["Represents the EP_N11 IOC."]

EP_N12Grp = Class(
    name="EP_N12Grp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_N12Grp.synonyms = ["Represents the EP_N12 IOC."]

EP_N13Grp = Class(
    name="EP_N13Grp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_N13Grp.synonyms = ["Represents the EP_N13 IOC."]

EP_N14Grp = Class(
    name="EP_N14Grp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_N14Grp.synonyms = ["Represents the EP_N14 IOC."]

EP_N15Grp = Class(
    name="EP_N15Grp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_N15Grp.synonyms = ["Represents the EP_N15 IOC."]

EP_N16Grp = Class(
    name="EP_N16Grp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_N16Grp.synonyms = ["Represents the EP_N16 IOC."]

EP_N17Grp = Class(
    name="EP_N17Grp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_N17Grp.synonyms = ["Represents the EP_N17 IOC."]

EP_N20Grp = Class(
    name="EP_N20Grp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_N20Grp.synonyms = ["Represents the EP_N20 IOC."]

EP_N21Grp = Class(
    name="EP_N21Grp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_N21Grp.synonyms = ["Represents the EP_N21 IOC."]

EP_N22Grp = Class(
    name="EP_N22Grp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_N22Grp.synonyms = ["Represents the EP_N22 IOC."]

EP_N26Grp = Class(
    name="EP_N26Grp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_N26Grp.synonyms = ["Represents the EP_N26 IOC."]

EP_N27Grp = Class(
    name="EP_N27Grp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_N27Grp.synonyms = ["Represents the EP_N27 IOC."]

EP_N31Grp = Class(
    name="EP_N31Grp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_N31Grp.synonyms = ["Represents the EP_N31 IOC."]

EP_N32Grp = Class(
    name="EP_N32Grp",
    attributes=[
        Property(name="EP_Common", type=EP_Common),
        Property(name="remotePlmnId", type=StringType),
        Property(name="remoteSeppAddress", type=StringType),
        Property(name="remoteSeppId", type=IntegerType),
        Property(name="n32cParas", type=StringType),
        Property(name="n32fPolicy", type=StringType),
        Property(name="withIPX", type=BooleanType)
    ]
)
EP_N32Grp.synonyms = ["Represents the EP_N32 IOC."]

EP_S5CGrp = Class(
    name="EP_S5CGrp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_S5CGrp.synonyms = ["Represents the EP_S5C IOC."]

EP_S5UGrp = Class(
    name="EP_S5UGrp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_S5UGrp.synonyms = ["Represents the EP_S5U IOC."]

EP_RxGrp = Class(
    name="EP_RxGrp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_RxGrp.synonyms = ["Represents the EP_Rx IOC."]

EP_MAP_SMSCGrp = Class(
    name="EP_MAP_SMSCGrp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_MAP_SMSCGrp.synonyms = ["Represents the EP_MAP_SMSC IOC."]

EP_NLSGrp = Class(
    name="EP_NLSGrp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_NLSGrp.synonyms = ["Represents the EP_NLS IOC."]

EP_NLGGrp = Class(
    name="EP_NLGGrp",
    attributes=[
        Property(name="EP_Common", type=EP_Common)
    ]
)
EP_NLGGrp.synonyms = ["Represents the EP_NLG IOC."]

EP_SBI_IPXGrp = Class(
    name="EP_SBI_IPXGrp",
    attributes=[
        Property(name="EP_Common", type=EP_Common),
        Property(name="sBIService", type=StringType, multiplicity=Multiplicity(1, "*"))
    ]
)
EP_SBI_IPXGrp.synonyms = ["Represents the EP_SBI_IPX IOC."]

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-ep",
    types={EP_MAP_SMSCGrp, EP_N10Grp, EP_N11Grp, EP_N12Grp, EP_N13Grp, EP_N14Grp, EP_N15Grp, EP_N16Grp, EP_N17Grp, 
           EP_N20Grp, EP_N21Grp, EP_N22Grp, EP_N26Grp, EP_N27Grp, EP_N2Grp, EP_N31Grp, EP_N32Grp, EP_N3Grp, EP_N4Grp, 
           EP_N5Grp, EP_N6Grp, EP_N7Grp, EP_N8Grp, EP_N9Grp, EP_NLGGrp, EP_NLSGrp, EP_RxGrp, EP_S5CGrp, EP_S5UGrp, 
           EP_SBI_IPXGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the 5GC related endpoint Information Object Classes (IOCs) that are part of the 5G Core Network Resource Model."]
