import unittest
from gol import Cell

class CommonCellBehaviour(unittest.TestCase):
    
    def assertAlive(self, nextGenCell):
        return self.assertEqual("alive", nextGenCell)

    def assertDead(self, nextGenCell):
        return self.assertEqual("dead", nextGenCell)
    
class LiveCellBehaviour(CommonCellBehaviour):

    def __init__(self, methodName='runTest'):
        CommonCellBehaviour.__init__(self, methodName=methodName)
        
    def setUp(self):
        self.cell = Cell("alive")
     
    def test_LiveCellWithFewerThanTwoLiveNeighbours_DiesOfLoneliness(self):
        '''Dies of Loneliness'''
        for liveNeighbours in (0, 1):
            nextGenCell = self.cell.regenerate(liveNeighbours)
            self.assertDead(nextGenCell)
        
    def test_LiveCellWithMoreThanThreeLiveNeighboursDiesOfOvercrowding(self):
        '''Dies of Overcrowding'''
        for liveNeighbours in (4, 5, 6, 7, 8):
            nextGenCell = self.cell.regenerate(liveNeighbours)
            self.assertDead(nextGenCell)
        
    def test_LiveCellWithTwoLiveNeighbours_LivesOn(self):
        '''Survival'''
        nextGenCell = self.cell.regenerate(liveNeighbours=2)
        self.assertAlive(nextGenCell)
        
    def test_LiveCellWithThreeLiveNeighbours_LivesOn(self):
        '''Survival'''
        nextGenCell = self.cell.regenerate(liveNeighbours=3)
        self.assertAlive(nextGenCell)

class DeadCellBehaviour(CommonCellBehaviour):

    def __init__(self, methodName='runTest'):
        CommonCellBehaviour.__init__(self, methodName=methodName)
        
    def setUp(self):
        self.cell = Cell("dead")
    
    def test_DeadCellWithoutTheMagicNumberOfNeighbours_remainsDead(self):
        for liveNeighbours in (0, 1, 2, 4, 5, 6, 7, 8):
            nextGenCell = self.cell.regenerate(liveNeighbours)
            self.assertDead(nextGenCell)
               
    def test_DeadCellWithExactlyThreeLiveNeighboursBecomesALiveCell(self):
        '''Reproduction'''
        nextGenCell = self.cell.regenerate(liveNeighbours=3)
        self.assertAlive(nextGenCell)
            
if __name__ == "__main__":
    unittest.main()