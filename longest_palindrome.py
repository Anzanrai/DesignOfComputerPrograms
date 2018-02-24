import itertools

a = 'where is the racecar?'

def is_palindrome(text):
	return text == text[::-1]


def slice_string(full_text):
	if len(full_text):		
		longest_palindrome = ''
		full_text = full_text.lower()
		pos = {'start_pos': 0, 'end_pos': 1}
		for start_pos in range(len(full_text)+1):
			for end_pos in  range(1, len(full_text)+1):
				if is_palindrome(full_text[start_pos:end_pos]) and len(longest_palindrome) < len(full_text[start_pos:end_pos]):
					longest_palindrome = full_text[start_pos:end_pos]
					pos.update({'start_pos': start_pos, 'end_pos': end_pos})

		return (pos['start_pos'], pos['end_pos'])
	return (0,0)

longest_palindrome, position = slice_string(a)
print 'longest_palindrome is: '+longest_palindrome
print '\nposition: '
print position


# optimized solution 

def longest_subpalindrome_slice(text):
	if text == '': return (0,0)

	def length(slice): a,b = slice; return b-a

	candidates = [grow(text, start, end) for start in range(len(text)) for end in (start, start+1)]
	return max(candidates, key=length)

def grow(text, start, end):
	while (start > 0 and end < len(text) and text[start-1].lower() == text[end].lower()):
		start -= 1; end += 1
	return (start, end)