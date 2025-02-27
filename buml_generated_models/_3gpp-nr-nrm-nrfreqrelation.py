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
NRFreqRelation = Class(name="NRFreqRelation", synonyms=["Together with the target NRFrequency, it represents the frequency properties applicable to the referencing NRFreqRelation."])

# NRFreqRelation class attributes and methods
NRFreqRelation_cellReselectionPriority: Property = Property(name="cellReselectionPriority", type=IntegerType, synonyms=["The absolute priority of the carrier frequency used by the cell reselection procedure. Value 0 means lowest priority. The value must not already used by other RAT, i.e. equal priorities between RATs are not supported. The UE behaviour when no value is entered is specified in subclause 5.2.4.1 of 3GPP TS 38.304."])
NRFreqRelation_cellReselectionSubPriority: Property = Property(name="cellReselectionSubPriority", type=IntegerType, synonyms=["Indicates a fractional value to be added to the value of cellReselectionPriority to obtain the absolute priority of the concerned carrier frequency for E-UTRA and NR."])
NRFreqRelation_nRFrequencyRef: Property = Property(name="nRFrequencyRef", type=types3gpp_model.get_type_by_name('DistinguishedName'), synonyms=["Reference to a corresponding NRFrequency instance."])
NRFreqRelation_pMax: Property = Property(name="pMax", type=IntegerType, synonyms=["Used for calculation of the parameter Pcompensation (defined in 3GPP TS 38.304), at cell reselection to a cell."])
NRFreqRelation_qOffsetFreq: Property = Property(name="qOffsetFreq", type=types3gpp_model.get_type_by_name('QOffsetRange'), synonyms=["The frequency specific offset applied when evaluating candidates for cell reselection."])
NRFreqRelation_qQualMin: Property = Property(name="qQualMin", type=IntegerType, synonyms=["Indicates the minimum required quality level in the cell. Value 0 means that it is not sent and UE applies in such case the (default) value of negative infinity for Qqualmin. Sent in SIB3 or SIB5."])
NRFreqRelation_qRxLevMin: Property = Property(name="qRxLevMin", type=IntegerType, synonyms=["Indicates the required minimum received Reference Symbol Received Power (RSRP) level in the NR frequency for cell reselection. Broadcast in SIB3 or SIB5, depending on whether the related frequency is intra- or inter-frequency. Resolution is 2."])
NRFreqRelation_tReselectionNR: Property = Property(name="tReselectionNR", type=IntegerType, synonyms=["Cell reselection timer for NR."])
NRFreqRelation_tReselectionNRSfHigh: Property = Property(name="tReselectionNRSfHigh", type=IntegerType, synonyms=["The attribute tReselectionNr (parameter TreselectionNR in 3GPP TS 38.304) is multiplied with this scaling factor if the UE is in high mobility state."])
NRFreqRelation_tReselectionNRSfMedium: Property = Property(name="tReselectionNRSfMedium", type=IntegerType, synonyms=["The attribute tReselectionNr (parameter TreselectionNR in 3GPP TS 38.304) multiplied with this scaling factor if the UE is in medium mobility state."])
NRFreqRelation_threshXHighP: Property = Property(name="threshXHighP", type=IntegerType, synonyms=["Specifies the Srxlev threshold used by the UE when reselecting towards a higher priority RAT/frequency than the current serving frequency. Each frequency of NR and E-UTRAN might have a specific threshold. Resolution is 2."])
NRFreqRelation_threshXHighQ: Property = Property(name="threshXHighQ", type=IntegerType, synonyms=["Specifies the Squal threshold used by the UE when reselecting towards a higher priority RAT/frequency than the current serving frequency. Each frequency of NR and E-UTRAN might have a specific threshold."])
NRFreqRelation_threshXLowP: Property = Property(name="threshXLowP", type=IntegerType, synonyms=["Specifies the Srxlev threshold used by the UE when reselecting towards a lower priority RAT/frequency than the current serving frequency. Each frequency of NR and E-UTRAN might have a specific threshold. Resolution is 2."])
NRFreqRelation_threshXLowQ: Property = Property(name="threshXLowQ", type=IntegerType, synonyms=["Specifies the Squal threshold used by the UE when reselecting towards a lower priority RAT/frequency than the current serving frequency. Each frequency of NR and E-UTRAN might have a specific threshold."])
NRFreqRelation.attributes={NRFreqRelation_cellReselectionPriority, NRFreqRelation_cellReselectionSubPriority, NRFreqRelation_nRFrequencyRef, NRFreqRelation_pMax, NRFreqRelation_qOffsetFreq, NRFreqRelation_qQualMin, NRFreqRelation_qRxLevMin, NRFreqRelation_tReselectionNR, NRFreqRelation_tReselectionNRSfHigh, NRFreqRelation_tReselectionNRSfMedium, NRFreqRelation_threshXHighP, NRFreqRelation_threshXHighQ, NRFreqRelation_threshXLowP, NRFreqRelation_threshXLowQ}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-nrfreqrelation",
    types={NRFreqRelation},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the NRFreqRelation Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
