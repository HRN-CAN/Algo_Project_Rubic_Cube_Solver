import numpy as np

MOVE_INDEX = { \
  "U": 0, "U'": 1, "U2": 2, "R": 3, "R'": 4, "R2": 5, "F": 6, "F'": 7, "F2": 8, \
  "D": 9, "D'": 10, "D2": 11, "L": 12, "L'": 13, "L2": 14, "B": 15, "B'": 16, "B2": 17, \
  "x": 18, "x'": 19, "x2": 20, "y": 21, "y'": 22, "y2": 23, "z": 24, "z'": 25, "z2": 26 \
}
    
PIECES = np.array([ \
  [  0, 21, 16], \
  [  2, 17,  8], \
  [  3,  9,  4], \
  [  1,  5, 20], \
  [ 12, 10, 19], \
  [ 13,  6, 11], \
  [ 15, 22,  7], \
])

MOVE_DEF = np.array([ \
  [  2,  0,  3,  1, 20, 21,  6,  7,  4,  5, 10, 11, 12, 13, 14, 15,  8,  9, 18, 19, 16, 17, 22, 23], \
  [  1,  3,  0,  2,  8,  9,  6,  7, 16, 17, 10, 11, 12, 13, 14, 15, 20, 21, 18, 19,  4,  5, 22, 23], \
  [  3,  2,  1,  0, 16, 17,  6,  7, 20, 21, 10, 11, 12, 13, 14, 15,  4,  5, 18, 19,  8,  9, 22, 23], \
  [  0,  9,  2, 11,  6,  4,  7,  5,  8, 13, 10, 15, 12, 22, 14, 20, 16, 17, 18, 19,  3, 21,  1, 23], \
  [  0, 22,  2, 20,  5,  7,  4,  6,  8,  1, 10,  3, 12,  9, 14, 11, 16, 17, 18, 19, 15, 21, 13, 23], \
  [  0, 13,  2, 15,  7,  6,  5,  4,  8, 22, 10, 20, 12,  1, 14,  3, 16, 17, 18, 19, 11, 21,  9, 23], \
  [  0,  1, 19, 17,  2,  5,  3,  7, 10,  8, 11,  9,  6,  4, 14, 15, 16, 12, 18, 13, 20, 21, 22, 23], \
  [  0,  1,  4,  6, 13,  5, 12,  7,  9, 11,  8, 10, 17, 19, 14, 15, 16,  3, 18,  2, 20, 21, 22, 23], \
  [  0,  1, 13, 12, 19,  5, 17,  7, 11, 10,  9,  8,  3,  2, 14, 15, 16,  6, 18,  4, 20, 21, 22, 23], \
  [  0,  1,  2,  3,  4,  5, 10, 11,  8,  9, 18, 19, 14, 12, 15, 13, 16, 17, 22, 23, 20, 21,  6,  7], \
  [  0,  1,  2,  3,  4,  5, 22, 23,  8,  9,  6,  7, 13, 15, 12, 14, 16, 17, 10, 11, 20, 21, 18, 19], \
  [  0,  1,  2,  3,  4,  5, 18, 19,  8,  9, 22, 23, 15, 14, 13, 12, 16, 17,  6,  7, 20, 21, 10, 11], \
  [ 23,  1, 21,  3,  4,  5,  6,  7,  0,  9,  2, 11,  8, 13, 10, 15, 18, 16, 19, 17, 20, 14, 22, 12], \
  [  8,  1, 10,  3,  4,  5,  6,  7, 12,  9, 14, 11, 23, 13, 21, 15, 17, 19, 16, 18, 20,  2, 22,  0], \
  [ 12,  1, 14,  3,  4,  5,  6,  7, 23,  9, 21, 11,  0, 13,  2, 15, 19, 18, 17, 16, 20, 10, 22,  8], \
  [  5,  7,  2,  3,  4, 15,  6, 14,  8,  9, 10, 11, 12, 13, 16, 18,  1, 17,  0, 19, 22, 20, 23, 21], \
  [ 18, 16,  2,  3,  4,  0,  6,  1,  8,  9, 10, 11, 12, 13,  7,  5, 14, 17, 15, 19, 21, 23, 20, 22], \
  [ 15, 14,  2,  3,  4, 18,  6, 16,  8,  9, 10, 11, 12, 13,  1,  0,  7, 17,  5, 19, 23, 22, 21, 20], \
  [  8,  9, 10, 11,  6,  4,  7,  5, 12, 13, 14, 15, 23, 22, 21, 20, 17, 19, 16, 18,  3,  2,  1,  0], \
  [ 23, 22, 21, 20,  5,  7,  4,  6,  0,  1,  2,  3,  8,  9, 10, 11, 18, 16, 19, 17, 15, 14, 13, 12], \
  [ 12, 13, 14, 15,  7,  6,  5,  4, 23, 22, 21, 20,  0,  1,  2,  3, 19, 18, 17, 16, 11, 10,  9,  8], \
  [  2,  0,  3,  1, 20, 21, 22, 23,  4,  5,  6,  7, 13, 15, 12, 14,  8,  9, 10, 11, 16, 17, 18, 19], \
  [  1,  3,  0,  2,  8,  9, 10, 11, 16, 17, 18, 19, 14, 12, 15, 13, 20, 21, 22, 23,  4,  5,  6,  7], \
  [  3,  2,  1,  0, 16, 17, 18, 19, 20, 21, 22, 23, 15, 14, 13, 12,  4,  5,  6,  7,  8,  9, 10, 11], \
  [ 18, 16, 19, 17,  2,  0,  3,  1, 10,  8, 11,  9,  6,  4,  7,  5, 14, 12, 15, 13, 21, 23, 20, 22], \
  [  5,  7,  4,  6, 13, 15, 12, 14,  9, 11,  8, 10, 17, 19, 16, 18,  1,  3,  0,  2, 22, 20, 23, 21], \
  [ 15, 14, 13, 12, 19, 18, 17, 16, 11, 10,  9,  8,  3,  2,  1,  0,  7,  6,  5,  4, 23, 22, 21, 20]  \
])

