# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
GNBDUFunction = Class(name="GNBDUFunction", synonyms=["Represents the logical function DU of gNB or en-gNB."])

# GNBDUFunction class attributes and methods
GNBDUFunction_aggressorSetID: Property = Property(name="aggressorSetID", type=IntegerType, synonyms=["Indicates the associated aggressor gNB Set ID of the cell Valid when Remote Interference Management function is supported."])
GNBDUFunction_gNBDUId: Property = Property(name="gNBDUId", type=IntegerType, synonyms=["Uniquely identifies the DU at least within a gNB."])
GNBDUFunction_gNBDUName: Property = Property(name="gNBDUName", type=StringType, synonyms=["Identifies the Distributed Unit of an NR node"])
GNBDUFunction_gNBId: Property = Property(name="gNBId", type=IntegerType, synonyms=["Identifies a gNB within a PLMN. The gNB Identifier (gNB ID) is part of the NR Cell Identifier (NCI) of the gNB cells."])
GNBDUFunction_gNBIdLength: Property = Property(name="gNBIdLength", type=IntegerType, synonyms=["Indicates the number of bits for encoding the gNB ID."])
GNBDUFunction_victimSetID: Property = Property(name="victimSetID", type=IntegerType, synonyms=["Indicates the associated victim gNB Set ID of the cell Valid when Remote Interference Management function is supported."])
GNBDUFunction.attributes={GNBDUFunction_aggressorSetID, GNBDUFunction_gNBDUId, GNBDUFunction_gNBDUName, GNBDUFunction_gNBId, GNBDUFunction_gNBIdLength, GNBDUFunction_victimSetID}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-gnbdufunction",
    types={GNBDUFunction},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the GNBDUFunction Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
