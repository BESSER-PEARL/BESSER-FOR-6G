# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models.ietf_inet_types import domain_model as inet_model
from buml_generated_models._3gpp_common_yang_types import domain_model as types3gpp_model
from buml_generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model

# Classes
AUSFFuntion = Class(name="AUSFFuntion", synonyms=["Represents the AUSFFuntion IOC"])

# AUSFFuntion class attributes and methods
AUSFFuntion_AUSFFunction: Property = Property(name="AUSFFunction", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["5G Core AUSF Function"])
AUSFFuntion_commModelList: Property = Property(name="commModelList", type=DataType('CommModel'), multiplicity=Multiplicity(1, "*"), synonyms=["Specifies a list of commModel. It can be used by NF and NF services to interact with each other in 5G Core network"])
AUSFFuntion_managedNFProfile: Property = Property(name="managedNFProfile", type=DataType('ManagedNFProfile'), multiplicity=Multiplicity(1, "*"))
AUSFFuntion_pLMNIdList: Property = Property(name="pLMNIdList", type=DataType('PLMNId'), multiplicity=Multiplicity(1, "*"), synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
AUSFFuntion_sBIFQDN: Property = Property(name="sBIFQDN", type=DataType('domain_name'), synonyms=["The FQDN of the registered NF instance in the service-based interface."])
AUSFFuntion_sNSSAIList: Property = Property(name="sNSSAIList", type=DataType('SNssai'), multiplicity=Multiplicity(0, "*"), synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
AUSFFuntion.attributes={AUSFFuntion_AUSFFunction, AUSFFuntion_commModelList, AUSFFuntion_managedNFProfile, AUSFFuntion_pLMNIdList, AUSFFuntion_sBIFQDN, AUSFFuntion_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-ausffunction",
    types={AUSFFuntion},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the AUSF function in 5GC. For more information about the AUSF, see 3GPP TS 23.501."]
