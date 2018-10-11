from . import OperatorEnum
class ContinuousQuery:
	"""
	Data object that encapsulates a continuous query, holding info on the column, operator, and value'
	"""
	def __init__(self, columnName:str, operator:OperatorEnum, value:float):
		"""
		:type columnName: string
		:param columnName: name of the column to be examined

		:type operator: OperatorEnum
		:param operator: representation of comparison operator such as ==, <, >=, etc.

		:type value: float
		:param value: the value that the examined column will be compared to

		"""
		self.columnName = columnName
		self.operator = operator
		self.value = value
