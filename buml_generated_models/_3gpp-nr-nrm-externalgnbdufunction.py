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
ExternalGNBDUFunction = Class(name="ExternalGNBDUFunction", synonyms=["Represets the ExternalGNBDUFunction IOC."])

# ExternalGNBDUFunction class attributes and methods
ExternalGNBDUFunction_gNBId: Property = Property(name="gNBId", type=IntegerType, synonyms=["Identifies a gNB within a PLMN."])
ExternalGNBDUFunction_gNBIdLength: Property = Property(name="gNBIdLength", type=IntegerType, synonyms=["Indicates the number of bits for encoding the gNB ID."])
ExternalGNBDUFunction_pLMNId: Property = Property(name="pLMNId", type=types3gpp_model.get_type_by_name('PLMNId'), multiplicity=Multiplicity(1, "*"), synonyms=["Specifies the PLMN identifier to be used as part of the global RAN node identity."])
ExternalGNBDUFunction.attributes={ExternalGNBDUFunction_gNBId, ExternalGNBDUFunction_gNBIdLength, ExternalGNBDUFunction_pLMNId}

ExternalGNBDUFunctionWrapper = Class(name="ExternalGNBDUFunctionWrapper")

# ExternalGNBDUFunctionWrapper class attributes and methods
ExternalGNBDUFunctionWrapper_ExternalGNBDUFunction: Property = Property(name="ExternalGNBDUFunction", type=list, multiplicity=Multiplicity(0, "*"), synonyms=["Represents the properties, known by the management function, of a GNBDUFunction managed by another management function."])
ExternalGNBDUFunctionWrapper.attributes={ExternalGNBDUFunctionWrapper_ExternalGNBDUFunction}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-externalgnbdufunction",
    types={ExternalGNBDUFunction, ExternalGNBDUFunctionWrapper},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the ExternalGNBDUFunction Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
