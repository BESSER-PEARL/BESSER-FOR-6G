# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
N3IWFFunction = Class(name="N3IWFFunction", synonyms=["5G Core N3IWF Function"])

# N3IWFFunction class attributes and methods
N3IWFFunction_commModelList: Property = Property(name="commModelList", type=list)
N3IWFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
N3IWFFunction.attributes={N3IWFFunction_commModelList, N3IWFFunction_pLMNIdList}

N3IWFFunctionGrp = Class(name="N3IWFFunctionGrp")

# N3IWFFunctionGrp class attributes and methods
N3IWFFunctionGrp_commModelList: Property = Property(name="commModelList", type=list)
N3IWFFunctionGrp_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
N3IWFFunctionGrp.attributes={N3IWFFunctionGrp_commModelList, N3IWFFunctionGrp_pLMNIdList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-n3iwffunction",
    types={N3IWFFunction, N3IWFFunctionGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the N3IWF function which is used to enable non-3GPP access networks connected to the 5GC. For more information about the N3IWF, see 3GPP TS 23.501."]
