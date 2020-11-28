# python-AI-learning
Đại học Công nghệ - Đại học Quốc Gia Hà Nội - Trí Tuệ nhân tạo
# Bài 1 : DFS
* Define state: node, action, cost;
* Initial State
+ Stack: chứa các state
+ Visited_list: đánh dấu các nút đã thăm
+ cost: tổng chi phí đạt được goal state
* Ý tưởng:
- Push vào stack state ban đầu
- Duyệt vòng lặp với điều kiện stack khác rỗng
- Nếu đỉnh của stack được lấy ra và là goal state thì return actions
- Ngược lại, thêm tất cả các successors của đỉnh của state hiện tại vào stack
- Lặp lại cho đến khi đạt được goal state
# Bài 2: BFS
+ Sử dụng queue
+ Enqueue lần lượt các đỉnh kề của 1 đỉnh (nếu đỉnh đó chưa được thăm) cho đến khi đạt được trạng thái mong muốn hoặc duyệt hết các đỉnh trên đồ thị thì thuật toán kết thúc
# Bài 3: USC
+ Sử dụng priorityQueue
+ Khởi đầu từ trạng thái ban đầu => enqueue(start_state)
+ Đưa tất cả các đỉnh kề với đỉnh đang xét vào priorityQueue (bao gồm có chi phí tới đỉnh đó)
+ Lần lượt mở rộng các nút từ queue và thực hiện lại bước trên cho đến khi đạt được goal state hoặc queue rỗng thì thuật toán kết thúc
# Bài 4: A*
+ Sử dụng priorityQueue và hàm heuristic
+ Hàm heuristic ước lượng khoảng cách từ node n đến node goal
+ f(n) = g(n) + h(n)
+ Đưa lần lượt các đỉnh kề với node đang xét vào priorityQueue với độ ưu tiên f(n)
+ Lần lượt lấy ra từ quêu và lặp lại bước trên. Cho đến khi đạt được goal state hoặc queue rỗng thì thuật toán kết thúc
# Bài 5: Finding All the Corners <Cài đặt CornersProblem>
+ State bao gồm: current_node và các corners đã đi tới
+ getStartState(): trả về trạng thái ban đầu
+ isGoalState():
+ Nếu current_node chưa có trong self.corners và chưa có trong các corners đã đi qua thì thêm nó vào list các corners đã đi qua
+ Kiểm tra nếu length của list các corners đã đi qua bằng 4 thì return True, ngược lại return False
+ getSuccessors():
+ Nếu đỉnh tiếp theo tại không chạm phải wall thì:
+ Nếu là corner và chưa thăm thì append vào list corners sẽ thăm tại đỉnh đó
+ successor trả về bao gồm node và các corners
# Bài 6: Corners Problem: Heuristic
+ Implement cornersHeuristic():
+ Get unvisitedCorners
+ Vòng lặp với điều kiện lặp len(unvisitedCorners) > 0:
+ Tìm min của khoảng các manhattan từ 1 đỉnh chưa thăm đến các đỉnh góc, cộng dồn vào heuristic

# Bài 7: Eating All The Dots
+ Using mazeDistance function
+ Return max mazeDistance của current_node tới các điểm có dấu chấm tròn.
+ Thực hiện A* với heuristic trả về bên trên

# Bài 8: Suboptimal Search
+ Dùng bfs để ăn các chấm liền kề