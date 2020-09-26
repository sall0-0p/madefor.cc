"""
All domains hosted by madefor.cc.

If you want to add your own, this is where you should do it!
"""

from typing import Dict, TypedDict


class DomainOptional(TypedDict, total=False):
    """Optional options for a domain."""

    # Whether to proxy through cloudflare or not. Defaults to false.
    cloudflare: bool


class Domain(DomainOptional):
    """Required options for a domain."""

    # The CNAME record which should be created.
    cname: str


domains: Dict[str, Domain] = {
    # Please make sure to keep this sorted!

    "metis": { "cname": "squiddev-cc.github.io" },
    "plethora": { "cname": "squiddev-cc.github.io" },
    "potatos": { "cname": "osmarks.tk" },
    "www": { "cname": "madefor.cc" },
}
