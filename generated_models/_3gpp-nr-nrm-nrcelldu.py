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
NRCellDUGrp = Class(name="NRCellDUGrp")
NRCellDU = Class(name="NRCellDU")

# NRCellDUGrp class attributes and methods
NRCellDUGrp_cellLocalId: Property = Property(name="cellLocalId", type=IntegerType)
NRCellDUGrp_operationalState: Property = Property(name="operationalState", type=types3gpp:OperationalState)
NRCellDUGrp_administrativeState: Property = Property(name="administrativeState", type=types3gpp:AdministrativeState)
NRCellDUGrp_cellState: Property = Property(name="cellState", type=types3gpp:CellState)
NRCellDUGrp_nRPCI: Property = Property(name="nRPCI", type=IntegerType)
NRCellDUGrp_nRTAC: Property = Property(name="nRTAC", type=types3gpp:Tac)
NRCellDUGrp_arfcnDL: Property = Property(name="arfcnDL", type=IntegerType)
NRCellDUGrp_arfcnUL: Property = Property(name="arfcnUL", type=IntegerType)
NRCellDUGrp_arfcnSUL: Property = Property(name="arfcnSUL", type=IntegerType)
NRCellDUGrp_bSChannelBwDL: Property = Property(name="bSChannelBwDL", type=IntegerType)
NRCellDUGrp_bSChannelBwUL: Property = Property(name="bSChannelBwUL", type=IntegerType)
NRCellDUGrp_bSChannelBwSUL: Property = Property(name="bSChannelBwSUL", type=IntegerType)
NRCellDUGrp_ssbFrequency: Property = Property(name="ssbFrequency", type=IntegerType)
NRCellDUGrp_ssbPeriodicity: Property = Property(name="ssbPeriodicity", type=IntegerType)
NRCellDUGrp_ssbSubCarrierSpacing: Property = Property(name="ssbSubCarrierSpacing", type=IntegerType)
NRCellDUGrp_ssbOffset: Property = Property(name="ssbOffset", type=IntegerType)
NRCellDUGrp_ssbDuration: Property = Property(name="ssbDuration", type=IntegerType)
NRCellDUGrp_pLMNInfoList: Property = Property(name="pLMNInfoList", type=list)
NRCellDUGrp.attributes={NRCellDUGrp_ssbSubCarrierSpacing, NRCellDUGrp_arfcnDL, NRCellDUGrp_cellState, NRCellDUGrp_arfcnSUL, NRCellDUGrp_bSChannelBwUL, NRCellDUGrp_ssbPeriodicity, NRCellDUGrp_bSChannelBwSUL, NRCellDUGrp_ssbFrequency, NRCellDUGrp_nRTAC, NRCellDUGrp_pLMNInfoList, NRCellDUGrp_ssbOffset, NRCellDUGrp_operationalState, NRCellDUGrp_ssbDuration, NRCellDUGrp_nRPCI, NRCellDUGrp_administrativeState, NRCellDUGrp_arfcnUL, NRCellDUGrp_bSChannelBwDL, NRCellDUGrp_cellLocalId}

# NRCellDU class attributes and methods
NRCellDU_cellLocalId: Property = Property(name="cellLocalId", type=IntegerType)
NRCellDU_operationalState: Property = Property(name="operationalState", type=types3gpp:OperationalState)
NRCellDU_administrativeState: Property = Property(name="administrativeState", type=types3gpp:AdministrativeState)
NRCellDU_cellState: Property = Property(name="cellState", type=types3gpp:CellState)
NRCellDU_nRPCI: Property = Property(name="nRPCI", type=IntegerType)
NRCellDU_nRTAC: Property = Property(name="nRTAC", type=types3gpp:Tac)
NRCellDU_arfcnDL: Property = Property(name="arfcnDL", type=IntegerType)
NRCellDU_arfcnUL: Property = Property(name="arfcnUL", type=IntegerType)
NRCellDU_arfcnSUL: Property = Property(name="arfcnSUL", type=IntegerType)
NRCellDU_bSChannelBwDL: Property = Property(name="bSChannelBwDL", type=IntegerType)
NRCellDU_bSChannelBwUL: Property = Property(name="bSChannelBwUL", type=IntegerType)
NRCellDU_bSChannelBwSUL: Property = Property(name="bSChannelBwSUL", type=IntegerType)
NRCellDU_ssbFrequency: Property = Property(name="ssbFrequency", type=IntegerType)
NRCellDU_ssbPeriodicity: Property = Property(name="ssbPeriodicity", type=IntegerType)
NRCellDU_ssbSubCarrierSpacing: Property = Property(name="ssbSubCarrierSpacing", type=IntegerType)
NRCellDU_ssbOffset: Property = Property(name="ssbOffset", type=IntegerType)
NRCellDU_ssbDuration: Property = Property(name="ssbDuration", type=IntegerType)
NRCellDU_pLMNInfoList: Property = Property(name="pLMNInfoList", type=list)
NRCellDU.attributes={NRCellDU_ssbSubCarrierSpacing, NRCellDU_arfcnDL, NRCellDU_arfcnSUL, NRCellDU_bSChannelBwUL, NRCellDU_ssbPeriodicity, NRCellDU_bSChannelBwSUL, NRCellDU_nRTAC, NRCellDU_administrativeState, NRCellDU_pLMNInfoList, NRCellDU_ssbOffset, NRCellDU_operationalState, NRCellDU_ssbDuration, NRCellDU_nRPCI, NRCellDU_cellState, NRCellDU_ssbFrequency, NRCellDU_arfcnUL, NRCellDU_bSChannelBwDL, NRCellDU_cellLocalId}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-nrcelldu",
    types={NRCellDUGrp, NRCellDU, types3gpp_model, mf3gpp_model, me3gpp_model, top3gpp_model, types5g3gpp_model, inet_model, subnet3gpp_model, Conf5QIs3gpp_model, eprp3gpp_model, af3gpp_model, amf3gpp_model, ausf3gpp_model, dn3gpp_model, lmf3gpp_model, n3iwf3gpp_model, ngeir3gpp_model, nrf3gpp_model, nssf3gpp_model, pcf3gpp_model, sepp3gpp_model, smf3gpp_model, smsf3gpp_model, udm3gpp_model, upf3gpp_model, yang_model, nfs3gpp_model, nfp3gpp_model, meas3gpp_model, subscr3gpp_model, fm3gpp_model, trace3gpp_model, yangmnt_model, cbeamff3gpp_model, gnbdu3gpp_model, nrsectcarr3gpp_model, nrcellcu3gpp_model, gnbcucp3gpp_model, nrcelldu3gpp_model, gnbcuup3gpp_model, eutranet3gpp_model, nrnet3gpp_model, extenb3gpp_model, extgnbcucp3gpp_model, nrrrmpolicy3gpp_model},
    associations={},
    generalizations={}
)
