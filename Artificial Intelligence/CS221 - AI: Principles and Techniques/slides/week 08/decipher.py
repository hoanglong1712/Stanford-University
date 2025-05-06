import re
import string

def readText(filename: str) -> str:
    with open(filename, 'r') as f:
        return re.sub('[^a-z ]', '', f.read().strip().lower())

languageModel = readText('lm.train')
cipherText = readText('ciphertext')

# all allowed characters
domain = string.ascii_lowercase + ' '

### Initialize HMM

# startProbs[h] = p_start(h)
# Uniform distribution (we could estimate from language model, but it's not necessary)
startProbs : dict[str, float] = {c: 1./len(domain) for c in domain}

# transitionProbs[h1][h2] = p_trans(h2 | h1)
# Estimate this from lm.train (some long English text)
transitionCounts : dict[tuple[str, str], int] = {(h1, h2): 0 for h1 in domain for h2 in domain}
occurenceCounts : dict[str, int] = {h: 0 for h in domain}
for h1, h2 in zip(languageModel[:-1], languageModel[1:]):
    transitionCounts[h1, h2] += 1
    occurenceCounts[h1] += 1
transitionProbs : dict[tuple[str, str], int] = {(h1, h2): transitionCounts[h1, h2] / occurenceCounts[h1] for (h1, h2) in transitionCounts}

# emissionProbs[h][e] = p_emit(e | h)
# Initialize it to uniform distribution (or we could randomly initialize)
emissionProbs : dict[tuple[str, str], float] = {(h, e): 1. / len(domain) for h in domain for e in domain}

def normalize(d: dict[str, float]) -> dict[str, float]:
    s = sum(d.values())
    return {k: v / s for k, v in d.items()}

def forwardBackward(observations, startProbs, transitionProbs, emissionProbs):
    n = len(observations)
    forwardMessage = normalize({h: startProbs[h]*emissionProbs[h, observations[0]] for h in domain})
    F : list[dict[str, float]] = [forwardMessage]
    for o in observations[1:]:
        newForwardMessage = {h: 0. for h in domain}
        for h1 in domain:
            for h2 in domain:
                newForwardMessage[h2] += forwardMessage[h1] * transitionProbs[h1, h2] * emissionProbs[h2, o]
        forwardMessage = normalize(newForwardMessage)
        F.append(forwardMessage)
    backwardMessage = normalize({h: 1. for h in domain})
    B : list[dict[str, float]] = [backwardMessage]
    for o in reversed(observations[1:]):
        newBackwardMessage = {h: 0. for h in domain}
        for h1 in domain:
            for h2 in domain:
                newBackwardMessage[h1] += backwardMessage[h2] * transitionProbs[h1, h2] * emissionProbs[h2, o]
        backwardMessage = normalize(newBackwardMessage)
        B.append(backwardMessage)
    B = list(reversed(B))
    q : list[dict[str, float]] = [
        normalize({h: f[h] * b[h] for h in domain})
        for f, b in zip(F, B)
    ]
    return q

def guess(q: list[dict[str, float]]) -> str:
    return ''.join([max(p, key=lambda h: p[h]) for p in q])

### Run EM

for t in range(2000):
    # E-step
    q = forwardBackward(cipherText, startProbs, transitionProbs, emissionProbs)
    print(guess(q))
    # M-step
    emissionCounts : dict[tuple[str, str], float] = {(h, e): 0. for h in domain for e in domain}
    occurenceCounts : dict[str, float] = {h: 0. for h in domain}
    for p, o in zip(q, cipherText):
        for h in domain:
            emissionCounts[h, o] += p[h]
            occurenceCounts[h] += p[h]
    emissionProbs = {(h, o): emissionCounts[h, o] / occurenceCounts[h] for h in domain for o in domain}