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
from generated_models._3gpp_common_managed_element import domain_model as me3gpp_model
from generated_models._3gpp_common_managed_function import domain_model as mf3gpp_model
from generated_models._3gpp_common_top import domain_model as top3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Enumerations
# Classes
AFFunctionGrp = Class(name="AFFunctionGrp")
AFFunction = Class(name="AFFunction")

# AFFunctionGrp class attributes and methods

# AFFunction class attributes and methods

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-affunction",
    types={AFFunctionGrp, AFFunction, types3gpp_model, mf3gpp_model, me3gpp_model, top3gpp_model},
    associations={},
    generalizations={}
)
