# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models.ietf_inet_types import domain_model as inet_model
from buml_generated_models._3gpp_common_yang_types import domain_model as types3gpp_model
from buml_generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model

# Classes
SMFFunction = Class(name="SMFFunction", synonyms=["5G Core SMF Function"])

# SMFFunction class attributes and methods
SMFFunction_commModelList: Property = Property(name="commModelList", type=types5g3gpp_model.get_type_by_name('CommModel'), multiplicity=Multiplicity(1, "*"), synonyms=["Specifies a list of commModel. It can be used by NF and NF services to interact with each other in 5G Core network"])
SMFFunction_configurable5QISetRef: Property = Property(name="configurable5QISetRef", type=types3gpp_model.get_type_by_name('DistinguishedName'), synonyms=["DN of the Configurable5QISet that the SMFFunction supports (is associated to)."])
SMFFunction_dynamic5QISetRef: Property = Property(name="dynamic5QISetRef", type=types3gpp_model.get_type_by_name('DistinguishedName'), synonyms=["DN of the Dynamic5QISet that the SMFFunction supports (is associated to)."])
SMFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=types3gpp_model.get_type_by_name('ManagedNFProfile'), multiplicity=Multiplicity(1, "*"))
SMFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=types3gpp_model.get_type_by_name('PLMNId'), multiplicity=Multiplicity(1, "*"), synonyms=["A list of PLMN identifiers (Mobile Country Code and Mobile Network Code)."])
SMFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=inet_model.get_type_by_name('domain_name'), synonyms=["The FQDN of the registered NF instance in the service-based interface."])
SMFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=types5g3gpp_model.get_type_by_name('SNssai'), multiplicity=Multiplicity(0, "*"), synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
SMFFunction.attributes={SMFFunction_commModelList, SMFFunction_configurable5QISetRef, SMFFunction_dynamic5QISetRef, SMFFunction_managedNFProfile, SMFFunction_pLMNIdList, SMFFunction_sBIFQDN, SMFFunction_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-smffunction",
    types={SMFFunction},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["SMFFunction derived from basic ManagedFunction."]
