from kivy.uix.scrollview import ScrollView
from kivy.uix.treeview import TreeView, TreeViewNode
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

from kivy.config import Config
from kivy.app import App

import os
import re

map_regs = {"Dir":"^[^.]+$", "File":"^.*\..+$"}

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
		
class GameView(BoxLayout):
	def load_map(self, map):
		self._recurse("maps"+os.sep+map, None)
	def _recurse(self, path, parent):	
		for item in os.listdir(path):
			node = self.build_item(item, path)
			self.ids['tree'].add_node(node, parent)
			if isinstance(node, Dir):
				self._recurse(path+os.sep+item, node)
	def build_item(self, item, path):
		if re.match(map_regs["Dir"], item):
			node = Dir(item)
		elif re.match(map_regs["File"], item):
			with open(path+os.sep+item) as f:
				data = f.read()
			node = File(item, data)
		else:
			raise NameError(item)
		return node
		
class DirectoryHeroApp(App):
	def build(self):
		self.title = "Directory Hero"
		
		#not sure how to deal with a generic location yet
		os.chdir("C:\\Users\\Taylor\\repos\\directory-hero")
		
		game = GameView()
		
		# create the directory tree
		tree = game.ids['tree']
		tree.bind(minimum_height=tree.setter('height'))
		game.load_map("Tutorial")
		
		return game
	
		
if __name__ == "__main__":
	DirectoryHeroApp().run()