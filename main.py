from kivy.uix.scrollview import ScrollView
from kivy.uix.treeview import TreeView, TreeViewNode
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label

from kivy.config import Config
from kivy.app import App

import os

class Dir(Label, TreeViewNode):
	def __init__(self, name):
		super().__init__(size_hint_y=None, height=40, text=name)
		self.name = name
	
class File(Button, TreeViewNode):
	def __init__(self, name, data=""):
		super().__init__(size_hint_y=None, height=40, text=name)
		self.name = name
		self.data = data
	
	def on_release(self):
		popup = Popup(title=self.name,
						content=Label(text=self.data),
						size_hint=(.5,.5))
		popup.open()
		
class DirectoryHeroApp(App):
	def build(self):
		self.title = "Directory Hero"
		
		# create the directory tree
		tree = TreeView()
		tree.bind(minimum_height=tree.setter('height'))
		
		d = Dir("dir")
		
		tree.add_node(d)
		tree.add_node(File("file", "hello"), d)
		tree.add_node(Dir("dir"))		
		
		view = ScrollView(do_scroll_x=False)
		view.add_widget(tree)
		
		return tree	
		
	def populate_tree_view(tree_view, parent, node):
		pass

if __name__ == "__main__":
	DirectoryHeroApp().run()