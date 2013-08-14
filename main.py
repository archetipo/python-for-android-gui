#!/usr/bin/python
#-*- coding:utf-8 -*-
import os,sys
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.checkbox import CheckBox
from kivy.properties import ObjectProperty
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.treeview import TreeView, TreeViewLabel
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
import logcat as TLogCat
import listpermission as lstp
import subprocess
import pkgutil
import imp


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)



class TabTools(TabbedPanel):
	#workaroud if call __init__() and super class
	#kv files dosen't work fine
	def init(self):
		self.lines=''
		self.oldline=''
		self.line=''
		self.adbpath=''
		self.py4a_path=''
		self.prj_load_path='~'
		self.sett_obj=None
		self.lines_count=0
		self.obj_builder=None
		self.builder_path=''
		self.MainBx=None
		self.apktype=''
		self.pb = None
		self.list_module_to_dist=[]
		self.list_permission_to_build=[]

	def setup(self):
		self.datalogcat=[]
		self.LogCat=None
		self.LogCat=TLogCat.ThLogCat(self)
		self.device_is_connected=False
		baseapp=os.path.join(self.py4a_path, 'dist')
		baseapp=os.path.join(baseapp, 'default')
		self.builder_path=baseapp
		self.obj_builder=lstp.get_args(baseapp)

		for tbp in self.tab_list:
			if 'Distribuite' in tbp.text:
				self.render_distribuite(tbp)
			if 'Build' in tbp.text:
				self.render_builder(tbp)



	def render_builder(self,tab):
		self.MainBx=BoxLayout(orientation='vertical')
		UpBx=BoxLayout()

		UpBx.padding=10
		UpBx.spacing=10
		UpBx.size_hint = (1,.99)
		#~ UpBx.pos_hint= {'x': 0, 'y': 0}

		btnBuild=Button(text='Build',size_hint=(1, 1))
		btnBuild.bind(on_press=self.start_build)
		btnInstall=Button(text='Install',size_hint=(1,1))
		btnInstall.bind(on_press=self.start_install)
		btnInstall.bind(on_release=self.install_prj)
		btnInstall.disabled=False

		BtnBx=BoxLayout()
		BtnBx.size_hint = (1,.1)
		BtnBx.add_widget(btnBuild)
		BtnBx.add_widget(btnInstall)

		self.MainBx.add_widget(UpBx)
		self.MainBx.add_widget(BtnBx)


		DxBox=BoxLayout(orientation='vertical')
		DxBox.padding=5
		DxBox.spacing=5

		ProojIntBx = GridLayout(cols=2) #init
		ProojIntBx.size_hint = (1, 0.3)
		vl=Label(text=u'Version')
		vl.text_size=(self.width, None)
		self.vt=TextInput()
		self.vt.multiline=False
		pnl=Label(text=u'Project Name')
		self.pnt=TextInput()
		self.pnt.multiline=False
		pkgl=Label(text=u'Base Package Name')
		self.pkgt=TextInput()
		self.pkgt.multiline=False
		ProojIntBx.add_widget(vl)
		ProojIntBx.add_widget(self.vt)
		ProojIntBx.add_widget(pnl)
		ProojIntBx.add_widget(self.pnt)
		ProojIntBx.add_widget(pkgl)
		ProojIntBx.add_widget(self.pkgt)

		FileBx=BoxLayout() #add file search and list permission
		FileBx.size_hint = (1, 0.95)
		self.prj_path=FileChooserListView(path=self.prj_load_path)
		self.prj_path.size_hint = (1, 1)
		FileBx.add_widget(self.prj_path)


		ActionOptBx = GridLayout(cols=4) #debug install ....
		ActionOptBx.padding=10
		ActionOptBx.spacing=10
		ActionOptBx.size_hint = (1, 0.1)
		DebugBox=BoxLayout()
		DebugBox.add_widget(Label(text='Debug'))
		self.chkDebug=CheckBox()
		DebugBox.add_widget(self.chkDebug)
		DebugBox.add_widget(Label(text='Release'))
		self.chkRelease=CheckBox()
		DebugBox.add_widget(self.chkRelease)
		ActionOptBx.add_widget(DebugBox)
		DxBox.add_widget(ProojIntBx)
		DxBox.add_widget(FileBx)
		DxBox.add_widget(ActionOptBx)

		#dxbox -> second in up box
		PermissionBx=BoxLayout(orientation='vertical') #treeviw pwrmission
		PermissionBx.padding=5
		PermissionBx.spacing=5
		PermissionBx.pos=(10, 0)

		#~ PermissionBx.size_hint = (1, 1)
		layouttv = GridLayout(cols=1, spacing=5, size_hint_y=None,pos=(0,10))
		layouttv.bind(minimum_height=layouttv.setter('height'))
		for x in self.obj_builder.permissions_list:
			btn = ToggleButton(text=x, size_hint_y=None, height=40)
			btn.bind(state=self.add_remove_permission)
			layouttv.add_widget(btn)

		root = ScrollView(size_hint=(None, None), size=(400, 500))
		root.size_hint = (1, .9)

		root.add_widget(layouttv)
		PermissionBx.add_widget(root)

		#reder all
		UpBx.add_widget(DxBox)
		UpBx.add_widget(PermissionBx)

		#add all in tab item
		tab.add_widget(self.MainBx)

	def install_prj(self,instance):
		popup=None
		if self.chkDebug.active:
			self.apktype='debug'
		elif self.chkRelease.active:
			self.apktype='release'
		cmd='%s/adb install bin/%s-%s-%s.apk' % (self.sett_obj.path_adb,self.pnt.text,self.vt.text,self.apktype)
		print cmd
		p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,cwd=self.builder_path)
		for line in p.stdout.readlines():
			if 'Failure' in line:
				popup=self.get_popup('Py4A Gui Installer','Installation \n'+line)
				popup.open()
			elif 'Success' in line:
				popup=self.get_popup('Py4A Gui Installer','Installation \n'+line)
				popup.open()
		instance.text='Install'


	def start_install(self,instance):
		instance.text='Installing.....'

	def prog_install(self,dt):
		self.pb.value += dt

	def get_popup(self,title,text,progr=False):
		btnclose = Button(text='Ok', size_hint_y=None, height='50sp')

		content = BoxLayout(orientation='vertical')
		content.add_widget(Label(text=text))
		self.pb = ProgressBar(max=1000)
		content.add_widget(self.pb )
		content.add_widget(btnclose)
		popup = Popup(content=content, title=title,
					  size_hint=(None, None), size=('300dp', '300dp'))
		btnclose.bind(on_release=popup.dismiss)
		if progr:
			popup.bind(on_open=self.start_install)
		return popup

	def start_build(self,instance):
		os.environ['ANDROIDSDK'] ='%s' % (self.sett_obj.path_sdk)
		args='--name %s ' % self.pnt.text
		args+='--package %s.%s ' % (self.pkgt.text,self.pnt.text)
		args+='--version %s ' % self.vt.text
		args+='--dir %s ' % self.prj_path.path
		if len(self.list_permission_to_build)>0:
			for p in self.list_permission_to_build:
				args+='--permission %s ' % p
		if self.chkDebug.active:
			self.apktype='debug'
			args+='debug'
		elif self.chkRelease.active:
			self.apktype='release'
			args+='release'
		cmd4='%s/./build.py %s' % (self.builder_path,args)
		print cmd4
		cmd="gnome-terminal --working-directory=%s --title='Build Py4 %s' --command='%s' " % (self.builder_path,self.pnt.text,cmd4)
		p = subprocess.Popen(cmd,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.STDOUT,env=os.environ,cwd=self.builder_path)

	def add_remove_permission(self,instance,value):
		if value=='down':
			if instance.text not in self.list_permission_to_build:
				self.list_permission_to_build.append(instance.text)
		else:
			for i in range(len(self.list_permission_to_build)-1):
				if self.list_permission_to_build[i]==instance.text:
					self.list_permission_to_build.pop(i)

	def render_distribuite(self,tab):
		Blayout=BoxLayout(orientation='vertical')
		btnDistr=Button(text='Start Distribuite',size_hint=(1, .1))
		btnDistr.bind(on_press=self.start_dist)
		layout = GridLayout(cols=4)
		thedir=os.path.join(self.py4a_path,'recipes')
		recipes=[ name for name in os.listdir(thedir) if os.path.isdir(os.path.join(thedir, name)) ]
		for r in recipes:
			t=ToggleButton(text=r)
			t.bind(state=self.add_remove)
			layout.add_widget(t)
		Blayout.add_widget(btnDistr)
		Blayout.add_widget(layout)
		tab.add_widget(Blayout)

	def start_dist(self,instance):
		self.sett_obj.distribuite(' '.join(self.list_module_to_dist))
		instance.text='Distribuited'

	def add_remove(self,instance,value):
		if value=='down':
			if instance.text not in self.list_module_to_dist:
				self.list_module_to_dist.append(instance.text)
		else:
			for i in range(len(self.list_module_to_dist)-1):
				if self.list_module_to_dist[i]==instance.text:
					self.list_module_to_dist.pop(i)

	def startLogcat(self):
		self.device_is_connected=False
		self.LogCat.alive=True
		self.LogCat.start()
		self.rstLogcat.text=''
		Clock.schedule_interval(self.load_logcat, 1/30.)

	def stopLogcat(self):
		self.LogCat.alive=False
		self.LogCat=None
		Clock.unschedule(self.load_logcat)
		self.device_is_connected=False

	def refresh_log(self):
		self.rstLogcat.text+=self.line


	def load_logcat(self, dt):
		self.rstLogcat.text+=self.line


