
class GolBoard(object):
    
    def __init__(self, length, width):
        pass
    
    def sowSeed(self, seed):
        pass
    
    def generate(self):
        return ("dead",)
    
class Cell(object):
    
    def __init__(self, state):
        self.state = state
    
    def regenerate(self, liveNeighbours):
        if liveNeighbours < 2 or liveNeighbours > 3:
            return "dead"
        if self.state == "dead" and liveNeighbours == 2:
            return "dead"
        return "alive"
