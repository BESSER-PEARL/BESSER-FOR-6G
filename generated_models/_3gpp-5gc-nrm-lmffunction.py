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
LMFFunctionGrp = Class(name="LMFFunctionGrp")
LMFFunction = Class(name="LMFFunction")

# LMFFunctionGrp class attributes and methods
LMFFunctionGrp_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
LMFFunctionGrp_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
LMFFunctionGrp_commModelList: Property = Property(name="commModelList", type=list)
LMFFunctionGrp.attributes={LMFFunctionGrp_commModelList, LMFFunctionGrp_pLMNIdList, LMFFunctionGrp_managedNFProfile}

# LMFFunction class attributes and methods
LMFFunction_pLMNIdList: Property = Property(name="pLMNIdList", type=list)
LMFFunction_managedNFProfile: Property = Property(name="managedNFProfile", type=list)
LMFFunction_commModelList: Property = Property(name="commModelList", type=list)
LMFFunction.attributes={LMFFunction_commModelList, LMFFunction_pLMNIdList, LMFFunction_managedNFProfile}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-5gc-nrm-lmffunction",
    types={LMFFunctionGrp, LMFFunction, types3gpp_model, mf3gpp_model, me3gpp_model, top3gpp_model, types5g3gpp_model, inet_model, subnet3gpp_model, Conf5QIs3gpp_model, eprp3gpp_model, af3gpp_model, amf3gpp_model, ausf3gpp_model, dn3gpp_model, lmf3gpp_model, n3iwf3gpp_model, ngeir3gpp_model, nrf3gpp_model, nssf3gpp_model, pcf3gpp_model, sepp3gpp_model, smf3gpp_model, smsf3gpp_model, udm3gpp_model, upf3gpp_model},
    associations={},
    generalizations={}
)
