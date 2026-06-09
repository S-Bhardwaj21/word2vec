# Word2Vec Explorer

A repository documenting my journey of understanding and implementing Word2Vec from scratch.

The goal of this project is not only to reproduce Word2Vec, but also to understand the ideas behind word embeddings, Skip-Gram, Negative Sampling, and related concepts through hands-on implementation.

---

## Project Goals

* Read and understand the Word2Vec paper
* Learn the mathematics required along the way
* Implement core components from scratch in Python
* Document learnings, experiments, and challenges
* Build intuition for modern NLP systems

---

## Current Progress

* [x] Read the Word2Vec paper
* [x] Created paper summary
* [x] Generated Skip-Gram training pairs manually
* [x] Implement Skip-Gram training pair generation in Python
* [ ] Build vocabulary
* [ ] Create word embeddings
* [ ] Understand Negative Sampling
* [ ] Train a simple Word2Vec model

---

## Repository Structure

```text
word2vec-explorer/

README.md

src/
    generate_pairs.py
    preprocess.py

paper_notes/
```

---

## What I Have Learned So Far

* Words can be represented as dense vectors called embeddings.
* Similar words tend to have similar vector representations.
* Skip-Gram learns by predicting surrounding words from a target word.
* Training efficiency is a major challenge when working with large datasets.

---

## Current Questions

* How exactly does Skip-Gram learn embeddings?
* Why does the dot product measure similarity?
* How does Negative Sampling work?
* How are embeddings updated during training?

---

## Next Step

Implement Skip-Gram training pair generation and understand the flow of data from text to training examples.

