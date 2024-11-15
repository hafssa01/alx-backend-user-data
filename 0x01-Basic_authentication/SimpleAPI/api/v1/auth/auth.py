from flask import request
from typing import List, TypeVar

def require_auth_for_dynamic_path(path: str,
                                  excluded_paths: List[str]) -> bool:
    """returns true if partial path requires authentication"""
    if len(excluded_paths) == 0:
        return True
    for item in excluded_paths:
        if path[:-1].startswith(item[:-1]):
            return False
    return True
class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.
        
        Currently returns False, as authentication checks will be added later.

        Returns:
            - True if path is None.
            - True if excluded_paths is None or empty.
            - False if path matches any entry in excluded_paths.
            - True if path doesn't match any entry in excluded_paths.
        """
        if path is None:
            return True
        if not excluded_paths:
            return True
        
        if not path.endswith('/'):
            path += '/'

        for ex_path in excluded_paths:
            if ex_path.endswith('/') and path == ex_path:
                return False
    
        return True
    def authorization_header(self, request=None) -> str:
        """
        Returns the authorization header from the request if present.

        Currently returns None, to be implemented with header extraction logic later.
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user.

        Currently returns None, to be implemented with user extraction logic later.
        """
        return None
