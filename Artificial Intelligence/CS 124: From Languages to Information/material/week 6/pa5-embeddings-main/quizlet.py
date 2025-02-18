"""
CS124 PA5: Quizlet // Stanford, Winter 2020
by @lcruzalb, with assistance from @jchen437
parts 3, 4 are new in 2025 by @gdmagana
"""
import csv
import sys
import getopt
import os
import math
import operator
import random
from collections import defaultdict
import numpy as np
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models.keyedvectors import KeyedVectors
import json

#############################################################################
###                    CS124 Homework 5: Quizlet!                         ###
#############################################################################

# ------------------------- Do not modify code below --------------------------------
        
class Part1_Runner():
    def __init__(self, find_synonym, part1_written):        
        self.find_synonym = find_synonym
        self.part1_written = part1_written

        # load embeddings
        self.embeddings = KeyedVectors.load_word2vec_format("data/embeddings/glove50_4k.txt", binary=False)

        # load questions
        root_dir = 'data/dev/'
        self.synonym_qs = load_synonym_qs(root_dir + 'synonyms.csv')

    def evaluate(self, print_q=True):
        print ('Part 1: Synonyms!')
        print ('-----------------')

        acc_euc_dist = self.get_synonym_acc('euc_dist', self.embeddings, self.synonym_qs, print_q)
        acc_cosine_sim = self.get_synonym_acc('cosine_sim', self.embeddings, self.synonym_qs, print_q)

        print ('accuracy using euclidean distance: %.5f' % acc_euc_dist)
        print ('accuracy using cosine similarity : %.5f' % acc_cosine_sim)
        
        # sanity check they answered written - this is just a heuristic
        written_ans = self.part1_written()
        if 'TODO' in written_ans:
            print ('Part 1 written answer contains TODO, did you answer it?')

        print (' ')
        return acc_euc_dist, acc_cosine_sim

    def get_synonym_acc(self, comparison_metric, embeddings, synonym_qs, print_q=False):
        '''
        Helper function to compute synonym answering accuracy
        '''
        if print_q:
            metric_str = 'cosine similarity' if comparison_metric == 'cosine_sim' else 'euclidean distance'
            print ('Answering part 1 using %s as the comparison metric...' % metric_str)

        n_correct = 0
        for i, (w, choices, answer) in enumerate(synonym_qs):
            ans = self.find_synonym(w, choices, embeddings, comparison_metric)

            if ans == answer: n_correct += 1

            if print_q:
                print ('%d. What is a synonym for %s?' % (i+1, w))
                a, b, c, d = choices[0], choices[1], choices[2], choices[3]
                print ('    a) %s\n    b) %s\n    c) %s\n    d) %s' % (a, b, c, d))
                print ('you answered: %s \n' % ans)

        acc = n_correct / len(synonym_qs)
        return acc


class Part2_Runner():
    def __init__(self, occupation_exploration, part2_written):        
        self.occupation_exploration = occupation_exploration
        self.part2_written = part2_written

        # load embeddings
        self.embeddings = KeyedVectors.load_word2vec_format("data/embeddings/glove50_4k.txt", binary=False)


    def evaluate(self):
        '''
        Runs part 2 functions
        '''
        print ('Part 2: Exploration!')
        print ('--------------------')

        occupations = load_occupations_list()
        top_man_occs, top_woman_occs = self.occupation_exploration(occupations, self.embeddings)
        
        print ('occupations closest to "man" - you answered:')
        for i, occ in enumerate(top_man_occs):
            print (' %d. %s' % (i+1, occ))
        print ('occupations closest to "woman" - you answered:')
        for i, occ in enumerate(top_woman_occs):
            print (' %d. %s' % (i+1, occ))

        # sanity check they answered written - this is just a heuristic
        written_ans = self.part2_written()
        if 'TODO' in written_ans:
            print ('Part 2 written answer contains TODO, did you answer it?')
        print (' ')
        return top_man_occs, top_woman_occs

