# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Enumerations
CommModelType = Enumeration(name="CommModelType")
CommModelType_DIRECT_COMMUNICATION_WITH_NRF = EnumerationLiteral(name="DIRECT_COMMUNICATION_WITH_NRF", owner=CommModelType, synonyms=["Directly communicate to other NF service discovered by NRF."])
CommModelType_DIRECT_COMMUNICATION_WO_NRF = EnumerationLiteral(name="DIRECT_COMMUNICATION_WO_NRF", owner=CommModelType, synonyms=["Directly communicate to other pre-configured NF service."])
CommModelType_INDIRECT_COMMUNICATION_WITH_DEDICATED_DISCOVERY = EnumerationLiteral(name="INDIRECT_COMMUNICATION_WITH_DEDICATED_DISCOVERY", owner=CommModelType, synonyms=["Communication to NF service discovered by NRF through SCP as a proxy."])
CommModelType_INDIRECT_COMMUNICATION_WO_DEDICATED_DISCOVERY = EnumerationLiteral(name="INDIRECT_COMMUNICATION_WO_DEDICATED_DISCOVERY", owner=CommModelType, synonyms=["Communicate to pre-configured other NF service through SCP as a proxy."])
CommModelType.literals = {CommModelType_DIRECT_COMMUNICATION_WITH_NRF, CommModelType_DIRECT_COMMUNICATION_WO_NRF, CommModelType_INDIRECT_COMMUNICATION_WITH_DEDICATED_DISCOVERY, CommModelType_INDIRECT_COMMUNICATION_WO_DEDICATED_DISCOVERY}

# Classes
CommModel = Class(name="CommModel")

# CommModel class attributes and methods
CommModel_commModelConfiguration: Property = Property(name="commModelConfiguration", type=StringType)
CommModel_commModelType: Property = Property(name="commModelType", type=StringType)
CommModel_groupId: Property = Property(name="groupId", type=IntegerType)
CommModel.attributes={CommModel_commModelConfiguration, CommModel_commModelType, CommModel_groupId}

PLMNInfo = Class(name="PLMNInfo", synonyms=["The PLMNInfo data type define a S-NSSAI member in a specific PLMNId, and it have two attributes PLMNId and S-NSSAI (PLMNId, S-NSSAI). The PLMNId represents a data type that is comprised of mcc (mobile country code) and mnc (mobile network code), (See TS 23.003 subclause 2.2 and 12.1) and S-NSSAI represents an data type, that is comprised of an SST (Slice/Service type) and an optional SD (Slice Differentiator) field"])

# PLMNInfo class attributes and methods
SNssai = Class(name="SNssai", synonyms=["Single Network Slice Selection Assistance Information(S-NSSAI)"])

# SNssai class attributes and methods
SNssai_sd: Property = Property(name="sd", type=StringType, synonyms=["Slice Differentiator If not needed, the value can be set to FFFFFF."])
SNssai_sst: Property = Property(name="sst", type=IntegerType, synonyms=["Slice/Service Type. Values 0 to 127 belong to standardized SST range and are defined in 3GPP TS 23.501. Values 128 to 255 belong to operator-specific range."])
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
domain_model.synonyms = ["The model defines common types for 5G networks and network slicing."]