class Py4AGui(Screen):
	def __init__(self, **kwargs):
		super(Screen, self).__init__(**kwargs)
		self.tb = TabTools()
		self.setting_obj=None
		self.add_widget(self.tb)
		self.devices=[]


	def check_devices(self):
		df=False
		self.devices=[]
		cmd='%s/adb devices' % self.path_adb
		p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		for line in p.stdout.readlines():
			if 'List of devices attached' in line:
				df=True
			elif df:
				self.devices.append(line)
		self.lbldevice.text="no device found"
		if len(self.devices)>0 and 'device' in self.devices[0] :
			self.lbldevice.text='Device id 0 Found: %s' %self.devices[0].split('\t')[0]
			Clock.unschedule(self.test_device)


	def test_device(self, dt):
		self.lbldevice.text="search device...."
		self.check_devices()

	def addSettPage(self,setting):
		self.setting_obj=setting
		self.tb.init()
		self.path_adb=self.setting_obj.path_adb
		self.tb.adbpath=self.path_adb
		self.tb.py4a_path=self.setting_obj.py4a_path
		self.tb.sett_obj=self.setting_obj
		self.tb.setup()
		self.check_devices()
		Clock.schedule_interval(self.test_device, 10)

class Py4AGuiSettings(Screen):
	def __init__(self, **kwargs):
		super(Screen, self).__init__(**kwargs)
		self.path_sdk=''
		self.path_ndk=''
		self.ndkver=''
		self.apiver=''
		self.path_adb=os.path.join(self.path_sdk,'platform-tools')
		self.py4a_path=''

		self.prj_path=''
		self.prj_name=''
		self.prj_package=''
		self.prj_version='1.0'
		self.prj_lst_perm='1.0'

		#~ self.lst_perm=lstp.list
		self.load_config()

	def load_config(self):
		listsett=[]
		cf=''
		with open('settings.txt') as stream:
			cf=stream.read()
		listsett=cf.split('\n')
		self.path_sdk=listsett[0]
		self.lblpathsdk.text=self.path_sdk
		self.path_ndk=listsett[1]
		self.lblpathndk.text=self.path_ndk
		self.ndkver=listsett[2]
		self.lblpathndkv.text=self.ndkver
		self.apiver=listsett[3]
		self.lblpathsdkv.text=self.apiver
		self.py4a_path=listsett[4]
		self.lblpathp4a.text=self.py4a_path
		self.path_adb=os.path.join(self.path_sdk,'platform-tools')
		#~ self.export_path_distrib('numpy')

	def distribuite(self,module):
		 # Make a copy of the current environment
		os.environ['ANDROIDSDK'] ='%s' % (self.path_sdk)
		os.environ['ANDROIDNDK'] ='%s' % (self.path_ndk)
		os.environ['ANDROIDNDKVER'] ='%s' % (self.ndkver)
		os.environ['ANDROIDAPI'] ='%s' % (self.apiver)
		#~  Search librrfaker.so for add to preload env path
		cmd_pd='locate librrfaker.so'
		p = subprocess.Popen(cmd_pd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		preload_path=''
		for line in p.stdout.readlines():
			if 'ERROR' not in line:
				preload_path=line
		os.environ['LD_PRELOAD'] ='%s' % preload_path.split('\n')[0]
		d = dict(os.environ.copy())
		cmd4='%s/./distribute.sh -m "%s"' % (self.py4a_path,module)
		cmd="gnome-terminal --working-directory=%s --title='Distribuie Py4a modules %s' --command='%s' " % (self.py4a_path,module,cmd4)
		p = subprocess.Popen(cmd, shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.STDOUT,env=os.environ,cwd=self.py4a_path,close_fds=True)
		#~TODO Controll the acrive process!!



class Py4AGuiApp(App):

	def build(self):
		sm = ScreenManager()
		sc=Py4AGuiSettings(name='settings')
		sp4a=Py4AGui(name='tool')
		sp4a.addSettPage(sc)
		sm.add_widget(sp4a)
		sm.add_widget(sc)
		Clock.max_iteration = 100
		return sm


if __name__ == '__main__':
	Py4AGuiApp().run()
