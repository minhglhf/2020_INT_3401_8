# Bài 1:
+ Sử dụng manhattan để tính evaluationFunction
+ minDis = ∞
+ action = 'Stop' ? => trả về -∞
+ Ngược lại tìm min manhattan từ newPos của pacman tới ví trị food
+ trả về minDis
# Bài 2:
+ Nếu agent_index = 0 ? tìm max với tất cả các min của successor
+ Ngược lại tìm min với tất cả các max của successor
+ Trả về action tối ưu cho agent
# Bài 3:
+ Tương tự bài 2, thêm bước check nếu alpha cross beta (tức là alpha > beta)
+ thì cắt bỏ toàn bộ cây con còn lại của đỉnh đang xét
# Bài 4:
+ Áp dụng minimax cho pacman
+ Với ghost -> đi bất kì không cần tối ưu -> Cần nhân với 1/ actions của agent với score evaluationFunction
+ Trả về action tối ưu cho pacman