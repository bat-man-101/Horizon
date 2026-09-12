"""AIAnalysisResult schema 校验测试: 脏数据必须被拦截, 好数据必须通过。

对应 analyzer._analyze_item 中的 schema 校验路径 —— 防止 AI 返回
score="high" / tags 非列表这类字段级脏数据静默流入下游。
"""

import pytest
from pydantic import ValidationError

from src.models import AIAnalysisResult


def test_valid_result():
    r = AIAnalysisResult.model_validate(
        {
            "score": 8,
            "reason": "high relevance",
            "summary": "摘要",
            "tags": ["AI", "tech"],
        }
    )
    assert r.score == 8.0
    assert r.tags == ["AI", "tech"]


def test_score_int_coerced_to_float():
    r = AIAnalysisResult.model_validate({"score": 7})  # int 合法, pydantic 转 float
    assert r.score == 7.0


def test_score_string_rejected():
    """AI 返回 score="high" 这种脏数据必须校验失败 (此前会 float("high") 抛异常)。"""
    with pytest.raises(ValidationError):
        AIAnalysisResult.model_validate({"score": "high"})


def test_score_out_of_range_rejected():
    with pytest.raises(ValidationError):
        AIAnalysisResult.model_validate({"score": 11})
    with pytest.raises(ValidationError):
        AIAnalysisResult.model_validate({"score": -1})


def test_tags_not_list_rejected():
    """AI 返回 tags="a,b" 字符串必须校验失败。"""
    with pytest.raises(ValidationError):
        AIAnalysisResult.model_validate({"tags": "a,b"})


def test_missing_fields_default():
    r = AIAnalysisResult.model_validate({"score": 5})
    assert r.reason == ""
    assert r.summary == ""
    assert r.tags == []


def test_extra_fields_ignored():
    r = AIAnalysisResult.model_validate({"score": 5, "unexpected": 123})
    assert r.score == 5.0
