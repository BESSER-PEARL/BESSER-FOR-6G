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
UPFFunction = Class(name="UPFFunction", synonyms=["Represents the UPFFunction IOC"])

# UPFFunction class attributes and methods
UPFFunction_UPFFunction: Property = Property(name="UPFFunction", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["5G Core UPF Function"])
UPFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=DataType('ManagedNFProfile'), multiplicity=Multiplicity(1, "*"))
UPFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=DataType('PLMNId'), multiplicity=Multiplicity(1, "*"), synonyms=["A list of PLMN identifiers (Mobile Country Code and Mobile Network Code)."])
UPFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=DataType('SNssai'), multiplicity=Multiplicity(0, "*"), synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
UPFFunction.attributes={UPFFunction_UPFFunction, UPFFunction_managedNFProfile, UPFFunction_pLMNIdList, UPFFunction_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-upffunction",
    types={UPFFunction},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["UPFFunction derived from basic ManagedFunction."]
