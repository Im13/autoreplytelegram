import unittest, auto_reply

class TestString(unittest.TestCase):
    def test1(self):
        self.assertEqual(auto_reply.string_handler(
            "Xq:565,010,x100 k,xq:181,585,x100 k c vân.".lower()), 
            (2, "xiên ghepx2:565,010,x100 k,xiên ghepx2:181,585,x100 k c vân."))

    def test2(self):
        self.assertEqual(auto_reply.string_handler(
            "De 42-80x100".lower()), 
            (0, "de 42-80x100"))
        
    def test3(self):
        self.assertEqual(auto_reply.string_handler(
            "T3 Xq 42-69-48-80x100".lower()), 
            (1, "t3 xiên ghepx2 42-69-48-80x100"))
        
    def test4(self):
        self.assertEqual(auto_reply.string_handler(
            "Xien quay 05,53,90,86x500k .35,53,90,86x300k".lower()), 
            (1, "xiên ghepx2 05,53,90,86x500k .35,53,90,86x300k"))
        
    def test5(self):
        self.assertEqual(auto_reply.string_handler(
            "Xien 86,90x1000k .86,53x1000k.".lower()), 
            (0, "xien 86,90x1000k .86,53x1000k."))

    def test6(self):
        self.assertEqual(auto_reply.string_handler(
            "Xq: 010.020 100n. Xq: 010.030 100n. Xien quay: 010.040 x 100k".lower()), 
            (3, "xiên ghepx2: 010.020 100n. xiên ghepx2: 010.030 100n. xiên ghepx2: 010.040 x 100k"))
        
if __name__=='__main__':
	unittest.main()