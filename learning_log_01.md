# Learning Log 01 — My Journey Towards Understanding Skip-Gram

Date: June 2026

## Starting Point

I was reading the Word2Vec paper but got stuck because I did not truly understand what the Skip-Gram model was.

The paper kept talking about:

* Skip-Gram
* Hierarchical Softmax
* Negative Sampling
* NCE

and I realized I was trying to understand advanced concepts without understanding the basic objective of the model.

So I decided to step back and build intuition from scratch.

---

# Question 1

Why can't we simply represent words as numbers?

Example:

doctor -> 0

nurse -> 1

banana -> 2

## Initial Thought

The computer needs numbers.

## Realization

These numbers are merely IDs.

They do not capture any relationship between words.

The model cannot conclude:

doctor is closer to nurse than banana.

In fact:

distance(doctor,nurse)

and

distance(nurse,banana)

would both be 1.

Therefore IDs contain no meaningful semantic information.

---

# Question 2

What should replace IDs?

## Idea

Instead of a single number:

doctor -> 0

use multiple numbers:

doctor -> [ ?, ?, ? ]

nurse -> [ ?, ?, ? ]

banana -> [ ?, ?, ? ]

## Why?

Because multiple dimensions provide space to encode information.

My own analogy:

Doctor and nurse may share factors such as:

* hospital
* patient
* medicine

while banana does not.

A vector can potentially capture such information.

---

# Question 3

How do we obtain those vectors?

## Important realization

The vectors are not manually assigned.

They start randomly.

Example:

learning -> [random]

deep -> [random]

loves -> [random]

The model gradually adjusts them during training.

---

# Question 4

What data is used for training?

Sentence:

deep learning loves data

Context window = 1

Generated pairs:

(learning, deep)

(learning, loves)

(loves, learning)

(loves, data)

Important realization:

Every word gets a chance to become the target word.

The neighboring words become the context words.

---

# Question 5

What is Skip-Gram actually trying to do?

This was my biggest confusion.

Eventually I realized:

For pair:

(learning, deep)

The objective is:

Given learning, predict deep.

For pair:

(doctor, hospital)

The objective is:

Given doctor, predict hospital.

This led to my first understanding of Skip-Gram:

"Given a target word, predict surrounding context words."

---

# Question 6

What should happen when the model makes mistakes?

Example:

Input: learning

Correct answer: deep

Model predicts: banana

My intuition:

* learning and deep should move closer
* learning and banana should move farther apart

This was the first moment where I intuitively understood what training is doing.

---

# Question 7

How do similar words become similar?

Important example:

The doctor treated the patient.

The nurse treated the patient.

The doctor works at the hospital.

The nurse works at the hospital.

Observation:

doctor and nurse never appear together.

Yet they share:

* patient
* hospital

Therefore they receive similar training signals.

Realization:

Words become similar because they have similar contexts.

Not because they appear together.

This was one of the most important insights of the day.

---

# Question 8

Where does the information inside a vector come from?

Earlier I thought vectors were arbitrary.

New understanding:

The vector for doctor becomes a compressed summary of the contexts in which doctor appears.

Examples:

* hospital
* patient
* medicine

The vector learns from usage.

The model is essentially learning:

"What kind of neighborhood does this word live in?"

---

# Question 9

How does the model decide whether hospital is a good prediction?

Suppose:

doctor = [10,8,9]

hospital = [11,7,8]

banana = [1,2,0]

My intuition:

Compare how close the vectors are.

doctor and hospital look similar.

doctor and banana look different.

Therefore the model needs a similarity score.

---

# Question 10

Why can't we simply compare vector totals?

Example:

doctor = [10,8,9]

Total = 27

wordY = [20,7,0]

Total = 27

Problem:

Same total.

Very different vectors.

Realization:

Similarity must consider every dimension.

Not just the sum.

---

# Question 11

Why does the model output scores?

Example:

hospital = 95

patient = 87

banana = 3

Observation:

Scores tell us which context words fit the target word better.

Higher score means stronger compatibility.

---

# Question 12

Why convert scores into probabilities?

Initial intuition:

Probabilities provide relative chances.

Example:

hospital = 0.42

patient = 0.38

banana = 0.01

This is easier to interpret than raw scores.

It also allows the model to compare candidates fairly.

---

# Question 13

Should probabilities depend on all candidate words?

Example 1:

hospital = 95

patient = 87

banana = 3

Example 2:

hospital = 95

patient = 87

banana = 90

Observation:

Even though hospital's score stayed the same, banana became a strong competitor.

Therefore hospital's probability should decrease.

Huge realization:

Probabilities are relative.

A word competes with all other words.

---

# Understanding the Objective Function

The paper writes:

(Equation omitted)

My translation:

For every word in the corpus and every context word around it:

Increase the probability of the correct context word.

In plain English:

"Given a target word, become better at predicting its surrounding words."

---

# Biggest Realizations of the Day

1. Word vectors are learned, not assigned.

2. Similar contexts create similar vectors.

3. Skip-Gram learns by predicting context words.

4. Meaning emerges from prediction.

5. Training means:

   * pull correct pairs closer
   * push incorrect pairs apart

6. Probabilities are relative and involve competition between words.

7. I now understand why the paper eventually needs Softmax and Negative Sampling, even though I have not studied them yet.

---

# Current State of Understanding

✅ Context pairs

✅ Why vectors are needed

✅ Similar contexts lead to similar embeddings

✅ Core intuition of Skip-Gram

✅ Similarity scores

✅ Need for probabilities

❓ Softmax equation

❓ How probabilities are computed

❓ Negative Sampling

❓ Hierarchical Softmax

❓ NCE
