class HalvingGame(object):
    def __init__(self, N):
        self.N = N

    # state = (player, number)

    def startState(self):
        return (+1, self.N)

    def isEnd(self, state):
        player, number = state
        return number == 0

    def utility(self, state):
        player, number = state
        assert number == 0
        return player * float('inf')

    def actions(self, state):
        return ['-', '/']

    def player(self, state):
        player, number = state
        return player

    def succ(self, state, action):
        player, number = state
        if action == '-':
            return (-player, number-1)
        elif action == '/':
            return (-player, number//2)

# general code

def humanPolicy(game, state):
    while True:
        action = input('Input action:')
        if action in game.actions(state):
            return action

# controller

policies = {+1: humanPolicy, -1: humanPolicy}
game = HalvingGame(N=15)
state = game.startState()

while not game.isEnd(state):
    print('='*10, state)
    player = game.player(state)
    policy = policies[player]
    action = policy(game, state)
    state = game.succ(state, action)

print('utility = {}'.format(game.utility(state)))

