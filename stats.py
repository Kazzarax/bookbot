def get_num_words(bookText):
	splitText = bookText.split()
	#print(str(len(splitText))+ " words found in the document")
	return len(splitText)

def get_characters(bookText):
	lText = bookText.lower()
	bookDict = {}
	for c in lText:
		if c in bookDict:
			bookDict[c] += 1
		else:
			bookDict[c] = 1
	return bookDict

def sorter(bookDict):
    cleaned = {k: v for k, v in bookDict.items() if k.isalpha()}

    # Sort by frequency, highest first
    sorted_dict = dict(
        sorted(cleaned.items(), key=lambda item: item[1], reverse=True)
    )
    return sorted_dict


