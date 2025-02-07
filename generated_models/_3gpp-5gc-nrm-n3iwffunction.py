# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
N3IWFFunction = Class(name="N3IWFFunction")

# N3IWFFunction class attributes and methods
N3IWFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
N3IWFFunction_commModelList: Property = Property(name="commModelList", type=list)
N3IWFFunction.attributes={N3IWFFunction_pLMNIdList, N3IWFFunction_commModelList}

