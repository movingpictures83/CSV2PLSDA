
import PyPluMA


import sys

def quote(s):
    return '\"' + s + '\"'

def unquote(s):
    return s[1:len(s)-1]

class CSV2PLSDAPlugin:
   def input(self, filename):
      # Parameter file
      self.parameters = dict()
      paramfile = open(filename, 'r')
      for line in paramfile:
         contents = line.split('\t')
         self.parameters[contents[0]] = contents[1].strip()
      normabund = open(PyPluMA.prefix()+"/"+self.parameters["normabund"], "r")
      metadata = open(PyPluMA.prefix()+"/"+self.parameters["metadata"], "r")

      metadata.readline()
      self.categories = dict()
      # Assuming two-column
      self.diffcat = set()
      for line in metadata:
         line = line.strip()
         contents = line.split(',')
         self.categories[contents[0]] = contents[1]
         self.diffcat.add(contents[1])


      microbes = normabund.readline().strip()
      self.contents = microbes.split(',')
      self.contents = self.contents[1:]
      self.lines = []
      for line in normabund:
          self.lines.append(line.strip())

   def run(self):
       pass

   def output(self, filename):
      obs_names = open(filename+"/"+self.parameters["categories"], 'w') # Categories, tabbed
      var_ID = open(filename+"/"+self.parameters["observables"], 'w') # Microbes, one column
      testsets = open(filename+"/"+self.parameters["targets"], 'w') # Different categories
      normabundmod = open(filename+"/"+self.parameters["samples"], 'w')

      present = {}
      for microbe in self.contents:
          if (microbe not in present):
              present[microbe] = 1
          else:
              present[microbe] += 1
              microbe = quote(unquote(microbe) + "_" + str(present[microbe]))
          var_ID.write(microbe+"\n")

      for entry in self.diffcat:
         testsets.write(entry+"\n")

      for j in range(0, len(self.lines)):
          contents = self.lines[j].split(',')
          sample = contents[0]
          contents = contents[1:]
          obs_names.write(self.categories[sample])
          if (j != len(self.lines)-1):
             obs_names.write('\t')

      # Transpose
      my_mat = []
      for i in range(0, len(self.lines)):
          my_mat.append(self.lines[i].strip().split(','))
      
      for j in range(1, len(my_mat[0])):
         for i in range(0, len(my_mat)):
             normabundmod.write(my_mat[i][j])
             if (i != len(my_mat)-1):
                 normabundmod.write(',')
             else:
                 normabundmod.write('\n')
#abundmat = []


#meta = []

