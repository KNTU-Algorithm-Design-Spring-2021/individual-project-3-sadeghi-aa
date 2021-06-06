def parse(sentence, previous=None):
    if not previous:
        sentence = sentence.lower()
    if sentence is '':
        return previous
    else:
        length = len(sentence)
        for i in list(range(2, length + 1)) + [1]:
            nextWord = sentence[0:i]
            if nextWord in wordSet:
                remSentence = sentence[i:]
                found = parse(remSentence, nextWord)
                if found:
                    if previous:
                        return f"{previous} {found}"
                    else:
                        return f"{found}"
        if not previous:
            return "This sentence can't be parsed :("



f = open('The_Oxford_3000.txt', 'r')
wordSet = set([s.lower() for s in f.read().split()])

if __name__ == '__main__':
    sentence = "IHOPETHISISOURLASTPROJECTINTHISCOURSE"
    print(parse(sentence))

    sentence = 'WEAREVERYTIREDRIGHTNOW'
    print(parse(sentence))

    sentence = 'SLEEPISINTHEDICTIONARY'
    print(parse(sentence))

    sentence = 'SLEEPYISNOTINTHEDICTIONARY' # Sleepy is not in the dictionary
    print(parse(sentence))
