import random;
sentence="deep learning loves data";
words=sentence.split();
pairs=[];
for i in range(len(words)):
    if i > 0:
        pairs.append((words[i], words[i-1]))
    if i < len(words)-1:
        pairs.append((words[i], words[i+1]))
print(pairs);
target, context = random.choice(pairs);
print("Positive pair:" + str((target,context)));
vocabulary=[
    "deep",
    "learning",
    "loves",
    "data",
    "at",
    "hospital",
    "banana",
    "guitar",
    "airplane",
    "pizza",
    "river"
]; 
negatives=[];
while len(negatives) < 5:
    negative=random.choice(vocabulary);
    if negative != context and negative != target and negative not in negatives:
        negatives.append(negative);

print("Negative pairs:");
for negative in negatives:
    print((target, negative));
    
