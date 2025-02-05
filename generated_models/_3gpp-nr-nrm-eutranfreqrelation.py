# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    Constraint
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_5gc_nrm_affunction import domain_model as af3gpp_model
from generated_models._3gpp_5gc_nrm_amffunction import domain_model as amf3gpp_model
from generated_models._3gpp_5gc_nrm_ausffunction import domain_model as ausf3gpp_model
from generated_models._3gpp_5gc_nrm_configurable5qiset import domain_model as Conf5QIs3gpp_model
from generated_models._3gpp_5gc_nrm_dnfunction import domain_model as dn3gpp_model
from generated_models._3gpp_5gc_nrm_lmffunction import domain_model as lmf3gpp_model
from generated_models._3gpp_5gc_nrm_n3iwffunction import domain_model as n3iwf3gpp_model
from generated_models._3gpp_5gc_nrm_nfprofile import domain_model as nfp3gpp_model
from generated_models._3gpp_5gc_nrm_nfservice import domain_model as nfs3gpp_model
from generated_models._3gpp_5gc_nrm_ngeirfunction import domain_model as ngeir3gpp_model
from generated_models._3gpp_5gc_nrm_nrffunction import domain_model as nrf3gpp_model
from generated_models._3gpp_5gc_nrm_nssffunction import domain_model as nssf3gpp_model
from generated_models._3gpp_5gc_nrm_pcffunction import domain_model as pcf3gpp_model
from generated_models._3gpp_5gc_nrm_seppfunction import domain_model as sepp3gpp_model
from generated_models._3gpp_5gc_nrm_smffunction import domain_model as smf3gpp_model
from generated_models._3gpp_5gc_nrm_smsffunction import domain_model as smsf3gpp_model
from generated_models._3gpp_5gc_nrm_udmfunction import domain_model as udm3gpp_model
from generated_models._3gpp_5gc_nrm_upffunction import domain_model as upf3gpp_model
from generated_models._3gpp_common_ep_rp import domain_model as eprp3gpp_model
from generated_models._3gpp_common_fm import domain_model as fm3gpp_model
from generated_models._3gpp_common_managed_element import domain_model as me3gpp_model
from generated_models._3gpp_common_managed_function import domain_model as mf3gpp_model
from generated_models._3gpp_common_measurements import domain_model as meas3gpp_model
from generated_models._3gpp_common_subnetwork import domain_model as subnet3gpp_model
from generated_models._3gpp_common_subscription_control import domain_model as subscr3gpp_model
from generated_models._3gpp_common_top import domain_model as top3gpp_model
from generated_models._3gpp_common_trace import domain_model as trace3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model
from generated_models._3gpp_nr_nrm_commonbeamformingfunction import domain_model as cbeamff3gpp_model
from generated_models._3gpp_nr_nrm_gnbcucpfunction import domain_model as gnbcucp3gpp_model
from generated_models._3gpp_nr_nrm_gnbcuupfunction import domain_model as gnbcuup3gpp_model
from generated_models._3gpp_nr_nrm_gnbdufunction import domain_model as gnbdu3gpp_model
from generated_models._3gpp_nr_nrm_nrcellcu import domain_model as nrcellcu3gpp_model
from generated_models._3gpp_nr_nrm_nrcelldu import domain_model as nrcelldu3gpp_model
from generated_models._3gpp_nr_nrm_nrsectorcarrier import domain_model as nrsectcarr3gpp_model

# Enumerations
# Classes
EUtranFreqRelationGrp = Class(name="EUtranFreqRelationGrp")
EUtranFreqRelation = Class(name="EUtranFreqRelation")

# EUtranFreqRelationGrp class attributes and methods
EUtranFreqRelationGrp_cellIndividualOffset: Property = Property(name="cellIndividualOffset", type=types3gpp:QOffsetRange)
EUtranFreqRelationGrp_cellReselectionPriority: Property = Property(name="cellReselectionPriority", type=IntegerType)
EUtranFreqRelationGrp_cellReselectionSubPriority: Property = Property(name="cellReselectionSubPriority", type=IntegerType)
EUtranFreqRelationGrp_pMax: Property = Property(name="pMax", type=IntegerType)
EUtranFreqRelationGrp_qOffsetFreq: Property = Property(name="qOffsetFreq", type=IntegerType)
EUtranFreqRelationGrp_qQualMin: Property = Property(name="qQualMin", type=IntegerType)
EUtranFreqRelationGrp_qRxLevMin: Property = Property(name="qRxLevMin", type=IntegerType)
EUtranFreqRelationGrp_threshXHighP: Property = Property(name="threshXHighP", type=IntegerType)
EUtranFreqRelationGrp_threshXHighQ: Property = Property(name="threshXHighQ", type=IntegerType)
EUtranFreqRelationGrp_threshXLowP: Property = Property(name="threshXLowP", type=IntegerType)
EUtranFreqRelationGrp_threshXLowQ: Property = Property(name="threshXLowQ", type=IntegerType)
EUtranFreqRelationGrp_tReselectionEutra: Property = Property(name="tReselectionEutra", type=IntegerType)
EUtranFreqRelationGrp_tReselectionEutraSfHigh: Property = Property(name="tReselectionEutraSfHigh", type=IntegerType)
EUtranFreqRelationGrp_tReselectionEutraSfMedium: Property = Property(name="tReselectionEutraSfMedium", type=IntegerType)
EUtranFreqRelationGrp_eUtranFrequencyRef: Property = Property(name="eUtranFrequencyRef", type=types3gpp:DistinguishedName)
EUtranFreqRelationGrp.attributes={EUtranFreqRelationGrp_threshXLowP, EUtranFreqRelationGrp_threshXHighP, EUtranFreqRelationGrp_cellReselectionPriority, EUtranFreqRelationGrp_qQualMin, EUtranFreqRelationGrp_threshXHighQ, EUtranFreqRelationGrp_tReselectionEutraSfHigh, EUtranFreqRelationGrp_tReselectionEutra, EUtranFreqRelationGrp_cellReselectionSubPriority, EUtranFreqRelationGrp_tReselectionEutraSfMedium, EUtranFreqRelationGrp_qRxLevMin, EUtranFreqRelationGrp_qOffsetFreq, EUtranFreqRelationGrp_pMax, EUtranFreqRelationGrp_threshXLowQ, EUtranFreqRelationGrp_cellIndividualOffset, EUtranFreqRelationGrp_eUtranFrequencyRef}

