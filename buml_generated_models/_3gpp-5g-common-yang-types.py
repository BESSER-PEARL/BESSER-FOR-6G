# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Enumerations
CommModelType = Enumeration(name="CommModelType")
CommModelType_DIRECT_COMMUNICATION_WITH_NRF = EnumerationLiteral(name="DIRECT_COMMUNICATION_WITH_NRF", owner=CommModelType)
CommModelType_DIRECT_COMMUNICATION_WO_NRF = EnumerationLiteral(name="DIRECT_COMMUNICATION_WO_NRF", owner=CommModelType)
CommModelType_INDIRECT_COMMUNICATION_WITH_DEDICATED_DISCOVERY = EnumerationLiteral(name="INDIRECT_COMMUNICATION_WITH_DEDICATED_DISCOVERY", owner=CommModelType)
CommModelType_INDIRECT_COMMUNICATION_WO_DEDICATED_DISCOVERY = EnumerationLiteral(name="INDIRECT_COMMUNICATION_WO_DEDICATED_DISCOVERY", owner=CommModelType)
CommModelType.literals = {CommModelType_DIRECT_COMMUNICATION_WITH_NRF, CommModelType_DIRECT_COMMUNICATION_WO_NRF, CommModelType_INDIRECT_COMMUNICATION_WITH_DEDICATED_DISCOVERY, CommModelType_INDIRECT_COMMUNICATION_WO_DEDICATED_DISCOVERY}

# Classes
CommModel = Class(name="CommModel")

# CommModel class attributes and methods
CommModel_commModelConfiguration: Property = Property(name="commModelConfiguration", type=StringType)
CommModel_commModelType: Property = Property(name="commModelType", type=StringType)
CommModel_groupId: Property = Property(name="groupId", type=IntegerType)
CommModel.attributes={CommModel_commModelConfiguration, CommModel_commModelType, CommModel_groupId}

PLMNInfo = Class(name="PLMNInfo")

# PLMNInfo class attributes and methods
SNssai = Class(name="SNssai")

# SNssai class attributes and methods
SNssai_sd: Property = Property(name="sd", type=StringType)
SNssai_sst: Property = Property(name="sst", type=IntegerType)
SNssai.attributes={SNssai_sd, SNssai_sst}

SupportedFunc = Class(name="SupportedFunc")

# SupportedFunc class attributes and methods
SupportedFunc_function: Property = Property(name="function", type=StringType)
SupportedFunc_policy: Property = Property(name="policy", type=StringType)
SupportedFunc.attributes={SupportedFunc_function, SupportedFunc_policy}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5g-common-yang-types",
    types={CommModel, CommModelType, PLMNInfo, SNssai, SupportedFunc},
    associations={},
    generalizations={}
)
