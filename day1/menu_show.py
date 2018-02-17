#-*- coding:utf-8-*- 
#__author__ = 'linux vfast'

# 1. 运行程序输出第一级菜单
# 2. 选择一级菜单某项，输出二级菜单，同理输出三级菜单
# 3. 菜单数据保存在文件中
# 4. 让用户选择是否要退出
# 5. 有返回上一级菜单的功能


data = {
    "电器":{
        "厨房电器":{
             "热水壶":['苏泊尔','九阳','半球'],
             "电饭煲":['美的','飞利浦','大松'],
             "电磁炉":['美的','苏泊尔','九阳'],
             "微波炉":['美的','格兰仕','松下']
         },
        "卫浴电器":{
             "浴霸":{'奥普','长虹','新飞'},
             "排风扇":['奥普','正野','艾美特']
         },
        "家用电器":{
             "电视":['海信','创维','TCL'],
             "空调":['格力','至高'],
             "洗衣机":['海尔','澳柯玛','容声']
         },
    },
    "服装":{
        "男装":{
             "外套":['羽绒服','夹克','卫衣'],
             "毛衣":['羊毛衫','针织衫'],
             "裤子":['牛仔裤','休闲裤','沙滩裤']
         },
        "女装":{
             "外套":['羽绒服','夹克'],
             "裤子":['牛仔裤','弹力裤','热裤'],
             "裙子":['连衣裙','短裙']
         },
    },
    "数码":{
         "电脑":{
             "笔记本":['游戏本','超极本','商务本'],
             "配件":['显示器','电源','CPU','内存','硬盘','键鼠','主板'],
             "平板":['iOS','Android','Windows']
         },
         "手机":{
             "华为":['mete10','P10','V9'],
             "苹果":['Iphone8','Iphone8PLUS','IphoneX'],
             "小米":['小米6','小米MIX2','红米']
         },
    },
}
'''
while True:
    for menu_1 in data:
        print(menu_1)
    # break
    choice = input('选择进入:')
    if choice in data:
        while True:
            for menu_2 in data[choice]:
                print('\t',menu_2)
            choice_2 = input('选择进入:')
            if choice_2 in data[choice]:
                while True:
                    for menu_3 in data[choice][choice_2]:
                        print('\t\t',menu_3)
                    choice_3 = input('选择进入:')
                    if choice_3 in data[choice][choice_2]:
                        for menu_4 in data[choice][choice_2][choice_3]:
                            print('\t\t\t',menu_4)
                        choice_4 = input('最后一层,按b返回:')
                    if choice_3 == 'b':
                        break
            if choice_2 == 'b':
                break
'''

while True:
    for menu_1 in data:
        print(menu_1)
    choice = input('选择进入:')
    if choice in data:
        for menu_2 in data[choice]:
            print('\t',menu_2)
        choice_2 = input('选择进入:')
        if choice_2 in data[choice]:
            for menu_3 in data[choice][choice_2]:
                print('\t\t',menu_3)
            choice_3 = input('选择进入:')
            if choice_3 in data[choice][choice_2]:
                for menu_4 in data[choice][choice_2][choice_3]:
                    print('\t\t\t',menu_4)
                choice_4 = input('已经是最后一层，按b返回上一层:')
                if choice_4 == 'b':
                    for menu_3 in data[choice][choice_2]:
                        print('\t\t', menu_3)
                    choice_3 = input('选择进入:')
            if choice_3 == 'b':
                for menu_2 in data[choice]:
                    print('\t', menu_2)
                choice_2 = input('选择进入:')
        if choice_2 == 'b':
            for menu_1 in data:
                print(menu_1)
            choice = input('选择进入:')


