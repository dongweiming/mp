# coding=utf-8
from datetime import datetime, timedelta

from elasticsearch_dsl import (
    DocType, Date, Integer, Text, Float, Boolean, Keyword, SF, Q, A,
    Completion)
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer

from config import SEARCH_FIELDS
from .speaker import User, session

connections.create_connection(hosts=['localhost'])
gauss_sf = SF('gauss', starts_at={
    'origin': 'now', 'offset': '7d', 'scale': '10d'
})
log_sf = SF('script_score', script={
    'lang': 'painless',
    'inline': ("Math.log10(doc['seats_taken'].value * doc['amount'].value) * "
               "doc['feedback_score'].value")
})

class CustomAnalyzer(_CustomAnalyzer):
    def get_analysis_definition(self):
        return {}

ik_analyzer = CustomAnalyzer(
    'ik_analyzer',
    filter=['lowercase']
)


class Live(DocType):
    id = Integer()
    speaker_id = Integer()
    speaker_name = Text(analyzer='ik_max_word')
    feedback_score = Float() # 评分
    topic_names = Text(analyzer='ik_max_word')  # 话题标签名字
    seats_taken = Integer()  # 参与人数
    subject = Text(analyzer='ik_max_word')  # 标题
    amount = Float()  # 价格(RMB)
    description = Text(analyzer='ik_max_word')
    status = Boolean()  # public(True)/ended(False)
    starts_at = Date()
    outline = Text(analyzer='ik_max_word')  # Live内容
    speaker_message_count = Integer()
    tag_names = Text(analyzer='ik_max_word')
    liked_num = Integer()
    topics = Keyword()
    live_suggest = Completion(analyzer=ik_analyzer)

    @property
    def speaker(self):
        return session.query(User).get(self.speaker_id)

    class Meta:
        index = 'live'

    def to_dict(self):
        d = self._d_.copy()
        d.update({
            'type': 'live',
            'speaker': self.speaker
        })
        return d

    @classmethod
    def add(cls, **kwargs):
        id = kwargs.pop('id', None)
        if id is None:
            return False
        live = cls(meta={'id': id}, **kwargs)
        live.save()
        return live

Live.init()
