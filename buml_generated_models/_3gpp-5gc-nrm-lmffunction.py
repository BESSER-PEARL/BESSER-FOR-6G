# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
LMFFunction = Class(name="LMFFunction", synonyms=["5G Core LMF Function"])

# LMFFunction class attributes and methods
LMFFunction_commModelList: Property = Property(name="commModelList", type=list)
LMFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
LMFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
LMFFunction.attributes={LMFFunction_commModelList, LMFFunction_managedNFProfile, LMFFunction_pLMNIdList}

LMFFunctionGrp = Class(name="LMFFunctionGrp")

# LMFFunctionGrp class attributes and methods
LMFFunctionGrp_commModelList: Property = Property(name="commModelList", type=list)
LMFFunctionGrp_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
LMFFunctionGrp_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
LMFFunctionGrp.attributes={LMFFunctionGrp_commModelList, LMFFunctionGrp_managedNFProfile, LMFFunctionGrp_pLMNIdList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-lmffunction",
    types={LMFFunction, LMFFunctionGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the LMF function defined in 3GPP TS 23.501."]
