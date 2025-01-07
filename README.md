# Personal Agent Framework

## Planning

Fast API to connect as a service

Incomming call from X
Incomming chat from Y

Both connect to Agent

System Prompt: Agent gets personality set in personality.
Role User Content ++ Agent gets environ context from live data.

TODO
Weather
Location of agent: From config in world config

## TODO

Get weather context, summarize, get location context for varun, summarize.

On every LLM Cycle, keep check on context length, summarize history after XX user/agent chat! And save it (Future).

## Tips and Tricks

Reducing context/prompt sizing
https://www.microsoft.com/en-us/research/blog/llmlingua-innovating-llm-efficiency-with-prompt-compression/

## Stack

Fast API
https://fastapi.tiangolo.com/async/#asynchronous-code

UV
https://github.com/astral-sh/uv?tab=readme-ov-file
