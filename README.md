## Sentiment Analysis Using fastText

This simple flask app predict reviews ratings (1 to 5). The text classification algorithm is based on fastText (see References).

Here is how the app looks like:

![ui-demo]
(images/ui-demo.png)

### Data

Amazon reviews from 1995 to 2013 are used for training. They can be downloaded from [here](https://archive.org/details/amazon-reviews-1995-2013). Downloaded zip file is put under the folder data/amazon/.

### Train fastText model

The classificaiton can be trained using:

```
sh train.sh
```

### Run app

To run the flask app, simple type:

```
python app.py
```

### References

- https://research.facebook.com/blog/fasttext/
- https://github.com/facebookresearch/fastText