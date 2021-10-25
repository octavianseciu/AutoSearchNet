import unittest
import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)
import searchYoutube as sy


class TestSearchYoutube (unittest.TestCase):

    def test_nrLinkrezultat_success(self):
        self.assertAlmostEqual(sy.nrLinkrezultat('1'),1)
        self.assertAlmostEqual(sy.nrLinkrezultat('doi'),2)
        self.assertAlmostEqual(sy.nrLinkrezultat('3'),3)
        self.assertAlmostEqual(sy.nrLinkrezultat('patru'),4)
        self.assertAlmostEqual(sy.nrLinkrezultat('5'),5)
        self.assertAlmostEqual(sy.nrLinkrezultat('6'),6)
        self.assertAlmostEqual(sy.nrLinkrezultat('7'),7)
        self.assertAlmostEqual(sy.nrLinkrezultat('8'),8)
        self.assertAlmostEqual(sy.nrLinkrezultat('noua'),9)
        self.assertAlmostEqual(sy.nrLinkrezultat('zece'),10)
       
       
if __name__ == '__main__':
    unittest.main()       



# python -m unittest test\test_youtubeSearch.py