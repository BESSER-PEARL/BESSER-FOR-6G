# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, DomainModel,
    IntegerType, StringType, BooleanType, FloatType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    PrimitiveDataType, Enumeration, EnumerationLiteral
)

# Classes
DESManagementFunction = Class(name="DESManagementFunction", synonyms=["Represents the DESManagementFunction IOC."])

# DESManagementFunction class attributes and methods
DESManagementFunction_desSwitch: Property = Property(name="desSwitch", type=BooleanType, synonyms=["This attribute determines whether the Distributed SON or Domain-Centralized SON energy saving function is enabled or disabled."])
DESManagementFunction_energySavingState: Property = Property(name="energySavingState", type=EnumerationType, synonyms=["Specifies the status regarding the energy saving in the cell."])
DESManagementFunction_esNotAllowedTimePeriod: Property = Property(name="esNotAllowedTimePeriod", type=list, synonyms=["This attribute indicates a list of time periods during which inter-RAT energy saving is not allowed."])
DESManagementFunction_interRatEsActivationCandidateCellParameters: Property = Property(name="interRatEsActivationCandidateCellParameters", type=list, synonyms=["This attribute indicates the traffic load threshold and the time duration, which are used by distributed inter-RAT ES algorithms to allow an original cell to enter the energySaving state."])
DESManagementFunction_interRatEsActivationOriginalCellParameters: Property = Property(name="interRatEsActivationOriginalCellParameters", type=list, synonyms=["This attribute indicates the traffic load threshold and the time duration, which are used by distributed inter-RAT ES algorithms to allow an original cell to enter the energySaving state."])
DESManagementFunction_interRatEsDeactivationCandidateCellParameters: Property = Property(name="interRatEsDeactivationCandidateCellParameters", type=list, synonyms=["This attribute indicates the traffic load threshold and the time duration which is used by distributed inter-RAT ES algorithms to allow an original cell to leave the energySaving state."])
DESManagementFunction_intraRatEsActivationCandidateCellsLoadParameters: Property = Property(name="intraRatEsActivationCandidateCellsLoadParameters", type=list, synonyms=["This attribute indicates the traffic load threshold and the time duration, which are used by distributed ES algorithms level to allow a n 'original' cell to enter the energySaving state."])
DESManagementFunction_intraRatEsActivationOriginalCellLoadParameters: Property = Property(name="intraRatEsActivationOriginalCellLoadParameters", type=list, synonyms=["This attributes is relevant, if the cell acts as an original cell.This attribute indicates the traffic load threshold and the time duration, which are used by distributed ES algorithms to allow a cell to enter the energySaving state."])
DESManagementFunction_intraRatEsDeactivationCandidateCellsLoadParameters: Property = Property(name="intraRatEsDeactivationCandidateCellsLoadParameters", type=list, synonyms=["This attributes is relevant, if the cell acts as a candidate cell.This attribute indicates the traffic load threshold and the time duration which is used by distributed ES algorithms to allow a cell to leave the energySaving state."])
DESManagementFunction_isProbingCapable: Property = Property(name="isProbingCapable", type=EnumerationType, synonyms=["This attribute indicates whether this cell is capable of performing the ES probing procedure."])
DESManagementFunction.attributes={DESManagementFunction_desSwitch, DESManagementFunction_energySavingState, DESManagementFunction_esNotAllowedTimePeriod, DESManagementFunction_interRatEsActivationCandidateCellParameters, DESManagementFunction_interRatEsActivationOriginalCellParameters, DESManagementFunction_interRatEsDeactivationCandidateCellParameters, DESManagementFunction_intraRatEsActivationCandidateCellsLoadParameters, DESManagementFunction_intraRatEsActivationOriginalCellLoadParameters, DESManagementFunction_intraRatEsDeactivationCandidateCellsLoadParameters, DESManagementFunction_isProbingCapable}

EsNotAllowedTimePeriod = Class(name="EsNotAllowedTimePeriod", synonyms=["Represents the the traffic load threshold and the time duration."])

# EsNotAllowedTimePeriod class attributes and methods
EsNotAllowedTimePeriod_daysOfWeekList: Property = Property(name="daysOfWeekList", type=StringType, synonyms=["This field indicate the list of weekday."])
EsNotAllowedTimePeriod_listoftimeperiods: Property = Property(name="listoftimeperiods", type=StringType, synonyms=["This field indicate the list of time periods."])
EsNotAllowedTimePeriod_periodOfDay: Property = Property(name="periodOfDay", type=StringType, synonyms=["This field indicate the period of day."])
EsNotAllowedTimePeriod_startTimeandendTime: Property = Property(name="startTimeandendTime", type=StringType, synonyms=["This field indicate valid UTC time."])
EsNotAllowedTimePeriod.attributes={EsNotAllowedTimePeriod_daysOfWeekList, EsNotAllowedTimePeriod_listoftimeperiods, EsNotAllowedTimePeriod_periodOfDay, EsNotAllowedTimePeriod_startTimeandendTime}

InterRatEsActivationCandidateCellParameters = Class(name="InterRatEsActivationCandidateCellParameters", synonyms=["Represents the the traffic load threshold and the time duration."])

# InterRatEsActivationCandidateCellParameters class attributes and methods
InterRatEsActivationCandidateCellParameters_loadThreshold: Property = Property(name="loadThreshold", type=IntegerType, synonyms=["This attribute is used by distributed ES algorithms to allow a cell to enter the energySaving state."])
InterRatEsActivationCandidateCellParameters_timeDuration: Property = Property(name="timeDuration", type=IntegerType, synonyms=["The time duration indicates how long the traffic load (both for UL and DL) in the candidate cell needs to have been below the threshold before any original cells which will be provided backup coverage by the candidate cell enters energySaving state."])
InterRatEsActivationCandidateCellParameters.attributes={InterRatEsActivationCandidateCellParameters_loadThreshold, InterRatEsActivationCandidateCellParameters_timeDuration}

