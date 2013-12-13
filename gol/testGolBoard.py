import unittest
from gol import GolBoard

class BoardBehaviour(unittest.TestCase):

    def test_canCreateCellularAutomationBoardOfSizeZero(self):
        matrix = GolBoard(length=0, width=0)
        
    def test_initBoardWithSimplestSeed(self):
        matrix = GolBoard(length=1, width=1)
        matrix.sowSeed(("dead",))
        
    def test_applyFirstGeneration(self):
        matrix = GolBoard(length=1, width=1)
        matrix.sowSeed(("dead",))
        self.assertEqual(("dead",), matrix.generate())
