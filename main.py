from kivy.uix.scrollview import ScrollView
from kivy.uix.treeview import TreeView, TreeViewNode, TreeViewLabel
from kivy.uix.button import Button

from kivy.config import Config

from kivy.app import App

from maps import MapManager

def populate_tree_view(tree_view, parent, node):
    if parent is None:
        tree_node = tree_view.add_node(TreeViewLabel(text=node['node_id'],
                                                     is_open=True))
    else:
        tree_node = tree_view.add_node(TreeViewLabel(text=node['node_id'],
                                                     is_open=True), parent)

    for child_node in node['children']:
        populate_tree_view(tree_view, tree_node, child_node)


class Folder(TreeView, TreeViewNode):
	pass
	
class File(Button, TreeViewNode):
	pass

class DirectoryHeroApp(App):
	def build(self):
		self.title = "Directory Hero"
		
		#create the directory tree
		tree = TreeView()
		tree.bind(minimum_height=tree.setter('height'))
		
		populate_tree_view(tree, None, MapManager.Tutorial)	
		
		view = ScrollView()
		view.add_widget(tree)
		
		return view		

if __name__ == "__main__":
	DirectoryHeroApp().run()