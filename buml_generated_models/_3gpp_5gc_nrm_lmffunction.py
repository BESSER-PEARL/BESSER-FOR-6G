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
LMFFunction = Class(name="LMFFunction")

# LMFFunction class attributes and methods
LMFFunction_LMFFunction: Property = Property(name="LMFFunction", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["5G Core LMF Function"])
LMFFunction_commModelList: Property = Property(name="commModelList", type=DataType('CommModel'), multiplicity=Multiplicity(1, "*"))
LMFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=DataType('ManagedNFProfile'), multiplicity=Multiplicity(1, "*"))
LMFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=DataType('PLMNId'), multiplicity=Multiplicity(1, "*"), synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
LMFFunction.attributes={LMFFunction_LMFFunction, LMFFunction_commModelList, LMFFunction_managedNFProfile, LMFFunction_pLMNIdList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-lmffunction",
    types={LMFFunction},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the LMF function defined in 3GPP TS 23.501."]
