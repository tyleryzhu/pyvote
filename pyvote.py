
class Society:
    ''' Creates a society of voters and alternatives, where voters have profiles on the alternatives'''
    alternatives = []
    voters = []
    profiles = {}

    def __init__(self, voters, alternatives):
        ''' Initialize a Society with voters and alternatives. '''
        self.voters = voters
        self.alternatives = alternatives

    def profiling(self, voter, ordering):
        ''' voter is a member of voters, while ordering is some strict weak ordering of X.'''
        if voter not in self.voters:
            raise ValueError('Voter {} was not a valid voter of the Society'.format(voter))
        if set(ordering.keys()) != set(self.alternatives):
            raise ValueError("Ordering was not an ordering of this society's alternatives")
        self.profiles[voter] = ordering

    def getVoters(self):
        return self.voters

    def getAlternatives(self):
        return self.alternatives
