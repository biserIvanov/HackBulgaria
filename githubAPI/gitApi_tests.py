import unittest
from gitAPI import DirectedGraph


class DirectedGraph_Test(unittest.TestCase):

    def setUp(self):
        self.graph1 = DirectedGraph()
        self.graph1.addEdge("Ivan", "Dragan")
        self.graph1.addEdge("Pesho", "Marto")
        self.graph1.addEdge("Pesho", "Dragan")
        self.graph1.addEdge("Sasho", "Dragan")
        self.graph1.addEdge("Dragan", "Ivan")

    def test_getNeighbours(self):
        self.assertEqual(['Dragan'], self.graph1.getNeighborsFor("Ivan"))

    def test_toString(self):
        self.assertEqual({'Ivan': ['Dragan'], 'Dragan': ['Ivan'], 'Marto': [], 'Pesho': [
                         'Marto', 'Dragan'], 'Sasho': ['Dragan']}, self.graph1.toString())

    def test_pathBetween(self):
        self.assertTrue(self.graph1.pathBetween("Pesho", "Ivan"))

    def test_longerWay(self):
        self.assertFalse(self.graph1.pathBetween("Dragan", "Pesho"))

if __name__ == '__main__':
    unittest.main()
