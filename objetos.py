class Path:
	def __init__(self, id_, option_):
		self.id = id_ # int, id del nodo a donde vamos
		self.option = option_ # str, que opcion es el path

class Nodo:
	def __init__(self, msg_entrada_, next_):
		self.msg_entreda = msg_entrada_
		self.next = next_ # lista de paths
