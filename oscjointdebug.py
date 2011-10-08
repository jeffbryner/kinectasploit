#! /usr/bin/env python

# python-osc
# Copyright (C) 2010 Ryan Coyner
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.

"""A synchronous UDP server that dispatches Open Sound Control messages."""

import oscd

global headz
global torsoz

class PrintMethod(oscd.Method):
	def __call__(self, address, typetags, data):
		global headz
		global torsoz	
		#print(('Address: %s' % address))
		#print(('Typetags: %s' % typetags))
		#print(('Data: %s' % data))
#		if data[0]=='head':
#			#print(('Head: %s' % data[4]))
#			headz=data[4]
		
#		if data[0]=='l_hand':

		print('%s: %s' % (data[0],data))
#			torsoz=data[4]
#		if (headz/torsoz !=1):
#			print('ratio %f' % (headz/torsoz) )

#		print(data)
	


if __name__ == '__main__':
	HOST = 'localhost'
	PORT = 7110
	server = oscd.Server((HOST, PORT))

	headz=1
	torsoz=1

	server.add_method(PrintMethod('/joint'))
	server.serve_forever()
