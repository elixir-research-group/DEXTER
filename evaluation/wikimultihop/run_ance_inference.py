from dexter.config.constants import Split
from dexter.data.loaders.RetrieverDataset import RetrieverDataset
from dexter.utils.metrics.SimilarityMatch import CosineSimilarity
from dexter.utils.metrics.retrieval.RetrievalMetrics import RetrievalMetrics
from dexter.retriever.dense.ANCE import ANCE

if __name__ == "__main__":
    loader = RetrieverDataset("wikimultihopqa","wiki-musiqueqa-corpus","evaluation/config.ini",Split.DEV)
    retriever = ANCE("tests/retriever/test_config.ini")
    queries, qrels, corpus = loader.qrels()
    qrels_ret = retriever.retrieve(corpus,queries,100,CosineSimilarity(),True)

    metrics = RetrievalMetrics(k_values=[1,10,100])
    print(metrics.evaluate_retrieval(qrels=qrels,results=qrels_ret))