"""
Constants shared across files.
"""
import re

# special tokens and number regex
UNK = '_UNK'  # unk/OOV word/char
WORD_START = '<w>'  # word star
WORD_END = '</w>'  # word end
NUM = 'NUM'  # number normalization string
NUMBERREGEX = re.compile("[0-9]+|[0-9]+\\.[0-9]+|[0-9]+[0-9,]+")

# tasks
POS = 'pos'  # part-of-speech tagging
CHUNK = 'chunk'  # chunking
SRL = 'srl'  # semantic role labeling
NER = 'ner'  # named entity recognition
TASK_NAMES = [POS, CHUNK, SRL, NER]

# domains
#DOMAINS = ['bc', 'bn', 'mz', 'nw', 'wb', 'tc', 'pt']
#DOMAINS = ['UD_English', 'UD_German', 'UD_Finnish', 'UD_Estonian', 'UD_Norwegian-Bokmaal', 'UD_Swedish', 'UD_Danish']

DOMAINS = 'UD_Finnish UD_Estonian UD_Hungarian UD_NorthSami UD_English UD_Norwegian-Bokmaal UD_Swedish UD_Danish UD_Spanish UD_Italian UD_Portuguese UD_Catalan'.split()

# model files
MODEL_FILE = 'sluice_net.model'
PARAMS_FILE = 'sluice_net_params.pkl'

# optimizers
SGD = 'sgd'
ADAM = 'adam'

# type of layer connections
STITCH = 'stitch'
CONCAT = 'concat'
SKIP = 'skip'
NONE = 'none'

# cross-stitch and layer-stitch initialization schemes
BALANCED = 'balanced'
IMBALANCED = 'imbalanced'
