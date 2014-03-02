from kivy.uix.scrollview import ScrollView
from kivy.uix.treeview import TreeView, TreeViewNode, TreeViewLabel
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label

from kivy.config import Config

from kivy.app import App

from maps import Maps

from collections import OrderedDict

class Dir(Label, TreeViewNode):
	pass
	
class File(Button, TreeViewNode):
	def display_file(self):
		popup = Popup(title=self.text,
						content=Label(text=self.data),
						size_hint=(.5,.5))
		popup.open()
	
class Tutorial(TreeView):
	pass
	
class DirectoryHeroApp(App):
	def build(self):
		self.title = "Directory Hero"
		
		#create the directory tree
		tree = Tutorial()
		tree.bind(minimum_height=tree.setter('height'))
		
		ids = OrderedDict(sorted(tree.ids.items(), key=lambda t: t[0]))
		
		for key,node in ids.items():
			tree.add_node(node, node.parent)
		
		view = ScrollView(do_scroll_x=False)
		view.add_widget(tree)
		
		return tree	

if __name__ == "__main__":
	DirectoryHeroApp().run()