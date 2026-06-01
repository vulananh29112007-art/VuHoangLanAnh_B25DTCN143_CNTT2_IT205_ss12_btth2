saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

while True:
    print("""
===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====
1. Xem danh sách sổ tiết kiệm
2. Mở sổ tiết kiệm mới
3. Cập nhật thông tin sổ tiết kiệm
4. Tất toán hoặc xóa sổ tiết kiệm
5. Tính lãi dự kiến khi đến hạn
6. Kiểm tra điều kiện rút trước hạn
7. Thoát chương trình
"""
    )

    choice = input("Mời bạn chọn chức năng (1-5): ")
    if not choice.isdigit():
        print("Chỉ nhập lựa chọn 1-5: ")
        continue
    choice = int(choice)

    match choice:
        case 1:
            if len(saving_accounts) == 0:
                print("Danh sách sổ tiết kiệm hiện đang trống")
                continue

            print("Danh sách sổ tiết kiệm:")
            for index, user in enumerate(saving_accounts, start = 1):
                print(f"Mã sổ: {user['account_id']:<8} | Khách hàng: {user['customer_name']:<15} | Số tiền gửi: {user['balance']:<10} | Kỳ hạn: {user['term_months']:<3} tháng | Lãi suất: {user['interest_rate']:<6}%/năm | Trạng thái: {user['status']}")
               
        case 2:
            while True:
                new_account_id = input("Nhập mã sổ tiết kiệm mới: ").strip().upper()
                for user in saving_accounts:
                    if user["account_id"] == new_account_id:
                        print("Mã sổ tiết kiệm không được trùng")
                        break
                else:
                    break
            while True:
                new_customer_name = input("Nhập tên khách hàng: ")
                if new_customer_name == "":
                    print("Tên khách hàng không được để trống")
                    continue
                break
            while True:
                new_balance = input("Nhập số tiền gửi: ")
                if not new_balance.isdigit(): 
                    print("Số tiền gửi không hợp lệ")
                    continue
                new_balance = float(new_balance)
                if new_balance <= 0:
                    print("Số tiền gửi không hợp lệ")
                    continue
                break
            while True:
                new_term_months = input("Nhập kỳ hạn gửi theo tháng: ")
                if not new_term_months.isdigit():
                    print("Nhập kỳ hạn theo tháng không hợp lệ")
                    continue
                new_term_months = int(new_term_months)
                if new_term_months <= 0:
                    print("Nhập kỳ hạn theo tháng không hợp lệ")
                    continue
                break
            while True:
                new_interest_rate = input("Nhập lãi suất năm: ")
                if not new_interest_rate.isdigit():
                    print("Nhập lãi suất năm không hợp lệ")
                    continue
                new_interest_rate = float(new_interest_rate)
                if new_interest_rate <= 0:
                    print("Nhập lãi suất năm không hợp lệ")
                    continue
                break
            saving_accounts.append({
                "account_id": new_account_id,
                "customer_name": new_customer_name,
                "balance": new_balance,
                "term_months": new_term_months,
                "interest_rate": new_interest_rate,
                "status": "active"
            })

        case 3:
            update_account_id= input("Nhập mã sổ tiết kiệm cần cập nhật:").strip().upper()
            for user in saving_accounts:
                if user["account_id"] == update_account_id:
                    if user["status"] == "active":
                        while True:
                            user["customer_name"] = input("Nhập tên khách hàng mới: ")
                            if user["customer_name"] == "":
                                print("Tên khách hàng không được để trống")
                                continue
                            break
                        while True:
                            user["balance"] = input("Nhập số tiền gửi mới: ")
                            if not user["balance"].isdigit():
                                print("Số tiền gửi không hợp lệ")
                                continue
                            user["balance"] = float(user["balance"])
                            if user["balance"] <= 0:
                                print("Số tiền gửi không hợp lệ")
                                continue
                            break
                        while True:
                            user["term_months"] = input("Nhập kỳ hạn gửi theo tháng mới: ")
                            if not user["term_months"].isdigit():
                                print("Nhập kỳ hạn theo tháng không hợp lệ")
                                continue
                            user["term_months"] = int(user["term_months"])
                            if user["term_months"] <= 0:
                                print("Nhập kỳ hạn theo tháng không hợp lệ")
                                continue
                            break
                        while True:
                            user["interest_rate"] = input("Nhập lãi suất năm mới: ")
                            if not user["interest_rate"].isdigit():
                                print("Nhập lãi suất năm không hợp lệ")
                                continue
                            user["interest_rate"] = int(user["interest_rate"])
                            if user["interest_rate"] <= 0:
                                print("Nhập lãi suất năm không hợp lệ")
                                continue
                            break
                    else:
                        print("Không thể cập nhật sổ tiết kiệm đã tất toán!")
                        break
            else:
                print("Không tìm thấy mã sổ tiết kiệm!")
                break
        case 4:
            settlement_account_id = input("Nhập mã sổ tiết kiệm cần tất toán/xóa: ").strip().upper()
            for user in saving_accounts:
                if user["account_id"] == settlement_account_id:
                    user["status"] = "closed"
                    break
            else:
                print("Không tìm thấy mã sổ tiết kiệm cần tất toán/xóa")
        
        case 5:
            interest_account_id = input("Nhập mã sổ tiết kiệm cần tính lãi: ").strip().upper()
            for user in saving_accounts:
                if user["account_id"] ==  interest_account_id and user["status"] == "active":
                    interest = user["balance"] * (user["interest_rate"] / 100) * (user["term_months"] / 12)
                    total_money = user["balance"] + interest 
                    print(f"Tiền lãi dự kiến: {interest}")
                    print(f"Tổng tiền nhận khi đến hạn: {total_money}")

            else:
                print("Không tìm thấy mã sổ tiết kiệm!")
        
        case 6:
            withdraw_account_id = input("Nhập mã sổ tiết kiệm cần kiểm tra: ").strip().upper()
            while True:
                actual_months = input("Nhập số tháng thực gửi: ")
                if not actual_months.isdigit():
                    print("Số tháng thực gửi không hợp lệ")
                    continue
                actual_months = int(actual_months)
                if actual_months <= 0:
                    print("Số tháng thực gửi không hợp lệ")
                    continue
                break

            for user in saving_accounts:
                if user["account_id"] == withdraw_account_id and user["status"] == "active": 
                    if actual_months < user["term_months"]:
                        interest = user["balance"] * (0.5 / 100) * (actual_months / 12) 
                        total_money = user["balance"] + interest 
                        print(f"Tiền lãi dự kiến: {interest}")
                        print(f"Tổng tiền nhận khi đến hạn: {total_money}")
                    else:
                        interest = user["balance"] * (user["interest_rate"] / 100) * (actual_months / 12)
                        total_money = user["balance"] + interest 
                        print(f"Tiền lãi dự kiến: {interest}")
                        print(f"Tổng tiền nhận khi đến hạn: {total_money}")
                break
            else:
                print("Không tìm thấy mã sổ tiết kiệm!")

        case 7:
            print("Thoát chương trình")
        case _:
            print("Lựa chọn không hợp lệ")

    
