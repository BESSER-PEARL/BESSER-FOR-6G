# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
ExternalAMFFunction = Class(name="ExternalAMFFunction", synonyms=["Represents the ExternalAMFFunction IOC."])

# ExternalAMFFunction class attributes and methods
ExternalAMFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list, synonyms=["List of at most six entries of PLMN Identifiers, but at least one (the primary PLMN Id). The PLMN Identifier is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
ExternalAMFFunction.attributes={ExternalAMFFunction_pLMNIdList}

ExternalAMFFunctionWrapper = Class(name="ExternalAMFFunctionWrapper")

# ExternalAMFFunctionWrapper class attributes and methods
ExternalAMFFunctionWrapper_ExternalAMFFunction: Property = Property(name="ExternalAMFFunction", type=list, synonyms=["Represents the properties, known by the management function, of a AMFFunction managed by another management function."])
ExternalAMFFunctionWrapper.attributes={ExternalAMFFunctionWrapper_ExternalAMFFunction}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-externalamffunction",
    types={ExternalAMFFunction, ExternalAMFFunctionWrapper},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the ExternalAMFFunction Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
