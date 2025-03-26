# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models.ietf_inet_types import domain_model as inet_model
from buml_generated_models._3gpp_common_top import domain_model as top3gpp_model
from buml_generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model

# Classes
SCPFunction = Class(name="SCPFunction")

# SCPFunction class attributes and methods
SCPFunction_SCPFunction: Property = Property(name="SCPFunction", type=DataType('Top_Grp'), multiplicity=Multiplicity(0, "*"), synonyms=["5G Core SCP Function"])
SCPFunction_address: Property = Property(name="address", type=DataType('host'), synonyms=["The host address of the SCP."])
SCPFunction_supportedFuncList: Property = Property(name="supportedFuncList", type=DataType('SupportedFunc'), multiplicity=Multiplicity(1, "*"))
SCPFunction.attributes={SCPFunction_SCPFunction, SCPFunction_address, SCPFunction_supportedFuncList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-scpfunction",
    types={SCPFunction},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the SCP function in 5GC. For more information about the SCP, see 3GPP TS 23.501."]
