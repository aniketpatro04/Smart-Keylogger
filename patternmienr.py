#Using Simple RAKE Algorithm in Pyton


import RAKE
import operator

stop_dir = "Stoplist.txt"
rake_object = RAKE.Rake("Stoplist.txt")

#Sort Extracted Key Phrases and scores
def SortTuple(tup):
    
    tup.sort(key = lambda x : x[1])
    return tup

#Instead of the Sample text, we will pass the contents of the log.txt file and find out the highest occuring phrases and keywords.
sample_text = "Sociable on as carriage my position weddings raillery consider. Peculiar trifling absolute and wandered vicinity property yet. The and collecting motionless difficulty son. His hearing staying ten colonel met. Sex drew six easy four dear cold deny. Moderate children at of outweigh it. Unsatiable it considered invitation he travelling insensible. Consulted admitting oh mr up as described acuteness propriety moonlight.Whether article spirits new her covered hastily sitting her. Money witty books nor son add. Chicken age had evening believe but proceed pretend mrs. At missed advice my it no sister. Miss told ham dull knew see she spot near can. Spirit her entire her called.Unpacked now declared put you confined daughter improved. Celebrated imprudence few interested especially reasonable off one. Wonder bed elinor family secure met. It want gave west into high no in. Depend repair met before man admire see and. An he observe be it covered delight hastily message. Margaret no ladyship endeavor ye to settling.Old unsatiable our now but considered travelling impression. In excuse hardly summer in basket misery. By rent an part need. At wrong of of water those linen. Needed oppose seemed how all. Very mrs shed shew gave you. Oh shutters do removing reserved wandered an. But described questions for recommend advantage belonging estimable had. Pianoforte reasonable as so am inhabiting. Chatty design remark and his abroad figure but its.Ye to misery wisdom plenty polite to as. Prepared interest proposal it he exercise. My wishing an in attempt ferrars. Visited eat you why service looking engaged. At place no walls hopes rooms fully in. Roof hope shy tore leaf joy paid boy. Noisier out brought entered detract because sitting sir. Fat put occasion rendered off humanity has."

keywords = SortTuple(rake_object.run(sample_text))[-10:]
keywords1 = SortTuple(rake_object.run(sample_text))
print('keywords : ',keywords)
print("keywords Set 1: ", keywords1)
# print(type(keywords[1])) #List of Tuples

