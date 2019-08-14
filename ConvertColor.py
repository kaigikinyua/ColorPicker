class Convert:
	def rgbTOhex(self,rgb):
		print("Convert RGB to Hex")
	def hexTOrgb(self,hexV):
		print("Convert HEX to RGB")
	def confirmHex(self,hexV):
		lenHex=len(hexV)
		startHex=hexV[0]
		hexV=hexV.upper()
		if(lenHex==7 and startHex=='#'):
			hexComp=['#','A','B','C','D','E','F','0','1','2','3','4','5','6','7','8','9']
			for c in hexV:
				for h in hexComp:
					if c==h:
						if(c==hexV[len(hexV)-1]):
							return True
						break
					else:
						if(h==hexComp[len(hexComp)-1]):
							return False
		else:
			return False
		return True


