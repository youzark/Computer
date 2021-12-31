class NerModelTestDouble:
    """
    Test double for spacy NLP model
    """
    def __init__(self,model_name):
        self.model = model_name

    def returns_doc_entities(self,ents):
        self.ents = ents

    def __call__(self,sent):
        return DocTestDouble(sent, self.ents)

class DocTestDouble:
    """
    Test Double for spacy Doc
    """
    def __init__(self,sent,ents):
        self.ents  = [SpanTestDoule(ent['text'],ent['label_']) for ent in ents]
    def patch_method(self,attr,return_value):
        def patched(): return return_value
        setattr(self,attr, patched)
        return self

class SpanTestDoule:
    """
    Test double for spacy Span
    """
    def __init__(self,text,label_):
        self.text = text
        self.label_ = label_
