import copy
list_ = [['lmao','hehehe','idk','something'],['eweq','wewqe','ewqeqr']]
something = copy.copy(list_)
somethingelse = copy.deepcopy(list_)
something[0][2] = 'kekw'
somethingelse[0][3] = 'ionno'
print(list_)
print(something)
print(somethingelse)