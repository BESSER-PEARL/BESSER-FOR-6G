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
from generated_models._3gpp_5gc_nrm_configurable5qiset import domain_model as Conf5QIs3gpp_model
from generated_models._3gpp_common_managed_element import domain_model as me3gpp_model
from generated_models._3gpp_common_managed_function import domain_model as mf3gpp_model
from generated_models._3gpp_common_subnetwork import domain_model as subnet3gpp_model
from generated_models._3gpp_common_top import domain_model as top3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Enumerations
# Classes
Dynamic5QISetGrp = Class(name="Dynamic5QISetGrp")
Dynamic5QISetSubtree = Class(name="Dynamic5QISetSubtree")

# Dynamic5QISetGrp class attributes and methods
Dynamic5QISetGrp_dynamic5QIs: Property = Property(name="dynamic5QIs", type=list)
Dynamic5QISetGrp.attributes={Dynamic5QISetGrp_dynamic5QIs}

# Dynamic5QISetSubtree class attributes and methods
Dynamic5QISetSubtree_Dynamic5QISet: Property = Property(name="Dynamic5QISet", type=list)
Dynamic5QISetSubtree.attributes={Dynamic5QISetSubtree_Dynamic5QISet}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-dynamic5qiset",
    types={Dynamic5QISetGrp, Dynamic5QISetSubtree, types3gpp_model, mf3gpp_model, me3gpp_model, top3gpp_model, types5g3gpp_model, inet_model, subnet3gpp_model, Conf5QIs3gpp_model},
    associations={},
    generalizations={}
)
