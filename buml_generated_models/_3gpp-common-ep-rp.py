# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models.ietf_inet_types import domain_model as inet_model
from buml_generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
EP_Common = Class(name="EP_Common")

# EP_Common class attributes and methods
EP_Common_localAddress: Property = Property(name="localAddress", type=types3gpp_model.get_type_by_name('AddressWithVlan'), multiplicity=Multiplicity(1, "*"), synonyms=["Local IP address and VLAN ID."])
EP_Common_remoteAddress: Property = Property(name="remoteAddress", type=inet_model.get_type_by_name('ip_address'), synonyms=["Remote IP address."])
EP_Common.attributes={EP_Common_localAddress, EP_Common_remoteAddress}

EP_RP = Class(name="EP_RP", synonyms=["Abstract class, represents an end point of a link used across a reference point between two network entities. For naming the subclasses of EP_RP, the following rules shall apply: -	The name of the subclassed IOC shall have the form 'EP_<rp>', where <rp> is a string that represents the name of the reference point. Thus, two valid examples of EP_RP subclassed IOC names would be: EP_S1 and EP_X2."])

# EP_RP class attributes and methods
EP_RP_farEndEntity: Property = Property(name="farEndEntity", type=types3gpp_model.get_type_by_name('DistinguishedName'))
EP_RP_userLabel: Property = Property(name="userLabel", type=StringType, synonyms=["A user-friendly (and user assignable) name of this object."])
EP_RP.attributes={EP_RP_farEndEntity, EP_RP_userLabel}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-common-ep-rp",
    types={EP_Common, EP_RP},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Common/basic class/grouping to be inherited/reused. This IOC represents an end point of a link used across a reference point between two network entities."]
