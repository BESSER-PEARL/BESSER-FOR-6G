# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models.ietf_inet_types import domain_model as inet_model
from buml_generated_models._3gpp_5gc_nrm_nfprofile import domain_model as nfp3gpp_model
from buml_generated_models._3gpp_common_yang_types import domain_model as types3gpp_model
from buml_generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model

# Classes
NRFFunction = Class(name="NRFFunction", synonyms=["Represents the NRFFunction IOC"])

# NRFFunction class attributes and methods
NRFFunction_NRFFunction: Property = Property(name="NRFFunction", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["5G Core NRF Function"])
NRFFunction_nFProfileList: Property = Property(name="nFProfileList", type=DataType('NFProfileGrp'), multiplicity=Multiplicity(0, "*"), synonyms=["Set of NFProfile(s) to be registered in the NRF instance."])
NRFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=DataType('PLMNId'), multiplicity=Multiplicity(1, "*"), synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
NRFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=DataType('domain_name'), synonyms=["The FQDN of the registered NF instance in the service-based interface."])
NRFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=DataType('SNssai'), multiplicity=Multiplicity(0, "*"), synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
NRFFunction.attributes={NRFFunction_NRFFunction, NRFFunction_nFProfileList, NRFFunction_pLMNIdList, NRFFunction_sBIFQDN, NRFFunction_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-nrffunction",
    types={NRFFunction},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the NRF function in 5GC. For more information about the NRF, see 3GPP TS 23.501 [2]."]
