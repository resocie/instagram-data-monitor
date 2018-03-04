import unittest
from instagram.instagram import InstagramUser

class TestInstagramUser(unittest.TestCase):
	def test_isonline(self):
		user = InstagramUser('alegomes')

	def test_name_retrieval(self):
		user = InstagramUser('alegomes')
		self.assertEqual('Alexandre Gomes', user.name)

	def test_id_retrieval(self):
		user = InstagramUser('alegomes')
		self.assertEqual('9999', user.id)
		

if __name__ == '__main__':
    unittest.main()