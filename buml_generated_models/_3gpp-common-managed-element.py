# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
ManagedElement = Class(name="ManagedElement")

# ManagedElement class attributes and methods
ManagedElement_ManagedElement: Property = Property(name="ManagedElement", type=list)
ManagedElement_priorityLabel: Property = Property(name="priorityLabel", type=IntegerType)
ManagedElement_swVersion: Property = Property(name="swVersion", type=StringType)
ManagedElement_userDefinedState: Property = Property(name="userDefinedState", type=StringType)
ManagedElement_vendorName: Property = Property(name="vendorName", type=StringType)
ManagedElement.attributes={ManagedElement_ManagedElement, ManagedElement_priorityLabel, ManagedElement_swVersion, ManagedElement_userDefinedState, ManagedElement_vendorName}

ManagedElement_ = Class(name="ManagedElement_")

# ManagedElement_ class attributes and methods
ManagedElement__dnPrefix: Property = Property(name="dnPrefix", type=StringType)
ManagedElement__locationName: Property = Property(name="locationName", type=StringType)
ManagedElement__userLabel: Property = Property(name="userLabel", type=StringType)
ManagedElement_.attributes={ManagedElement__dnPrefix, ManagedElement__locationName, ManagedElement__userLabel}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-common-managed-element",
    types={ManagedElement, ManagedElement_},
    associations={},
    generalizations={}
)
