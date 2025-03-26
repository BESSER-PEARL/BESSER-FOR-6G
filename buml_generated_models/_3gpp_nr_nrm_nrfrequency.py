# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Classes
NRFrequency = Class(name="NRFrequency", synonyms=["Represents the NRFrequency IOC."])

# NRFrequency class attributes and methods
NRFrequency_absoluteFrequencySSB: Property = Property(name="absoluteFrequencySSB", type=IntegerType, synonyms=["The absolute frequency applicable for a downlink NR carrier frequency associated with the SSB, in terms of NR-ARFCN."])
NRFrequency_sSBSubCarrierSpacing: Property = Property(name="sSBSubCarrierSpacing", type=IntegerType, synonyms=["Sub-carrier spacing of the SSB."])
NRFrequency.attributes={NRFrequency_absoluteFrequencySSB, NRFrequency_sSBSubCarrierSpacing}

NRFrequencyWrapper = Class(name="NRFrequencyWrapper")

# NRFrequencyWrapper class attributes and methods
NRFrequencyWrapper_NRFrequency: Property = Property(name="NRFrequency", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["Represents certain NR frequency properties."])
NRFrequencyWrapper.attributes={NRFrequencyWrapper_NRFrequency}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-nrfrequency",
    types={NRFrequency, NRFrequencyWrapper},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the NRFrequency Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