COLORS = np.zeros([7, 3, 3], dtype=int)
COLORS[0, 0, :] = [0, 5, 4]; COLORS[0, 1, :] = [4, 0, 5]; COLORS[0, 2, :] = [5, 4, 0]
COLORS[1, 0, :] = [0, 4, 2]; COLORS[1, 1, :] = [2, 0, 4]; COLORS[1, 2, :] = [4, 2, 0]
COLORS[2, 0, :] = [0, 2, 1]; COLORS[2, 1, :] = [1, 0, 2]; COLORS[2, 2, :] = [2, 1, 0]
COLORS[3, 0, :] = [0, 1, 5]; COLORS[3, 1, :] = [5, 0, 1]; COLORS[3, 2, :] = [1, 5, 0]
COLORS[4, 0, :] = [3, 2, 4]; COLORS[4, 1, :] = [4, 3, 2]; COLORS[4, 2, :] = [2, 4, 3]
COLORS[5, 0, :] = [3, 1, 2]; COLORS[5, 1, :] = [2, 3, 1]; COLORS[5, 2, :] = [1, 2, 3]
COLORS[6, 0, :] = [3, 5, 1]; COLORS[6, 1, :] = [1, 3, 5]; COLORS[6, 2, :] = [5, 1, 3]

INDICES = np.zeros([58, 2], dtype=int)
INDICES[50] = [0, 0]; INDICES[54] = [0, 1]; INDICES[13] = [0, 2]
INDICES[28] = [1, 0]; INDICES[42] = [1, 1]; INDICES[ 8] = [1, 2]
INDICES[14] = [2, 0]; INDICES[21] = [2, 1]; INDICES[ 4] = [2, 2]
INDICES[52] = [3, 0]; INDICES[15] = [3, 1]; INDICES[11] = [3, 2]
INDICES[47] = [4, 0]; INDICES[30] = [4, 1]; INDICES[40] = [4, 2]
INDICES[25] = [5, 0]; INDICES[18] = [5, 1]; INDICES[35] = [5, 2]
INDICES[23] = [6, 0]; INDICES[57] = [6, 1]; INDICES[37] = [6, 2]

HASH_O_P = np.array([1, 2, 10])
FACT_6 = np.array([720, 120, 24, 6, 2, 1])
POW_3 = np.array([1, 3, 9, 27, 81, 243])
POW_7 = np.array([1, 7, 49, 343, 2401, 16807])

def apply_movement(cube_state, move):
  return cube_state[MOVE_DEF[move]]

def apply_algorithm_string(cube_state, alg):
  moves = alg.split(" ")
  for m in moves:
    if m in MOVE_INDEX:
      cube_state = apply_movement(cube_state, MOVE_INDEX[m])
  return cube_state

def initialize_state():
  return np.array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5])

def is_cube_solved(cube_state):
  for i in range(6):
    if not (cube_state[4 * i:4 * i + 4] == cube_state[4 * i]).all():
      return False
  return True

def normalize_face_colors(cube_state):
  norm_cols = np.zeros(6, dtype=int)
  norm_cols[cube_state[18] - 3] = 1
  norm_cols[cube_state[23] - 3] = 2
  norm_cols[cube_state[14]] = 3
  norm_cols[cube_state[18]] = 4
  norm_cols[cube_state[23]] = 5
  return norm_cols[cube_state]

def get_stickers(sOP):
  cube_state = np.zeros(24, dtype=int)
  cube_state[[14, 18, 23]] = [3, 4, 5]
  for i in range(7):
    cube_state[PIECES[i]] = COLORS[sOP[i, 0], sOP[i, 1], :]
  return cube_state

