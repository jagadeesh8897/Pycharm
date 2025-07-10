def count_words(flnm):
    with open(flnm,'r') as f:
        content=f.read()
        words=content.split()
        cnt=len(words)
        return f"No of words in a file: {cnt}"
file=('file')
print(count_words(file))
