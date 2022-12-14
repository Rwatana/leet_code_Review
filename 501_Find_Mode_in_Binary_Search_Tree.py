# T(n)
# S(n)
class Solution(object):
    
    def findMode(self, root):
        if not root:
            return []
        map_ = {}
        self.getFrequency(root, map_)
        mode = max(map_.values())
        res = []
        for i in map_:
            if map_[i] == mode:
                res.append(i)
        return res
        
    def getFrequency(self, root, map_):
        if not root:
            return
        else:
            if (root.val in map_):
                map_[root.val] += 1
            else:
                map_[root.val] = 1
            self.getFrequency(root.left, map_)
            self.getFrequency(root.right, map_)
