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
ExternalNSSFFunction = Class(name="ExternalNSSFFunction")

# ExternalNSSFFunction class attributes and methods
ExternalNSSFFunction_ExternalNSSFFunction: Property = Property(name="ExternalNSSFFunction", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["5G Core External NSSF Function"])
ExternalNSSFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=DataType('PLMNId'), multiplicity=Multiplicity(1, "*"), synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
ExternalNSSFFunction.attributes={ExternalNSSFFunction_ExternalNSSFFunction, ExternalNSSFFunction_pLMNIdList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-externalnssffunction",
    types={ExternalNSSFFunction},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents external NSSF function controlled by another management domain."]
