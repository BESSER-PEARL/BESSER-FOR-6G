# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
SNssai = Class(name="SNssai")

# SNssai class attributes and methods
SNssai_sd: Property = Property(name="sd", type=StringType)
SNssai_sst: Property = Property(name="sst", type=IntegerType)
SNssai.attributes={SNssai_sd, SNssai_sst}

PLMNInfo = Class(name="PLMNInfo")

# PLMNInfo class attributes and methods
CommModel = Class(name="CommModel")

# CommModel class attributes and methods
CommModel_groupId: Property = Property(name="groupId", type=IntegerType)
CommModel_commModelType: Property = Property(name="commModelType", type=CommModelType)
CommModel_commModelConfiguration: Property = Property(name="commModelConfiguration", type=StringType)
CommModel.attributes={CommModel_groupId, CommModel_commModelType, CommModel_commModelConfiguration}

SupportedFunc = Class(name="SupportedFunc")

# SupportedFunc class attributes and methods
SupportedFunc_function: Property = Property(name="function", type=StringType)
SupportedFunc_policy: Property = Property(name="policy", type=StringType)
SupportedFunc.attributes={SupportedFunc_function, SupportedFunc_policy}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5g-common-yang-types",
    types={SNssai, PLMNInfo, CommModel, SupportedFunc},
    associations={},
    generalizations={}
)
