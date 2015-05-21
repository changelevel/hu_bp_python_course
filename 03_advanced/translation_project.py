import random
import sys
import types

class BioMolecule(object):
    """
    A generic molecule that has basic attributes like id, name and
    mass.

    @type id: int
    @type name: str
    @type mass: float
    """
    def __init__(self,id, name, mass=0.):
        #print 'in init', name
	#print type(name)
	#print 'wert'
	#print id
	#print type(id)
        self._id = id
        self.name = name
        self.mass = mass
        
    #def __repr__(self):
    #	return '_id = '+str(self._id)+'\nname = '+str(self.name)+'\nmass = '+str(self.mass)
    def __str__(self):
	answer =''
	#print answer
	k=vars(self).keys()
	#print k
	#print vars(self)
	for key in k:
		answer=answer+str(key)+' = '+str(vars(self)[key])+'\n'
	return answer

    # 1. Write setter and getter methods for all attributes.

    def __getattr__(self,name):
	if name in dir(self):
		return self.__dict__[name]
    #    Use @property decorators as dicussed in the lecture
    # 2. In the setter methods check for the type of each attribute.

    def __setattr__(self,name,value):
	if str(name) not in ['_id','mass','name']:
		#print 'in if'
		raise TypeError('Attribute "'+str(name)+'" does not exist.')
	else:
		#print 'in else'
		#print type(name)
		#print 'wert'
		#print value
		#print type(value)
		#print'instanz'
		#print isinstance(value, types.BuiltinFunctionType)
		#print isinstance(value, )
		if name=='_id' and isinstance(value, types.BuiltinFunctionType):
			self.__dict__[name] = value
		elif name =='name' and isinstance(value, str):
			self.__dict__[name] = value
		elif name =='mass' and isinstance(value, float):
			self.__dict__[name] = value
		else:
			raise TypeError('Type of value of '+str(name)+' does not match requirements.')

class Polymer(BioMolecule):
    """
    A polymer molecule that has a sequence attribute which is
    accessible via indexing the object. 

    @type id: int
    @type name: str
    @type sequence: str
    @type mass: float
    """
    def __init__(self, id, name, sequence, mass=0.):
        # 3. Initialize the parent class correctly
        super(Polymer,self).__init__(id,name,mass)
        self._sequence = sequence

    
    # 4. Write getter and setter for sequence, again check for type
	#def __getitem__(self,value):
	#	return self.sequence[value]
	#def __setitem__(self,name,value):
	#	self.sequence[name] = value
	#woops existiert ja bereits
	
    # 5. run in ipython, instantiate this class, and test it
    def __getitem__(self, value):
        """
        Makes the sequence accessible via the indexing operators:
<        p[10] returns the tenth character in the sequence.
        """
        return self._sequence[value]

    def __setitem__(self, key, value):
        """
         Enables changing of sequence characters via the indexing operators.       
        """
        self.sequence[key] = value
    def __setattr__(self,name,value):
	if str(name) not in ['_id','mass','name','_sequence']:
		raise TypeError('Attribute "'+str(name)+'" does not exist.')
	else:
		#print name
		#print type(name)
		#print 'wert'
		#print value
		#print type(value)
		#print'instanz'
		if name=='_id' and isinstance(value, types.BuiltinFunctionType):
			self.__dict__[name] = value
		elif name =='name' and isinstance(value, str):
			self.__dict__[name] = value
		elif name =='mass' and isinstance(value, float):
			self.__dict__[name] = value
		elif name=='_sequence' and isinstance(value, str):
			self.__dict__[name] = value.upper()
		else:
			raise TypeError('Type of value of '+str(name)+'  does not match requirements.')

    def __getattr__(self,name):
	if name in dir(self):
		return self.__dict__[name]

