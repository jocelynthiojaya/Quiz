#this is the corrected code
class Spell:   
    def __init__(self, incantation, name):    
         self.name = name    
         self.incantation = incantation   
    
    def __str__(self):    
        return self.name + ' ' + self.incantation + '\n' + self.get_description()   
    
    def get_description(self):    
        return 'No description' 
        
    def execute(self):    
        print(self.incantation) #tambah kurung
 
class Accio(Spell):   
    def __init__(self):    
        Spell.__init__(self, 'Accio', 'Summoning Charm')

    def get_description(self):     #i added this
        return 'This charm summons an object to the caster, potentially over a significant distance'   
    
    def study_spell(self, Spell):    #and this
        print(Spell)     

class Confundo(Spell):   
    def __init__(self):    
        Spell.__init__(self, 'Confundo', 'Confundus Charm')   
        
    def get_description(self):    
        return 'Causes the victim to become confused and befuddled.'   
    
    def study_spell(self, Spell):    
        print(Spell)    
        
spell = Confundo()  
#spell.execute()
#study_spell(Confundo())
spell.study_spell(spell)  
#study_spell(Confundo())

#1. The Parent class is Spell, the child classes are Accio and Confundo
#2. it prints out Accio and then has an error
#3. the description method in class Confundo is called: 
    #Causes the victim to become confused and befuddled.
#4. we need to add a get_description method to Accio, and 
    #return 'This charm summons an object to the caster, potentially over a significant distance'