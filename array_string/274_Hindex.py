class Solution:
    # O(nlog(n))
    def hIndex1(self, citations: List[int]) -> int:
        N = len(citations)
        citations.sort()

        for idx, citation in enumerate(citations):
            if N-idx <= citation:
                return N-idx
        return 0

    # O(n)
    def hIndex2(self, citations: List[int]) -> int:
        # [3,0,6,1,5]
        # [1,1,0,1,0,2] extra memory space
        #  0 1 2 3 4 5
        # each index represents the total count of citations for the index number
        N = len(citations)
        temp = [0 for _ in range(N+1)]

        for idx, citation in enumerate(citations):
            if citation > N:
                temp[N] += 1
            else:
                temp[citation] += 1
        total = 0
        for idx in range(N,-1,-1):
            total += temp[idx]
            if total >= idx:
                return idx
                