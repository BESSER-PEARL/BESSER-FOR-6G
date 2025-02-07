# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
EP_S5C = Class(name="EP_S5C")

# EP_S5C class attributes and methods
EP_S5U = Class(name="EP_S5U")

# EP_S5U class attributes and methods
EP_Rx = Class(name="EP_Rx")

# EP_Rx class attributes and methods
EP_MAP_SMSC = Class(name="EP_MAP_SMSC")

# EP_MAP_SMSC class attributes and methods
EP_NLS = Class(name="EP_NLS")

# EP_NLS class attributes and methods
EP_NLG = Class(name="EP_NLG")

# EP_NLG class attributes and methods
EP_SBI_IPX = Class(name="EP_SBI_IPX")

# EP_SBI_IPX class attributes and methods
EP_N2 = Class(name="EP_N2")

# EP_N2 class attributes and methods
EP_N3 = Class(name="EP_N3")

# EP_N3 class attributes and methods
EP_N4 = Class(name="EP_N4")

# EP_N4 class attributes and methods
EP_N5 = Class(name="EP_N5")

# EP_N5 class attributes and methods
EP_N6 = Class(name="EP_N6")

# EP_N6 class attributes and methods
EP_N7 = Class(name="EP_N7")

# EP_N7 class attributes and methods
EP_N8 = Class(name="EP_N8")

# EP_N8 class attributes and methods
EP_N9 = Class(name="EP_N9")

# EP_N9 class attributes and methods
EP_N10 = Class(name="EP_N10")

# EP_N10 class attributes and methods
EP_N11 = Class(name="EP_N11")

# EP_N11 class attributes and methods
EP_N12 = Class(name="EP_N12")

# EP_N12 class attributes and methods
EP_N13 = Class(name="EP_N13")

# EP_N13 class attributes and methods
EP_N14 = Class(name="EP_N14")

# EP_N14 class attributes and methods
EP_N15 = Class(name="EP_N15")

# EP_N15 class attributes and methods
EP_N16 = Class(name="EP_N16")

# EP_N16 class attributes and methods
EP_N17 = Class(name="EP_N17")

# EP_N17 class attributes and methods
EP_N20 = Class(name="EP_N20")

# EP_N20 class attributes and methods
EP_N21 = Class(name="EP_N21")

# EP_N21 class attributes and methods
EP_N22 = Class(name="EP_N22")

# EP_N22 class attributes and methods
EP_N26 = Class(name="EP_N26")

# EP_N26 class attributes and methods
EP_N27 = Class(name="EP_N27")

# EP_N27 class attributes and methods
EP_N31 = Class(name="EP_N31")

# EP_N31 class attributes and methods
EP_N32 = Class(name="EP_N32")

# EP_N32 class attributes and methods
EP_N32_remoteSeppAddress: Property = Property(name="remoteSeppAddress", type=inet:host)
EP_N32_remoteSeppId: Property = Property(name="remoteSeppId", type=IntegerType)
EP_N32_n32cParas: Property = Property(name="n32cParas", type=StringType)
EP_N32_n32fPolicy: Property = Property(name="n32fPolicy", type=StringType)
EP_N32_withIPX: Property = Property(name="withIPX", type=BooleanType)
EP_N32.attributes={EP_N32_remoteSeppAddress, EP_N32_remoteSeppId, EP_N32_n32cParas, EP_N32_n32fPolicy, EP_N32_withIPX}

