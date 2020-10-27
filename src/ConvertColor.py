import re
class Convert:
	@staticmethod
	def rgbTOhex(rgb):
		print("Convert RGB to Hex")

	@staticmethod
	def hexTOrgb(hexV):
		print("Convert HEX to RGB")

	@staticmethod
	def confirmHex(hexV):
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

	@staticmethod
	def color_to_hex(color):
		if(Color.color_check(color)):
			div=int(color)/16
			rem=int(color)%16
			return div+rem

	@staticmethod
	def hex_to_rgb(color):
		if(Color.hex_check(color)):
			red=Color.single_hex_to_rgb(color[1:3])
			green=Color.single_hex_to_rgb(color[3:5])
			blue=Color.single_hex_to_rgb(color[5:7])
			color={"red":red,"green":green,"blue":blue}
			return color
		return False

class Color:
	@staticmethod
	def color_check(color):
		if(int(color)>-1 and int(color)<256):
			return True
		return False

	@staticmethod
	def hex_check(color):
		x=re.search("^#[A-Fa-f0-9]",color)
		if(X!=None):
			return True
		return False

	@staticmethod
	def single_hex_to_rgb(hex):
		tenths=Color.decimal_equivalent(hex[0])
		ones=Color.decimal_equivalent(hex[1])
		value=(tenths*16)+ones

	@staticmethod
	def decimal_equivalent(hex):
		try:
			hex=int(hex)
			return hex
		except:
			hex_codes={"a":10,"b":11,"c":12,"d":13,"e":14,"f":15}
			for code in hex_codes:
				if(lower(hex)==code):
					return hex_codes[hex]
		return False


