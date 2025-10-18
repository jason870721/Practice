import random
from time import sleep


#產生中獎號碼
def generate_winning_numbers(count=6, start=1, end=50):
    winning_numbers = random.sample(range(start, end), count)
    winning_numbers.sort()
    return winning_numbers

#獲得使用者號碼
def get_user_number(i, selected_numbers):
    while True:
        user_input = input(f"請輸入第'{i}'個數字：: ").strip().lower()

        if user_input == "":
            print("「不能空白，請輸入一個數字！」")
            continue

        try:
            num = int(user_input)
        except ValueError:
            print("輸入非數字：「請輸入數字！」")
            continue

        if num in selected_numbers:
            print("「這個數字已經選過了，請選擇其他數字！」")
            continue

        if not (1 <= num <= 49):
            print("數字超出範圍：「數字必須在1-49之間！」")
            continue

        user_input_confirm = input("確認嗎？(y/n)：")

        if user_input_confirm == "y":
            return num
            break
        elif user_input_confirm == "n":
            print("請再次輸入想要的數字")
            continue
        else:
            print("----請輸入 y/n----")

#取得使用者中獎結果
def get_user_prize_result(selected_numbers, winning_numbers):
    winning_analysis = []
    prize_dict = {
        6: "頭獎",
        5: "二獎",
        4: "三獎",
        3: "四獎"
    }
    count = 0

    for num in selected_numbers:
        if num in winning_numbers:
            winning_analysis.append(num)
            print(f"✓ {num} - 中！")
            count += 1

    if count >= 3:
        print(f"恭喜！您中了 {count} 個號碼，獲得{prize_dict[count]}！")
    else:
        print(f"您只中了 {count} 個號碼，沒中獎。")



if __name__ == "__main__":
    while True:
        selected_numbers = []
        winning_numbers = generate_winning_numbers()
        print(winning_numbers)
        print("歡迎來到樂透遊戲！規則：請選擇6個不重複的數字（1 - 49)")
        for i in range(1, 7):
            num = get_user_number(i, selected_numbers)
            selected_numbers.append(num)
            print(f"已選擇 {num}，目前選擇的數字有: {selected_numbers}")

        print("開獎階段\n開始開獎...")
        sleep(1)
        for i in range(3):
            print("🎲 開獎中...")
            sleep(1)

        get_user_prize_result(selected_numbers, winning_numbers)

        print("繼續遊戲")
        next_round = input("是否要進行下一輪遊戲？(y/n)：")

        if next_round == "y":
            print("下一輪遊戲開始！")
            continue
        elif next_round == "n":
            break
        else:
            print("----請輸入 y/n----")




