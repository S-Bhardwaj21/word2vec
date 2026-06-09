sentence="deep learning loves data";
words=sentence.split();
pairs=[];
for i in range(len(words)):
    if i > 0:
        pairs.append((words[i], words[i-1]))
    if i < len(words)-1:
        pairs.append((words[i], words[i+1]))
print(pairs);
    
    
