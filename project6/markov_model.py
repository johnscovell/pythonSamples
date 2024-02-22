from symboltable import SymbolTable
import stdio
import stdrandom
import sys


class MarkovModel(object):
    # Creates a Markov model of order k from the given text.
    def __init__(self, text, k):
        self._k = k
        self._st = {}
        circ_text = text + text[:k]
        for i in range(len(circ_text) - k):
            kgram = circ_text[i:i+k]
            next_char = circ_text[i+k]
            self._st.setdefault(kgram, {})
            self._st[kgram].setdefault(next_char, 0)
            self._st[kgram][next_char] += 1

    # Returns the order this Markov model.
    def order(self):
        return self._k

    # Returns the number of occurrences of kgram in this Markov model; and 0 if kgram is
    # nonexistent. Raises an error if kgram is not of length k.
    def kgram_freq(self, kgram):
        if self._k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' + str(self._k))

        if kgram in self._st:
            return sum((self._st[kgram]).values())
        else:
            return 0

    # Returns number of times character c follows kgram in this Markov model and 0 if kgram is
    # nonexistent or if it is not followed by c. Raises an error if kgram is not of length k.
    def char_freq(self, kgram, c):
        if self._k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' + str(self._k))

        if kgram in self._st and c in self._st[kgram]:
            return self._st[kgram][c]
        else:
            return 0

    # Returns a random character following kgram in this Markov model. Raises an error if kgram is
    # not of length k or if kgram is nonexistent.
    def rand(self, kgram):
        if self._k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' + str(self._k))
        if kgram not in self._st:
            raise ValueError('Unknown kgram ' + kgram)

        key_list = list(self._st[kgram].keys())
        value_list = list(self._st[kgram].values())
        rand = stdrandom.discrete(value_list)
        return key_list[rand]

    # Generates and returns a string of length n from this Markov model, the first k characters of
    # which is kgram.
    def gen(self, kgram, n):
        final = kgram
        while len(final) < n:
            final += self.rand(final[-self._k:])
        return final

    # Replaces unknown characters (~) in corrupted with most probable characters from this Markov
    # model, and returns that string.
    def replace_unknown(self, corrupted):

        # Given a list a, _argmax returns the index of the maximum value in a.
        def argmax(a):
            return a.index(max(a))

        original = ''
        for i in range(len(corrupted)):
            if corrupted[i] == '~':
                t = {}
                char = self._st[corrupted[i - self._k:i]].keys()
                for key in char:
                    rep = self.order() + 1
                    for q in range(rep):
                        kgram = corrupted[i - self._k + q:i + q].replace('~', key)
                        character = corrupted[i + q].replace('~', key)
                        if kgram in self._st:
                            p = (self.char_freq(kgram, character) / float(self.kgram_freq(kgram)))
                        else:
                            p = 0
                        if key in t:
                            t[key] *= p
                        else:
                            t.setdefault(key, p)

                x = argmax(list(t.values()))
                t_keys = list(t.keys())
                original += t_keys[x]
            else:
                original += corrupted[i]
        return original


# Unit tests the data type [DO NOT EDIT].
def _main():
    text = sys.argv[1]
    k = int(sys.argv[2])
    model = MarkovModel(text, k)
    a = []
    while not stdio.isEmpty():
        kgram = stdio.readString()
        char = stdio.readString()
        a.append((kgram.replace('-', ' '), char.replace('-', ' ')))
    for kgram, char in a:
        if char == ' ':
            stdio.writef('freq(%s) = %s\n', kgram, model.kgram_freq(kgram))
        else:
            stdio.writef('freq(%s, %s) = %s\n', kgram, char, model.char_freq(kgram, char))


if __name__ == '__main__':
    _main()
