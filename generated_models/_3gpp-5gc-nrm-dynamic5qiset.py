# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
Dynamic5QISet = Class(name="Dynamic5QISet")

# Dynamic5QISet class attributes and methods
Dynamic5QISet_dynamic5QIs: Property = Property(name="dynamic5QIs", type=list)
Dynamic5QISet.attributes={Dynamic5QISet_dynamic5QIs}

Dynamic5QISetSubtree = Class(name="Dynamic5QISetSubtree")

# Dynamic5QISetSubtree class attributes and methods
Dynamic5QISetSubtree_Dynamic5QISet: Property = Property(name="Dynamic5QISet", type=list)
Dynamic5QISetSubtree.attributes={Dynamic5QISetSubtree_Dynamic5QISet}

