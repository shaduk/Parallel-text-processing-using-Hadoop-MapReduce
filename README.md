# Parallel-text-processing-using-MapReduce-MR-and-Hadoop-Distributed-File-System-HDFS

This problem was provided by researchers in the Classics department at UB. They have provided
two classical texts and a lemmatization file to convert words from one form to a standard or
normal form. In this case several passes through the documents were done. 
Pass 1: Lemmetization using the lemmas.csv file
Pass 2: Identify the words in the texts by <word <docid, [chapter#, line#]> for two documents.
Pass 3: Repeat this for multiple documents.
Here is a rough algorithm (non-MR version):
 for each word in the text
      normalize the word spelling by replacing j with i and v with u throughout
      check lemmatizer for the normalized spelling of the word
      if the word appears in the lemmatizer
            obtain the list of lemmas for this word
            for each lemma, create a key/value pair from the lemma and the location where the
            word was found
      else
          create a key/value pair from the normalized spelling and
           the location where the word was found
