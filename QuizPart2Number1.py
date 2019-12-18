class Spell:
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation
    def __str__(self):
        return self.name + '' + self.incantation + '\n' + self.get_description()
    def get_description(self):
        return 'No description'
    def execute(self):
        print(self.incantation)#i put parantheses here
class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
    def get_description(self):#added this code so print Accio() will print an appropriate description
        return 'This charm summons an object to the caster, potentially over a significant distance'

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')
    def get_description(self):
        return 'Causes the victim to become confused and befuddled.'

def study_spell(spell):#i put out this function outside class confundo to make the code work
        print(spell)
spell = Accio()
spell.execute()
study_spell(spell)
study_spell(Confundo())
print(Accio())#added this to check if the get desc on accio works or not and have a proper desc

#I fixed the code by putting a parantheses on line 10 and putting out def study_spell outside the class confundo
#Number 1
#1A, Parent class: Spell & Child class: Accio & Confundo
#1B,output:
#   Accio
#   Summoning CharmAccio
#   No description
#   Confundus CharmConfundo
#   Causes the victim to become confused and befuddled.
#1C, get description inside class confundo is called, why? because inside the get description in class confundo has the return function containing the description so when "study_spell(Confundo())"" gets called it gives us Confudus CharmConfundus and its description as its output
#1D, Added  def get_description(self): 
                #return 'This charm summons an object to the caster, potentially over a significant distance'
#   inside the class Accio(Spell) so when we print out Accio() it has a proper description