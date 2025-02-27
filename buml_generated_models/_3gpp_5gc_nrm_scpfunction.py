# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models.ietf_inet_types import domain_model as inet_model
from buml_generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model

# Classes
SCPFunction = Class(name="SCPFunction", synonyms=["5G Core SCP Function"])

# SCPFunction class attributes and methods
SCPFunction_address: Property = Property(name="address", type=inet_model.get_type_by_name('host'), synonyms=["The host address of the SCP."])
SCPFunction_supportedFuncList: Property = Property(name="supportedFuncList", type=types5g3gpp_model.get_type_by_name('SupportedFunc'), multiplicity=Multiplicity(1, "*"))
SCPFunction.attributes={SCPFunction_address, SCPFunction_supportedFuncList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-scpfunction",
    types={SCPFunction},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the SCP function in 5GC. For more information about the SCP, see 3GPP TS 23.501."]
