

class chopsticks():
    """
        Representation Example: the chopsticks position
        
                    11
                    23
​
        is represented by the 5-length str 11230. The fourth index represents whos turn it is. Even is p1 odd is p2
    """
    def __init__(self, initial_position = '11110'):
        self.initial_position = initial_position

    def GenerateMoves(self, position):
        moves = []
        if int(position[4]) % 2 == 0:
            if int(position[0]) < 5 and int(position[2]) < 5:
                moves.append((0, 2))
            if int(position[0]) < 5 and int(position[3]) < 5:
                moves.append((0, 3))
            if int(position[1]) < 5 and int(position[2]) < 5:
                moves.append((1, 2))
            if int(position[1]) < 5 and int(position[3]) < 5:
                moves.append((1, 3))
        else:
            if int(position[0]) < 5 and int(position[2]) < 5:
                moves.append((2, 0))
            if int(position[0]) < 5 and int(position[3]) < 5:
                moves.append((3, 0))
            if int(position[1]) < 5 and int(position[2]) < 5:
                moves.append((2, 1))
            if int(position[1]) < 5 and int(position[3]) < 5:
                moves.append((3, 1))

        return moves
        

    def DoMove(self, position, move):
        #Get indeces of hands we are moving
        hand1, hand2 = move[0], move[1]
        #Change hand 2 to be hand2 + hand1
        return position[:hand2] + str(int(position[hand1]) + int(position[hand2])) + position[hand2 + 1: -1] + str(int(position[4]) + 1)

    

    def PrimitiveValue(self, position):
        if int(position[0]) >= 5 and int(position[1]) >= 5 and int(position[4]) % 2 == 0:
            return "primitive"
        elif int(position[2]) >= 5 and int(position[3]) >= 5 and  int(position[4]) %2 != 0:
            return "primitive"
        else:
            return "not_primitive" 

    def __str__(self):
        return 'Chopsticks game'


def Memoized_Solve(game):
    """
        We store all memoization results in the visited_positions dictionary.
        Key: Position
        Value: A tuple (VALUE, IS_PRIMITIVE)
    """
    visited_positions = {}

    def Solve(position):
        primitive_value = game.PrimitiveValue(position)
        if primitive_value != 'not_primitive':
            visited_positions[position] = (primitive_value, True)
            return primitive_value
        
        seen_lose, seen_tie = False, False
        child_value = ''
        for move in game.GenerateMoves(position):
            child_position = game.DoMove(position, move)
            if child_position in visited_positions:
                child_value = visited_positions[child_position][0]
            else:
                child_value = Solve(child_position)
            if child_value == 'lose':
                seen_lose = True
            elif child_value == 'tie':
                seen_tie = True
        value = 'win' if seen_lose else 'tie' if seen_tie else 'lose'
        visited_positions[position] = (value, False)
        return value

    return Solve(game.initial_position), visited_positions

    

def display_counts(game, visited_positions):
    num_loses, num_ties, num_wins = 0, 0, 0
    num_primitive_loses,num_primitive_ties, num_primitive_wins = 0, 0, 0
    for position in visited_positions:
        value, is_primitive = visited_positions[position]
        if value == 'win':
            num_wins += 1
            if is_primitive:
                num_primitive_wins += 1
        elif value == 'tie':
            num_ties += 1
            if is_primitive:
                num_primitive_ties += 1
        else:
            num_loses += 1
            if is_primitive:
                num_primitive_loses += 1

    print(f"\n{game} is a {visited_positions[game.initial_position][0]} for the first player.")
    print(f"There are {num_loses + num_wins + num_ties} reachable positions, of which {num_primitive_loses + num_primitive_wins + num_primitive_ties} are primitive.")
    print(f"There are {num_loses} loses, of which {num_primitive_loses} are primitive.")
    print(f"There are {num_wins} wins, of which {num_primitive_wins} are primitive.")
    print(f"There are {num_ties} ties, of which {num_primitive_ties} are primitive.\n")

    
game = chopsticks()
position = '11110'
while(game.PrimitiveValue(position)) != "primitive":
    print(position)
    moves = game.GenerateMoves(position)
    print(moves)
    position = game.DoMove(position, moves[-1])
    

    
