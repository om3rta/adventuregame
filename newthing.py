

# LIST
sample_ls = ['oine', 'twp', 'the']

# TUPLE
sample_tp = ()

# DICTIONARY
sample_dc = {
	"one": "apple", "two": "banana", "three": "big booty",
	"four": {
		"uno": "ringo", "dos": "sacapuntas", "tres": "el steamer del cleavland"
	}
}


#print sample_dc["one"]
#print sample_dc["four"]["dos"]

for entry in sample_dc:
	if entry == "four":
		newvar = sample_dc["four"]
		for key in newvar:
			print newvar[key]
