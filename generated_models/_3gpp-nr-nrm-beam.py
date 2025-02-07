# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral
)

# Import referenced models
from generated_models._3gpp_5g_common_yang_types import domain_model as types5g3gpp_model
from generated_models._3gpp_common_yang_types import domain_model as types3gpp_model

# Classes
Beam = Class(name="Beam")

# Beam class attributes and methods
Beam_beamIndex: Property = Property(name="beamIndex", type=IntegerType)
Beam_beamType: Property = Property(name="beamType", type=BeamType)
Beam_beamAzimuth: Property = Property(name="beamAzimuth", type=IntegerType)
Beam_beamTilt: Property = Property(name="beamTilt", type=IntegerType)
Beam_beamHorizWidth: Property = Property(name="beamHorizWidth", type=IntegerType)
Beam_beamVertWidth: Property = Property(name="beamVertWidth", type=IntegerType)
Beam.attributes={Beam_beamIndex, Beam_beamType, Beam_beamAzimuth, Beam_beamTilt, Beam_beamHorizWidth, Beam_beamVertWidth}

