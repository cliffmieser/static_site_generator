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
        attr = [f"{name}:{value}" for name, value in self.props.items() if self.props is not None]
        return f"{" ".join(attr)}" if self.props is not None else ""
    
    def __repr__(self):
        print(f"Tag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps: {self.props}")