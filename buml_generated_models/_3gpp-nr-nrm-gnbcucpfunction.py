# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
GNBCUCPFunction = Class(name="GNBCUCPFunction", synonyms=["Represents the logical function CU-CP of gNB and en-gNB."])

# GNBCUCPFunction class attributes and methods
GNBCUCPFunction_configurable5QISetRef: Property = Property(name="configurable5QISetRef", type=StringType, synonyms=["DN of the Configurable5QISet that the GNBCUCPFunction supports (is associated to)."])
GNBCUCPFunction_dynamic5QISetRef: Property = Property(name="dynamic5QISetRef", type=StringType, synonyms=["DN of the Dynamic5QISet that the GNBCUCPFunction supports (is associated to)."])
GNBCUCPFunction_gNBCUName: Property = Property(name="gNBCUName", type=StringType, synonyms=["Identifies the Central Unit of an gNB."])
GNBCUCPFunction_gNBId: Property = Property(name="gNBId", type=IntegerType, synonyms=["Identifies a gNB within a PLMN. The gNB Identifier (gNB ID) is part of the NR Cell Identifier (NCI) of the gNB cells."])
GNBCUCPFunction_gNBIdLength: Property = Property(name="gNBIdLength", type=IntegerType, synonyms=["Indicates the number of bits for encoding the gNB ID."])
GNBCUCPFunction_pLMNId: Property = Property(name="pLMNId", type=list, synonyms=["The PLMN identifier to be used as part of the global RAN node identity."])
GNBCUCPFunction.attributes={GNBCUCPFunction_configurable5QISetRef, GNBCUCPFunction_dynamic5QISetRef, GNBCUCPFunction_gNBCUName, GNBCUCPFunction_gNBId, GNBCUCPFunction_gNBIdLength, GNBCUCPFunction_pLMNId}

GNBCUCPFunctionGrp = Class(name="GNBCUCPFunctionGrp", synonyms=["Represents the GNBCUCPFunction IOC."])

# GNBCUCPFunctionGrp class attributes and methods
GNBCUCPFunctionGrp_configurable5QISetRef: Property = Property(name="configurable5QISetRef", type=StringType, synonyms=["DN of the Configurable5QISet that the GNBCUCPFunction supports (is associated to)."])
GNBCUCPFunctionGrp_dynamic5QISetRef: Property = Property(name="dynamic5QISetRef", type=StringType, synonyms=["DN of the Dynamic5QISet that the GNBCUCPFunction supports (is associated to)."])
GNBCUCPFunctionGrp_gNBCUName: Property = Property(name="gNBCUName", type=StringType, synonyms=["Identifies the Central Unit of an gNB."])
GNBCUCPFunctionGrp_gNBId: Property = Property(name="gNBId", type=IntegerType, synonyms=["Identifies a gNB within a PLMN. The gNB Identifier (gNB ID) is part of the NR Cell Identifier (NCI) of the gNB cells."])
GNBCUCPFunctionGrp_gNBIdLength: Property = Property(name="gNBIdLength", type=IntegerType, synonyms=["Indicates the number of bits for encoding the gNB ID."])
GNBCUCPFunctionGrp_pLMNId: Property = Property(name="pLMNId", type=list, synonyms=["The PLMN identifier to be used as part of the global RAN node identity."])
GNBCUCPFunctionGrp.attributes={GNBCUCPFunctionGrp_configurable5QISetRef, GNBCUCPFunctionGrp_dynamic5QISetRef, GNBCUCPFunctionGrp_gNBCUName, GNBCUCPFunctionGrp_gNBId, GNBCUCPFunctionGrp_gNBIdLength, GNBCUCPFunctionGrp_pLMNId}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-gnbcucpfunction",
    types={GNBCUCPFunction, GNBCUCPFunctionGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the GNBCUCPFunction Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
