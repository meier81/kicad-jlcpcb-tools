"""Events used througout the plugin."""

from wx.lib.newevent import NewEvent  # pylint: disable=import-error

ResetGaugeEvent, EVT_RESET_GAUGE_EVENT = NewEvent()
UpdateGaugeEvent, EVT_UPDATE_GAUGE_EVENT = NewEvent()
MessageEvent, EVT_MESSAGE_EVENT = NewEvent()
AssignPartsEvent, EVT_ASSIGN_PARTS_EVENT = NewEvent()
PopulateFootprintListEvent, EVT_POPULATE_FOOTPRINT_LIST_EVENT = NewEvent()
UpdateSetting, EVT_UPDATE_SETTING = NewEvent()
LogboxAppendEvent, EVT_LOGBOX_APPEND_EVENT = NewEvent()
