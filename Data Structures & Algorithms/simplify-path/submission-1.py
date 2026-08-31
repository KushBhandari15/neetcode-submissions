class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        i = 0
        n = len(path)
        while i < n:
            while i < n and path[i] == "/":
                i += 1

            directory = ""
            while i < n and path[i] != "/":
                directory += path[i]
                i += 1
            
            if directory == "..":
                if stack:
                    stack.pop()
            elif directory == ".":
                pass
            else:
                if directory:
                    stack.append(directory)
            


        
        print(stack)
        path = '/'.join(stack)
        path = '/' + path

        return path