from collections import deque

class Solution:
    
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        # write your code here
        if not image or not len(image[0]) or x is None or y is None:
            return 0
        
        n = len(image)
        m = len(image[0])
        top, bottom, left, right = x, x, y, y
        q = deque([(x, y)])
        visited = set([(x, y)])
        
        # bfs find vertices
        while q:
            x_, y_, is_v, is_h = q.popleft()            
            top = min(top, x_)
            bottom = max(bottom, x_)
            left = min(left, y_)
            right = max(right, y_)
            
            left_ = self.find_left(image, x_, y_)
            if (x_, left_) not in visited:
                q.append((x_, left_))
                visited.add((x_, left_))
                
            right_ = self.find_right(image, x_, y_)
            if (x_, right_) not in visited:
                q.append((x_, right_))
                visited.add((x_, right_))
                    
            top_ = self.find_top(image, x_, y_)
            if (top_, y_) not in visited:
                q.append((top_, y_))
                visited.add((top_, y_))
            
            bottom_ = self.find_bottom(image, x_, y_)
            if (bottom_, y_) not in visited:
                q.append((bottom_, y_))
                visited.add((bottom_, y_))
        
        return (bottom - top + 1) * (right - left + 1)
        
        
    def find_top(self, image, x, y):
        start = 0
        end = x
        while start + 1 < end:
            mid = (start + end) / 2
            if image[mid][y] == '1':
                end = mid
            else:
                start = mid
        
        if image[start][y] == '1':
            return start
        
        return end
    
    def find_bottom(self, image, x, y):
        start = x
        end = len(image)-1
        while start + 1 < end:
            mid = (start + end) / 2
            if image[mid][y] == '0':
                end = mid
            else:
                start = mid
        
        if image[end][y] == '1':
            return end
        
        return start
    
    def find_left(self, image, x, y):
        start = 0
        end = y
        while start + 1 < end:
            mid = (start + end) / 2
            if image[x][mid] == '1':
                end = mid
            else:
                start = mid
        
        if image[x][start] == '1':
            return start
        
        return end
    
    def find_right(self, image, x, y):
        start = y
        end = len(image[0])-1
        while start + 1 < end:
            mid = (start + end) / 2
            if image[x][mid] == '0':
                end = mid
            else:
                start = mid
        
        if image[x][end] == '1':
            return end
        
        return start
        

if __name__ == '__main__':
    sol = Solution()

    image = ["0010","0110","0100"]

    print sol.minArea(image, 0, 2)
        
                