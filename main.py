from kivy.uix.scrollview import ScrollView
from kivy.uix.treeview import TreeView, TreeViewNode
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

from kivy.config import Config
from kivy.app import App

import os
import re

map_regs = {"Dir":"^[^.]+$", "File":"^.+\..+$", "Hidden":"^\..+$"}

class Dir(Label, TreeViewNode):
	def __init__(self, name):
		super().__init__(size_hint_y=None, height=45, text=name)
		self.name = name

class File(Button, TreeViewNode):
	def __init__(self, name, data=""):
		super().__init__(size_hint_y=None, height=45, text=name)
		self.name = name
		self.data = data
	
	def on_release(self):
		popup = Popup(title=self.name,
						content=Label(text=self.data),
						size_hint=(.5,.5))
		popup.open()

class Hidden(GridLayout, TreeViewNode):
	def __init__(self, password, data):
		super().__init__(cols=2, rows=1, size_hint_y=None, height=45)
		self.password = password
		self.data = data
	def check(self):
		#print(self.password)
		if self.ids['password'].text == self.password:
			Popup(title="HIDDEN", 
			content=Label(text=self.data), 
			size_hint=(.5,.5)).open()
		else:
			Popup(title="HIDDEN", 
			content=Label(text="PERMISSION DENIED"), 
			size_hint=(.5,.5)).open()
		
class GameView(BoxLayout):
	def load_map(self, map):
		self.map = map
		self._recurse("maps"+os.sep+map, None)
	def _recurse(self, path, parent):	
		for item in os.listdir(path):
			node = self.build_item(item, path)
			self.ids['tree'].add_node(node, parent)
			if isinstance(node, Dir):
				self._recurse(path+os.sep+item, node)
	def build_item(self, item, path):
		#build a Dir object
		if re.match(map_regs["Dir"], item):
			node = Dir(item)
		#build a File object
		elif re.match(map_regs["File"], item):
			with open(path+os.sep+item) as f:
				data = f.read()
			node = File(item, data)
		#build a Hidden object
		elif re.match(map_regs["Hidden"], item):
			with open(path+os.sep+item) as f:
				data = f.read()
			node = Hidden(item[1:], data)
		else:
			raise NameError(item)
		return node
	def check(self):
		t_input = self.ids['input'].text
		print(t_input)
		if t_input.strip() == '6':
			Popup(content=Label(text="Correct!"), size_hint=(.5,.5)).open()
		else:
			Popup(content=Label(text="Incorrect."), size_hint=(.5,.5)).open()
		
class DirectoryHeroApp(App):
	def build(self):
		self.title = "Directory Hero"
		
		os.chdir(os.path.dirname(os.path.realpath(__file__)))
		
		game = GameView()
		
		# create the directory tree
		tree = game.ids['tree']
		tree.bind(minimum_height=tree.setter('height'))
		game.load_map("Tutorial")
		
		return game
	
		
if __name__ == "__main__":
	DirectoryHeroApp().run()