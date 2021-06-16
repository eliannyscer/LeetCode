class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        memo = {}
        words = set(words)

        def longest_chain(w):
            if w not in memo:
                max_chain = 1
                for i in range(len(w)):
                    nxt = w[:i] + w[i + 1:]
                    if nxt in words:
                        max_chain = max(1 + longest_chain(nxt), max_chain)
                memo[w] = max_chain
            return memo[w]

        for w in words:
            longest_chain(w)

        return max(memo.values())