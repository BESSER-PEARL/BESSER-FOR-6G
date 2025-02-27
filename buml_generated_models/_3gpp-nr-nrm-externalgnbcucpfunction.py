# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
ExternalGNBCUCPFunction = Class(name="ExternalGNBCUCPFunction", synonyms=["Represets the ExternalGNBCUCPFunction IOC."])

# ExternalGNBCUCPFunction class attributes and methods
ExternalGNBCUCPFunction_gNBId: Property = Property(name="gNBId", type=IntegerType, synonyms=["Identifies a gNB within a PLMN."])
ExternalGNBCUCPFunction_gNBIdLength: Property = Property(name="gNBIdLength", type=IntegerType, synonyms=["Indicates the number of bits for encoding the gNB ID."])
ExternalGNBCUCPFunction_pLMNId: Property = Property(name="pLMNId", type=list, synonyms=["Specifies the PLMN identifier to be used as part of the global RAN node identity."])
ExternalGNBCUCPFunction.attributes={ExternalGNBCUCPFunction_gNBId, ExternalGNBCUCPFunction_gNBIdLength, ExternalGNBCUCPFunction_pLMNId}

ExternalGNBCUCPFunctionWrapper = Class(name="ExternalGNBCUCPFunctionWrapper")

# ExternalGNBCUCPFunctionWrapper class attributes and methods
ExternalGNBCUCPFunctionWrapper_ExternalGNBCUCPFunction: Property = Property(name="ExternalGNBCUCPFunction", type=list, synonyms=["Represents the properties, known by the management function, of a GNBCUCPFunction managed by another management function."])
ExternalGNBCUCPFunctionWrapper.attributes={ExternalGNBCUCPFunctionWrapper_ExternalGNBCUCPFunction}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-externalgnbcucpfunction",
    types={ExternalGNBCUCPFunction, ExternalGNBCUCPFunctionWrapper},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the ExternalGNBCUCPFunction Information Object Class (IOC), that is part of the NR Network Resource Model (NRM)."]
