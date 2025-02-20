# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, Enumeration, EnumerationLiteral, StringType, BooleanType
)

# Classes
EP_E1 = Class(name="EP_E1")

# EP_E1 class attributes and methods
EP_F1C = Class(name="EP_F1C")

# EP_F1C class attributes and methods
EP_F1U = Class(name="EP_F1U")

# EP_F1U class attributes and methods
EP_XnC = Class(name="EP_XnC")

# EP_XnC class attributes and methods
EP_XnU = Class(name="EP_XnU")

# EP_XnU class attributes and methods
EP_NgC = Class(name="EP_NgC")

# EP_NgC class attributes and methods
EP_NgU = Class(name="EP_NgU")

# EP_NgU class attributes and methods
EP_X2C = Class(name="EP_X2C")

# EP_X2C class attributes and methods
EP_X2U = Class(name="EP_X2U")

# EP_X2U class attributes and methods
EP_S1U = Class(name="EP_S1U")

# EP_S1U class attributes and methods
# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-ep",
    types={EP_E1, EP_F1C, EP_F1U, EP_XnC, EP_XnU, EP_NgC, EP_NgU, EP_X2C, EP_X2U, EP_S1U},
    associations={},
    generalizations={}
)
