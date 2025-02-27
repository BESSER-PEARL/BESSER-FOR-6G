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
UPFFunction = Class(name="UPFFunction", synonyms=["5G Core UPF Function"])

# UPFFunction class attributes and methods
UPFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=types3gpp_model.get_type_by_name('ManagedNFProfile'), multiplicity=Multiplicity(1, "*"))
UPFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=types3gpp_model.get_type_by_name('PLMNId'), multiplicity=Multiplicity(1, "*"), synonyms=["A list of PLMN identifiers (Mobile Country Code and Mobile Network Code)."])
UPFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=types5g3gpp_model.get_type_by_name('SNssai'), multiplicity=Multiplicity(0, "*"), synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
UPFFunction.attributes={UPFFunction_managedNFProfile, UPFFunction_pLMNIdList, UPFFunction_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-upffunction",
    types={UPFFunction},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["UPFFunction derived from basic ManagedFunction."]
