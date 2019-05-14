Operation: Criminal CryptoKitty
===============================

### CryptoKitties *was* HUGE
> The smart contract of CryptoKitties has accounted for nearly 14 percent of the entire Ethereum network’s transaction volume, which is higher than the transaction volume of all other cryptocurrencies in the market combined, including bitcoin.

### WTF is it?
> CryptoKitties is a game centered around breedable, collectible, and oh-so-adorable creatures we call CryptoKitties! Each cat is one-of-a-kind and 100% owned by you; it cannot be replicated, taken away, or destroyed.

- *100% owned by you* - Essentially, these are tokens that **aren't used as currency**, and they've spawned an entire new world of "True Ownership" and "Digital Collectibles". Your proof of ownership is actually tied to the blockchain. This creates a few really interesting opportunities: (1) You own this item beyond this game, meaning you can possibly take it with you to other ecosystems -- spinoffs, alternate gaming universes, etc. and (2) You can now sell this item independent of the game.
- *breedable* - each CryptoKitty has it's own DNA and how it expresses them physically. Taking this even further, there's a complex algorithm to crossbreed new kitties, complete with dominant & recessive genes, as well as mutations!
- *adorable* - The internet *is* cats. Something interesting to me is the joy and love people actually have towards their own CryptoKitties.

---

