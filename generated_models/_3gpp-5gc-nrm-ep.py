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
from generated_models._3gpp_common_managed_element import domain_model as me3gpp_model
from generated_models._3gpp_common_managed_function import domain_model as mf3gpp_model
from generated_models._3gpp_common_subnetwork import domain_model as subnet3gpp_model
from generated_models._3gpp_common_top import domain_model as top3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Enumerations
# Classes
EP_N2Grp = Class(name="EP_N2Grp")
EP_N3Grp = Class(name="EP_N3Grp")
EP_N4Grp = Class(name="EP_N4Grp")
EP_N5Grp = Class(name="EP_N5Grp")
EP_N6Grp = Class(name="EP_N6Grp")
EP_N7Grp = Class(name="EP_N7Grp")
EP_N8Grp = Class(name="EP_N8Grp")
EP_N9Grp = Class(name="EP_N9Grp")
EP_N10Grp = Class(name="EP_N10Grp")
EP_N11Grp = Class(name="EP_N11Grp")
EP_N12Grp = Class(name="EP_N12Grp")
EP_N13Grp = Class(name="EP_N13Grp")
EP_N14Grp = Class(name="EP_N14Grp")
EP_N15Grp = Class(name="EP_N15Grp")
EP_N16Grp = Class(name="EP_N16Grp")
EP_N17Grp = Class(name="EP_N17Grp")
EP_N20Grp = Class(name="EP_N20Grp")
EP_N21Grp = Class(name="EP_N21Grp")
EP_N22Grp = Class(name="EP_N22Grp")
EP_N26Grp = Class(name="EP_N26Grp")
EP_N27Grp = Class(name="EP_N27Grp")
EP_N31Grp = Class(name="EP_N31Grp")
EP_N32Grp = Class(name="EP_N32Grp")
EP_S5CGrp = Class(name="EP_S5CGrp")
EP_S5UGrp = Class(name="EP_S5UGrp")
EP_RxGrp = Class(name="EP_RxGrp")
EP_MAP_SMSCGrp = Class(name="EP_MAP_SMSCGrp")
EP_NLSGrp = Class(name="EP_NLSGrp")
EP_NLGGrp = Class(name="EP_NLGGrp")
EP_SBI_IPXGrp = Class(name="EP_SBI_IPXGrp")

# EP_N2Grp class attributes and methods

# EP_N3Grp class attributes and methods

# EP_N4Grp class attributes and methods

# EP_N5Grp class attributes and methods

# EP_N6Grp class attributes and methods

# EP_N7Grp class attributes and methods

# EP_N8Grp class attributes and methods

# EP_N9Grp class attributes and methods

# EP_N10Grp class attributes and methods

# EP_N11Grp class attributes and methods

# EP_N12Grp class attributes and methods

# EP_N13Grp class attributes and methods

# EP_N14Grp class attributes and methods

# EP_N15Grp class attributes and methods

# EP_N16Grp class attributes and methods

# EP_N17Grp class attributes and methods

# EP_N20Grp class attributes and methods

# EP_N21Grp class attributes and methods

# EP_N22Grp class attributes and methods

# EP_N26Grp class attributes and methods

# EP_N27Grp class attributes and methods

# EP_N31Grp class attributes and methods

# EP_N32Grp class attributes and methods
EP_N32Grp_remoteSeppAddress: Property = Property(name="remoteSeppAddress", type=inet:host)
EP_N32Grp_remoteSeppId: Property = Property(name="remoteSeppId", type=IntegerType)
EP_N32Grp_n32cParas: Property = Property(name="n32cParas", type=StringType)
EP_N32Grp_n32fPolicy: Property = Property(name="n32fPolicy", type=StringType)
EP_N32Grp_withIPX: Property = Property(name="withIPX", type=BooleanType)
EP_N32Grp.attributes={EP_N32Grp_withIPX, EP_N32Grp_remoteSeppAddress, EP_N32Grp_n32cParas, EP_N32Grp_remoteSeppId, EP_N32Grp_n32fPolicy}

# EP_S5CGrp class attributes and methods

# EP_S5UGrp class attributes and methods

# EP_RxGrp class attributes and methods

# EP_MAP_SMSCGrp class attributes and methods

# EP_NLSGrp class attributes and methods

# EP_NLGGrp class attributes and methods

# EP_SBI_IPXGrp class attributes and methods

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-ep",
    types={EP_N2Grp, EP_N3Grp, EP_N4Grp, EP_N5Grp, EP_N6Grp, EP_N7Grp, EP_N8Grp, EP_N9Grp, EP_N10Grp, EP_N11Grp, EP_N12Grp, EP_N13Grp, EP_N14Grp, EP_N15Grp, EP_N16Grp, EP_N17Grp, EP_N20Grp, EP_N21Grp, EP_N22Grp, EP_N26Grp, EP_N27Grp, EP_N31Grp, EP_N32Grp, EP_S5CGrp, EP_S5UGrp, EP_RxGrp, EP_MAP_SMSCGrp, EP_NLSGrp, EP_NLGGrp, EP_SBI_IPXGrp, types3gpp_model, mf3gpp_model, me3gpp_model, top3gpp_model, types5g3gpp_model, inet_model, subnet3gpp_model, Conf5QIs3gpp_model, eprp3gpp_model, af3gpp_model, amf3gpp_model, ausf3gpp_model, dn3gpp_model, lmf3gpp_model, n3iwf3gpp_model, ngeir3gpp_model, nrf3gpp_model, nssf3gpp_model, pcf3gpp_model, sepp3gpp_model, smf3gpp_model, smsf3gpp_model, udm3gpp_model, upf3gpp_model},
    associations={},
    generalizations={}
)
