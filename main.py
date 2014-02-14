from kivy.uix.scrollview import ScrollView
from kivy.uix.treeview import TreeView, TreeViewNode, TreeViewLabel

from kivy.config import Config

from kivy.app import App

class DirectoryHeroApp(App):
	def build(self):
		self.title = "Directory Hero"
		
		#create the directory tree
		tree = TreeView()
		tree.bind(minimum_height=tree.setter('height'))
		
		#add some test nodes to the tree
		tree.add_node(TreeViewLabel(text="Folder 1"))
		tree.add_node(TreeViewLabel(text="Folder2"))		
		
		view = ScrollView()
		view.add_widget(tree)
		
		return view		

if __name__ == "__main__":
	DirectoryHeroApp().run()