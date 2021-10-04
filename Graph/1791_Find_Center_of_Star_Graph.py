class Solution:
    def findCenter(self, e):
        return (set(e[0]) & set(e[1])).pop()
