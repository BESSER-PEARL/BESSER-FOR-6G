# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
ExternalEUtranCellFDD = Class(name="ExternalEUtranCellFDD", synonyms=["Represents the ExternalEUtranCellFDD IOC."])

# ExternalEUtranCellFDD class attributes and methods
ExternalEUtranCellFDD_earfcnDL: Property = Property(name="earfcnDL", type=IntegerType, synonyms=["The channel number for the central DL frequency."])
ExternalEUtranCellFDD_earfcnUL: Property = Property(name="earfcnUL", type=IntegerType, synonyms=["The channel number for the central UL frequency. Value 0 means that the UL channel number is N/A for the DL-only bands."])
ExternalEUtranCellFDD.attributes={ExternalEUtranCellFDD_earfcnDL, ExternalEUtranCellFDD_earfcnUL}

ExternalEUtranCellFDDWrapper = Class(name="ExternalEUtranCellFDDWrapper")

# ExternalEUtranCellFDDWrapper class attributes and methods
ExternalEUtranCellFDDWrapper_ExternalEUtranCellFDD: Property = Property(name="ExternalEUtranCellFDD", type=list, synonyms=["Represents the common properties of external E-UTRAN FDD cell provided by eNB or NG-RAN FDD cell provided by ng-eNB."])
ExternalEUtranCellFDDWrapper.attributes={ExternalEUtranCellFDDWrapper_ExternalEUtranCellFDD}

ExternalEUtranCellTDD = Class(name="ExternalEUtranCellTDD", synonyms=["Represents the ExternalEUtranCellTDD IOC."])

# ExternalEUtranCellTDD class attributes and methods
ExternalEUtranCellTDD_earfcn: Property = Property(name="earfcn", type=IntegerType, synonyms=["The frequency number for the central frequency."])
ExternalEUtranCellTDD.attributes={ExternalEUtranCellTDD_earfcn}

ExternalEUtranCellTDDWrapper = Class(name="ExternalEUtranCellTDDWrapper")

# ExternalEUtranCellTDDWrapper class attributes and methods
ExternalEUtranCellTDDWrapper_ExternalEUtranCellTDD: Property = Property(name="ExternalEUtranCellTDD", type=list, synonyms=["Represents the common properties of external E-UTRAN cell TDD provided by eNB or NG-RAN TDD cell provided by ng-eNB."])
ExternalEUtranCellTDDWrapper.attributes={ExternalEUtranCellTDDWrapper_ExternalEUtranCellTDD}

ExternalEUtranGenericCell = Class(name="ExternalEUtranGenericCell", synonyms=["Represents the ExternalEUtranGenericCell IOC."])

# ExternalEUtranGenericCell class attributes and methods
ExternalEUtranGenericCell_cellLocalId: Property = Property(name="cellLocalId", type=IntegerType, synonyms=["Unambiguously identifies a cell within an eNodeB."])
ExternalEUtranGenericCell_eNBId: Property = Property(name="eNBId", type=IntegerType, synonyms=["Unambiguously identifies an eNodeB within a PLMN."])
ExternalEUtranGenericCell_pci: Property = Property(name="pci", type=IntegerType, synonyms=["The Physical Cell Identity (PCI) of the cell (for NM-Centralized, EM-Centralized and Distributed PCI assignment cases). In the case of NM-Centralized PCI assignment, see 3GPP TS 36.300."])
ExternalEUtranGenericCell_plmnIdList: Property = Property(name="plmnIdList", type=list, synonyms=["List of unique identities for PLMNs. A cell can broadcast up to 6 PLMN IDs. This is to support the case that one cell can be used by up to 6 operator's core networks. The PLMN(s) included in this list will use the same single tracking area code (TAC) and the same Cell Identity (cellLocalId) for sharing the radio access network resources. One member of plmnIdList is the primary PLMN ID. A PLMN ID included in this list cannot be included in the cellAccessInfoList. The PLMN ID is composed of a Mobile Country Code (MCC) and a Mobile Network Code (MNC)."])
ExternalEUtranGenericCell.attributes={ExternalEUtranGenericCell_cellLocalId, ExternalEUtranGenericCell_eNBId, ExternalEUtranGenericCell_pci, ExternalEUtranGenericCell_plmnIdList}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-externaleutrancell",
    types={ExternalEUtranCellFDD, ExternalEUtranCellFDDWrapper, ExternalEUtranCellTDD, ExternalEUtranCellTDDWrapper, ExternalEUtranGenericCell},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the ExternalEUtranCellFDD and ExternalEUtranCellTDD Information Object Classes (IOCs) that are part of the NR Network Resource Model (NRM)."]
