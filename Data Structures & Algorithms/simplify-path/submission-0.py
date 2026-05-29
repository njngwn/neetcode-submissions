class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")
        path_stack = []

        for p in path_list:
            if p == "..":
                if path_stack: path_stack.pop()
            elif p and p != ".":
                path_stack.append(p)

        return "/" + "/".join(path_stack)
        