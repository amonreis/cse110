from sentences import get_determiner, get_noun, get_preposition, get_prepositional_phrase, get_verb, get_adjective, get_adverb, get_sentence
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners
    
def test_get_noun():
    # 1. Test the single nouns.

    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_noun function which
        # should return a single noun.
        word = get_noun(1)

        # Verify that the word returned from get_noun
        # is one of the words in the single_nouns list.
        assert word in single_nouns

    # 2. Test the plural nouns.

    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_noun function which
        # should return a plural noun.
        word = get_noun(2)

        # Verify that the word returned from get_noun
        # is one of the words in the plural_nouns list.
        assert word in plural_nouns

def test_get_verb():
    # 1. Test the past tense verbs.

    past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb function which
        # should return a past tense verb.
        word = get_verb(1, "past")

        # Verify that the word returned from get_verb
        # is one of the words in the past_verbs list.
        assert word in past_verbs

    # 2. Test the present tense verbs for single nouns.

    present_verb_single_noun = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb function which
        # should return a present tense verb for single nouns.
        word = get_verb(1, "present")

        # Verify that the word returned from get_verb
        # is one of the words in the present_verb_single_noun list.
        assert word in present_verb_single_noun

    # 3. Test the present tense verbs for plural nouns.

    present_verb_plural_noun = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb function which
        # should return a present tense verb for plural nouns.
        word = get_verb(2, "present")

        # Verify that the word returned from get_verb
        # is one of the words in the present_verb_plural_noun list.
        assert word in present_verb_plural_noun

    # 4. Test the future tense verbs.

    future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb function which
        # should return a future tense verb.
        word = get_verb(1, "future")

        # Verify that the word returned from get_verb
        # is one of the words in the future_verbs list.
        assert word in future_verbs

def test_get_preposition():
    # 1. Test the prepositions.
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_preposition function which
        # should return a preposition.
        preposition = get_preposition()

        # Verify that the word returned from get_preposition
        # is one of the words in the prepositions list.
        assert preposition in prepositions

def test_get_adjective():
    # 1. Test the adjectives.
    adjectives = ["beautiful", "busy", "crazy", "delightful", "fast", "gifted", "happy", "healthy", "hilarius", "hungry", "kind", "lucky", "mysterius", "perfect", "successful", "scary", "smart", "tired", "thankful"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_adjective function which
        # should return an adjective.
        adjective = get_adjective()

        # Verify that the word returned from get_adjective
        # is one of the words in the adjectives list.
        assert adjective in adjectives


def test_get_prepositional_phrase():
    # 1. Test the single prepositional phrases.
    single_prepositional_phrase = get_prepositional_phrase(1).split()
    
    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    single_determiners = ["a", "one", "the"]
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        single_prepositional_phrase

        assert len(single_prepositional_phrase) == 3
        assert single_prepositional_phrase[0] in prepositions
        assert single_prepositional_phrase[1] in single_determiners
        assert single_prepositional_phrase[2] in single_nouns

    # 2. Test the plural determiners.
    plural_preposition_phrase = get_prepositional_phrase(2).split()

    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        plural_preposition_phrase

        assert len(plural_preposition_phrase) == 3
        assert plural_preposition_phrase[0] in prepositions
        assert plural_preposition_phrase[1] in plural_determiners
        assert plural_preposition_phrase[2] in plural_nouns


def test_get_adverb():
    # 1. Test the adverbs
    adverbs = ["always", "never", "unexpectedly", "stupidly", "sadly", "nicely", "obediently", "seriously", "awkwardly", "arrogantly", "naturally", "mysteriously", "innocently", "freely", "furiously", "elegantly", "correctly", "cautiously", "curiously"]

    # This loop will repeat the statments inside it 4 times
    for _ in range(4):
        
        # Call the get_adverb function which
        # should return an adverb.
        adverb = get_adverb()

        # Verify that the word returned from get_adverb
        # is one of the words in the adverbs list.
        assert adverb in adverbs


def test_get_sentence():
    """Test the get_sentence function to see if it works"""
    
    # Test the get_sentences function using one for the parameter quantity and "past" for the parameter tense 
    single_past_sentence = get_sentence(1, "past").split(' ')

    single_determiners = ["a", "one", "the"]
    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    adjectives = ["beautiful", "busy", "crazy", "delightful", "fast", "gifted", "happy", "healthy", "hilarius", "hungry", "kind", "lucky", "mysterius", "perfect", "successful", "scary", "smart", "tired", "thankful"]
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    adverbs = ["always", "never", "unexpectedly", "stupidly", "sadly", "nicely", "obediently", "seriously", "awkwardly", "arrogantly", "naturally", "mysteriously", "innocently", "freely", "furiously", "elegantly", "correctly", "cautiously", "curiously"]
    verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        single_past_sentence

        assert len(single_past_sentence) == 11
        assert single_past_sentence[0] in single_determiners
        assert single_past_sentence[1] in adjectives
        assert single_past_sentence[2] in single_nouns
        assert single_past_sentence[3] in prepositions
        assert single_past_sentence[4] in single_determiners
        assert single_past_sentence[5] in single_nouns
        assert single_past_sentence[6] in adverbs
        assert single_past_sentence[7] in verbs
        assert single_past_sentence[8] in prepositions
        assert single_past_sentence[9] in single_determiners
        assert single_past_sentence[10] in single_nouns

    # Test the get_sentences function using two for the parameter quantity and "past" for the parameter tense 
    plural_past_sentence = get_sentence(2, "past").split(' ')

    plural_determiners = ["some", "many", "the"]
    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        plural_past_sentence

        assert len(plural_past_sentence) == 11
        assert plural_past_sentence[0] in plural_determiners
        assert plural_past_sentence[2] in plural_nouns
        assert plural_past_sentence[4] in plural_determiners
        assert plural_past_sentence[5] in plural_nouns
        assert plural_past_sentence[9] in plural_determiners
        assert plural_past_sentence[10] in plural_nouns

    # Test the get_sentences function using one for the parameter quantity and "present" for the parameter tense 
    single_present_sentence = get_sentence(1, "present").split(' ')
    
    verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]

    # This loop will repeat the statments inside it 4 times
    for _ in range(4):
        single_present_sentence

        assert len(single_present_sentence) == 11
        assert single_present_sentence[7] in verbs
    
    # Test the get_sentences function using two for the parameter quantity and "present" for the parameter tense    
    plural_present_sentence = get_sentence(2, "present").split(' ')

    verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

    # This loop will repeat the statments inside it 4 times
    for _ in range(4):
        plural_present_sentence

        assert len(plural_present_sentence) == 11
        assert plural_present_sentence[7] in verbs

    # Test the get_sentences function using one or two for the parameter quantity and "future" for the parameter tense
    num = [1, 2]
    single_future_sentence = get_sentence(random.choice(num), "future").split(' ')

    # This loop will repeat the statments inside it 4 times
    for _ in range(4):
        single_future_sentence

        assert len(single_future_sentence) == 12
        assert single_future_sentence[6] == "will"
        assert single_future_sentence[7] in adverbs
        assert single_future_sentence[8] in verbs


# Call the main function that is part of pytest so that the
# computer will execute the test fu 
# def test_get_prepositional_phrase():ctions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])