InterRatEsActivationOriginalCellParameters = Class(name="InterRatEsActivationOriginalCellParameters", synonyms=["Represents the the traffic load threshold and the time duration."])

# InterRatEsActivationOriginalCellParameters class attributes and methods
InterRatEsActivationOriginalCellParameters_loadThreshold: Property = Property(name="loadThreshold", type=IntegerType, synonyms=["The time duration indicates how long the traffic load (both for UL and DL) needs to have been below the threshold."])
InterRatEsActivationOriginalCellParameters_timeDuration: Property = Property(name="timeDuration", type=IntegerType, synonyms=["The time duration indicates how long the load needs to have been below the threshold."])
InterRatEsActivationOriginalCellParameters.attributes={InterRatEsActivationOriginalCellParameters_loadThreshold, InterRatEsActivationOriginalCellParameters_timeDuration}

InterRatEsDeactivationCandidateCellParameters = Class(name="InterRatEsDeactivationCandidateCellParameters", synonyms=["Represents the the traffic load threshold and the time duration."])

# InterRatEsDeactivationCandidateCellParameters class attributes and methods
InterRatEsDeactivationCandidateCellParameters_loadThreshold: Property = Property(name="loadThreshold", type=IntegerType, synonyms=["This attribute is used by distributed ES algorithms to allow a cell to enter the energySaving state."])
InterRatEsDeactivationCandidateCellParameters_timeDuration: Property = Property(name="timeDuration", type=IntegerType, synonyms=["The time duration indicates how long the traffic load (either for UL or DL) in the candidate cell needs to have been above the threshold to wake up one or more original cells which have been provided backup coverage by the candidate cell."])
InterRatEsDeactivationCandidateCellParameters.attributes={InterRatEsDeactivationCandidateCellParameters_loadThreshold, InterRatEsDeactivationCandidateCellParameters_timeDuration}

IntraRatEsActivationCandidateCellsLoadParameters = Class(name="IntraRatEsActivationCandidateCellsLoadParameters", synonyms=["Represents the the traffic load threshold and the time duration."])

# IntraRatEsActivationCandidateCellsLoadParameters class attributes and methods
IntraRatEsActivationCandidateCellsLoadParameters_loadThreshold: Property = Property(name="loadThreshold", type=IntegerType, synonyms=["This attribute is used by distributed ES algorithms to allow a cell to enter the energySaving state."])
IntraRatEsActivationCandidateCellsLoadParameters_timeDuration: Property = Property(name="timeDuration", type=IntegerType, synonyms=["The time duration indicates how long the load needs to have been below the threshold."])
IntraRatEsActivationCandidateCellsLoadParameters.attributes={IntraRatEsActivationCandidateCellsLoadParameters_loadThreshold, IntraRatEsActivationCandidateCellsLoadParameters_timeDuration}

IntraRatEsActivationOriginalCellLoadParameters = Class(name="IntraRatEsActivationOriginalCellLoadParameters", synonyms=["Represents the the traffic load threshold and the time duration."])

# IntraRatEsActivationOriginalCellLoadParameters class attributes and methods
IntraRatEsActivationOriginalCellLoadParameters_loadThreshold: Property = Property(name="loadThreshold", type=IntegerType, synonyms=["This attribute is used by distributed ES algorithms to allow a cell to enter the energySaving state."])
IntraRatEsActivationOriginalCellLoadParameters_timeDuration: Property = Property(name="timeDuration", type=IntegerType, synonyms=["The time duration indicates how long the load needs to have been below the threshold."])
IntraRatEsActivationOriginalCellLoadParameters.attributes={IntraRatEsActivationOriginalCellLoadParameters_loadThreshold, IntraRatEsActivationOriginalCellLoadParameters_timeDuration}

IntraRatEsDeactivationCandidateCellsLoadParameters = Class(name="IntraRatEsDeactivationCandidateCellsLoadParameters", synonyms=["Represents the the traffic load threshold and the time duration."])

# IntraRatEsDeactivationCandidateCellsLoadParameters class attributes and methods
IntraRatEsDeactivationCandidateCellsLoadParameters_loadThreshold: Property = Property(name="loadThreshold", type=IntegerType, synonyms=["This attribute is used by distributed ES algorithms to allow a cell to enter the energySaving state."])
IntraRatEsDeactivationCandidateCellsLoadParameters_timeDuration: Property = Property(name="timeDuration", type=IntegerType, synonyms=["The time duration indicates how long the load needs to have been below the threshold."])
IntraRatEsDeactivationCandidateCellsLoadParameters.attributes={IntraRatEsDeactivationCandidateCellsLoadParameters_loadThreshold, IntraRatEsDeactivationCandidateCellsLoadParameters_timeDuration}

# Domain Model with References
domain_model = DomainModel(
    name="_3gpp-nr-nrm-desmanagementfunction",
    types={DESManagementFunction, EsNotAllowedTimePeriod, InterRatEsActivationCandidateCellParameters, InterRatEsActivationOriginalCellParameters, InterRatEsDeactivationCandidateCellParameters, IntraRatEsActivationCandidateCellsLoadParameters, IntraRatEsActivationOriginalCellLoadParameters, IntraRatEsDeactivationCandidateCellsLoadParameters},
    associations={},
    generalizations={}
)
domain_model.synonyms = ["Defines the YANG mapping of the DESManagementFunction Information Object Class (IOC) that is part of the NR Network Resource Model (NRM)."]
