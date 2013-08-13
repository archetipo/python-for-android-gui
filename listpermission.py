class Build_o():
	def __init__(self,pathbuild):
		self.arg_list=[]
		self.path_builder=pathbuild
		self.permissions_list=["ACCESS_CHECKIN_PROPERTIES" ,
								"ACCESS_COARSE_LOCATION" ,
								"ACCESS_FINE_LOCATION" ,
								"ACCESS_LOCATION_EXTRA_COMMANDS" ,
								"ACCESS_MOCK_LOCATION" ,
								"ACCESS_NETWORK_STATE" ,
								"ACCESS_SURFACE_FLINGER" ,
								"ACCESS_WIFI_STATE" ,
								"ACCOUNT_MANAGER" ,
								"AUTHENTICATE_ACCOUNTS" ,
								"BATTERY_STATS" ,
								"BIND_APPWIDGET" ,
								"BIND_DEVICE_ADMIN" ,
								"BIND_INPUT_METHOD" ,
								"BIND_REMOTEVIEWS" ,
								"BIND_WALLPAPER" ,
								"BLUETOOTH" ,
								"BLUETOOTH_ADMIN" ,
								"BRICK" ,
								"BROADCAST_PACKAGE_REMOVED" ,
								"BROADCAST_SMS" ,
								"BROADCAST_STICKY" ,
								"BROADCAST_WAP_PUSH" ,
								"CALL_PHONE",
								"CALL_PRIVILEGED" ,
								"CAMERA",
								"CHANGE_COMPONENT_ENABLED_STATE" ,
								"CHANGE_CONFIGURATION" ,
								"CHANGE_NETWORK_STATE" ,
								"CHANGE_WIFI_MULTICAST_STATE" ,
								"CHANGE_WIFI_STATE" ,
								"CLEAR_APP_CACHE" ,
								"CLEAR_APP_USER_DATA" ,
								"CONTROL_LOCATION_UPDATES" ,
								"DELETE_CACHE_FILES" ,
								"DELETE_PACKAGES" ,
								"DEVICE_POWER" ,
								"DIAGNOSTIC" ,
								"DISABLE_KEYGUARD" ,
								"DUMP" ,
								"EXPAND_STATUS_BAR" ,
								"FACTORY_TEST" ,
								"FLASHLIGHT" ,
								"FORCE_BACK" ,
								"GET_ACCOUNTS" ,
								"GET_PACKAGE_SIZE" ,
								"GET_TASKS" ,
								"GLOBAL_SEARCH" ,
								"HARDWARE_TEST" ,
								"INJECT_EVENTS" ,
								"INSTALL_LOCATION_PROVIDER" ,
								"INSTALL_PACKAGES" ,
								"INTERNAL_SYSTEM_WINDOW" ,
								"INTERNET",
								"KILL_BACKGROUND_PROCESSES" ,
								"MANAGE_ACCOUNTS" ,
								"MANAGE_APP_TOKENS" ,
								"MASTER_CLEAR" ,
								"MODIFY_AUDIO_SETTINGS" ,
								"MODIFY_PHONE_STATE" ,
								"MOUNT_FORMAT_FILESYSTEMS" ,
								"MOUNT_UNMOUNT_FILESYSTEMS" ,
								"NFC" ,
								"PROCESS_OUTGOING_CALLS" ,
								"READ_CALENDAR" ,
								"READ_CONTACTS" ,
								"READ_FRAME_BUFFER" ,
								"READ_HISTORY_BOOKMARKS" ,
								"READ_INPUT_STATE" ,
								"READ_LOGS" ,
								"READ_PHONE_STATE" ,
								"READ_SMS" ,
								"READ_SYNC_SETTINGS" ,
								"READ_SYNC_STATS" ,
								"REBOOT" ,
								"RECEIVE_BOOT_COMPLETED" ,
								"RECEIVE_MMS" ,
								"RECEIVE_SMS" ,
								"RECEIVE_WAP_PUSH" ,
								"RECORD_AUDIO" ,
								"REORDER_TASKS" ,
								"RESTART_PACKAGES" ,
								"SEND_SMS" ,
								"SET_ACTIVITY_WATCHER" ,
								"SET_ALARM" ,
								"SET_ALWAYS_FINISH" ,
								"SET_ANIMATION_SCALE" ,
								"SET_DEBUG_APP" ,
								"SET_ORIENTATION" ,
								"SET_POINTER_SPEED" ,
								"SET_PROCESS_LIMIT" ,
								"SET_TIME" ,
								"SET_TIME_ZONE" ,
								"SET_WALLPAPER" ,
								"SET_WALLPAPER_HINTS" ,
								"SIGNAL_PERSISTENT_PROCESSES" ,
								"STATUS_BAR" ,
								"SUBSCRIBED_FEEDS_READ" ,
								"SUBSCRIBED_FEEDS_WRITE" ,
								"SYSTEM_ALERT_WINDOW" ,
								"UPDATE_DEVICE_STATS" ,
								"USE_CREDENTIALS" ,
								"USE_SIP" ,
								"VIBRATE" ,
								"WAKE_LOCK" ,
								"WRITE_APN_SETTINGS" ,
								"WRITE_CALENDAR" ,
								"WRITE_CONTACTS" ,
								"WRITE_EXTERNAL_STORAGE" ,
								"WRITE_GSERVICES" ,
								"WRITE_HISTORY_BOOKMARKS" ,
								"WRITE_SECURE_SETTINGS" ,
								"WRITE_SETTINGS" ,
								"WRITE_SMS" ,
								"WRITE_SYNC_SETTINGS"]


	def add_argument(self,name,dest='',help='',required=False,default='',action='',nargs=''):
		self.arg_list.append({'name':name,'dest':dest,'help':help,'required':required,'default':default,'action':action,'nargs':nargs})


