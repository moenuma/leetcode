class Solution:
    # Time: O(n)
    # Space: O(n)
    def simplifyPath1(self, path: str) -> str:
        pathList = path.split("/")
        pathStack = []
        
        for path in pathList:
            if not path or path == ".":
                continue
            if path == "..":
                if pathStack:
                    pathStack.pop()
            else:
                pathStack.append(path)
        
        res = "/" + "/".join(pathStack)
        return res
    
    def simplifyPath2(self, path: str) => str:
        stack = []
        cur = "" # current file or directory name

        for c in path + "/":
            if c == "/":
                if cur == "..":
                    if stack:
                        stack.pop()
                elif cur != "" and cur != ".":
                    stack.append(cur)
                cur = ""
            else:
                cur += c

        return "/" + "/".join(stack)