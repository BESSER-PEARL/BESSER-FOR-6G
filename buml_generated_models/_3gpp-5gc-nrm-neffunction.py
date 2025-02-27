# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
NEFFunction = Class(name="NEFFunction", synonyms=["5G Core NEF Function"])

# NEFFunction class attributes and methods
NEFFunction_isCAPIFSup: Property = Property(name="isCAPIFSup", type=BooleanType)
NEFFunction_isINEF: Property = Property(name="isINEF", type=BooleanType)
NEFFunction_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType, synonyms=["The FQDN of the registered NF instance in the service-based interface."])
NEFFunction_sNSSAIList: Property = Property(name="sNSSAIList", type=list, synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
NEFFunction.attributes={NEFFunction_isCAPIFSup, NEFFunction_isINEF, NEFFunction_sBIFQDN, NEFFunction_sNSSAIList}

NEFFunctionGrp = Class(name="NEFFunctionGrp", synonyms=["Represents the NEFFunction IOC"])

# NEFFunctionGrp class attributes and methods
NEFFunctionGrp_isCAPIFSup: Property = Property(name="isCAPIFSup", type=BooleanType)
NEFFunctionGrp_isINEF: Property = Property(name="isINEF", type=BooleanType)
NEFFunctionGrp_sBIFQDN: Property = Property(name="sBIFQDN", type=StringType, synonyms=["The FQDN of the registered NF instance in the service-based interface."])
NEFFunctionGrp_sNSSAIList: Property = Property(name="sNSSAIList", type=list, synonyms=["List of S-NSSAIs the managed object is capable of supporting. (Single Network Slice Selection Assistance Information) An S-NSSAI has an SST (Slice/Service type) and an optional SD (Slice Differentiator) field."])
NEFFunctionGrp.attributes={NEFFunctionGrp_isCAPIFSup, NEFFunctionGrp_isINEF, NEFFunctionGrp_sBIFQDN, NEFFunctionGrp_sNSSAIList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-neffunction",
    types={NEFFunction, NEFFunctionGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the NEF function in 5GC. For more information about the NEF, see 3GPP TS 23.501."]