class MRNA(Polymer):
    def __init__(self, id, name, sequence, mass=0.):
        # 6. Initialize the parent class correctly
	super(MRNA,self).__init__(id,name,sequence,mass)

        # 7. Create a list that stores if a ribosome is bound for each
        # codon (triplet).
        
        #0 ungebunden, 1 gebunden
        self.binding = [0]*(len(sequence)/3) # use this attribute for 7.
        #print self.binding
	self.calculate_mass()
	
    def calculate_mass(self):
        NA_mass = {'A': 1.0, 'U': 2.2, 'G':2.1, 'C':1.3}
        for member in self._sequence:
		self.mass+= NA_mass[member]
		#print self.mass
        # 8. calculate the mass for the whole sequence
    
    
    #the usual stuff
    def __setattr__(self,name,value):
	if str(name) not in ['_id','mass','name','_sequence','binding']:
		raise TypeError('Attribute "'+str(name)+'" does not exist.')
	else:
		#print name
		#print type(name)
		#print 'wert'
		#print value
		#print type(value)
		#print'instanz'
		if name=='_id' and isinstance(value, types.BuiltinFunctionType):
			self.__dict__[name] = value
		elif name =='name' and isinstance(value, str):
			self.__dict__[name] = value
		elif name =='mass' and isinstance(value, float):
			self.__dict__[name] = value
		elif name=='_sequence' and isinstance(value, str):
			self.__dict__[name] = value.upper()
		elif name=='binding' and isinstance(value, list):
			self.__dict__[name] = value
		else:
			raise TypeError('Type of value of '+str(name)+' does not match requirements.')

class Protein(Polymer):
    """Protein with Polymer features and mass calculation. A global class
    attribute counts the number of proteins that have been instantiated.
    
    A protein can be elongated using the "+" operator:
    
    >> protein = Protein(1, "prot", "MVFT")
    >> protein + "A"
    >> protein.sequence
    MVFTA

    
    Basically just copied that, for it's nothing new and corrected a mistake in the code
    """
    number_of_proteins = 0  # init instance counter
    def __init__(self, id, name, sequence, mass=0.):
        super(Protein, self).__init__(id, name, sequence, mass)
        self.number_of_proteins += 1
	self.calculate_mass()

    def __add__(self, AS):
        self._sequence += AS._sequence 
        self.calculate_mass()

    def calculate_mass(self):
        AA_mass = {"A": 89.0929, "R": 175.208, "N": 132.118, "D": 132.094, "C": 121.158, "Q": 146.144,
                    "E": 146.121, "G": 75.0664, "H":155.154, "I":131.172, "L": 131.172, "K": 147.195,
                    "M": 149.211, "F": 165.189, "P": 115.13, "S": 105.092, "T": 119.119, "W": 204.225,
                    "Y":181.188, "V":117.146}
        for aa in self._sequence:
            self.mass += AA_mass[aa]
    
    #and again the usual stuff
    def __setattr__(self,name,value):
	if str(name) not in ['_id','mass','name','_sequence','number_of_proteins']:
		raise TypeError('Attribute "'+str(name)+'" does not exist.')
	else:
		#print name
		#print type(name)
		#print 'wert'
		#print value
		#print type(value)
		#print'instanz'
		if name=='_id' and isinstance(value, types.BuiltinFunctionType):
			self.__dict__[name] = value
		elif name =='name' and isinstance(value, str):
			self.__dict__[name] = value
		elif name =='mass' and isinstance(value, float):
			self.__dict__[name] = value
		elif name=='_sequence' and isinstance(value, str):
			self.__dict__[name] = value.upper()
		elif name=='number_of_proteins' and isinstance(value, int):
			self.__dict__[name] = value
		else:
			raise TypeError('Type of value of '+str(name)+'  does not match requirements.')
   

