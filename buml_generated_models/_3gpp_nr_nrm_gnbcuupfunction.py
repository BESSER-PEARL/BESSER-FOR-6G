# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models._3gpp_common_yang_types import domain_model as types3gpp_model
from buml_generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model

# Classes
BackhaulAddress = Class(name="BackhaulAddress", synonyms=["Indicates the backhauladdress of gNB."])

# BackhaulAddress class attributes and methods
BackhaulAddress_gNBId: Property = Property(name="gNBId", type=IntegerType, synonyms=["It identifies a gNB within a PLMN. The gNB ID is part of the NR Cell Identifier (NCI) of the gNB cells."])
BackhaulAddress_tAI: Property = Property(name="tAI", type=list, multiplicity=Multiplicity(1, "*"), synonyms=["Tracking Area Identity"])
BackhaulAddress.attributes={BackhaulAddress_gNBId, BackhaulAddress_tAI}

GNBCUUPFunction = Class(name="GNBCUUPFunction", synonyms=["Represents the logical function CU-UP of gNB or en-gNB."])

# GNBCUUPFunction class attributes and methods
GNBCUUPFunction_configurable5QISetRef: Property = Property(name="configurable5QISetRef", type=types3gpp_model.get_type_by_name('DistinguishedName'), synonyms=["DN of the Configurable5QISet that the GNBCUUPFunction supports (is associated to)."])
GNBCUUPFunction_dynamic5QISetRef: Property = Property(name="dynamic5QISetRef", type=types3gpp_model.get_type_by_name('DistinguishedName'), synonyms=["DN of the Dynamic5QISet that the GNBCUUPFunction supports (is associated to)."])
GNBCUUPFunction_gNBCUUPId: Property = Property(name="gNBCUUPId", type=IntegerType, synonyms=["Identifies the gNB-CU-UP at least within a gNB-CU-CP"])
GNBCUUPFunction_gNBId: Property = Property(name="gNBId", type=IntegerType, synonyms=["Identifies a gNB within a PLMN. The gNB ID is part of the NR Cell Identifier (NCI) of the gNB cells."])
GNBCUUPFunction_gNBIdLength: Property = Property(name="gNBIdLength", type=IntegerType, synonyms=["Indicates the number of bits for encoding the gNB Id."])
GNBCUUPFunction_mappingSetIDBackhaulAddressList: Property = Property(name="mappingSetIDBackhaulAddressList", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["Specifies a list of mappingSetIDBackhaulAddress used to retrieve the backhaul address of the victim set. Must be present if Remote Interference Management function is supported."])
GNBCUUPFunction_pLMNInfoList: Property = Property(name="pLMNInfoList", type=types5g3gpp_model.get_type_by_name('PLMNInfo'), multiplicity=Multiplicity(0, "*"), synonyms=["The PLMNInfoList is a list of PLMNInfo data type. It defines which PLMNs that can be served by the GNBCUUPFunction and which S-NSSAIs can be supported by the GNBCUUPFunction for corresponding PLMN in case of network slicing feature is supported"])
GNBCUUPFunction.attributes={GNBCUUPFunction_configurable5QISetRef, GNBCUUPFunction_dynamic5QISetRef, GNBCUUPFunction_gNBCUUPId, GNBCUUPFunction_gNBId, GNBCUUPFunction_gNBIdLength, GNBCUUPFunction_mappingSetIDBackhaulAddressList, GNBCUUPFunction_pLMNInfoList}

MappingSetIDBackhaulAddress = Class(name="MappingSetIDBackhaulAddress", synonyms=["Mapping relationship between setID and backhaulAddress of gNB"])

# MappingSetIDBackhaulAddress class attributes and methods
MappingSetIDBackhaulAddress_backhaulAddress: Property = Property(name="backhaulAddress", type=list, multiplicity=Multiplicity(1, "*"), synonyms=["Indicates the backhauladdress of gNB."])
MappingSetIDBackhaulAddress_idx: Property = Property(name="idx", type=IntegerType, synonyms=["ID value"])
MappingSetIDBackhaulAddress_setID: Property = Property(name="setID", type=IntegerType, synonyms=["Indicates the setID of gNB."])
MappingSetIDBackhaulAddress.attributes={MappingSetIDBackhaulAddress_backhaulAddress, MappingSetIDBackhaulAddress_idx, MappingSetIDBackhaulAddress_setID}

TAI = Class(name="TAI", synonyms=["Tracking Area Identity"])

# TAI class attributes and methods
TAI_nRTAC: Property = Property(name="nRTAC", type=IntegerType, synonyms=["Identity of the common Tracking Area Code for the PLMNs allowedValues: a) It is the TAC or Extended-TAC. b) A cell can only broadcast one TAC or Extended-TAC. See TS 36.300, subclause 10.1.7 (PLMNID and TAC relation). c) TAC is defined in subclause 19.4.2.3 of 3GPP TS 23.003 and Extended-TAC is defined in subclause 9.3.1.29 of 3GPP TS 38.473. d) For a 5G SA (Stand Alone), it has a non-null value."])
TAI_pLMNId: Property = Property(name="pLMNId", type=types3gpp_model.get_type_by_name('PLMNId'), multiplicity=Multiplicity(0, "*"), synonyms=["PLMN IDs for the Tracking area"])
TAI.attributes={TAI_nRTAC, TAI_pLMNId}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-gnbcuupfunction",
    types={BackhaulAddress, GNBCUUPFunction, MappingSetIDBackhaulAddress, TAI},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the GNBCUUPFunction Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
