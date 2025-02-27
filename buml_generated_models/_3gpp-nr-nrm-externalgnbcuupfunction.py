# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
ExternalGNBCUUPFunction = Class(name="ExternalGNBCUUPFunction", synonyms=["Represets the ExternalGNBCUUPFunction IOC."])

# ExternalGNBCUUPFunction class attributes and methods
ExternalGNBCUUPFunction_gNBId: Property = Property(name="gNBId", type=IntegerType, synonyms=["Identifies a gNB within a PLMN."])
ExternalGNBCUUPFunction_gNBIdLength: Property = Property(name="gNBIdLength", type=IntegerType, synonyms=["Indicates the number of bits for encoding the gNB ID."])
ExternalGNBCUUPFunction.attributes={ExternalGNBCUUPFunction_gNBId, ExternalGNBCUUPFunction_gNBIdLength}

ExternalGNBCUUPFunctionWrapper = Class(name="ExternalGNBCUUPFunctionWrapper")

# ExternalGNBCUUPFunctionWrapper class attributes and methods
ExternalGNBCUUPFunctionWrapper_ExternalGNBCUUPFunction: Property = Property(name="ExternalGNBCUUPFunction", type=list, synonyms=["Represents the properties, known by the management function, of a GNBCUUPFunction managed by another management function."])
ExternalGNBCUUPFunctionWrapper.attributes={ExternalGNBCUUPFunctionWrapper_ExternalGNBCUUPFunction}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-externalgnbcuupfunction",
    types={ExternalGNBCUUPFunction, ExternalGNBCUUPFunctionWrapper},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the ExternalGNBCUUPFunction Information Object Class (IOC), that is part of the NR Network Resource Model (NRM)."]
