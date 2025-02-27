# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models._3gpp_5gc_nrm_configurable5qiset import domain_model as Conf5QIs3gpp_model
from buml_generated_models._3gpp_common_top import domain_model as top3gpp_model

# Classes
Dynamic5QISet = Class(name="Dynamic5QISet", synonyms=["Represents the Dynamic5QISet IOC."])

# Dynamic5QISet class attributes and methods
Dynamic5QISet_dynamic5QIs: Property = Property(name="dynamic5QIs", type=Conf5QIs3gpp_model.get_type_by_name('FiveQICharacteristics'), multiplicity=Multiplicity(0, "*"), synonyms=["Represents the Dynamic5QISet IOC."])
Dynamic5QISet.attributes={Dynamic5QISet_dynamic5QIs}

Dynamic5QISetSubtree = Class(name="Dynamic5QISetSubtree", synonyms=["Helps augmenting Dynamic5QISet into multiple places."])

# Dynamic5QISetSubtree class attributes and methods
Dynamic5QISetSubtree_Dynamic5QISet: Property = Property(name="Dynamic5QISet", type=top3gpp_model.get_type_by_name('Top_Grp'), multiplicity=Multiplicity(0, "*"), synonyms=["Specifies the dynamic 5QIs including their QoS characteristics, see 3GPP TS 23.501."])
Dynamic5QISetSubtree.attributes={Dynamic5QISetSubtree_Dynamic5QISet}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-dynamic5qiset",
    types={Dynamic5QISet, Dynamic5QISetSubtree},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["This IOC represents the dynamic 5QIs including their QoS characteristics."]