# EUtranFreqRelation class attributes and methods
EUtranFreqRelation_cellIndividualOffset: Property = Property(name="cellIndividualOffset", type=types3gpp:QOffsetRange)
EUtranFreqRelation_cellReselectionPriority: Property = Property(name="cellReselectionPriority", type=IntegerType)
EUtranFreqRelation_cellReselectionSubPriority: Property = Property(name="cellReselectionSubPriority", type=IntegerType)
EUtranFreqRelation_pMax: Property = Property(name="pMax", type=IntegerType)
EUtranFreqRelation_qOffsetFreq: Property = Property(name="qOffsetFreq", type=IntegerType)
EUtranFreqRelation_qQualMin: Property = Property(name="qQualMin", type=IntegerType)
EUtranFreqRelation_qRxLevMin: Property = Property(name="qRxLevMin", type=IntegerType)
EUtranFreqRelation_threshXHighP: Property = Property(name="threshXHighP", type=IntegerType)
EUtranFreqRelation_threshXHighQ: Property = Property(name="threshXHighQ", type=IntegerType)
EUtranFreqRelation_threshXLowP: Property = Property(name="threshXLowP", type=IntegerType)
EUtranFreqRelation_threshXLowQ: Property = Property(name="threshXLowQ", type=IntegerType)
EUtranFreqRelation_tReselectionEutra: Property = Property(name="tReselectionEutra", type=IntegerType)
EUtranFreqRelation_tReselectionEutraSfHigh: Property = Property(name="tReselectionEutraSfHigh", type=IntegerType)
EUtranFreqRelation_tReselectionEutraSfMedium: Property = Property(name="tReselectionEutraSfMedium", type=IntegerType)
EUtranFreqRelation_eUtranFrequencyRef: Property = Property(name="eUtranFrequencyRef", type=types3gpp:DistinguishedName)
EUtranFreqRelation.attributes={EUtranFreqRelation_threshXLowP, EUtranFreqRelation_threshXHighP, EUtranFreqRelation_cellReselectionPriority, EUtranFreqRelation_qQualMin, EUtranFreqRelation_tReselectionEutraSfHigh, EUtranFreqRelation_tReselectionEutra, EUtranFreqRelation_cellReselectionSubPriority, EUtranFreqRelation_tReselectionEutraSfMedium, EUtranFreqRelation_qRxLevMin, EUtranFreqRelation_qOffsetFreq, EUtranFreqRelation_threshXHighQ, EUtranFreqRelation_pMax, EUtranFreqRelation_threshXLowQ, EUtranFreqRelation_cellIndividualOffset, EUtranFreqRelation_eUtranFrequencyRef}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-eutranfreqrelation",
    types={EUtranFreqRelationGrp, EUtranFreqRelation, types3gpp_model, mf3gpp_model, me3gpp_model, top3gpp_model, types5g3gpp_model, inet_model, subnet3gpp_model, Conf5QIs3gpp_model, eprp3gpp_model, af3gpp_model, amf3gpp_model, ausf3gpp_model, dn3gpp_model, lmf3gpp_model, n3iwf3gpp_model, ngeir3gpp_model, nrf3gpp_model, nssf3gpp_model, pcf3gpp_model, sepp3gpp_model, smf3gpp_model, smsf3gpp_model, udm3gpp_model, upf3gpp_model, yang_model, nfs3gpp_model, nfp3gpp_model, meas3gpp_model, subscr3gpp_model, fm3gpp_model, trace3gpp_model, yangmnt_model, cbeamff3gpp_model, gnbdu3gpp_model, nrsectcarr3gpp_model, nrcellcu3gpp_model, gnbcucp3gpp_model, nrcelldu3gpp_model, gnbcuup3gpp_model},
    associations={},
    generalizations={}
)