![Criminal Kitty](http://www.buoydontfloat.com/assets/img/electronic-rituals/criminal-kitty.png)
*This project inspired by this lovely kitty I bred, which I admit looks like a criminal...*

---

![](https://i.imgur.com/xikMxAL.png)

---

## Let's look at some CryptoKitties!

![](https://i.imgur.com/7nz1RiW.png)

---
![](https://i.imgur.com/jExYACy.png)

---
![](https://i.imgur.com/BGHIz09.png)
**Celestial Cyber Dimension, a one-of-a-kind CryptoKitty, sold for $140,000!**

---
![](https://i.imgur.com/pLa9zwE.png)

---
![](https://i.imgur.com/zv2r62W.png)

---
![](https://i.imgur.com/eR82AB1.png)

---

## Cattributes

The 8 primary cattribute categories are:

Fur / Body
Pattern
Eye Color
Eye Shape / Type
Base Color
Highlight / Pattern Color
Accent / Secondary Color
Mouth

---
![](https://i.imgur.com/rrBYfS5.png)

---
## Genetype vs Phenotype

![](https://i.imgur.com/8oa5cEn.jpg)

Basic Gene
Recessive Gene
Mutation
Mystery, Secret, and Unknown genes

---
---

# Scraping

some pythonz and cryptokitties API

# Labeling

* Web Classifier vs. Mechanical Turk

![](https://i.imgur.com/H3VQ9EQ.png)
**Mechanical Turk made more sense than our web classifier. It just has built in QC and mirrors better the way Image Classification datasets are labeled in the real world.**

IMO this is where the project gets interesting because there isn't an actual database of criminal kitties. Instead, we get the beautiful opportunity to do shoddy data collection, meaning get our own labels. Instead of real data, I propose we use peoples' gut reactions toward CryptoKitty images. Also let's explore getting ITP to label the data, and compare that with results from mechanical turk.
    - we essentially did 1 pass on mechnical turk... and the results were surprisingly good!
    - we explored building our own custom labeler: [Cryptokitties Labeler](http://cryptokitty-phrenology.buoydontfloat.com/)

---

## Training

[Python Notebook](https://github.com/epylinkn/operation-criminal-kitty/blob/master/classification/predictor.ipynb)

## Web API

[In second git repo, via Falcon](https://github.com/79/phrenology-api/blob/master/main.py)

## DEMO: Chrome Extension

---
---

Takeaways
---------

We hope that our provocative findings generate a range of press coverage.

using cryptokitties as the vector to explore algorithmic bias

the internet is cats!
we don't care about labeling humans as criminals (as much as we should)
but maybe we'll care more about locking up digital collectible cats

seeing if there's more empathy for them than humans

what is objective? what is biased?
> it is reasonable to call it objective, that is, it does not in itself embody biases about facial appearance or criminality

crpytokitties was built to teach blockchain
cryptokitty physiognomy was built to teach about "scientific racism" hidden in artificial intelligence and machine learning

Xiaolin Wu and Xi Zhang’s paper, “Automated Inference on Criminality Using Face Images”

Wu and Zhang’s claim is that machine learning techniques can predict the likelihood that a person is a convicted criminal with nearly 90% accuracy using nothing but a driver’s license-style face photo.

The roots of physiognomy lie in the human propensity to interpret a person’s appearance associatively, metaphorically, and even poetically.

---
Next Steps
----------

### Faception?
The roots of physiognomy lie in the human propensity to interpret a person’s appearance associatively, metaphorically, and even poetically.

The Faception team are not shy about promoting applications of their technology, offering specialized engines for recognizing “High IQ”, “White-Collar Offender”, “Pedophile”, and “Terrorist” from a face image.

### More nuance:

> What do supposedly “nice” and “mean” faces look like? Research on social perception of faces in the last decade has shown that one’s impression of a face can be reduced to a few basic dimensions, including dominance, attractiveness, and valence. (“Valence” is associated with positive evaluations like “trustworthy” and “sociable”.)

### More ideas:
Build that wall?
Othering?
Story generators?

---
---
Algorithmic Bias
----------------

I've also been spending a lot of time reading about human rights, ethics, and social good. The physiognomy article we read for class really piqued my interest because as junk science as it can be people are actually using it. Perhaps even more troublesome is that beyond the obviously visceral reactions to phrenology, *opaque algorithms do encode subtle biases*. For example, there are articles floating about claiming self-driving cars do a poor job at detecting dark-skinned pedestrians.

But alas, it seems people avoid these heavy topics.

---

Physiognomy
-----------

The physiognomy reading for class is interesting because despite being so wrong, people can still find ways to draw such meaningful conclusions. Many problems abound in the study. Of note:
* There was a not a lot of data (~500 portraits of felons)
* The images were not well-controlled in the experiment

At the same time, our guts tell us that there are interesting questions in the realm of Physiognomy. That is, we believe that they do have some measure of prediction -- e.g. a beautiful (proportional?) person is generally perceived to have an easier life, making the opposite scenario plausible.

---

References
----------

- [The Anatomy of ERC721 (Non-Fungible Tokens)](https://medium.com/crypto-currently/the-anatomy-of-erc721-e9db77abfc24)
- [A new study finds a potential risk with self-driving cars: failure to detect dark-skinned pedestrians](https://www.vox.com/future-perfect/2019/3/5/18251924/self-driving-car-racial-bias-study-autonomous-vehicle-dark-skin)
- [Who Spends $140,000 on a CryptoKitty?](https://www.nytimes.com/2018/05/18/style/cryptokitty-auction.html)
- [Celestial Cyber Dimension](https://www.cryptokitties.co/kitty/127)
- [Physiognomy's New Clothes @ Medium](https://medium.com/@blaisea/physiognomys-new-clothes-f2d4b59fdd6a)
- [The CryptoKitties Genome Project @ Medium](https://medium.com/@kaigani/the-cryptokitties-genome-project-68582016f687)
- [CryptoKitties Genome Mapping](https://medium.com/newtown-partners/cryptokitties-genome-mapping-6412136c0ae4)
- https://cryptokitties411.com/category/genetics/
- https://www.ccn.com/cryptokitties-isnt-as-popular-as-you-think-it-is
  > The smart contract of CryptoKitties has accounted for nearly 14 percent of the entire Ethereum network’s transaction volume, which is higher than the transaction volume of all other cryptocurrencies in the market combined, including bitcoin.
- https://medium.com/cryptokitties/the-many-ways-to-value-a-kitty-e286f9e061d1
- https://cryptokitties411.com/2018/01/26/original-artwork/
- https://cryptokitties411.com/category/genetics/
  - Normal traits, Recessive traits, Mutations
  - (Note: Mutations are separate from the “recessive” genes that have a chance to gene swap into the dominant position.)
- https://www.wired.com/2015/04/people-care-pets-humans/

---
## Class Feedback

cyptokitties are meant to be judged by appearance!
* that's part of the magic circle

pricing models

reading into owners -
- based on their penchant for harboring criminals
- this owner harbors criminals!

