class SymbolNode:
    
    def __init__(self, start_symbol=None, symbolic_str=''):
        self.start_symbol = start_symbol
        self.raw_str = raw_str
        self.children = []


class SymbolTree:
    
    def __init__(self, startSymbol):
        self.root = SymbolNode(startSymbol)
    
    def parse_node(self, raw_str):
        start_symbol = None

        for i, c in enumerate(raw_str):
            if c.isupper():
                start_symbol = c
            else:
                symbolic_str += c
        
        return SymbolNode(start_symbol, symbolic_str)
    
    def search(self, root, start_symbol):
        if root.start == start_symbol:
            return root
        
        for child in root.children:
            node = self.search(child, start_symbol)
            if node:
                return node
                
        return None
    
    def add_node(self, start_symbol, raw_str):
        child = self.parse_node(raw_str)
        
        parent = self.search(self.root, start_symbol)
        if not parent:
            return
    
        parent.children.append(child)
   

class Solution:
    
    """
    @param generator: Generating set of rules.
    @param startSymbol: Start symbol.
    @param symbolString: Symbol string.
    @return: Return true if the symbol string can be generated, otherwise return false.
    """
    def canBeGenerated(self, generator, startSymbol, symbolString):
        # Write  your code here.
        if not generator or not startSymbol or not symbolString:
            return False
            
        tree = SymbolTree(startSymbol)
        for rule in generator:
            start_sumbol, raw_str = rule.split(' -> ')
            tree.add_node(start_sumbol, raw_str)
            
        return self.find_symbol(tree.root, '', symbolString)
        
    def find_symbol(self, root, prevString, symbolString):
        curString = prevString + root.symbol_str
        print root.start, curString

        if not root.start and curString == symbolString:
            return True
        
        for child in root.children:
            if self.find_symbol(child, curString, symbolString):
                return True
        
        return False
        
        
if __name__ == '__main__':
    sol = Solution()

    generator = ["S -> abc", "S -> aA", "A -> b", "A -> c"]
    startSymbol = 'S'
    symbolString = 'ac'
    #print sol.canBeGenerated(generator, startSymbol, symbolString)

    generator = ["S -> abcd", "S -> A", "A -> abc"]
    symbolString = 'abc'
    #print sol.canBeGenerated(generator, startSymbol, symbolString)

    generator = ["S -> abc", "S -> aA", "A -> b", "A -> c"]
    symbolString = 'a'
    #print sol.canBeGenerated(generator, startSymbol, symbolString)

    generator = ["S -> abcd", "S -> A", "A -> abc"]
    symbolString = 'ab'
    print sol.canBeGenerated(generator, startSymbol, symbolString)



