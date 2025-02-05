# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    Constraint
)

# Import referenced models
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Enumerations
CommModelType: Enumeration = Enumeration(
    name="CommModelType",
    literals={
            EnumerationLiteral(name="DIRECT_COMMUNICATION_WO_NRF"),
			EnumerationLiteral(name="DIRECT_COMMUNICATION_WITH_NRF"),
			EnumerationLiteral(name="INDIRECT_COMMUNICATION_WO_DEDICATED_DISCOVERY"),
			EnumerationLiteral(name="INDIRECT_COMMUNICATION_WITH_DEDICATED_DISCOVERY")
    }
)

# Classes
SNssai = Class(name="SNssai")
PLMNInfo = Class(name="PLMNInfo")
CommModel = Class(name="CommModel")
SupportedFunc = Class(name="SupportedFunc")

# SNssai class attributes and methods
SNssai_sd: Property = Property(name="sd", type=StringType)
SNssai_sst: Property = Property(name="sst", type=IntegerType)
SNssai.attributes={SNssai_sst, SNssai_sd}

# PLMNInfo class attributes and methods

# CommModel class attributes and methods
CommModel_groupId: Property = Property(name="groupId", type=IntegerType)
CommModel_commModelType: Property = Property(name="commModelType", type=CommModelType)
CommModel_commModelConfiguration: Property = Property(name="commModelConfiguration", type=StringType)
CommModel.attributes={CommModel_commModelConfiguration, CommModel_groupId, CommModel_commModelType}

# SupportedFunc class attributes and methods
SupportedFunc_function: Property = Property(name="function", type=StringType)
SupportedFunc_policy: Property = Property(name="policy", type=StringType)
SupportedFunc.attributes={SupportedFunc_policy, SupportedFunc_function}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5g-common-yang-types",
    types={SNssai, PLMNInfo, CommModel, SupportedFunc, CommModelType, types3gpp_model},
    associations={},
    generalizations={}
)
