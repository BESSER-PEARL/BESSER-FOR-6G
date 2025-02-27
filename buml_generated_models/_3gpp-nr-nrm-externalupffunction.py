# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
ExternalUPFFunction = Class(name="ExternalUPFFunction", synonyms=["Represents the ExternalUPFFunction IOC."])

# ExternalUPFFunction class attributes and methods
ExternalUPFFunctionWrapper = Class(name="ExternalUPFFunctionWrapper")

# ExternalUPFFunctionWrapper class attributes and methods
ExternalUPFFunctionWrapper_ExternalUPFFunction: Property = Property(name="ExternalUPFFunction", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["Represents the properties, known by the management function, of a UPFFunction managed by another management function."])
ExternalUPFFunctionWrapper.attributes={ExternalUPFFunctionWrapper_ExternalUPFFunction}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-externalupffunction",
    types={ExternalUPFFunction, ExternalUPFFunctionWrapper},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the ExternalUPFFunction Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
