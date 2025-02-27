# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
BackhaulAddressGrp = Class(name="BackhaulAddressGrp", synonyms=["Indicates the backhauladdress of gNB."])

# BackhaulAddressGrp class attributes and methods
BackhaulAddressGrp_gNBId: Property = Property(name="gNBId", type=IntegerType, synonyms=["It identifies a gNB within a PLMN. The gNB ID is part of the NR Cell Identifier (NCI) of the gNB cells."])
BackhaulAddressGrp_tAI: Property = Property(name="tAI", type=list, synonyms=["Tracking Area Identity"])
BackhaulAddressGrp.attributes={BackhaulAddressGrp_gNBId, BackhaulAddressGrp_tAI}

GNBCUUPFunction = Class(name="GNBCUUPFunction", synonyms=["Represents the logical function CU-UP of gNB or en-gNB."])

# GNBCUUPFunction class attributes and methods
GNBCUUPFunction_configurable5QISetRef: Property = Property(name="configurable5QISetRef", type=StringType, synonyms=["DN of the Configurable5QISet that the GNBCUUPFunction supports (is associated to)."])
GNBCUUPFunction_dynamic5QISetRef: Property = Property(name="dynamic5QISetRef", type=StringType, synonyms=["DN of the Dynamic5QISet that the GNBCUUPFunction supports (is associated to)."])
GNBCUUPFunction_gNBCUUPId: Property = Property(name="gNBCUUPId", type=IntegerType, synonyms=["Identifies the gNB-CU-UP at least within a gNB-CU-CP"])
GNBCUUPFunction_gNBId: Property = Property(name="gNBId", type=IntegerType, synonyms=["Identifies a gNB within a PLMN. The gNB ID is part of the NR Cell Identifier (NCI) of the gNB cells."])
GNBCUUPFunction_gNBIdLength: Property = Property(name="gNBIdLength", type=IntegerType, synonyms=["Indicates the number of bits for encoding the gNB Id."])
GNBCUUPFunction_mappingSetIDBackhaulAddressList: Property = Property(name="mappingSetIDBackhaulAddressList", type=list, synonyms=["Specifies a list of mappingSetIDBackhaulAddress used to retrieve the backhaul address of the victim set. Must be present if Remote Interference Management function is supported."])
GNBCUUPFunction_pLMNInfoList: Property = Property(name="pLMNInfoList", type=list, synonyms=["The PLMNInfoList is a list of PLMNInfo data type. It defines which PLMNs that can be served by the GNBCUUPFunction and which S-NSSAIs can be supported by the GNBCUUPFunction for corresponding PLMN in case of network slicing feature is supported"])
GNBCUUPFunction.attributes={GNBCUUPFunction_configurable5QISetRef, GNBCUUPFunction_dynamic5QISetRef, GNBCUUPFunction_gNBCUUPId, GNBCUUPFunction_gNBId, GNBCUUPFunction_gNBIdLength, GNBCUUPFunction_mappingSetIDBackhaulAddressList, GNBCUUPFunction_pLMNInfoList}

GNBCUUPFunctionGrp = Class(name="GNBCUUPFunctionGrp", synonyms=["Represents the GNBCUUPFunction IOC."])

# GNBCUUPFunctionGrp class attributes and methods
GNBCUUPFunctionGrp_configurable5QISetRef: Property = Property(name="configurable5QISetRef", type=StringType, synonyms=["DN of the Configurable5QISet that the GNBCUUPFunction supports (is associated to)."])
GNBCUUPFunctionGrp_dynamic5QISetRef: Property = Property(name="dynamic5QISetRef", type=StringType, synonyms=["DN of the Dynamic5QISet that the GNBCUUPFunction supports (is associated to)."])
GNBCUUPFunctionGrp_gNBCUUPId: Property = Property(name="gNBCUUPId", type=IntegerType, synonyms=["Identifies the gNB-CU-UP at least within a gNB-CU-CP"])
GNBCUUPFunctionGrp_gNBId: Property = Property(name="gNBId", type=IntegerType, synonyms=["Identifies a gNB within a PLMN. The gNB ID is part of the NR Cell Identifier (NCI) of the gNB cells."])
GNBCUUPFunctionGrp_gNBIdLength: Property = Property(name="gNBIdLength", type=IntegerType, synonyms=["Indicates the number of bits for encoding the gNB Id."])
GNBCUUPFunctionGrp_mappingSetIDBackhaulAddressList: Property = Property(name="mappingSetIDBackhaulAddressList", type=list, synonyms=["Specifies a list of mappingSetIDBackhaulAddress used to retrieve the backhaul address of the victim set. Must be present if Remote Interference Management function is supported."])
GNBCUUPFunctionGrp_pLMNInfoList: Property = Property(name="pLMNInfoList", type=list, synonyms=["The PLMNInfoList is a list of PLMNInfo data type. It defines which PLMNs that can be served by the GNBCUUPFunction and which S-NSSAIs can be supported by the GNBCUUPFunction for corresponding PLMN in case of network slicing feature is supported"])
GNBCUUPFunctionGrp.attributes={GNBCUUPFunctionGrp_configurable5QISetRef, GNBCUUPFunctionGrp_dynamic5QISetRef, GNBCUUPFunctionGrp_gNBCUUPId, GNBCUUPFunctionGrp_gNBId, GNBCUUPFunctionGrp_gNBIdLength, GNBCUUPFunctionGrp_mappingSetIDBackhaulAddressList, GNBCUUPFunctionGrp_pLMNInfoList}

MappingSetIDBackhaulAddressGrp = Class(name="MappingSetIDBackhaulAddressGrp", synonyms=["Mapping relationship between setID and backhaulAddress of gNB"])

# MappingSetIDBackhaulAddressGrp class attributes and methods
MappingSetIDBackhaulAddressGrp_backhaulAddress: Property = Property(name="backhaulAddress", type=list, synonyms=["Indicates the backhauladdress of gNB."])
MappingSetIDBackhaulAddressGrp_idx: Property = Property(name="idx", type=IntegerType, synonyms=["ID value"])
MappingSetIDBackhaulAddressGrp_setID: Property = Property(name="setID", type=IntegerType, synonyms=["Indicates the setID of gNB."])
MappingSetIDBackhaulAddressGrp.attributes={MappingSetIDBackhaulAddressGrp_backhaulAddress, MappingSetIDBackhaulAddressGrp_idx, MappingSetIDBackhaulAddressGrp_setID}

TAIGrp = Class(name="TAIGrp", synonyms=["Tracking Area Identity"])

# TAIGrp class attributes and methods
TAIGrp_nRTAC: Property = Property(name="nRTAC", type=IntegerType, synonyms=["Identity of the common Tracking Area Code for the PLMNs allowedValues: a) It is the TAC or Extended-TAC. b) A cell can only broadcast one TAC or Extended-TAC. See TS 36.300, subclause 10.1.7 (PLMNID and TAC relation). c) TAC is defined in subclause 19.4.2.3 of 3GPP TS 23.003 and Extended-TAC is defined in subclause 9.3.1.29 of 3GPP TS 38.473. d) For a 5G SA (Stand Alone), it has a non-null value."])
TAIGrp_pLMNId: Property = Property(name="pLMNId", type=list, synonyms=["PLMN IDs for the Tracking area"])
TAIGrp.attributes={TAIGrp_nRTAC, TAIGrp_pLMNId}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-gnbcuupfunction",
    types={BackhaulAddressGrp, GNBCUUPFunction, GNBCUUPFunctionGrp, MappingSetIDBackhaulAddressGrp, TAIGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the GNBCUUPFunction Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
