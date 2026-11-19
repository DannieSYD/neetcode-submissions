class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def bfs(money, coins):
            if money == 0:
                return 0

            i = 0

            queue = deque([money])

            while queue:
                level_size = len(queue)
                i += 1
                visited = {money}
                
                for _ in range(level_size):
                    a = queue.popleft()
                    for n in coins:
                        if a - n > 0 and (a - n) not in visited:
                            queue.append(a - n)
                            visited.add(a - n)
                        elif a - n == 0:
                            return i
            
            return -1
        
        i = bfs(amount, coins)
        
        return i