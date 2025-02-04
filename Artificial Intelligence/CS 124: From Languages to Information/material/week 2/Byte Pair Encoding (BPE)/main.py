def pairing(V: []) -> {}:
    a_dict = {}
    for i in range(len(V)):
        if i < len(V) - 1:
            left = V[i]
            right = V[i + 1]
            if left != ' ' and right != ' ':  # bo qua truong hop cuoi cung cua tu
                new = (left, right)  # tuple, list bi loi
                if new not in a_dict.keys():
                    a_dict[new] = 1
                    pass
                else:
                    a_dict[new] = a_dict[new] + 1
                    pass
                pass
            pass
        pass
    return a_dict


def replacing(corpus: [], keys: ()) -> []:
    tL = keys[0]
    tR = keys[1]
    tNew = f'{tL}{tR}'
    new_corpus = []
    i = 0
    while i < len(corpus):
        i_th = corpus[i]
        if i_th != tL:
            new_corpus.append(i_th)
            pass
        else:
            if i != len(corpus) - 1:
                j_th = corpus[i + 1]
                if j_th == tR:
                    new_corpus.append(tNew)
                    i = i + 1 # vuot qua chu vua ghep
                    pass
                else:
                    new_corpus.append(i_th)
                    pass
                pass
            else:
                new_corpus.append(i_th)
                pass
            pass
        i = i + 1
        pass
    return new_corpus


def BYTE_PAIR_ENCODING(C: str, k: int) -> []:
    # V <- all unique characters in C
    corpus = list(C.replace(' ', '_ '))
    V = list(set(corpus))
    for i in range(k):
        print(f'V = {V}')
        print(f'corpus: {corpus}')
        pairs = pairing(corpus)
        # tL, tR Most frequent pair of adjacent tokens in C
        max_keys = max(pairs, key=pairs.get)
        max_value = pairs[max_keys]
        keys = [k for k, v in pairs.items() if v == max_value]
        #print(max_value)
        #print(keys)

        # Replace each occurrence of tL, tR in C with tNEW # and update the corpus
        for item in keys:
            tL = item[0]
            tR = item[1]
            # tNEW <- tL + tR # make new token by concatenating
            tNew = f'{tL}{tR}'
            # V <- V + tNEW # update the vocabulary
            V.append(tNew)
            corpus = replacing(corpus=corpus, keys=item)
            pass
        pass
    return V


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    corpus = "low low low low low lowest lowest newer newer newer newer newer newer wider wider wider new new"
    BYTE_PAIR_ENCODING(C=corpus, k=12)
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
