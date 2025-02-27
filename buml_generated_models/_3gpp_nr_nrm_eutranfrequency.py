# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
EUtranFrequency = Class(name="EUtranFrequency", synonyms=["Represents the EUtranFrequency IOC."])

# EUtranFrequency class attributes and methods
EUtranFrequency_earfcnDL: Property = Property(name="earfcnDL", type=IntegerType, synonyms=["Specifies the channel number for the central DL frequency."])
EUtranFrequency.attributes={EUtranFrequency_earfcnDL}

EUtranFrequencyWrapper = Class(name="EUtranFrequencyWrapper")

# EUtranFrequencyWrapper class attributes and methods
EUtranFrequencyWrapper_EUtranFrequency: Property = Property(name="EUtranFrequency", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["Represents certain E-UTRAN frequency properties."])
EUtranFrequencyWrapper.attributes={EUtranFrequencyWrapper_EUtranFrequency}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-eutranfrequency",
    types={EUtranFrequency, EUtranFrequencyWrapper},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the EUtranFrequency Information Object Class (IOC), that is part of the NR Network Resource Model (NRM)."]
