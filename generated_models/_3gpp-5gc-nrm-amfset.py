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
AMFSetGrp = Class(name="AMFSetGrp")
AMFSet = Class(name="AMFSet")

# AMFSetGrp class attributes and methods
AMFSetGrp_aMFRegion: Property = Property(name="aMFRegion", type=instance-identifier)
AMFSetGrp_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
AMFSetGrp_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
AMFSetGrp.attributes={AMFSetGrp_sNSSAIList, AMFSetGrp_pLMNIdList, AMFSetGrp_aMFRegion}

# AMFSet class attributes and methods
AMFSet_aMFRegion: Property = Property(name="aMFRegion", type=instance-identifier)
AMFSet_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
AMFSet_sNSSAIList: Property = Property(name="sNSSAIList", type=list)
AMFSet.attributes={AMFSet_sNSSAIList, AMFSet_pLMNIdList, AMFSet_aMFRegion}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-amfset",
    types={AMFSetGrp, AMFSet, types3gpp_model, mf3gpp_model, me3gpp_model, top3gpp_model, types5g3gpp_model, inet_model, subnet3gpp_model},
    associations={},
    generalizations={}
)
