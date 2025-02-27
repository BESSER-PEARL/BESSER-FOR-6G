# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
ExternalSEPPFunction = Class(name="ExternalSEPPFunction", synonyms=["5G Core SEPP Function"])

# ExternalSEPPFunction class attributes and methods
ExternalSEPPFunction_fqdn: Property = Property(name="fqdn", type=StringType, synonyms=["The domain name of the SEPP."])
ExternalSEPPFunction_sEPPId: Property = Property(name="sEPPId", type=IntegerType)
ExternalSEPPFunction.attributes={ExternalSEPPFunction_fqdn, ExternalSEPPFunction_sEPPId}

ExternalSEPPFunctionGrp = Class(name="ExternalSEPPFunctionGrp")

# ExternalSEPPFunctionGrp class attributes and methods
ExternalSEPPFunctionGrp_fqdn: Property = Property(name="fqdn", type=StringType, synonyms=["The domain name of the SEPP."])
ExternalSEPPFunctionGrp_sEPPId: Property = Property(name="sEPPId", type=IntegerType)
ExternalSEPPFunctionGrp.attributes={ExternalSEPPFunctionGrp_fqdn, ExternalSEPPFunctionGrp_sEPPId}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-externalseppfunction",
    types={ExternalSEPPFunction, ExternalSEPPFunctionGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the external SEPP function which support message filtering and policing on inter-PLMN control plane interface. For more information about the SEPP, see 3GPP TS 23.501."]
