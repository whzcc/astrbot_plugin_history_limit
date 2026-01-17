from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import os,json,datetime
from astrbot.api.provider import ProviderRequest

@register("history_limit", "whzc", "限制上文长度", "1.0.0", "repo url")

class Main(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @filter.on_llm_request()
    async def history_limit(self, event: AstrMessageEvent, req: ProviderRequest): # 请注意有三个参数
        if "清除上下文" in req.prompt or "清空上下文" in req.prompt:
            req.contexts = []
            req.prompt = []
            logger.info("已清除。")
        # 以下弃用，请使用官方提供的功能
        # if len(req.contexts) >= 20:
        #     req.contexts.pop(0)
        #     req.contexts.pop(0)
            
