# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
Dynamic5QISet = Class(name="Dynamic5QISet")

# Dynamic5QISet class attributes and methods
Dynamic5QISet_dynamic5QIs: Property = Property(name="dynamic5QIs", type=list)
Dynamic5QISet.attributes={Dynamic5QISet_dynamic5QIs}

Dynamic5QISetSubtree = Class(name="Dynamic5QISetSubtree")

# Dynamic5QISetSubtree class attributes and methods
Dynamic5QISetSubtree_Dynamic5QISet: Property = Property(name="Dynamic5QISet", type=list)
Dynamic5QISetSubtree.attributes={Dynamic5QISetSubtree_Dynamic5QISet}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-dynamic5qiset",
    types={Dynamic5QISet, Dynamic5QISetSubtree},
    associations={},
    generalizations={}
)
