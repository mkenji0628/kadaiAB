gyou = int(input('行数を入力してください: '))
retu = int(input('列数を入力してください: '))

for cnt1 in range(1, gyou + 1):
    for cnt2 in range(1, retu + 1):
        # print(cnt1, '✕', cnt2, '=', cnt1 * cnt2, end=' | ')
        print(f" {cnt1} × {cnt2} = {str(cnt1 * cnt2).rjust(2)}", end=" | ")

    print('\n', end='')
