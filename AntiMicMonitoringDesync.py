import obspython as obs

######## Global Variables ########
type = "input"
source_name = ""
update_interval = 60

######## Config Variables ########
min_slider_value = 1
max_slider_value = 3600
slider_inverval = 1
default_update_interval = 60

######## Methods ########


def reset_monitoring():
  global source_name
  source = obs.obs_get_source_by_name(source_name)
  if source:
    monitoring_type = obs.obs_source_get_monitoring_type(source)
    obs.obs_source_set_monitoring_type(
        source, obs.OBS_MONITORING_TYPE_NONE)
    print("Monitoring disabled")
    obs.obs_source_set_monitoring_type(source, monitoring_type)
    print("Monitoring enabled")
  else:
    print(f"Monitoring device not found with the name {source_name}.")


def update_sources(list):
  sources = obs.obs_enum_sources()
  obs.obs_property_list_clear(list)
  if sources:
    for source in sources:
      source_id = obs.obs_source_get_id(source)
      if source_type in source_id:
        name = obs.obs_source_get_name(source)
        obs.obs_property_list_add_string(list, name, name)
        print(f"Device type found: {name}.")
  else:
    obs.obs_property_list_add_string(
        list, "No source found", "No source found")
  obs.source_list_release(sources)

######## Main OBS functions ########


def script_defaults(settings):
  global default_update_interval, source_type
  obs.obs_data_set_default_string(settings, "type", "input")
  obs.obs_data_set_default_int(
      settings, "update_interval", default_update_interval)


def script_update(settings):
  global update_interval, source_name, source_type
  source_type = obs.obs_data_get_string(settings, "type")
  source_name = obs.obs_data_get_string(settings, "source")
  update_interval = obs.obs_data_get_int(settings, "update_interval")
  obs.timer_remove(reset_monitoring)
  obs.timer_add(reset_monitoring, update_interval*1000)


def script_load(settings):
  global update_interval, source_name, source_type
  source_type = obs.obs_data_get_string(settings, "type")
  source_name = obs.obs_data_get_string(settings, "source")
  update_interval = obs.obs_data_get_int(settings, "update_interval")
  obs.timer_add(reset_monitoring, update_interval*1000)


def script_properties():
  props = obs.obs_properties_create()
  input_type_drop_list = obs.obs_properties_add_list(
      props, "type", "Source Type", obs.OBS_COMBO_TYPE_LIST, obs.OBS_COMBO_FORMAT_STRING)
  sources_drop_list = obs.obs_properties_add_list(
      props, "source", "Device", obs.OBS_COMBO_TYPE_LIST, obs.OBS_COMBO_FORMAT_STRING)
  obs.obs_properties_add_int_slider(
      props, "update_interval", "Update Interval (s):", min_slider_value, max_slider_value, slider_inverval)
  update_sources(sources_drop_list)
  obs.obs_property_set_modified_callback(
      input_type_drop_list, lambda props, prop, settings: True if update_sources(sources_drop_list) else True)
  obs.obs_property_list_add_string(input_type_drop_list, "Inputs", "input")
  obs.obs_property_list_add_string(input_type_drop_list, "Outputs", "output")
  obs.obs_property_list_add_string(input_type_drop_list, "All Sources", "")

  return props


def script_description():
  return '<center><h2> Anti Mic Monitoring Desync</h2></center><center><h4>If you run into any problems, open an issue on <a href="https://github.com/MechanicallyDev/OBS-Anti-Mic-Monitoring-Desync">GitHub</a></h4></center>This script periodically resets the audio monitoring for a selected device to mitigate the buffer buildup issue.'
