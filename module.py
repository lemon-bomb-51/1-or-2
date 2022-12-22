#입력되는 변수가 True여야 함수가 실행됩니다.
def jayunsu_only_abs(answer_abs):
    if answer_abs == True:
        jayunsu = input("홀/수를 판단합니다. 수를 입력해 주세요:")
        '''
        -0.1 형식, 0.1형식, 0, 1, 2, -1, -2를 input로 받아올 시
        정수만을 구별하는 함수
        '''
        if '-' not in jayunsu and '.' not in jayunsu:
            jayunsu = int(jayunsu)
            if jayunsu > 0:
                if jayunsu%2 == 0:
                    print("짝수 입니다.")
                else:
                    print("홀수 입니다.")
            else:
                print("0 보다 큰 수를 입력해 주세요")
        else:
            print("정수를 입력해 주세요")
