import logging; logging.basicConfig(level = logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

def index(requests):
    return web.Response(body = b'<h1>Hello</h1>')

async def init(loop):
    app = web.Application(loop = loop)