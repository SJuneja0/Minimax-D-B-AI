import saucy_boy
import board
import tree_node
import communicator

import unittest

class testFileMethods(unittest.TestCase):
    # For tests, use functions that use AssertEquals, etc.
    def defaultTest(self):
        self.assertTrue(True)
    
    def test_board_functions(self, bd):
        test_board = board(9, 9, "Test", "Test Opponent")
        bd.create_board()
        self.assertEqual(test_board.dots, bd.dots)
        self.assertEqual(test_board.edges, bd.edges)
        self.assertEqual(test_board.box, bd.box)
        self.assertFalse(test_board.is_game_over())
        test_legal_moves = test_board.get_legal_moves()
        # Unsure how to test update_board
    
    def test_saucy_boy_functions(self, sb):
        test_sb = saucy_boy("Test Opponent")

        self.assertTrue(True)

    def test_tree_node_construct_path(self, tn_root, tn_child):

        self.assertTrue(True)

    def test_communicator_functions(self, comm):
        self.assertTrue(True)
