#-*- coding:utf-8-*- 
#__author__ = 'linux vfast'

def login_user():
    '''登录用户并且保存用户和密码，超过三次密码错误锁定'''
    #检查用户是否被锁定
    username = input('please input your name:')
    lock_info = []
    with open('lock_user.txt','r',encoding='utf-8') as lock_file:
        for lock_user in lock_file:
            # print(lock_user)
            lock_info.append(lock_user)
    lock_file.close()

    if username in lock_info:
        print('The user [%s] has been locked'% username)
        exit()
    #读取用户列表
    user_info = []
    with open('user_info.txt','r') as user_file:
        for user in user_file:
            user_info.append(user.strip('\n').split())
    user_file.close()
    # print(user_info)

    #判断密码输入是否超过三次，超过三次锁定
    count = 0
    flag_test = True
    while flag_test:
        if username not in lock_user:
            for user_list in user_info:
                if user_list[0] == username:
                    # print(user_list[0])
                    # print(user_list[1])
                    password = input('please input your password:')
                    if password == user_list[1]:
                        print('welcome user [%s] login system!'% username)
                        flag_test = False
                    else:
                        count += 1
                        if count > 2:
                            print('The user [%s] password input error more than three times has been locked' % username)
                            with open('lock_user.txt','a',encoding='utf-8') as write_file:
                                write_file.writelines('\n' + username)
                            write_file.close()
                            flag_test = False
                        else:
                            print('Wrong password,try again')

            else:
                print('user [%s] not exist'% username)
                break

login_user()