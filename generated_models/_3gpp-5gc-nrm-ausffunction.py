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
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_managed_element import domain_model as me3gpp_model
from generated_models._3gpp_common_managed_function import domain_model as mf3gpp_model
from generated_models._3gpp_common_subnetwork import domain_model as subnet3gpp_model
from generated_models._3gpp_common_top import domain_model as top3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Enumerations
# Classes
AUSFFuntionGrp = Class(name="AUSFFuntionGrp")
AUSFFunction = Class(name="AUSFFunction")

# AUSFFuntionGrp class attributes and methods
AUSFFuntionGrp_sBIFQDN: Property = Property(name="sBIFQDN", type=inet:domain-name)
AUSFFuntionGrp_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
AUSFFuntionGrp_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
AUSFFuntionGrp_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
AUSFFuntionGrp_commModelList: Property = Property(name="commModelList", type=list)
AUSFFuntionGrp.attributes={AUSFFuntionGrp_pLMNIdList, AUSFFuntionGrp_sNSSAIList, AUSFFuntionGrp_managedNFProfile, AUSFFuntionGrp_commModelList, AUSFFuntionGrp_sBIFQDN}

# AUSFFunction class attributes and methods
AUSFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=inet:domain-name)
AUSFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
AUSFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
AUSFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
AUSFFunction_commModelList: Property = Property(name="commModelList", type=list)
AUSFFunction.attributes={AUSFFunction_pLMNIdList, AUSFFunction_sNSSAIList, AUSFFunction_managedNFProfile, AUSFFunction_commModelList, AUSFFunction_sBIFQDN}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-ausffunction",
    types={AUSFFuntionGrp, AUSFFunction, types3gpp_model, mf3gpp_model, me3gpp_model, top3gpp_model, types5g3gpp_model, inet_model, subnet3gpp_model},
    associations={},
    generalizations={}
)