class Part3_Runner():
    """
    This is now the new part 3, which is contextual embeddings with BERT.
    """
    def __init__(self, part3, get_bert_word_embedding, cosine_similarity):
        self.get_bert_word_embedding = get_bert_word_embedding
        self.cosine_similarity = cosine_similarity
        self.part3 = part3

    def evaluate(self):

        # Run the part 3 function

        print("Part 3: Contextual embeddings with BERT")
        print("---------------------------------------")
        print("Polyseme disambiguation: ")
        word, sentence1, sentence2 = self.part3()
        print(f"Word: {word}")
        print(f"Sentence 1: {sentence1}")
        print(f"Sentence 2: {sentence2}")
        embedding1 = self.get_bert_word_embedding(sentence1, word)
        embedding2 = self.get_bert_word_embedding(sentence2, word)
        similarity = self.cosine_similarity(embedding1, embedding2)
        
        return(f"This word is {similarity*100:.2f}% similar in the two sentences.")
        

class Part4_Runner():
    def __init__(self, search_web, get_bert_sentence_embeddings):
        self.search_web = search_web
        self.get_bert_sentence_embeddings = get_bert_sentence_embeddings

    def evaluate(self):
        """
        Run the part 4 function
        """
        print("Part 4: Web search simulation with BERT")
        print("---------------------------------------")
        test_queries = ["What is the capital of Canada?", 
                        "What do people speak in Brazil?", 
                        "Who is Shakespeare?"]
        
        for query in test_queries:
            self.test_web_search(query, 3)
        return 
    
    def test_web_search(self, query, k):
        """
        helper function to test the web search function
        """
        top_questions, top_answers = self.search_web(query, k)
        print(f"Top {k} questions similar to '{query}':")
        for question, answer in zip(top_questions, top_answers):
            print(f"- Did you mean.... {question}")
            print(f"    Answer(s):  {answer}")
        
        
        


# Helper functions to load questions
# def load_entity_data():
#     data = []
#     with open("data/WikiSRS_similarity.csv.pro", "r") as f:
#         reader = csv.reader(f, delimiter="\t")
#         for row in reader:
#             data.append(row)
#     return data

def load_synonym_qs(filename):
    '''
    input line:
        word    c1,c2,c3,c4     answer

    returns list of tuples, each of the form:
        (word, [c1, c2, c3, c4], answer)
    '''
    synonym_qs = []
    with open(filename) as f:
        f.readline()    # skip header
        for line in f:
            word, choices_str, ans = line.strip().split('\t')
            choices = [c.strip() for c in choices_str.split(',')]
            synonym_qs.append((word.strip(), choices, ans.strip()))
    return synonym_qs

# def load_analogy_qs(filename):
#     '''
#     input line:
#         a,b,aa,bb   c1,c2,c3,c4

#     returns list of tuples, each of the form:
#         (a, b, aa, bb)  // for analogy a:b --> aa:bb
#     '''
#     analogy_qs = []
#     with open(filename) as f:
#         f.readline()    # skip header
#         for line in f:
#             toks, choices_str = line.strip().split('\t')
#             analogy_words = tuple(toks.strip().split(','))          # (a, b, aa, bb)
#             choices = [c.strip() for c in choices_str.split(',')]   # [c1, c2, c3, c4]
#             analogy_qs.append((analogy_words, choices))
#     return analogy_qs

# def load_sentence_sim_qs(filename):
#     '''
#     input line:
#         label   s1  s2
    
#     returns list of tuples, each of the form:
#         (label, s1, s2)
#     '''
#     samples = []
#     with open(filename) as f:
#         for line in f:
#             line = line.strip()
#             label_str, s1, s2 = line.split('\t')
#             label = int(label_str)
#             samples.append((label, s1.strip(), s2.strip()))
#     return samples


def load_occupations_list():
    '''
    Helper that loads the list of occupations for part 4
    '''
    occupations = []
    with open("data/occupations.txt") as f:
        for line in f:
            occupations.append(line.strip())
    return occupations

def load_stanford_web_questions():
    with open('data/stanford_web_questions.json', 'r') as f:
        dict = json.load(f)
    return dict

def main():
    print("Run homework assignment in pa5-quizlet.ipynb")

if __name__ == "__main__":
        main()
