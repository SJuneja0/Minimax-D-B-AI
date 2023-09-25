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
        test_board = board.Board(9, 9, "Test", "Test Opponent")
        bd.create_board()
        self.assertEqual(test_board.dots, bd.dots)
        self.assertEqual(test_board.edges, bd.edges)
        self.assertEqual(test_board.box, bd.box)
        self.assertFalse(test_board.is_game_over())
        test_legal_moves = test_board.get_legal_moves()
        # Unsure how to test update_board
    
    def test_saucy_boy_functions(self, sb):
        test_sb = saucy_boy.saucy_boy("Test Opponent")

        self.assertTrue(True)

    def test_tree_node_construct_path(self):
        rootNode = tree_node.treeNode(None, [], None, True)
        a1 = tree_node.treeNode(None, [], rootNode, False)
        rootNode.children.append(a1)
        a2 = tree_node.treeNode(None, [], rootNode, False)
        rootNode.children.append(a2)
        a3 = tree_node.treeNode(None, [], rootNode, False)
        rootNode.children.append(a3)

        b1 = tree_node.treeNode(None, [], a1, False)
        a1.children.append(b1)
        b2 = tree_node.treeNode(None, [], a2, False)
        a2.children.append(b2)
        b3 = tree_node.treeNode(None, [], a2, False)
        a2.children.append(b3)
        b4 = tree_node.treeNode(None, [], a2, False)
        a2.children.append(b4)
        b5 = tree_node.treeNode(None, [], a3, False)
        a3.children.append(b5)
        b6 = tree_node.treeNode(None, [], a3, False)
        a3.children.append(b6)

        c1 = tree_node.treeNode(None, [], b1, False)
        b1.children.append(c1)
        c2 = tree_node.treeNode(None, [], b2, False)
        b2.children.append(c2)
        c3 = tree_node.treeNode(None, [], b2, False)
        b2.children.append(c3)
        c4 = tree_node.treeNode(None, [], b5, False)
        b5.children.append(c4)
        c5 = tree_node.treeNode(None, [], b5, False)
        b5.children.append(c5)
        c6 = tree_node.treeNode(None, [], b5, False)
        b5.children.append(c6)
        c7 = tree_node.treeNode(None, [], b6, False)
        b6.children.append(c7)

        test_path_1 = [c1, b1, a1, rootNode]
        self.assertEqual(test_path_1, c1.construct_path([]))
        test_path_2 = [b3, a2, rootNode]
        self.assertEqual(test_path_2, b3.construct_path([]))
        test_path_3 = [c6, b5, a3, rootNode]
        self.assertEqual(test_path_3, c6.construct_path([]))

    def test_communicator_functions(self, comm):
        self.assertTrue(True)
