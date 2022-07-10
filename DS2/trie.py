class Trie:
    head = {}

    def add(self, word):
        current = self.head

        for ch in word:
            if ch not in current:
                current[ch] = {}
            current = current[ch]
        current["*"] = True

    def search(self, word):
        current = self.head

        for ch in word:
            if ch not in current:
                return False
            current = current[ch]
        if "*" in current:
            return True
        else:
            return False


dictionary = Trie()
dictionary.add("hi")
dictionary.add("hello")
print(dictionary.search("hi"))
print(dictionary.search("hello"))
print(dictionary.search("hey"))
