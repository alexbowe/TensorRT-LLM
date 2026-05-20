__all__ = ['OpenAIServer', 'OpenAIDisaggServer']


def __getattr__(name):
    if name == 'OpenAIServer':
        from .openai_server import OpenAIServer

        return OpenAIServer
    if name == 'OpenAIDisaggServer':
        from .openai_disagg_server import OpenAIDisaggServer

        return OpenAIDisaggServer
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
