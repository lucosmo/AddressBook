import datetime

#global variable storing the next available id number for address card
last_id = 1

class Address:
	"""Represents single address card in the address book"""
	
	def __init__(self, fname, phoneNo, lname="", addressNo=0, addressStr="", 
	addressPost="", addressCity="", tag=""):
		"""Initializes an address card. Arguments:
				fname -- first name
				lname -- last name, default ""
				addressNo -- number of the building, default 0
				addressStr -- street name, default ""
				addressPost -- postcode, default ""
				addressCity -- city/town/village name, default ""
				phoneNo -- phone number (string)
				tag -- optional tag or mix of tags (SCHOOL,WORK,FRIEND,FAMILY)
			Address object contains also:
				id -- unique id number
				createDate -- date of creation of address card""" 
		
		self.fname = fname
		self.lname = lname
		self.addressNo = addressNo
		self.addressStr = addressStr
		self.addressPost = addressPost
		self.addressCity = addressCity
		self.phoneNo = phoneNo
		self.tag = tag
		self.createDate = datetime.date.today()
		global last_id
		self.id = last_id
		last_id += 1
	
	def __getAttr(self):
		return [x for x in dir(self) if not (x.startswith("__") or x.startswith("_"))]
	def _match(self,filter):
		"""Matches address card against filter
				filter -- list of searched words/numbers e.g filter=["111"], filter=["Adam"], filter=["Adam","SCHOOL"]
				returns False/True"""
		matched_list = []
		for x in filter:
			matched = False
			for y in self.__getAttr():
				if str(x)==str(getattr(self,str(y))):
					matched = True
			matched_list.append(matched)
			
		return all(matched_list)
		
