# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
EP_E1Grp = Class(name="EP_E1Grp", synonyms=["Represents the EP_E1 IOC."])

# EP_E1Grp class attributes and methods
EP_F1CGrp = Class(name="EP_F1CGrp", synonyms=["Represents the EP_F1C IOC."])

# EP_F1CGrp class attributes and methods
EP_F1UGrp = Class(name="EP_F1UGrp", synonyms=["Represents the EP_F1U IOC."])

# EP_F1UGrp class attributes and methods
EP_NgCGrp = Class(name="EP_NgCGrp", synonyms=["Represents the EP_NgC IOC."])

# EP_NgCGrp class attributes and methods
EP_NgUGrp = Class(name="EP_NgUGrp", synonyms=["Represents the EP_NgU IOC."])

# EP_NgUGrp class attributes and methods
EP_S1UGrp = Class(name="EP_S1UGrp", synonyms=["Represents the EP_S1U IOC."])

# EP_S1UGrp class attributes and methods
EP_X2CGrp = Class(name="EP_X2CGrp", synonyms=["Represents the EP_X2C IOC."])

# EP_X2CGrp class attributes and methods
EP_X2UGrp = Class(name="EP_X2UGrp", synonyms=["Represents the EP_X2U IOC."])

# EP_X2UGrp class attributes and methods
EP_XnCGrp = Class(name="EP_XnCGrp", synonyms=["Represents the EP_XnC IOC."])

# EP_XnCGrp class attributes and methods
EP_XnUGrp = Class(name="EP_XnUGrp", synonyms=["Represents the EP_XnU IOC."])

# EP_XnUGrp class attributes and methods
# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-ep",
    types={EP_E1Grp, EP_F1CGrp, EP_F1UGrp, EP_NgCGrp, EP_NgUGrp, EP_S1UGrp, EP_X2CGrp, EP_X2UGrp, EP_XnCGrp, EP_XnUGrp},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the NR related endpoint Information Object Classes (IOCs) that are part of the NR Network Resource Model (NRM)."]
