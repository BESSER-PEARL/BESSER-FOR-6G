# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models.ietf_inet_types import domain_model as inet_model
from buml_generated_models._3gpp_common_top import domain_model as top3gpp_model

# Classes
ExternalSEPPFunction = Class(name="ExternalSEPPFunction")

# ExternalSEPPFunction class attributes and methods
ExternalSEPPFunction_ExternalSEPPFunction: Property = Property(name="ExternalSEPPFunction", type=DataType('Top_Grp'), multiplicity=Multiplicity(0, "*"), synonyms=["5G Core SEPP Function"])
ExternalSEPPFunction_fqdn: Property = Property(name="fqdn", type=DataType('domain_name'), synonyms=["The domain name of the SEPP."])
ExternalSEPPFunction_sEPPId: Property = Property(name="sEPPId", type=IntegerType)
ExternalSEPPFunction.attributes={ExternalSEPPFunction_ExternalSEPPFunction, ExternalSEPPFunction_fqdn, ExternalSEPPFunction_sEPPId}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-externalseppfunction",
    types={ExternalSEPPFunction},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the external SEPP function which support message filtering and policing on inter-PLMN control plane interface. For more information about the SEPP, see 3GPP TS 23.501."]
