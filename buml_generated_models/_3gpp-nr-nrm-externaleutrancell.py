# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
ExternalEUtranCellFDD = Class(name="ExternalEUtranCellFDD")

# ExternalEUtranCellFDD class attributes and methods
ExternalEUtranCellFDD_earfcnDL: Property = Property(name="earfcnDL", type=IntegerType)
ExternalEUtranCellFDD_earfcnUL: Property = Property(name="earfcnUL", type=IntegerType)
ExternalEUtranCellFDD.attributes={ExternalEUtranCellFDD_earfcnDL, ExternalEUtranCellFDD_earfcnUL}

ExternalEUtranCellFDDWrapper = Class(name="ExternalEUtranCellFDDWrapper")

# ExternalEUtranCellFDDWrapper class attributes and methods
ExternalEUtranCellFDDWrapper_ExternalEUtranCellFDD: Property = Property(name="ExternalEUtranCellFDD", type=list)
ExternalEUtranCellFDDWrapper.attributes={ExternalEUtranCellFDDWrapper_ExternalEUtranCellFDD}

ExternalEUtranCellTDD = Class(name="ExternalEUtranCellTDD")

# ExternalEUtranCellTDD class attributes and methods
ExternalEUtranCellTDD_earfcn: Property = Property(name="earfcn", type=IntegerType)
ExternalEUtranCellTDD.attributes={ExternalEUtranCellTDD_earfcn}

ExternalEUtranCellTDDWrapper = Class(name="ExternalEUtranCellTDDWrapper")

# ExternalEUtranCellTDDWrapper class attributes and methods
ExternalEUtranCellTDDWrapper_ExternalEUtranCellTDD: Property = Property(name="ExternalEUtranCellTDD", type=list)
ExternalEUtranCellTDDWrapper.attributes={ExternalEUtranCellTDDWrapper_ExternalEUtranCellTDD}

ExternalEUtranGenericCell = Class(name="ExternalEUtranGenericCell")

# ExternalEUtranGenericCell class attributes and methods
ExternalEUtranGenericCell_cellLocalId: Property = Property(name="cellLocalId", type=IntegerType)
ExternalEUtranGenericCell_eNBId: Property = Property(name="eNBId", type=IntegerType)
ExternalEUtranGenericCell_pci: Property = Property(name="pci", type=IntegerType)
ExternalEUtranGenericCell_plmnIdList: Property = Property(name="plmnIdList", type=list)
ExternalEUtranGenericCell.attributes={ExternalEUtranGenericCell_cellLocalId, ExternalEUtranGenericCell_eNBId, ExternalEUtranGenericCell_pci, ExternalEUtranGenericCell_plmnIdList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-externaleutrancell",
    types={ExternalEUtranCellFDD, ExternalEUtranCellFDDWrapper, ExternalEUtranCellTDD, ExternalEUtranCellTDDWrapper, ExternalEUtranGenericCell},
    associations={},
    generalizations={}
)
