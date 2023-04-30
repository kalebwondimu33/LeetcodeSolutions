class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        hashtable = {
		'a': '.-',   'b': '-...', 'c': '-.-.', 'd': '-..',  'e': '.',    'f': '..-.', 'g': '--.',
		'h': '....', 'i': '..',   'j': '.---', 'k': '-.-',  'l': '.-..', 'm': '--',   'n': '-.',
		'o': '---',  'p': '.--.', 'q': '--.-', 'r': '.-.',  's': '...',  't': '-',    'u': '..-',
		'v': '...-', 'w': '.--',  'x': '-..-', 'y': '-.--', 'z': '--..',
	}
        unique=set()
        for i in words:
            count=""
            for j in i:
                count+=hashtable[j]
            unique.add(count)
        return len(unique)
                   