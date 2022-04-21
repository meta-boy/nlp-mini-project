
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from nltk.tokenize import sent_tokenize

def outputsumm(input_text):
	LANGUAGE = "english"

	sentences = sent_tokenize(input_text)

	SENTENCES_COUNT = len(sentences) // 2

	parser = PlaintextParser.from_string(input_text, Tokenizer(LANGUAGE))

	stemmer = Stemmer(LANGUAGE)
	summarizer = Summarizer(stemmer)
	summarizer.stop_words = get_stop_words(LANGUAGE)
	summarized_sentences = summarizer(parser.document, SENTENCES_COUNT)
	return " ".join(map(str, summarized_sentences))


