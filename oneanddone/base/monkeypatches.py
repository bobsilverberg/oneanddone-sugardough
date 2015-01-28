import logging


__all__ = ['patch']


# Prevent from patching twice.
_has_patched = False


def patch():
    global _has_patched
    if _has_patched:
        return

    # # Monkey-patch django forms to avoid having to use Jinja2's |safe
    # # everywhere.
    import jingo.monkey
    jingo.monkey.patch()

    # Monkey-patch Django's csrf_protect decorator to use session-based CSRF
    # tokens:
    import session_csrf
    session_csrf.monkeypatch()

    from jingo import load_helpers
    load_helpers()

    logging.debug("Note: monkey patches executed in %s" % __file__)

    # Prevent it from being run again later.
    _has_patched = True
