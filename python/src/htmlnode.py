from htmlnode import LeafNode, ParentNode


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError("to_html method should be overridden by subclasses")

    def props_to_html(self):
        return ' '.join(f'{key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return (f"HTMLNode(tag={self.tag}, value={self.value}, "
                f"children={self.children}, props={self.props})")

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode requires a value")
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode requires a value")
        if self.tag is None:
            return self.value
        else:
            props_html = self.props_to_html()
            return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"

    def __repr__(self):
        return (f"LeafNode(tag={self.tag}, value={self.value}, "
                f"props={self.props})")
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode requires a tag")
        if not children:
            raise ValueError("ParentNode must have children")
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode requires a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")
        
        children_html = ''.join(child.to_html() for child in self.children)
        props_html = self.props_to_html()
        
        return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"
    
    def text_node_to_html_node(text_node):
        if text_node.text_type == "text":
            return LeafNode(None, text_node.text)
        elif text_node.text_type == "bold":
            return LeafNode("b", text_node.text)
        elif text_node.text_type == "italic":
            return LeafNode("i", text_node.text)
        elif text_node.text_type == "code":
            return LeafNode("code", text_node.text)
        elif text_node.text_type == "link":
            if "href" not in text_node.url:
                raise ValueError("Link text node must have a 'href' property.")
            return ParentNode("a", [LeafNode(None, text_node.text)], {"href": text_node.url})
        elif text_node.text_type == "image":
            if "src" not in text_node.url:
                raise ValueError("Image text node must have a 'src' property.")
            if "alt" not in text_node.url:
                raise ValueError("Image text node must have an 'alt' property.")
            return LeafNode("img", "", {"src": text_node.url["src"], "alt": text_node.url["alt"]})
        else:
            raise ValueError("Unsupported text node type.")

