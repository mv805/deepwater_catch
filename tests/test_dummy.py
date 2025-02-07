import unittest


class TestDummy(unittest.TestCase):
    def test_dummy_success(self):
        # This dummy test always passes and is used for GitHub workflow testing.
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
