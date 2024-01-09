class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bankSet = set(bank)
        
        queue = deque()
        queue.append((startGene, 0)) # (gene, numOfMutation)
        visit = set()

        while queue:
            gene, num = queue.popleft()
            if gene == endGene:
                return num

            for i in range(len(startGene)):
                for c in 'ACGT':
                    nextGene = gene[:i] + c + gene[i+1:]
                    if nextGene not in visit and nextGene in bankSet:
                        queue.append((nextGene, num+1))
                        visit.add(nextGene)
        
        return -1