# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
ExternalENBFunction = Class(name="ExternalENBFunction", synonyms=["Represets the ExternalENBFunction IOC."])

# ExternalENBFunction class attributes and methods
ExternalENBFunction_eNBId: Property = Property(name="eNBId", type=IntegerType, synonyms=["Unambiguously identifies an eNodeB within a PLMN."])
ExternalENBFunction.attributes={ExternalENBFunction_eNBId}

ExternalENBFunctionWrapper = Class(name="ExternalENBFunctionWrapper")

# ExternalENBFunctionWrapper class attributes and methods
ExternalENBFunctionWrapper_ExternalENBFunction: Property = Property(name="ExternalENBFunction", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["Represents an external eNB functionality."])
ExternalENBFunctionWrapper.attributes={ExternalENBFunctionWrapper_ExternalENBFunction}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-externalenbfunction",
    types={ExternalENBFunction, ExternalENBFunctionWrapper},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the ExternalENBFunction Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
