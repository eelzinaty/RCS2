from os import path
import networkx as nx
import unittest

from comp61542.database import database

class TestDatabase(unittest.TestCase):

    def setUp(self):
        dir, _ = path.split(__file__)
        self.data_dir = path.join(dir, "..", "data")
        #0153462 : ABCDEFG
        
    def test_get_author_distance_AB(self):
        db = database.Database()
        db.read(path.join(self.data_dir, "dblp_distance_graph.xml"))
        #data = db.search_author_by_name("author1")
        d = db.get_author_distance("A","B")# A => B
       # print [p for p in db.get_author_distance(0,1)]
        self.assertEqual(d,[["A","B"]])
          
    def test_get_author_distance_CD(self):
        db = database.Database()
        db.read(path.join(self.data_dir, "dblp_distance_graph.xml"))
        #data = db.search_author_by_name("author1")
        d = db.get_author_distance("C","D")# C => B => D & C => G => D
        self.assertEqual(d,[["C","B","D"],["C","G","D"]])

          
    def test_get_author_distance_CE(self):
        db = database.Database()
        db.read(path.join(self.data_dir, "dblp_distance_graph.xml"))
        #data = db.search_author_by_name("author1")
        d = db.get_author_distance("C","E")# C => B => A => E & C => G => A =>E
        self.assertEqual(d,[["C","B","A","E"],["C","G","A","E"]])    
           
    def test_get_author_distance_AF(self):
        db = database.Database()
        db.read(path.join(self.data_dir, "dblp_distance_graph.xml"))
        #data = db.search_author_by_name("author1")
        d = db.get_author_distance("A","F")# X
        self.assertEqual(d,[])  
if __name__ == '__main__':
    unittest.main()
