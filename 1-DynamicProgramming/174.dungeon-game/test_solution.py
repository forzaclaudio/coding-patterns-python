from solution import Solution

def test_solution_1():
    s = Solution()
    dungeon = [[0]]
    assert s.calculateMinimumHP(dungeon) == 1

def test_solution_2():
    s = Solution()
    dungeon = [
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5]
   ]
    assert s.calculateMinimumHP(dungeon) == 7

def test_solution_3():
    s = Solution()
    dungeon = [[100]]
    assert s.calculateMinimumHP(dungeon) == 1

def test_solution_4():
    s = Solution()
    dungeon = [[0, 0]]
    assert s.calculateMinimumHP(dungeon) == 1

def test_solution_5():
    s = Solution()
    dungeon = [[-200]]
    assert s.calculateMinimumHP(dungeon) == 201

def test_solution_6():
    s = Solution()
    dungeon = [[0,-3]]
    assert s.calculateMinimumHP(dungeon) == 4


def test_solution_7():
    s = Solution()
    dungeon = [[-3,5]]
    assert s.calculateMinimumHP(dungeon) == 4

def test_solution_8():
    s = Solution()
    dungeon = [[-3],[-7]]
    assert s.calculateMinimumHP(dungeon) == 11

def test_solution_9():
    s = Solution()
    dungeon = [[0,-3], [-10,0]]
    assert s.calculateMinimumHP(dungeon) == 4

def test_solution_10():
    s = Solution()
    dungeon = [[0,5], [-2,-3]]
    assert s.calculateMinimumHP(dungeon) == 1

def test_solution_11():
    s = Solution()
    dungeon = [[0,0], [-5,-4]]
    assert s.calculateMinimumHP(dungeon) == 5

def test_solution_12():
    s = Solution()
    dungeon = [[-1,1]]
    assert s.calculateMinimumHP(dungeon) == 2

def test_solution_13():
    s = Solution()
    dungeon = [[2,1], [1,-1]]
    assert s.calculateMinimumHP(dungeon) == 1

def test_solution_14():
    s = Solution()
    dungeon = [[0], [0]]
    assert s.calculateMinimumHP(dungeon) == 1
