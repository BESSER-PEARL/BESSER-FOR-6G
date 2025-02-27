# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models.ietf_inet_types import domain_model as inet_model
from buml_generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model

# Classes
NEFFunction = Class(name="NEFFunction", synonyms=["5G Core NEF Function"])

# NEFFunction class attributes and methods
NEFFunction_isCAPIFSup: Property = Property(name="isCAPIFSup", type=BooleanType)
NEFFunction_isINEF: Property = Property(name="isINEF", type=BooleanType)
NEFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=inet_model.get_type_by_name('domain_name'), synonyms=["The FQDN of the registered NF instance in the service-based interface."])
NEFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=types5g3gpp_model.get_type_by_name('SNssai'), multiplicity=Multiplicity(0, "*"), synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
NEFFunction.attributes={NEFFunction_isCAPIFSup, NEFFunction_isINEF, NEFFunction_sBIFQDN, NEFFunction_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-neffunction",
    types={NEFFunction},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the NEF function in 5GC. For more information about the NEF, see 3GPP TS 23.501."]
