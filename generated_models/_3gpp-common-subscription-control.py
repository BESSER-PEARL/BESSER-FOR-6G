# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
HeartbeatControl = Class(name="HeartbeatControl")

# HeartbeatControl class attributes and methods
HeartbeatControl_heartbeatNtfPeriod: Property = Property(name="heartbeatNtfPeriod", type=IntegerType)
HeartbeatControl.attributes={HeartbeatControl_heartbeatNtfPeriod}

NtfSubscriptionControl = Class(name="NtfSubscriptionControl")

# NtfSubscriptionControl class attributes and methods
NtfSubscriptionControl_notificationFilter: Property = Property(name="notificationFilter", type=StringType)
NtfSubscriptionControl_notificationRecipientAddress: Property = Property(name="notificationRecipientAddress", type=StringType)
NtfSubscriptionControl_scope: Property = Property(name="scope", type=list)
NtfSubscriptionControl.attributes={NtfSubscriptionControl_notificationFilter, NtfSubscriptionControl_notificationRecipientAddress, NtfSubscriptionControl_scope}

SubscriptionControlSubtree = Class(name="SubscriptionControlSubtree")

# SubscriptionControlSubtree class attributes and methods
SubscriptionControlSubtree_NtfSubscriptionControl: Property = Property(name="NtfSubscriptionControl", type=list)
SubscriptionControlSubtree.attributes={SubscriptionControlSubtree_NtfSubscriptionControl}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-common-subscription-control",
    types={HeartbeatControl, NtfSubscriptionControl, SubscriptionControlSubtree},
    associations={},
    generalizations={}
)
