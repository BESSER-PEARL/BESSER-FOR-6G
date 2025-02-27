# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models._3gpp_common_yang_types import domain_model as types3gpp_model
from buml_generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model

# Classes
SMSFFunction = Class(name="SMSFFunction", synonyms=["5G Core SMSF Function"])

# SMSFFunction class attributes and methods
SMSFFunction_commModelList: Property = Property(name="commModelList", type=types5g3gpp_model.get_type_by_name('CommModel'), multiplicity=Multiplicity(1, "*"))
SMSFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=types3gpp_model.get_type_by_name('ManagedNFProfile'), multiplicity=Multiplicity(1, "*"))
SMSFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=types3gpp_model.get_type_by_name('PLMNId'), multiplicity=Multiplicity(1, "*"), synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
SMSFFunction.attributes={SMSFFunction_commModelList, SMSFFunction_managedNFProfile, SMSFFunction_pLMNIdList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-smsffunction",
    types={SMSFFunction},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the SMSF function defined in 3GPP TS 23.501."]
