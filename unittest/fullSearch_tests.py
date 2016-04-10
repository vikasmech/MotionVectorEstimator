__author__ = 'davidsiecinski'
import unittest
import fullSearch

class PreProcessingMethods (unittest.TestCase):
    def setUp(self):
        current_picture=[[0,0,0,0],[0,1,0,0],[0,3,0,0],[0,0,0,0]]
        reference_picture=[[0,0,0,0],[0,0,1,0],[0,0,3,0],[0,0,0,0]]
        self.fullsearch_= fullSearch.FullSearch(current_picture,reference_picture)

        small_current_picture=[[0,1,0,0]]
        small_reference_picture=[[0,0,1,0]]
        self.small_fullsearch = fullSearch.FullSearch(small_current_picture,small_reference_picture)

    def test_macroblock(self):
        # y is reverse counted  to fit x and y axis
        self.fullsearch_.y=2
        self.fullsearch_.x=0
        i=0
        j=1
        self.assertEqual(self.fullsearch_.__makroBlock__(i,j),1)

    def test_macroblock2(self):
        self.fullsearch_.y=2
        self.fullsearch_.x=1
        i=0
        j=1
        self.assertEqual(self.fullsearch_.__makroBlock__(i,j,isCurrent=False),1)

    def test_motionVector(self):
        self.small_fullsearch.p = 2
        return_value = [0, 1]
        # coordinates of top left corner of macro block
        self.small_fullsearch. y= 0
        self.small_fullsearch.x = 0
        self.assertEqual(self.small_fullsearch.motionVector(), return_value)

    def test_motionEstimation(self):
        # result should fit one of 2 choices
        result1=[[[0, 1],[0, -1]], [[0, -1],[0, 1]]]
        result2=[[[0, 1],[-1, -1]], [[1, -1],[0, 1]]]

        self.assertEqual(self.fullsearch_.motionEstimation(),result1)


    # def test_url_preprocessing(self):
    #     self.assertEqual(self.preprocessing_.preprocess_url("https://www.google.pl"), 'URL')
