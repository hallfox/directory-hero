"""Map properties:
id - string:"#.#.#..."
name - string:will be visible to player
children - list:contains children
type - string?:contains information about whether it's a file or a dir"""

_tutorial = {'id':'1',
			'name':'Open me.',
			'type':'dir',
			'children':[{'id': '1.1',
						'name':'A directory.',
						'type':'dir',
						'children':[{'id':'1.1.1',
									'name':'Nothing here.',
									'type':'file',
									'content':"nothing",
									'children':[]},
									{'id':'1.1.2',
									'name':'Look at me!',
									'type':'file',
									'content':"look",
									'children':[]},
									{'id':'1.1.3',
									'name':"You can't see me",
									'type':'hidden',
									'children':[]}]},
						{'id': '1.2',
						'name':'I\'m and empty directory',
						'type':'dir',
						'children':[]},
						{'id': '1.3',
						'name':"I'm a file.",
						'type':'file',
						'content':'magic',
						'children':[]}]}
						
Maps = {'Tutorial':_tutorial}