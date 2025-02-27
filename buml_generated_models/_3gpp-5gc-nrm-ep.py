# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
EP_MAP_SMSCGrp = Class(name="EP_MAP_SMSCGrp")

# EP_MAP_SMSCGrp class attributes and methods
EP_N10Grp = Class(name="EP_N10Grp")

# EP_N10Grp class attributes and methods
EP_N11Grp = Class(name="EP_N11Grp")

# EP_N11Grp class attributes and methods
EP_N12Grp = Class(name="EP_N12Grp")

# EP_N12Grp class attributes and methods
EP_N13Grp = Class(name="EP_N13Grp")

# EP_N13Grp class attributes and methods
EP_N14Grp = Class(name="EP_N14Grp")

# EP_N14Grp class attributes and methods
EP_N15Grp = Class(name="EP_N15Grp")

# EP_N15Grp class attributes and methods
EP_N16Grp = Class(name="EP_N16Grp")

# EP_N16Grp class attributes and methods
EP_N17Grp = Class(name="EP_N17Grp")

# EP_N17Grp class attributes and methods
EP_N20Grp = Class(name="EP_N20Grp")

# EP_N20Grp class attributes and methods
EP_N21Grp = Class(name="EP_N21Grp")

# EP_N21Grp class attributes and methods
EP_N22Grp = Class(name="EP_N22Grp")

# EP_N22Grp class attributes and methods
EP_N26Grp = Class(name="EP_N26Grp")

# EP_N26Grp class attributes and methods
EP_N27Grp = Class(name="EP_N27Grp")

# EP_N27Grp class attributes and methods
EP_N2Grp = Class(name="EP_N2Grp")

# EP_N2Grp class attributes and methods
EP_N31Grp = Class(name="EP_N31Grp")

# EP_N31Grp class attributes and methods
EP_N32Grp = Class(name="EP_N32Grp")

# EP_N32Grp class attributes and methods
EP_N32Grp_n32cParas: Property = Property(name="n32cParas", type=StringType)
EP_N32Grp_n32fPolicy: Property = Property(name="n32fPolicy", type=StringType)
EP_N32Grp_remoteSeppAddress: Property = Property(name="remoteSeppAddress", type=StringType, synonyms=["The host address of the SEPP."])
EP_N32Grp_remoteSeppId: Property = Property(name="remoteSeppId", type=IntegerType)
EP_N32Grp_withIPX: Property = Property(name="withIPX", type=BooleanType)
EP_N32Grp.attributes={EP_N32Grp_n32cParas, EP_N32Grp_n32fPolicy, EP_N32Grp_remoteSeppAddress, EP_N32Grp_remoteSeppId, EP_N32Grp_withIPX}

EP_N3Grp = Class(name="EP_N3Grp")

# EP_N3Grp class attributes and methods
EP_N4Grp = Class(name="EP_N4Grp")

# EP_N4Grp class attributes and methods
EP_N5Grp = Class(name="EP_N5Grp")

# EP_N5Grp class attributes and methods
EP_N6Grp = Class(name="EP_N6Grp")

# EP_N6Grp class attributes and methods
EP_N7Grp = Class(name="EP_N7Grp")

# EP_N7Grp class attributes and methods
EP_N8Grp = Class(name="EP_N8Grp")

# EP_N8Grp class attributes and methods
EP_N9Grp = Class(name="EP_N9Grp")

# EP_N9Grp class attributes and methods
EP_NLGGrp = Class(name="EP_NLGGrp")

# EP_NLGGrp class attributes and methods
EP_NLSGrp = Class(name="EP_NLSGrp")

# EP_NLSGrp class attributes and methods
EP_RxGrp = Class(name="EP_RxGrp")

# EP_RxGrp class attributes and methods
EP_S5CGrp = Class(name="EP_S5CGrp")

# EP_S5CGrp class attributes and methods
EP_S5UGrp = Class(name="EP_S5UGrp")

# EP_S5UGrp class attributes and methods
EP_SBI_IPXGrp = Class(name="EP_SBI_IPXGrp")

# EP_SBI_IPXGrp class attributes and methods
# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-ep",
    types={EP_MAP_SMSCGrp, EP_N10Grp, EP_N11Grp, EP_N12Grp, EP_N13Grp, EP_N14Grp, EP_N15Grp, EP_N16Grp, EP_N17Grp, EP_N20Grp, EP_N21Grp, EP_N22Grp, EP_N26Grp, EP_N27Grp, EP_N2Grp, EP_N31Grp, EP_N32Grp, EP_N3Grp, EP_N4Grp, EP_N5Grp, EP_N6Grp, EP_N7Grp, EP_N8Grp, EP_N9Grp, EP_NLGGrp, EP_NLSGrp, EP_RxGrp, EP_S5CGrp, EP_S5UGrp, EP_SBI_IPXGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the 5GC related endpoint Information Object Classes (IOCs) that are part of the 5G Core Network Resource Model."]
