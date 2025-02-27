# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models._3gpp_common_top import domain_model as top3gpp_model

# Classes
HeartbeatControl = Class(name="HeartbeatControl", synonyms=["Attributes of HeartbeatControl. Note the triggerHeartbeatNtf attribute has no mapping in the present release."])

# HeartbeatControl class attributes and methods
HeartbeatControl_heartbeatNtfPeriod: Property = Property(name="heartbeatNtfPeriod", type=IntegerType, synonyms=["Specifies the periodicity of heartbeat notification emission. The value of zero has the special meaning of stopping the heartbeat notification emission."])
HeartbeatControl.attributes={HeartbeatControl_heartbeatNtfPeriod}

NtfSubscriptionControl = Class(name="NtfSubscriptionControl", synonyms=["Attributes of a specific notification subscription"])

# NtfSubscriptionControl class attributes and methods
NtfSubscriptionControl_notificationFilter: Property = Property(name="notificationFilter", type=StringType, synonyms=["Defines a filter to be applied to candidate notifications identified by the notificationTypes attribute. If notificationFilter is present, only notifications that pass the filter criteria are forwarded to the notification recipient; all other notifications are discarded. The filter can be applied to any field of a notification."])
NtfSubscriptionControl_notificationRecipientAddress: Property = Property(name="notificationRecipientAddress", type=StringType)
NtfSubscriptionControl_scope: Property = Property(name="scope", type=list, multiplicity=Multiplicity(1, "*"), synonyms=["Describes which object instances are selected with respect to a base object instance."])
NtfSubscriptionControl.attributes={NtfSubscriptionControl_notificationFilter, NtfSubscriptionControl_notificationRecipientAddress, NtfSubscriptionControl_scope}

SubscriptionControlSubtree = Class(name="SubscriptionControlSubtree", synonyms=["Contains notification subscription related classes. Should be used in all classes (or classes inheriting from) - SubNetwork - ManagedElement If some YAM wants to augment these classes/list/groupings they must augment all user classes!"])

# SubscriptionControlSubtree class attributes and methods
SubscriptionControlSubtree_NtfSubscriptionControl: Property = Property(name="NtfSubscriptionControl", type=top3gpp_model.get_type_by_name('Top_Grp'), multiplicity=Multiplicity(0, "*"), synonyms=["A NtfSubscriptionControl instance represents the notification subscription of a particular notification recipient. The scope attribute is used to select managed object instances. The base object instance of the scope is the object instance name-containing the NtfSubscriptionControl instance. The notifications related to the selected managed object instances are candidates to be sent to the address specified by the notificationRecipientAddress attribute. The notificationType attribute and notificationFilter attribute allow MnS consumers to exercise control over which candidate notifications are sent to the notificationRecipientAddress. If the notificationType attribute is supported and present, its value identifies the types of notifications that are candidate to be sent to the notificationRecipientAddress. If the notificationType attribute is not supported or not present, all types of notifications are candidate to be sent to notificationRecipientAddress. If supported, the notificationFilter attribute defines a filter that is applied to the set of candidate notifications. Only candidate notifications that pass the filter criteria are sent to the notificationRecipientAddress. If the notificationFilter attribute is not supported all candidate notificatios are sent to the notificationRecipientAddress. To receive notifications, a MnS consumer has to create NtfSubscriptionControl object instancess on the MnS producer. A MnS consumer can create a subscription for another MnS consumer since it is not required the notificationRecipientAddress be his own address. When a MnS consumer does not wish to receive notifications any more the MnS consumer shall delete the corresponding NtfSubscriptionControl instance. Creation and deletion of NtfSubscriptionControl instances by MnS consumers is optional; when not supported, the NtfSubscriptionControl instances may be created and deleted by the system or be pre-installed."])
SubscriptionControlSubtree.attributes={SubscriptionControlSubtree_NtfSubscriptionControl}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-common-subscription-control",
    types={HeartbeatControl, NtfSubscriptionControl, SubscriptionControlSubtree},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines IOCs for subscription and heartbeat control."]
