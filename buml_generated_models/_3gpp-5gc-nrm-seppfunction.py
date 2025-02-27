# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Enumerations
SEPPType = Enumeration(name="SEPPType")
SEPPType_CSEPP = EnumerationLiteral(name="CSEPP", owner=SEPPType, synonyms=["consumer SEPP"])
SEPPType_PSEPP = EnumerationLiteral(name="PSEPP", owner=SEPPType, synonyms=["producer SEPP"])
SEPPType.literals = {SEPPType_CSEPP, SEPPType_PSEPP}

# Classes
SEPPFunction = Class(name="SEPPFunction", synonyms=["5G Core SEPP Function"])

# SEPPFunction class attributes and methods
SEPPFunction_fqdn: Property = Property(name="fqdn", type=StringType, synonyms=["The domain name of the SEPP."])
SEPPFunction_sEPPId: Property = Property(name="sEPPId", type=IntegerType)
SEPPFunction_sEPPType: Property = Property(name="sEPPType", type=StringType)
SEPPFunction.attributes={SEPPFunction_fqdn, SEPPFunction_sEPPId, SEPPFunction_sEPPType}

SEPPFunctionGrp = Class(name="SEPPFunctionGrp")

# SEPPFunctionGrp class attributes and methods
SEPPFunctionGrp_fqdn: Property = Property(name="fqdn", type=StringType, synonyms=["The domain name of the SEPP."])
SEPPFunctionGrp_sEPPId: Property = Property(name="sEPPId", type=IntegerType)
SEPPFunctionGrp_sEPPType: Property = Property(name="sEPPType", type=StringType)
SEPPFunctionGrp.attributes={SEPPFunctionGrp_fqdn, SEPPFunctionGrp_sEPPId, SEPPFunctionGrp_sEPPType}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-seppfunction",
    types={SEPPFunction, SEPPFunctionGrp, SEPPType},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the SEPP function which support message filtering and policing on inter-PLMN control plane interface. For more information about the SEPP, see 3GPP TS 23.501."]
