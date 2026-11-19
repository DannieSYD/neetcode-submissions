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
                        r = a - n
                        if r > 0 and (r) not in visited:
                            queue.append(r)
                            visited.add(r)
                        elif r == 0:
                            return i
            
            return -1
        
        i = bfs(amount, coins)
        
        return i