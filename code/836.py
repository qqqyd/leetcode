"""
836. 矩形重叠
矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。
如果相交的面积为正，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。
给出两个矩形，判断它们是否重叠并返回结果。
示例 1：
输入：rec1 = [0,0,2,2], rec2 = [1,1,3,3]
输出：true

我的思想：

优解思想：

收获：

"""

def solution(rec1, rec2):
    # rec1: List[int], rec2: List[int]
    return not (rec1[0] >= rec2[2] or rec2[0] >= rec1[2] or rec1[1] >= rec2[3] or rec2[1] >= rec1[3])
    
def excellent():
    pass

if __name__ == '__main__':
    rec1 = [0,0,2,2]
    rec2 = [1,1,3,3]
    print(solution(rec1, rec2))
