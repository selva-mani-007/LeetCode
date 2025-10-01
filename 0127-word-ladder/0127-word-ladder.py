class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        q = deque()
        q.append((beginWord,1))

        if beginWord in word_set:
            word_set.remove(beginWord)

        while q:
            word,steps = q.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):
                for ch in 'qwertyuiopasdfghjklzxcvbnm':
                    new_word = word[:i] + ch + word[i+1:]

                    if new_word in word_set:
                        word_set.remove(new_word)
                        q.append((new_word,steps+1))
        
        return 0
