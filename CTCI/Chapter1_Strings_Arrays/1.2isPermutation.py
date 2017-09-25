def isPermu(a,b):
	if len(a)!=len(b):
		return False
	else:
		if len(a)==len(b):
			if list((set(a)-set(b))) ==[]:
				return True
