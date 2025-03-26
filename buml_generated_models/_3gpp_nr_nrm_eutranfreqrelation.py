# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel, Multiplicity,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, DataType, Enumeration, EnumerationLiteral
)

# Import referenced models
from buml_generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
EUtranFreqRelation = Class(name="EUtranFreqRelation", synonyms=["Represents the EUtranFreqRelation IOC."])

# EUtranFreqRelation class attributes and methods
EUtranFreqRelation_EUtranFreqRelation: Property = Property(name="EUtranFreqRelation", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["Represents a frequency relation between an NR cell and an E-UTRAN cell."])
EUtranFreqRelation_cellIndividualOffset: Property = Property(name="cellIndividualOffset", type=DataType('QOffsetRange'), synonyms=["Offset applicable to a neighbouring cell. Used for evaluating the neighbouring cell for handover in connected mode. Used by the HandOver parameter Optimization (HOO) function or Load Balancing Optimization (LBO) function."])
EUtranFreqRelation_cellReselectionPriority: Property = Property(name="cellReselectionPriority", type=IntegerType, synonyms=["The absolute priority of the carrier frequency used by the cell reselection procedure. Value 0 means lowest priority. The value must not already used by other RAT, i.e. equal priorities between RATs are not supported. The UE behaviour when no value is entered is specified in subclause 5.2.4.1 of 3GPP TS 38.304."])
EUtranFreqRelation_cellReselectionSubPriority: Property = Property(name="cellReselectionSubPriority", type=IntegerType, synonyms=["Indicates a fractional value to be added to the value of cellReselectionPriority to obtain the absolute priority of the concerned carrier frequency for E-UTRA and NR."])
EUtranFreqRelation_eUtranFrequencyRef: Property = Property(name="eUtranFrequencyRef", type=DataType('DistinguishedName'), synonyms=["Reference to a corresponding EUtranFrequency instance."])
EUtranFreqRelation_pMax: Property = Property(name="pMax", type=IntegerType, synonyms=["Used for calculation of the parameter Pcompensation (defined in 3GPP TS 38.304), at cell reselection to a cell."])
EUtranFreqRelation_qOffsetFreq: Property = Property(name="qOffsetFreq", type=IntegerType, synonyms=["The frequency specific offset applied when evaluating candidates for cell reselection."])
EUtranFreqRelation_qQualMin: Property = Property(name="qQualMin", type=IntegerType, synonyms=["Indicates the minimum required quality level in the cell. Value 0 means that it is not sent and UE applies in such case the (default) value of negative infinity for Qqualmin. Sent in SIB3 or SIB5."])
EUtranFreqRelation_qRxLevMin: Property = Property(name="qRxLevMin", type=IntegerType, synonyms=["Indicates the required minimum received Reference Symbol Received Power (RSRP) level in the (E-UTRA) frequency for cell reselection. Broadcast in SIB3 or SIB5, depending on whether the related frequency is intra- or inter-frequency. Resolution is 2."])
EUtranFreqRelation_tReselectionEutra: Property = Property(name="tReselectionEutra", type=IntegerType, synonyms=["Cell reselection timer for intra frequency E-UTRA cell reselection. May be used for Mobility Robustness Optimization."])
EUtranFreqRelation_tReselectionEutraSfHigh: Property = Property(name="tReselectionEutraSfHigh", type=IntegerType, synonyms=["The attribute tReselectionEutra (parameter TreselectionEUTRA in 3GPP TS 38.304) multiplied with this scaling factor if the UE is in high mobility state."])
EUtranFreqRelation_tReselectionEutraSfMedium: Property = Property(name="tReselectionEutraSfMedium", type=IntegerType, synonyms=["The attribute tReselectionEutra (parameter TreselectionEUTRA in 3GPP TS 38.304) multiplied with this scaling factor if the UE is in medium mobility state."])
EUtranFreqRelation_threshXHighP: Property = Property(name="threshXHighP", type=IntegerType, synonyms=["Specifies the Srxlev threshold used by the UE when reselecting towards a higher priority RAT/frequency than the current serving frequency. Each frequency of NR and E-UTRAN might have a specific threshold. Resolution is 2."])
EUtranFreqRelation_threshXHighQ: Property = Property(name="threshXHighQ", type=IntegerType, synonyms=["Specifies the Squal threshold used by the UE when reselecting towards a higher priority RAT/frequency than the current serving frequency. Each frequency of NR and E-UTRAN might have a specific threshold."])
EUtranFreqRelation_threshXLowP: Property = Property(name="threshXLowP", type=IntegerType, synonyms=["Specifies the Srxlev threshold used by the UE when reselecting towards a lower priority RAT/frequency than the current serving frequency. Each frequency of NR and E-UTRAN might have a specific threshold. Resolution is 2."])
EUtranFreqRelation_threshXLowQ: Property = Property(name="threshXLowQ", type=IntegerType, synonyms=["Specifies the Squal threshold used by the UE when reselecting towards a lower priority RAT/frequency than the current serving frequency. Each frequency of NR and E-UTRAN might have a specific threshold."])
EUtranFreqRelation.attributes={EUtranFreqRelation_EUtranFreqRelation, EUtranFreqRelation_cellIndividualOffset, EUtranFreqRelation_cellReselectionPriority, EUtranFreqRelation_cellReselectionSubPriority, EUtranFreqRelation_eUtranFrequencyRef, EUtranFreqRelation_pMax, EUtranFreqRelation_qOffsetFreq, EUtranFreqRelation_qQualMin, EUtranFreqRelation_qRxLevMin, EUtranFreqRelation_tReselectionEutra, EUtranFreqRelation_tReselectionEutraSfHigh, EUtranFreqRelation_tReselectionEutraSfMedium, EUtranFreqRelation_threshXHighP, EUtranFreqRelation_threshXHighQ, EUtranFreqRelation_threshXLowP, EUtranFreqRelation_threshXLowQ}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-eutranfreqrelation",
    types={EUtranFreqRelation},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the EUtranFreqRelation Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