def get_piece_orientation_and_permutation(cube_state):
  return INDICES[np.dot(cube_state[PIECES], HASH_O_P)]

def index_permutation2(sOP):
  return np.dot([sOP[i, 0] - np.count_nonzero(sOP[:i, 0] < sOP[i, 0]) for i in range(6)], FACT_6)

def index_orientation(sOP):
  return np.dot(sOP[:-1, 1], POW_3)

def index_permutation(sOP):
  return np.dot(sOP[:-1, 0], POW_7)

def index_piece_orientation_and_permutation(sOP):
  return index_orientation(sOP) * 5040 + index_permutation2(sOP)

def print_cube(cube_state):
  print("      ┌──┬──┐")
  print("      │ {}│ {}│".format(cube_state[0], cube_state[1]))
  print("      ├──┼──┤")
  print("      │ {}│ {}│".format(cube_state[2], cube_state[3]))
  print("┌──┬──┼──┼──┼──┬──┬──┬──┐")
  print("│ {}│ {}│ {}│ {}│ {}│ {}│ {}│ {}│".format(cube_state[16], cube_state[17], cube_state[8], cube_state[9], cube_state[4], cube_state[5], cube_state[20], cube_state[21]))
  print("├──┼──┼──┼──┼──┼──┼──┼──┤")
  print("│ {}│ {}│ {}│ {}│ {}│ {}│ {}│ {}│".format(cube_state[18], cube_state[19], cube_state[10], cube_state[11], cube_state[6], cube_state[7], cube_state[22], cube_state[23]))
  print("└──┴──┼──┼──┼──┴──┴──┴──┘")
  print("      │ {}│ {}│".format(cube_state[12], cube_state[13]))
  print("      ├──┼──┤")
  print("      │ {}│ {}│".format(cube_state[14], cube_state[15]))
  print("      └──┴──┘")

if __name__ == "__main__":
  cube_state = initialize_state()
  print_cube(cube_state)
  cube_state = apply_algorithm_string(cube_state, "x y R U' R' U' F2 U' R U R' U F2")
  print_cube(cube_state)
  cube_state = normalize_face_colors(cube_state)
  print_cube(cube_state)
    
HASH_O = np.ones(729, dtype=int) * 12
HASH_P = np.ones(117649, dtype=int) * 12

moveStrs = {0: "U", 1: "U'", 2: "U2", 3: "R", 4: "R'", 5: "R2", 6: "F", 7: "F'", 8: "F2"}

def generate_permutation_table(cube_state, d, last_movement=-3):
  index = index_permutation(get_piece_orientation_and_permutation(cube_state))
  if d < HASH_P[index]:
    HASH_P[index] = d
    for m in range(9):
      if int(m / 3) == int(last_movement / 3):
        continue
      generate_permutation_table(apply_movement(cube_state, m), d + 1, m)
      
def generate_orientation_table(cube_state, d, last_movement=-3):
  index = index_orientation(get_piece_orientation_and_permutation(cube_state))
  if d < HASH_O[index]:
    HASH_O[index] = d
    for m in range(9):
      if int(m / 3) == int(last_movement / 3):
        continue
      generate_orientation_table(apply_movement(cube_state, m), d + 1, m)

def IDA_star(cube_state, d, moves, last_movement=-3):
  if is_cube_solved(cube_state):
    print_moves(moves)
    return True
  else:
    sOP = get_piece_orientation_and_permutation(cube_state)
    if d > 0 and d >= HASH_O[index_orientation(sOP)] and d >= HASH_P[index_permutation(sOP)]:
      dOptimal = False
      for m in range(9):
        if int(m / 3) == int(last_movement / 3):
          continue
        newMoves = moves[:]; newMoves.append(m)
        solved = IDA_star(apply_movement(cube_state, m), d - 1, newMoves, m)
        if solved and not dOptimal:
          dOptimal = True
      if dOptimal:
        return True
  return False

def print_moves(moves):
  moveStr = ""
  for m in moves:
    moveStr += moveStrs[m] + " "
  print(moveStr)


def solve_cube(cube_state):
  print_cube(cube_state)

  print("normalizing stickers...")
  cube_state = normalize_face_colors(cube_state)

  print("generating pruning tables...")
  generate_orientation_table(initialize_state(), 0)
  generate_permutation_table(initialize_state(), 0)

  print("searching...")
  solved = False
  depth = 1
  while depth <= 11 and not solved:
    print("depth {}".format(depth))
    solved = IDA_star(cube_state, depth, [])
    depth += 1

if __name__ == "__main__":
  cube_state = apply_algorithm_string(initialize_state(), "R U2 R2 F2 R' F2 R F R")
  solve_cube(cube_state)