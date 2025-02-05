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
from generated_models._3gpp_common_top import domain_model as top3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Enumerations
# Classes
AMFFunctionGrp = Class(name="AMFFunctionGrp")
AMFFunction = Class(name="AMFFunction")

# AMFFunctionGrp class attributes and methods
AMFFunctionGrp_sBIFQDN: Property = Property(name="sBIFQDN", type=inet:domain-name)
AMFFunctionGrp_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
AMFFunctionGrp_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
AMFFunctionGrp_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
AMFFunctionGrp_commModelList: Property = Property(name="commModelList", type=list)
AMFFunctionGrp.attributes={AMFFunctionGrp_commModelList, AMFFunctionGrp_sBIFQDN, AMFFunctionGrp_pLMNIdList, AMFFunctionGrp_sNSSAIList, AMFFunctionGrp_managedNFProfile}

# AMFFunction class attributes and methods
AMFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=inet:domain-name)
AMFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
AMFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
AMFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
AMFFunction_commModelList: Property = Property(name="commModelList", type=list)
AMFFunction.attributes={AMFFunction_commModelList, AMFFunction_sBIFQDN, AMFFunction_pLMNIdList, AMFFunction_sNSSAIList, AMFFunction_managedNFProfile}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-amffunction",
    types={AMFFunctionGrp, AMFFunction, types3gpp_model, mf3gpp_model, me3gpp_model, top3gpp_model, types5g3gpp_model, inet_model},
    associations={},
    generalizations={}
)
