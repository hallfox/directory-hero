import os
import re
import kivy

from kivy.uix.scrollview import ScrollView
from kivy.uix.treeview import TreeView, TreeViewNode
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

from kivy.config import Config
from kivy.app import App

kivy.require('1.8.0')

#NEVER EVER TOUCH THESE
map_regs = {"Dir":"^[^.]+$", "File":"^.+\..+$", "Hidden":"^\..+$"}
MAPS = ["Tutorial", "Rot13"]
MAP_IDX = -1
PASSWORDS = {"Tutorial":"1337", "Rot13":"tang"}

class Dir(Label, TreeViewNode):
	def __init__(self, name):
		super().__init__(size_hint_y=None, height=45, text=name)
		self.name = name
	def __str__(self):
		return self.text

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
			Popup(title="", 
			content=Label(text=self.data), 
			size_hint=(.5,.5)).open()
		else:
			Popup(title="", 
			content=Label(text="INCORRECT PASSWORD"), 
			size_hint=(.5,.5)).open()
		
class GameView(BoxLayout):
	def load_map(self):
		global MAP_IDX, MAPS

		if len(self.ids['tree'].root.nodes) > 0:
			self.clear_tree()

		#THE ONLY PLACE MAP_IDX SHOULD CHANGE
		#NEVER EVER CHANGE THIS LINE
		MAP_IDX += 1
		if MAP_IDX < len(MAPS):
			self.map = MAPS[MAP_IDX]
		else:
			return
		
		self._recurse("maps"+os.sep+self.map, None)
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
		if t_input.strip() == PASSWORDS[self.map]:
			Popup(title="Riddle Me Yes", content=Label(text="Correct!"), size_hint=(.5,.5), on_dismiss=self.load_map()).open()
			self.ids['input'].select_all()
			self.ids['input'].delete_selection()
		else:
			Popup(title="Riddle Me No", content=Label(text="Incorrect."), size_hint=(.5,.5)).open()
	def clear_tree(self):
		#lolwut
		nodes = self.ids['tree'].root.nodes
		while len(nodes) > 0:
			self.ids['tree'].remove_node(nodes[0])
		
class DirectoryHeroApp(App):
	def build(self):
		self.title = "Directory Hero"
		Config.set("graphics", "width", 200)
		Config.set("graphics", "height", 600)
		
		os.chdir(os.path.dirname(os.path.realpath(__file__)))
		
		game = GameView()
		
		# create the directory tree
		tree = game.ids['tree']
		tree.bind(minimum_height=tree.setter('height'))
		game.load_map()
		
		return game
	
		
if __name__ == "__main__":
	DirectoryHeroApp().run()