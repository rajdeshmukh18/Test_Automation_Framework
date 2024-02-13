import softest


class Utilis(softest.TestCase):
    def assertListItem(self,list,value):
        for stop in list:
            print("The text is:" + stop.text)
            self.soft_assert(self.assertEqual,stop.text,value )
            if stop.text==value:
                print("Test Case is PASSED")
            else:
                print("Test Case is FAILED")
        self.assert_all()
