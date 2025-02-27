# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models.ietf_inet_types import domain_model as inet_model
from buml_generated_models._3gpp_5gc_nrm_seppfunction import domain_model as sepp3gpp_model

# Enumerations
SEPPType = Enumeration(name="SEPPType")
SEPPType_CSEPP = EnumerationLiteral(name="CSEPP", owner=SEPPType, synonyms=["consumer SEPP"])
SEPPType_PSEPP = EnumerationLiteral(name="PSEPP", owner=SEPPType, synonyms=["producer SEPP"])
SEPPType.literals = {SEPPType_CSEPP, SEPPType_PSEPP}

# Classes
SEPPFunction = Class(name="SEPPFunction", synonyms=["5G Core SEPP Function"])

# SEPPFunction class attributes and methods
SEPPFunction_fqdn: Property = Property(name="fqdn", type=inet_model.get_type_by_name('domain_name'), synonyms=["The domain name of the SEPP."])
SEPPFunction_sEPPId: Property = Property(name="sEPPId", type=IntegerType)
SEPPFunction_sEPPType: Property = Property(name="sEPPType", type=sepp3gpp_model.get_type_by_name('SEPPType'))
SEPPFunction.attributes={SEPPFunction_fqdn, SEPPFunction_sEPPId, SEPPFunction_sEPPType}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-seppfunction",
    types={SEPPFunction, SEPPType},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the SEPP function which support message filtering and policing on inter-PLMN control plane interface. For more information about the SEPP, see 3GPP TS 23.501."]
