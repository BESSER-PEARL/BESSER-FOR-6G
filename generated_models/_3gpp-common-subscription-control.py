# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
HeartbeatControl = Class(name="HeartbeatControl")

# HeartbeatControl class attributes and methods
HeartbeatControl_heartbeatNtfPeriod: Property = Property(name="heartbeatNtfPeriod", type=IntegerType)
HeartbeatControl.attributes={HeartbeatControl_heartbeatNtfPeriod}

SubscriptionControlSubtree = Class(name="SubscriptionControlSubtree")

# SubscriptionControlSubtree class attributes and methods
SubscriptionControlSubtree_NtfSubscriptionControl: Property = Property(name="NtfSubscriptionControl", type=list)
SubscriptionControlSubtree.attributes={SubscriptionControlSubtree_NtfSubscriptionControl}

NtfSubscriptionControl = Class(name="NtfSubscriptionControl")

# NtfSubscriptionControl class attributes and methods
NtfSubscriptionControl_notificationFilter: Property = Property(name="notificationFilter", type=StringType)
NtfSubscriptionControl_scope: Property = Property(name="scope", type=list)
NtfSubscriptionControl_notificationRecipientAddress: Property = Property(name="notificationRecipientAddress", type=StringType)
NtfSubscriptionControl.attributes={NtfSubscriptionControl_notificationFilter, NtfSubscriptionControl_scope, NtfSubscriptionControl_notificationRecipientAddress}