class Ribosome(BioMolecule):
    """A ribosome can bind MRNA and translate it. After translation is
    finished it produces a protein.

    During initiation the ribosome checks if a given MRNA is bound
    by another ribosome and binds only if position 0 is empty.

    Elongation checks if the next codon is unbound and only elongates
    if the ribosome can move on. If the ribosome encounters a stop
    codon ("*") translation terminates. The MRNA is detached from the
    ribosome and the finished protein is returned.
    """
    code = dict([('UCA','S'), ('UCG','S'), ('UCC','S'), ('UCU','S'),
                 ('UUU','F'), ('UUC','F'), ('UUA','L'), ('UUG','L'),
                 ('UAU','Y'), ('UAC','Y'), ('UAA','*'), ('UAG','*'),
                 ('UGU','C'), ('UGC','C'), ('UGA','*'), ('UGG','W'),
                 ('CUA','L'), ('CUG','L'), ('CUC','L'), ('CUU','L'),
                 ('CCA','P'), ('CCG','P'), ('CCC','P'), ('CCU','P'),
                 ('CAU','H'), ('CAC','H'), ('CAA','Q'), ('CAG','Q'),
                 ('CGA','R'), ('CGG','R'), ('CGC','R'), ('CGU','R'),
                 ('AUU','I'), ('AUC','I'), ('AUA','I'), ('AUG','M'),
                 ('ACA','T'), ('ACG','T'), ('ACC','T'), ('ACU','T'),
                 ('AAU','N'), ('AAC','N'), ('AAA','K'), ('AAG','K'),
                 ('AGU','S'), ('AGC','S'), ('AGA','R'), ('AGG','R'),
                 ('GUA','V'), ('GUG','V'), ('GUC','V'), ('GUU','V'),
                 ('GCA','A'), ('GCG','A'), ('GCC','A'), ('GCU','A'),
                 ('GAU','D'), ('GAC','D'), ('GAA','E'), ('GAG','E'),
                 ('GGA','G'), ('GGG','G'), ('GGC','G'), ('GGU','G')])

    def __init__(self, id, name):
        super(Ribosome, self).__init__(id, name)
        self.bound_mrna = False
        self.position = None  # position on a bound MRNA

    def initiate(self, mrna):
        """
        Tries to bind to a given MRNA.

        @type mrna: MRNA
        """
        if not self.bound_mrna and not mrna.binding[0]:  # no mrna bound
                                                    # yet and target
                                                    # mrna still free
                                                    # at pos 0
            self.bound_mrna = mrna
            self.nascent_prot = None  # 10. Instantiate a new Protein
            self.position = 0
            self.bound_mrna.binding  # 11. Mark position 0 of MRNA to be bound by ribosome
            
    def elongate(self):
        """Elongate the new protein by the correct amino acid. Check if an
        MRNA is bound and if ribosome can move to next codon.
        Terminate if the ribosome reaches a STOP codon.

        @type return: Protein or False
        """
        if not self.bound_mrna: # can't elongate because there is no MRNA
            return False

        # 12. Implement the described features.

    def terminate(self):
        """
        Splits the ribosome/MRNA complex and returns a protein.
        """
        # 13. Dissociate the complex.
        return self.nascent_prot

	def __setattr__(self,name,value):
	if str(name) not in ['_id','mass','name','bound_mrna']:
		raise TypeError('Attribute "'+str(name)+'" does not exist.')
	else:
		#print name
		#print type(name)
		#print 'wert'
		#print value
		#print type(value)
		#print'instanz'
		if name=='_id' and isinstance(value, types.BuiltinFunctionType):
			self.__dict__[name] = value
		elif name =='name' and isinstance(value, str):
			self.__dict__[name] = value
		elif name =='mass' and isinstance(value, float):
			self.__dict__[name] = value
		elif name=='_sequence' and isinstance(value, str):
			self.__dict__[name] = value.upper()
		elif name=='number_of_proteins' and isinstance(value, int):
			self.__dict__[name] = value
		else:
			raise TypeError('Type of value of '+str(name)+'  does not match requirements.')
        

class Cell(object):
    def __init__(self):
        self.ribosomes = [Ribosome(i, 'Ribo_{0}'.format(i)) for i in xrange(200)]
        self.mrnas = [MRNA(i, 'MRNA_{0}'.format(i), "UUUUUUUUUUAA") for i in xrange(20)]
        self.proteins = [[] for x in xrange(20)]

    def step(self):
        for r in self.ribosomes:
            if not r.bound:
                r.initiate(self.mrnas[random.randint(0,len(self.mrnas)-1)])
            else:
                prot = r.elongate()
                if prot:
                    self.proteins[prot.id].append(prot)

    def simulate(self, steps, p=True):
        for s in xrange(steps):
            self.step()
            if p:
                print [len(x) for x in self.proteins]
                
                
if __name__ == "__main__":  
	test=BioMolecule(id,'test')
	print test
	b='UAG'
	test2=Polymer(id, 'test2',b)
	print test2
	test3=MRNA(id,'test3',b)
	print test3
	c='ADDFVT'
	test4=Protein(id,'test4',c)
	print test4
	#print 'a'
	#print dir(test2)
	#test.name='peter'
	# the following is called if the module is executed
    # 14. Instantiate the Cell class and call the simulation method.
    #pass

# 15. Generate a set of mRNA sequences to initiate the cell.
# 16. Implement protein degradation.