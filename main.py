from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout

from kivy.app import App

class DirectoryHeroApp(App):
	def build(self):
		self.title = "Directory Hero"
		
		layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
		layout.bind(minimum_height=layout.setter('height'))
		for i in range(10):
			btn = Button(text=str(i), size_hint_y=None, height=40)
			layout.add_widget(btn)
		view = ScrollView(size_hint_y=None, height=400)
		view.add_widget(layout)
		
		return view
		
if __name__ == "__main__":
	DirectoryHeroApp().run()