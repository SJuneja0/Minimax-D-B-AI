import SaucyBoy
import board
import tree_node
import communicator

import unittest

class testFileMethods(unittest.TestCase):
    # For tests, use functions that use AssertEquals, etc.
    def defaultTest(self):
        self.assertTrue(True)
    
    def test_board_functions(self):
        test_board = board.Board(3, 3, "Test", "Test Opponent")
        test_dots = []
        test_edges = []
        test_boxes = []
        for i in range(4):
            for j in range(4):
                test_dots.append(board.Dot(i, j))
        for x in range(3):
            for y in range(4):
                edge = board.Edge(test_dots[4 * x + y], test_dots[4 * (x + 1) + y])
                test_edges.append(edge)
        for x in range(4):
            for y in range(3):
                edge = board.Edge(test_dots[4 * x + y], test_dots[4 * x + y + 1])
                test_edges.append(edge)
        for x in range(3):
            for y in range(3):
                top_edge = test_edges[4 * x + y]
                bottom_edge = test_edges[4 * (x + 1) + y + 7]
                left_edge = test_edges[4 * x + y + 4]
                right_edge = test_edges[4 * (x + 1) + y + 4]
                test_boxes.append(board.Box([top_edge, right_edge, bottom_edge, left_edge]))
        self.assertEqual(test_board.dots, test_dots)
        self.assertEqual(test_board.edges, test_edges)
        self.assertEqual(test_board.box, test_boxes)
        self.assertFalse(test_board.is_game_over())
        self.assertEqual(3, test_board.find_edge_in_board(test_edges[3]))
        self.assertEqual(test_edges, test_board.get_legal_moves())
        test_board.edges[3].owner = "Test"
        self.assertEqual(test_edges[3], test_board.edges_controlled_by("Test"))
        # Unsure how to test update_board
    
    def test_saucy_boy_functions(self, sb):
        test_sb = ai.AI("Test Opponent")

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
