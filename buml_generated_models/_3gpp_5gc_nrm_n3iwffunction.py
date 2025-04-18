# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models._3gpp_common_yang_types import domain_model as types3gpp_model
from buml_generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model

# Classes
N3IWFFunction = Class(name="N3IWFFunction")

# N3IWFFunction class attributes and methods
N3IWFFunction_N3IWFFunction: Property = Property(name="N3IWFFunction", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["5G Core N3IWF Function"])
N3IWFFunction_commModelList: Property = Property(name="commModelList", type=DataType('CommModel'), multiplicity=Multiplicity(1, "*"))
N3IWFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=DataType('PLMNId'), multiplicity=Multiplicity(1, "*"), synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
N3IWFFunction.attributes={N3IWFFunction_N3IWFFunction, N3IWFFunction_commModelList, N3IWFFunction_pLMNIdList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-n3iwffunction",
    types={N3IWFFunction},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the N3IWF function which is used to enable non-3GPP access networks connected to the 5GC. For more information about the N3IWF, see 3GPP TS 23.501."]
