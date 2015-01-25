'''
This is a code sample made by Clinton Bowen.


Description:
Given a file of words, find all pairs of permutations of words.

e.g.
[dictionary.txt]
cab
team
door
meat
bac

[python PermutationAnalsis.py dictionary]
[cab,bac]
[team,meat]
[door]
'''
import sys
import os
import os.path
class PermutationAnalysis(object):
	'''
	Finds all pairs of permutations of words from a file.


	e.g.
	permutationAnalyzer = PermutationAnalysis('/the/path/to/dictionary.txt')
	permutationAnalyzer.DisplayPermutations()
	
	remarks:
		1) this is a case sensitive, i.e. 'cab' and 'CaB' are treated differently. 
	'''
	def __init__(self,filePathName):
		'''
		1)  check if filePathName path exists and accessible
		2)  if filePathName exists, read the file, throw all permutation pairs into a corresponding dictionary.
		'''
		if not os.path.isfile(filePathName):
			raise Exception("%s is not a file path!"%(filePathName))
		if not os.access(filePathName, os.R_OK):
			raise Exception("%s is not readable!"%(filePathName))
		self.filePointer = open(filePathName,'r')
		self.permutationDictionary = self.CreatePermutationDictionary()
	def CreatePermutationDictionary(self):
		'''
		This method creates a dictionary of permutations from a text file.
		'''
		wordDictionary = dict()
		try:
			for line in self.filePointer:
				'''
				1) strip white space per line and obtain list of words in line
				2.a) wordDictionary key is line.sort()
				2.b) wordDictionary value is a list of the lines whose line.sort() is the key
				'''
				listOfWordsInLine = line.split()
				for word in listOfWordsInLine:
					key = ''.join(sorted(word))
					if key in wordDictionary.keys():
						wordDictionary[key].append(word)
					else:
						wordDictionary[key] = [word]
		finally:
			self.filePointer.close()
		return wordDictionary
	def DisplayPermutations(self):
		for v in self.permutationDictionary.itervalues():
			print v


if __name__ == "__main__":
	if len(sys.argv) > 1:
		for i in range(len(sys.argv)):
			if i > 0:
				permutationAnalyzer = PermutationAnalysis(sys.argv[i])
				permutationAnalyzer.DisplayPermutations()
	else:
		print "USAGE:  python PermutationAnalsis.py /the/path/to/dictionary1.txt [/the/path/to/dictionary2.txt [.....]]"