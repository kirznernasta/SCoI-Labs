SENTENCE_PATTERN = r'[.!\?]+'
NON_DECLARATIVE_PATTERN = r'[!\?]+'
WORD_PATTERN = r'\b[a-zA-Z\d]+\b'
NUMBER_PATTERN = r'\b\d+\b'

ONE_WORD_ABBREVIATIONS = [
    'etc.', 'vs.', 'jr.', 'sr.', 'mr.', 'ms.', 'mrs.', 'smb.', 'smth.', 'n.', 'v.', 'adj.', 'prep.', 'p.', 'pp.', 'par.', 'ex.',
    'pl.', 'sing.', 're.', 'rf.', 'edu.', 'appx.', 'sec.', 'gm.', 'cm.', 'yr.', 'jan.', 'feb.', 'mar.',
    'apr.', 'jun.', 'jul.', 'aug.', 'sep.', 'oct.', 'nov.', 'dec.', 'mon.', 'tue.', 'wed.', 'thu', 'fri.', 'sat.',
    'sun.']

TWO_WORDS_ABBREVIATIONS = ['e.g.', 'i.e.', 'p.s.']

THREE_WORDS_ABBREVIATIONS = ['v.i.p.', 'p.p.s.']
