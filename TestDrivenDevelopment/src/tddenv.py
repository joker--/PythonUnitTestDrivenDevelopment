""" This is a test driver framework example"""

import unittest
import tempfile
import shutil
import os
import glob

class TestDD(unittest.TestCase):
	
	def setUp(self):
		self.orgdir = os.getcwd()
		self.dirname = tempfile.mkdtemp("tempySurjit");
		print("Created Directory",self.dirname)
		os.chdir(self.dirname)

	def test_1(self):
		'''Verify if creation of file is possible'''
		
		for filename in ["index.html","LICENSE","README"]:
			f = open(filename,"wb+")
			f.write("Somedata\n")
			f.close()
			self.assertTrue(f.closed)

	def test_emptydir(self):
		''' If current directory is empty'''
		self.assertEqual(glob.glob("*"),[],"Directory is not empty")

	def tearDown(self):
		os.chdir(self.orgdir)
		shutil.rmtree(self.dirname)
		print("Cleaned up created directories")

if __name__ == "__main__":
	unittest.main()
