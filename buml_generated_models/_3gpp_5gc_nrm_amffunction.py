# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Import referenced models
# from buml_generated_models.ietf_inet_types import domain_model as inet_model
# from buml_generated_models._3gpp_common_yang_types import domain_model as types3gpp_model
# from buml_generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model

# Classes
AMFFunction = Class(name="AMFFunction", synonyms=["5G Core AMF Function"])

# AMFFunction class attributes and methods
AMFFunction_commModelList: Property = Property(name="commModelList", type=CommModel, multiplicity=Multiplicity(1, "*"), synonyms=["Specifies a list of commModel. It can be used by NF and NF services to interact with each other in 5G Core network"])
AMFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=types3gpp_model.get_type_by_name('ManagedNFProfile'), multiplicity=Multiplicity(1, "*"))
AMFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=types3gpp_model.get_type_by_name('PLMNId'), multiplicity=Multiplicity(1, "*"), synonyms=["A list of PLMN identifiers (Mobile Country Code and Mobile Network Code)."])
AMFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=inet_model.get_type_by_name('domain_name'), synonyms=["The FQDN of the registered NF instance in the service-based interface."])
AMFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=types5g3gpp_model.get_type_by_name('SNssai'), multiplicity=Multiplicity(1, "*"), synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
AMFFunction.attributes={AMFFunction_commModelList, AMFFunction_managedNFProfile, AMFFunction_pLMNIdList, AMFFunction_sBIFQDN, AMFFunction_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-amffunction",
    types={AMFFunction},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["AMFFunction derived from basic ManagedFunction."]

from besser_generator.json_schema_generator import JSONSchemaGenerator
generator = JSONSchemaGenerator(domain_model, "generatedsmartdata")
generator.generate()
print("Successfully generated schema for _3gpp-5gc-nrm-amffunction")
