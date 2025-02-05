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
from generated_models._3gpp_nr_nrm_eutranetwork import domain_model as eutranet3gpp_model
from generated_models._3gpp_nr_nrm_externalenbfunction import domain_model as extenb3gpp_model
from generated_models._3gpp_nr_nrm_externalgnbcucpfunction import domain_model as extgnbcucp3gpp_model
from generated_models._3gpp_nr_nrm_gnbcucpfunction import domain_model as gnbcucp3gpp_model
from generated_models._3gpp_nr_nrm_gnbcuupfunction import domain_model as gnbcuup3gpp_model
from generated_models._3gpp_nr_nrm_gnbdufunction import domain_model as gnbdu3gpp_model
from generated_models._3gpp_nr_nrm_nrcellcu import domain_model as nrcellcu3gpp_model
from generated_models._3gpp_nr_nrm_nrcelldu import domain_model as nrcelldu3gpp_model
from generated_models._3gpp_nr_nrm_nrnetwork import domain_model as nrnet3gpp_model
from generated_models._3gpp_nr_nrm_nrsectorcarrier import domain_model as nrsectcarr3gpp_model
from generated_models._3gpp_nr_nrm_rrmpolicy import domain_model as nrrrmpolicy3gpp_model

# Enumerations
# Classes
NRFreqRelationGrp = Class(name="NRFreqRelationGrp")
NRFreqRelation = Class(name="NRFreqRelation")

# NRFreqRelationGrp class attributes and methods
NRFreqRelationGrp_cellReselectionPriority: Property = Property(name="cellReselectionPriority", type=IntegerType)
NRFreqRelationGrp_cellReselectionSubPriority: Property = Property(name="cellReselectionSubPriority", type=IntegerType)
NRFreqRelationGrp_pMax: Property = Property(name="pMax", type=IntegerType)
NRFreqRelationGrp_qOffsetFreq: Property = Property(name="qOffsetFreq", type=types3gpp:QOffsetRange)
NRFreqRelationGrp_qQualMin: Property = Property(name="qQualMin", type=IntegerType)
NRFreqRelationGrp_qRxLevMin: Property = Property(name="qRxLevMin", type=IntegerType)
NRFreqRelationGrp_threshXHighP: Property = Property(name="threshXHighP", type=IntegerType)
NRFreqRelationGrp_threshXHighQ: Property = Property(name="threshXHighQ", type=IntegerType)
NRFreqRelationGrp_threshXLowP: Property = Property(name="threshXLowP", type=IntegerType)
NRFreqRelationGrp_threshXLowQ: Property = Property(name="threshXLowQ", type=IntegerType)
NRFreqRelationGrp_tReselectionNR: Property = Property(name="tReselectionNR", type=IntegerType)
NRFreqRelationGrp_tReselectionNRSfHigh: Property = Property(name="tReselectionNRSfHigh", type=IntegerType)
NRFreqRelationGrp_tReselectionNRSfMedium: Property = Property(name="tReselectionNRSfMedium", type=IntegerType)
NRFreqRelationGrp_nRFrequencyRef: Property = Property(name="nRFrequencyRef", type=types3gpp:DistinguishedName)
NRFreqRelationGrp.attributes={NRFreqRelationGrp_tReselectionNR, NRFreqRelationGrp_threshXHighQ, NRFreqRelationGrp_cellReselectionSubPriority, NRFreqRelationGrp_tReselectionNRSfHigh, NRFreqRelationGrp_threshXLowQ, NRFreqRelationGrp_tReselectionNRSfMedium, NRFreqRelationGrp_cellReselectionPriority, NRFreqRelationGrp_threshXLowP, NRFreqRelationGrp_qQualMin, NRFreqRelationGrp_pMax, NRFreqRelationGrp_qRxLevMin, NRFreqRelationGrp_threshXHighP, NRFreqRelationGrp_nRFrequencyRef, NRFreqRelationGrp_qOffsetFreq}

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
NRFreqRelation.attributes={NRFreqRelation_tReselectionNR, NRFreqRelation_threshXHighQ, NRFreqRelation_cellReselectionSubPriority, NRFreqRelation_tReselectionNRSfHigh, NRFreqRelation_tReselectionNRSfMedium, NRFreqRelation_threshXHighP, NRFreqRelation_cellReselectionPriority, NRFreqRelation_threshXLowP, NRFreqRelation_qQualMin, NRFreqRelation_pMax, NRFreqRelation_qRxLevMin, NRFreqRelation_threshXLowQ, NRFreqRelation_nRFrequencyRef, NRFreqRelation_qOffsetFreq}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-nrfreqrelation",
    types={NRFreqRelationGrp, NRFreqRelation, types3gpp_model, mf3gpp_model, me3gpp_model, top3gpp_model, types5g3gpp_model, inet_model, subnet3gpp_model, Conf5QIs3gpp_model, eprp3gpp_model, af3gpp_model, amf3gpp_model, ausf3gpp_model, dn3gpp_model, lmf3gpp_model, n3iwf3gpp_model, ngeir3gpp_model, nrf3gpp_model, nssf3gpp_model, pcf3gpp_model, sepp3gpp_model, smf3gpp_model, smsf3gpp_model, udm3gpp_model, upf3gpp_model, yang_model, nfs3gpp_model, nfp3gpp_model, meas3gpp_model, subscr3gpp_model, fm3gpp_model, trace3gpp_model, yangmnt_model, cbeamff3gpp_model, gnbdu3gpp_model, nrsectcarr3gpp_model, nrcellcu3gpp_model, gnbcucp3gpp_model, nrcelldu3gpp_model, gnbcuup3gpp_model, eutranet3gpp_model, nrnet3gpp_model, extenb3gpp_model, extgnbcucp3gpp_model, nrrrmpolicy3gpp_model},
    associations={},
    generalizations={}
)
