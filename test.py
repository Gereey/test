#用户交互层
def UI():
    print('请输入你的年级?')
    grade_input = input()
    while grade_input[0] not in ['一','二','三','四','五','六']:
        print('重新输入年级！')
        grade_input = input()
    grade = grade_input[0]
    print("请输入题目数量")
    num_test = int(input())
    num_right=offerTest(grade,num_test)
    print("结束！错了",str(num_right),'道题哦')