def count_words(flnm):
    with open(flnm,'r') as f:
        content=f.read()
        words=content.split()
        cnt=len(words)
        return f"No of words in a file: {cnt}"
fi=('file')
print(count_words(fi))
