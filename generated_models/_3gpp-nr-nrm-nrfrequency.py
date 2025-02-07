# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

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

