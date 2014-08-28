import re, sys
const = r"bcdfghjklmnpqrstvwxyz"
vow = r'aeiou'
def syl_count(s):
	syl_count = 0
	qu = re.compile(r'qu')
	s = qu.sub('qw',s)



	ends = re.compile(r'(es$)|(que$)|(gue$)')
	s = ends.sub('',s)

	s = re.sub(r'^re',r'ren',s)
	s = re.sub(r'^gua',r'ga',s)
	s = re.sub(r'([aeiou])(l+e$)',r'\g<1>',s)
	(s,nsyl_count) = re.subn(r'([bcdfghjklmnpqrstvwxyz])(l+e$)',r'\g<1>',s)
	syl_count += nsyl_count


	s = re.sub(r'([aeiou])(ed$)',r'\g<1>',s)
	(s,nsyl_count) = re.subn(r'([bcdfghjklmnpqrstvwxyz])(ed$)',r'\g<1>',s)
	syl_count += nsyl_count

	endsp = re.compile(r'(ly$)|(ful$)|(ness$)|(ing$)|(est$)|(er$)|(ent$)|(ence$)')
	(s,nsyl_count) = endsp.subn(r'',s)
	syl_count += nsyl_count
	(s,nsyl_count) = endsp.subn(r'',s)
	syl_count += nsyl_count

	s = re.sub(r'(^y)([aeiou][aeiou]*)',r'\g<2>',s)
	s = re.sub(r'([aeiou])(y)',r'\g<1>t',s)
	(s,nsyl_count) = re.subn(r'(^y)([bcdfghjklmnpqrstvwxyz])',r'\g<2>',s)
	syl_count += nsyl_count
	syl_count += nsyl_count


	s = re.sub(r'aa+',r'a',s)
	s = re.sub(r'ee+',r'e',s)
	s = re.sub(r'ii+',r'i',s)
	s = re.sub(r'oo+',r'o',s)
	s = re.sub(r'uu+',r'u',s)

	dipthongs = re.compile(r'(ai)|(au)|(ea)|(ei)|(eu)|(ie)|(io)|(oa)|(oe)|(oi)|(ou)|(ue)|(ui)')
	s,nsyl_count = dipthongs.subn('',s)
	syl_count += nsyl_count

	if(len(s)>3):
			s = re.sub(r'([bcdfghjklmnpqrstvwxyz])(e$)',r'\g<1>',s)

	s,nsyl_count = re.subn(r'[aeiouy]','',s)
	syl_count += nsyl_count
	return syl_count
#st = sys.argv[1]
import nltk, string
from nltk.tokenize.punkt import PunktWordTokenizer

with open('positive-words.txt') as f:
	for w in f:
		w = w.translate(None, string.punctuation)
		ws = PunktWordTokenizer().tokenize(w)
		for ww in ws:
			print ww, syl_count(ww.lower())