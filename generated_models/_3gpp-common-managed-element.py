# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
ManagedElement_ = Class(name="ManagedElement_")

# ManagedElement_ class attributes and methods
ManagedElement__dnPrefix: Property = Property(name="dnPrefix", type=types3gpp:DistinguishedName)
ManagedElement__userLabel: Property = Property(name="userLabel", type=StringType)
ManagedElement__locationName: Property = Property(name="locationName", type=StringType)
ManagedElement_.attributes={ManagedElement__dnPrefix, ManagedElement__userLabel, ManagedElement__locationName}

ManagedElement = Class(name="ManagedElement")

# ManagedElement class attributes and methods
ManagedElement_vendorName: Property = Property(name="vendorName", type=StringType)
ManagedElement_userDefinedState: Property = Property(name="userDefinedState", type=StringType)
ManagedElement_swVersion: Property = Property(name="swVersion", type=StringType)
ManagedElement_priorityLabel: Property = Property(name="priorityLabel", type=IntegerType)
ManagedElement_ManagedElement: Property = Property(name="ManagedElement", type=list)
ManagedElement.attributes={ManagedElement_vendorName, ManagedElement_userDefinedState, ManagedElement_swVersion, ManagedElement_priorityLabel, ManagedElement_ManagedElement}

