# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
GNBCUCPFunction = Class(name="GNBCUCPFunction", synonyms=["Represents the logical function CU-CP of gNB and en-gNB."])

# GNBCUCPFunction class attributes and methods
GNBCUCPFunction_configurable5QISetRef: Property = Property(name="configurable5QISetRef", type=types3gpp_model.get_type_by_name('DistinguishedName'), synonyms=["DN of the Configurable5QISet that the GNBCUCPFunction supports (is associated to)."])
GNBCUCPFunction_dynamic5QISetRef: Property = Property(name="dynamic5QISetRef", type=types3gpp_model.get_type_by_name('DistinguishedName'), synonyms=["DN of the Dynamic5QISet that the GNBCUCPFunction supports (is associated to)."])
GNBCUCPFunction_gNBCUName: Property = Property(name="gNBCUName", type=StringType, synonyms=["Identifies the Central Unit of an gNB."])
GNBCUCPFunction_gNBId: Property = Property(name="gNBId", type=IntegerType, synonyms=["Identifies a gNB within a PLMN. The gNB Identifier (gNB ID) is part of the NR Cell Identifier (NCI) of the gNB cells."])
GNBCUCPFunction_gNBIdLength: Property = Property(name="gNBIdLength", type=IntegerType, synonyms=["Indicates the number of bits for encoding the gNB ID."])
GNBCUCPFunction_pLMNId: Property = Property(name="pLMNId", type=types3gpp_model.get_type_by_name('PLMNId'), multiplicity=Multiplicity(1, "*"), synonyms=["The PLMN identifier to be used as part of the global RAN node identity."])
GNBCUCPFunction.attributes={GNBCUCPFunction_configurable5QISetRef, GNBCUCPFunction_dynamic5QISetRef, GNBCUCPFunction_gNBCUName, GNBCUCPFunction_gNBId, GNBCUCPFunction_gNBIdLength, GNBCUCPFunction_pLMNId}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-gnbcucpfunction",
    types={GNBCUCPFunction},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the GNBCUCPFunction Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
