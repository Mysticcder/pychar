import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode(tag="a", value="Click here", props={"href": "https://www.google.com"})
        expected_repr = ("HTMLNode(tag=a, value=Click here, children=[], "
                         "props={'href': 'https://www.google.com'})")
        self.assertEqual(repr(node), expected_repr)

class TestLeafNode(unittest.TestCase):
    def test_to_html_without_tag(self):
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")

    def test_to_html_with_tag(self):
        node = LeafNode("p", "This is a paragraph.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph.</p>")

    def test_to_html_with_tag_and_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()

    def test_repr(self):
        node = LeafNode("a", "Click here", {"href": "https://www.google.com"})
        expected_repr = ("LeafNode(tag=a, value=Click here, "
                         "props={'href': 'https://www.google.com'})")
        self.assertEqual(repr(node), expected_repr)

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        expected_html = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_no_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode(None, [LeafNode("b", "Bold text")])

    def test_no_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode("p", [])

    def test_nested_nodes(self):
        inner_node = ParentNode(
            "div",
            [
                LeafNode("p", "Paragraph 1"),
                LeafNode("p", "Paragraph 2"),
            ]
        )
        outer_node = ParentNode(
            "div",
            [
                LeafNode("h1", "Header"),
                inner_node,
            ]
        )
        expected_html = "<div><h1>Header</h1><div><p>Paragraph 1</p><p>Paragraph 2</p></div></div>"
        self.assertEqual(outer_node.to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()
