


class HTMLNode: 
    def __init__(self, tag = None, value = None, children = None, props = None):
        """ 
        Represents and HTML node like <p>, outputs HTML 
            tag: string representation of the html node 
            value: value inside the html tag (text in paragraph for ex)
            children: list of HTMLNode objects representing the child of the node  
            props: dict of key-val paries reprenting attributes for the tag 
            (Ex: <a> tag may have {"href": "https://www.google.com"} )
        """ 

        self.tag = tag 
        self.value = value 
        self.children = children 
        self.props = props 

    def to_html(self): 
        raise NotImplementedError("Not implemented") 
    
    def props_to_html(self): 
        if self.props is not None:
            attr = [f"{name}:{value}" for name, value in self.props.items() if self.props is not None]
            return f"{" ".join(attr)}" if self.props is not None else ""
        else:
            return 
    def __repr__(self):
        return f"Tag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps: {self.props}"


class ParentNode(HTMLNode): 
    """
        A child class of HTMLNode which handles nesting of HTML nodes inside one another.
        Parent nodes are defined as HTML nodes that aren't leaf nods (i.e it has children)
    """
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Argument `tag` is required.")
        elif self.children is None:
            raise ValueError("Parent nodes must have children.")
        else:
            children_html = ""
            for child in self.children:
                children_html += child.to_html() 
            return f"<{self.tag}{f"" if self.props is None else f" {self.props.to_html}"}>{children_html}</{self.tag}>"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None: 
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None: 
            return f"{self.value}" 
        
        if self.props is not None:
            tag = f"{self.tag}" # to append to original tag if not None
            attributes = [(attr, name) for attr, name in self.props.items()]
            if attributes:
                for attr in attributes:
                    tag += f" {attr[0]}={attr[1]}"
                return f"<{tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"Tag: {self.tag}\nValue: {self.value}\nProps: {self.props}"

    

