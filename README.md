## Sentiment Analysis Using fastText
-----------

This simple flask app predict reviews ratings (1 to 5). The text classification algorithm is based on fastText (see References).

Here is how the app looks like:

![ui-demo]
(images/ui-demo.png)

### Data

Amazon reviews from 1995 to 2013 are used as training data. They can be downloaded from [here](https://archive.org/details/amazon-reviews-1995-2013).

### Train model

The classificaiton can be trained using:

```
sh train.sh
```

### References
--------------------------------------------------------------------------------
- https://research.facebook.com/blog/fasttext/
- https://github.com/facebookresearch/fastText