# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
NRFrequency = Class(name="NRFrequency")

# NRFrequency class attributes and methods
NRFrequency_absoluteFrequencySSB: Property = Property(name="absoluteFrequencySSB", type=IntegerType)
NRFrequency_sSBSubCarrierSpacing: Property = Property(name="sSBSubCarrierSpacing", type=IntegerType)
NRFrequency.attributes={NRFrequency_absoluteFrequencySSB, NRFrequency_sSBSubCarrierSpacing}

NRFrequencyWrapper = Class(name="NRFrequencyWrapper")

# NRFrequencyWrapper class attributes and methods
NRFrequencyWrapper_NRFrequency: Property = Property(name="NRFrequency", type=list)
NRFrequencyWrapper.attributes={NRFrequencyWrapper_NRFrequency}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-nrfrequency",
    types={NRFrequency, NRFrequencyWrapper},
    associations={},
    generalizations={}
)
