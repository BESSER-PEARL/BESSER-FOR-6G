# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Enumerations
ActionAllowed = Enumeration(name="ActionAllowed")
ActionAllowed_NO = EnumerationLiteral(name="NO", owner=ActionAllowed)
ActionAllowed_YES = EnumerationLiteral(name="YES", owner=ActionAllowed)
ActionAllowed.literals = {ActionAllowed_NO, ActionAllowed_YES}

EnergySavingCoverage = Enumeration(name="EnergySavingCoverage")
EnergySavingCoverage_NO = EnumerationLiteral(name="NO", owner=EnergySavingCoverage)
EnergySavingCoverage_PARTIAL = EnumerationLiteral(name="PARTIAL", owner=EnergySavingCoverage)
EnergySavingCoverage_YES = EnumerationLiteral(name="YES", owner=EnergySavingCoverage)
EnergySavingCoverage.literals = {EnergySavingCoverage_NO, EnergySavingCoverage_PARTIAL, EnergySavingCoverage_YES}

# Classes
EUtranCellRelation = Class(name="EUtranCellRelation", synonyms=["Represents the EUtranCellRelation IOC."])

# EUtranCellRelation class attributes and methods
EUtranCellRelation_EUtranCellRelation: Property = Property(name="EUtranCellRelation", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["Represents a relation between an NR cell and an E-UTRAN cell."])
EUtranCellRelation_adjacentCell: Property = Property(name="adjacentCell", type=DataType('DistinguishedName'), synonyms=["Reference to an EUtranCellFDD/TDD or ExternalEUtranCellFDD/TDD instance."])
EUtranCellRelation_cellIndividualOffset: Property = Property(name="cellIndividualOffset", type=DataType('QOffsetRange'), synonyms=["Offset applicable to a neighbouring cell. It is used for evaluating the neighbouring cell for handover in connected mode. Used by the HandOver parameter Optimization (HOO) function or Load Balancing Optimization (LBO) function."])
EUtranCellRelation_isENDCAllowed: Property = Property(name="isENDCAllowed", type=StringType, synonyms=["Indicates if EN-DC is allowed or prohibited. If TRUE, the target cell is allowed to be used for EN-DC. The target cell is referenced by the NRCellRelation that contains this isENDCAllowed. If FALSE, EN-DC shall not be allowed."])
EUtranCellRelation_isESCoveredBy: Property = Property(name="isESCoveredBy", type=StringType, synonyms=["Indicates whether the adjacent cell according to this planning provides no, partial or full coverage for the parent cell instance. Adjacent cells with this attribute equal to YES are recommended to be considered as candidate cells to take over the coverage when the original cell is about to be transferred to energy saving state. The entirety of adjacent cells with this property equal to PARTIAL are recommended to be considered as entirety of candidate cells to take over the coverage when the original cell is about to be transferred to energy saving state."])
EUtranCellRelation_isHOAllowed: Property = Property(name="isHOAllowed", type=StringType, synonyms=["Indicates if handover is allowed or prohibited. If YES, handover is allowed from source cell to target cell. Source cell is represented by the parent cell instance. Target cell is the adjacent cell referenced by this EUtranCellRelation instance. If NO, handover shall not be allowed."])
EUtranCellRelation_isICICInformationSendAllowed: Property = Property(name="isICICInformationSendAllowed", type=StringType, synonyms=["Indicates if ICIC (Inter Cell Interference Coordination) load information message sending is allowed or prohibited. If YES, ICIC load information message sending is allowed from source cell to target cell. Source cell is represented by the parent cell instance. Target cell is the adjacent cell referenced by this EUtranCellRelation instance. If NO, ICIC load information message sending shall not be allowed."])
EUtranCellRelation_isLBAllowed: Property = Property(name="isLBAllowed", type=StringType, synonyms=["Indicates if load balancing is allowed or prohibited from source cell to target cell. If YES, load balancing is allowed from source cell to target cell. Source cell is represented by the parent cell instance. Target cell is the adjacent cell referenced by this EUtranCellRelation instance. If NO, load balancing shall be prohibited from source cell to target cell."])
EUtranCellRelation_isRemoveAllowed: Property = Property(name="isRemoveAllowed", type=StringType, synonyms=["Indicates if the subject EUtranCellRelation can be removed (deleted) or not. If YES, the subject EUtranCellRelation instance can be removed (deleted). If NO, the subject EUtranCellRelation instance shall not be removed (deleted) by any entity but an IRPManager."])
EUtranCellRelation_qOffset: Property = Property(name="qOffset", type=DataType('QOffsetRange'), synonyms=["Offset applicable to a specific neighbouring cell used for evaluating the cell as a candidate for cell re-selection. Corresponds to parameter q-OffsetCell broadcast in SIB4 for intra-frequency cells and in SIB5 for inter-frequency cells. Used for Mobility Robustness Optimization."])
EUtranCellRelation_tCI: Property = Property(name="tCI", type=IntegerType, synonyms=["Target Cell Identifier. Consists of E-UTRAN Cell Global Identifier (ECGI) and Physical Cell Identifier (PCI) of the target cell. Identifies the target cell from the perspective of the parent cell instance."])
EUtranCellRelation.attributes={EUtranCellRelation_EUtranCellRelation, EUtranCellRelation_adjacentCell, EUtranCellRelation_cellIndividualOffset, EUtranCellRelation_isENDCAllowed, EUtranCellRelation_isESCoveredBy, EUtranCellRelation_isHOAllowed, EUtranCellRelation_isICICInformationSendAllowed, EUtranCellRelation_isLBAllowed, EUtranCellRelation_isRemoveAllowed, EUtranCellRelation_qOffset, EUtranCellRelation_tCI}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-eutrancellrelation",
    types={ActionAllowed, EUtranCellRelation, EnergySavingCoverage},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the EUtranCellRelation Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
