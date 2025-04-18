# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
ExternalNRFFunction = Class(name="ExternalNRFFunction")

# ExternalNRFFunction class attributes and methods
ExternalNRFFunction_ExternalNRFFunction: Property = Property(name="ExternalNRFFunction", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["5G Core External NRF Function"])
ExternalNRFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=DataType('PLMNId'), multiplicity=Multiplicity(1, "*"), synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
ExternalNRFFunction.attributes={ExternalNRFFunction_ExternalNRFFunction, ExternalNRFFunction_pLMNIdList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-externalnrffunction",
    types={ExternalNRFFunction},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents external NRF function controlled by another management domain."]
