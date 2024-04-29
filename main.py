#quickstart

x = []
y = [x, [x], dict(x=x)]
import objgraph

objgraph.show_refs([y], filename='sample-graph.png')

print('----------')

#backrefences

objgraph.show_backrefs([x], filename='sample-backref-graph.png')

print('----------')

#memory leak examples

#first try

objgraph.show_most_common_types()

print('---')


#second try

class MyBigFatObject(object):
	pass

def computate_sth(_cache={}):
	_cache[42] = dict(foo=MyBigFatObject(),
			  bar=MyBigFatObject())
	x = MyBigFatObject()

objgraph.show_growth(limit=3)
computate_sth()
objgraph.show_growth()

print('---')

#using random

import random
objgraph.show_chain(
	objgraph.find_backref_chain(
		random.choice(objgraph.by_type('MyBigFatObject')),
		objgraph.is_proper_module),
	filename='chain.png') 


print('----------')

#reference counting bugs

roots = objgraph.get_leaking_objects()

len(roots)

print('---')

objgraph.show_most_common_types(objects=roots)

print('---')

objgraph.show_refs(roots[:3], refcounts=True, filename='roots.png')
