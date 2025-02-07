# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
NRFreqRelation = Class(name="NRFreqRelation")

# NRFreqRelation class attributes and methods
NRFreqRelation_cellReselectionPriority: Property = Property(name="cellReselectionPriority", type=IntegerType)
NRFreqRelation_cellReselectionSubPriority: Property = Property(name="cellReselectionSubPriority", type=IntegerType)
NRFreqRelation_pMax: Property = Property(name="pMax", type=IntegerType)
NRFreqRelation_qOffsetFreq: Property = Property(name="qOffsetFreq", type=types3gpp:QOffsetRange)
NRFreqRelation_qQualMin: Property = Property(name="qQualMin", type=IntegerType)
NRFreqRelation_qRxLevMin: Property = Property(name="qRxLevMin", type=IntegerType)
NRFreqRelation_threshXHighP: Property = Property(name="threshXHighP", type=IntegerType)
NRFreqRelation_threshXHighQ: Property = Property(name="threshXHighQ", type=IntegerType)
NRFreqRelation_threshXLowP: Property = Property(name="threshXLowP", type=IntegerType)
NRFreqRelation_threshXLowQ: Property = Property(name="threshXLowQ", type=IntegerType)
NRFreqRelation_tReselectionNR: Property = Property(name="tReselectionNR", type=IntegerType)
NRFreqRelation_tReselectionNRSfHigh: Property = Property(name="tReselectionNRSfHigh", type=IntegerType)
NRFreqRelation_tReselectionNRSfMedium: Property = Property(name="tReselectionNRSfMedium", type=IntegerType)
NRFreqRelation_nRFrequencyRef: Property = Property(name="nRFrequencyRef", type=types3gpp:DistinguishedName)
NRFreqRelation.attributes={NRFreqRelation_cellReselectionPriority, NRFreqRelation_cellReselectionSubPriority, NRFreqRelation_pMax, NRFreqRelation_qOffsetFreq, NRFreqRelation_qQualMin, NRFreqRelation_qRxLevMin, NRFreqRelation_threshXHighP, NRFreqRelation_threshXHighQ, NRFreqRelation_threshXLowP, NRFreqRelation_threshXLowQ, NRFreqRelation_tReselectionNR, NRFreqRelation_tReselectionNRSfHigh, NRFreqRelation_tReselectionNRSfMedium, NRFreqRelation_nRFrequencyRef}

