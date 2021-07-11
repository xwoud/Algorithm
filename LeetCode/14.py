class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        else:
            max_string = ''
            root = strs[0]

            i, counter = 1, 1

            while i <= len(root):
                if root[:i] == strs[counter][:i]:
                    if counter < len(strs) - 1:
                        counter += 1
                        continue
                    else:
                        max_string = root[:i]
                        i += 1
                        counter = 1
                        continue
                else:
                    break
        return max_string