def get_args(pathbuild):

	obj_builder=Build_o(pathbuild)

	obj_builder.add_argument('--package', dest='package', help='The name of the java package the project will be packaged under.', required=True)
	obj_builder.add_argument('--name', dest='name', help='The human-readable name of the project.', required=True)
	obj_builder.add_argument('--version', dest='version', help='The version number of the project. This should consist of numbers and dots, and should have the same number of groups of numbers as previous versions.', required=True)
	obj_builder.add_argument('--numeric-version', dest='numeric_version', help='The numeric version number of the project. If not given, this is automatically computed from the version.')
	obj_builder.add_argument('--dir', dest='dir', help='The directory containing public files for the project.')
	obj_builder.add_argument('--private', dest='private', help='The directory containing additional private files for the project.')
	obj_builder.add_argument('--launcher', dest='launcher', action='store_true',
			help='Provide this argument to build a multi-obj_builder. launcher, rather than a single obj_builder..')
	obj_builder.add_argument('--icon-name', dest='icon_name', help='The name of the project\'s launcher icon.')
	obj_builder.add_argument('--orientation', dest='orientation', default='landscobj_builder.',
			help='The orientation that the game will display in. Usually one of "landscobj_builder.", "portrait" or "sensor"')
	obj_builder.add_argument('--permission', dest='permissions', action='obj_builder.end', help='The permissions to give this obj_builder..')
	obj_builder.add_argument('--ignore-path', dest='ignore_path', action='obj_builder.end', help='Ignore path when building the obj_builder.')
	obj_builder.add_argument('--icon', dest='icon', help='A png file to use as the icon for the obj_builder.lication.')
	obj_builder.add_argument('--presplash', dest='presplash', help='A jpeg file to use as a screen while the obj_builder.lication is loading.')
	obj_builder.add_argument('--ouya-category', dest='ouya_category', help='Valid values are GAME and obj_builder.. This must be specified to enable OUYA console support.')
	obj_builder.add_argument('--ouya-icon', dest='ouya_icon', help='A png file to use as the icon for the obj_builder.lication if it is installed on an OUYA console.')
	obj_builder.add_argument('--install-location', dest='install_location', default='auto', help='The default install location. Should be "auto", "preferExternal" or "internalOnly".')
	obj_builder.add_argument('--compile-pyo', dest='compile_pyo', action='store_true', help='Compile all .py files to .pyo, and only distribute the compiled bytecode.')
	obj_builder.add_argument('--intent-filters', dest='intent_filters', help='Add intent-filters xml rules to the AndroidManifest.xml file. The argument is a filename containing xml. The filename should be located relative to the python-for-android directory')
	obj_builder.add_argument('--with-billing', dest='billing_pubkey', help='If set, the billing service will be added')
	obj_builder.add_argument('--blacklist', dest='blacklist',
		default='',
		help='Use a blacklist file to match unwanted file in the final obj_builder.')
	obj_builder.add_argument('--sdk', dest='sdk_version', default='8', help='Android SDK version to use. Default to 8')
	obj_builder.add_argument('--minsdk', dest='min_sdk_version', default='8', help='Minimum Android SDK version to use. Default to 8')
	obj_builder.add_argument('--window', dest='window', action='store_true',
			help='Indicate if the obj_builder.lication will be windowed')
	obj_builder.add_argument('--wakelock', dest='wakelock', action='store_true',
			help='Indicate if the obj_builder.lication needs the device to stay on')
	obj_builder.add_argument('command', nargs='*', help='The command to pass to ant (debug, release, installd, installr)')
	obj_builder.add_argument('--add-jar', dest='add_jar', action='obj_builder.end', help='Add a Java .jar to the libs, so you can access its classes with pyjnius. You can specify this argument more than once to include multiple jars')
	return obj_builder

