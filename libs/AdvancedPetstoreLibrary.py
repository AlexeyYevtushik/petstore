from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from datetime import datetime
import requests
from requests import Response
import json


# ===== PATTERN: Strategy Pattern for different response handlers =====
class ResponseHandler(ABC):
    """Abstract base class for response handling strategies"""
    
    @abstractmethod
    def handle_response(self, response: Response) -> Dict[str, Any]:
        pass


class JsonResponseHandler(ResponseHandler):
    """Concrete strategy for JSON responses"""
    
    def handle_response(self, response: Response) -> Dict[str, Any]:
        try:
            return {
                'success': True,
                'data': response.json(),
                'status_code': response.status_code,
                'content_type': 'json'
            }
        except json.JSONDecodeError:
            return {
                'success': False,
                'error': 'Invalid JSON response',
                'status_code': response.status_code
            }


class TextResponseHandler(ResponseHandler):
    """Concrete strategy for text responses"""
    
    def handle_response(self, response: Response) -> Dict[str, Any]:
        return {
            'success': True,
            'data': response.text,
            'status_code': response.status_code,
            'content_type': 'text'
        }


# ===== PATTERN: Singleton Pattern =====
class SingletonMeta(type):
    """Metaclass for implementing Singleton pattern"""
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        # ACCESS MODIFIERS DEMO: cls is accessible within metaclass
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)  # SUPER() USAGE: Calling parent metaclass
            cls._instances[cls] = instance
        return cls._instances[cls]


# ===== OOP: Abstract Base Class with Access Modifiers =====
class BaseApiLibrary(metaclass=SingletonMeta):
    """
    Base class with common API functionality using access modifiers
    Demonstrates protected and private attributes/methods
    """
    
    def __init__(self, base_url: str):
        # ACCESS MODIFIERS DEMO: 
        # Protected attribute (single underscore) - meant for internal use and subclasses
        self._base_url = base_url
        
        # Private attribute (double underscore) - name mangling, truly private
        self.__session = requests.Session()
        
        # Private dictionary with name mangling
        self.__response_handlers = {
            'json': JsonResponseHandler(),
            'text': TextResponseHandler()
        }
        
        # Protected attributes for subclass access
        self._last_response = None
        self._last_processed_data = None
        self._created_entities = []
        
        # Private counter with name mangling
        self.__request_count = 0
    
    # ===== MAGIC METHODS =====
    def __str__(self) -> str:
        """String representation - public method"""
        return f"{self.__class__.__name__}(requests={self.__request_count}, entities={len(self)})"
    
    def __repr__(self) -> str:
        """Technical representation - public method"""
        return f"<{self.__class__.__name__} at {hex(id(self))}>"
    
    def __len__(self) -> int:
        """Length implementation - public method"""
        return len(self._created_entities)
    
    def __getitem__(self, index: int) -> tuple:
        """Indexing support - public method"""
        return self._created_entities[index]
    
    def __iter__(self):
        """Iterator support - public method"""
        return iter(self._created_entities)
    
    def __contains__(self, entity_id: int) -> bool:
        """Membership test - public method"""
        return any(str(entity_id) in str(entity) for entity in self._created_entities)
    
    def __enter__(self):
        """Context manager entry - public method"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit with auto cleanup - public method"""
        self.cleanup_created()
    
    # ===== PROTECTED METHODS (internal use, accessible by subclasses) =====
    def _increment_request_count(self):
        """
        Protected method - meant for internal use and subclasses
        Single underscore indicates 'internal use'
        """
        self.__request_count += 1
    
    def _store_response(self, response: Response, handler_type: str = 'json'):
        """
        Protected method - processes and stores response data
        Accessible by subclasses for extension
        """
        self._last_response = response
        self._increment_request_count()  # Calling another protected method
        
        # ACCESS MODIFIERS DEMO: Accessing private attribute via name mangling
        handler = self.__response_handlers.get(handler_type, JsonResponseHandler())
        self._last_processed_data = handler.handle_response(response)
    
    def _make_request(self, method: str, endpoint: str, **kwargs) -> Response:
        """
        Protected method - main request handler
        Subclasses can override or extend this method
        """
        url = f"{self._base_url}{endpoint}"
        
        # ACCESS MODIFIERS DEMO: Using private attribute
        response = self.__session.request(method, url, **kwargs)
        self._store_response(response)
        return response
    
    # ===== PUBLIC METHODS =====
    def get_request_count(self) -> int:
        """
        Public getter for private attribute
        Demonstrates encapsulation - internal implementation is hidden
        """
        return self.__request_count
    
    def get_last_processed_data(self) -> Optional[Dict[str, Any]]:
        """Public method to access protected data"""
        return self._last_processed_data


# ===== OOP: Inheritance with super() =====
class AdvancedPetstoreLibrary(BaseApiLibrary):
    """
    Enhanced PetStore library with advanced OOP features
    Demonstrates inheritance and super() usage
    """
    
    def __init__(self):
        # SUPER() USAGE: Calling parent class constructor
        # This ensures BaseApiLibrary.__init__() is properly executed
        super().__init__("https://petstore.swagger.io/v2")
        
        # Additional initialization specific to this subclass
        self.ROBOT_LIBRARY_SCOPE = 'GLOBAL'
        
        # ACCESS MODIFIERS DEMO: Private attribute in subclass
        self.__performance_data = []
    
    # ===== MAGIC METHODS =====
    def __str__(self) -> str:
        """
        SUPER() USAGE: Extending parent's __str__ method
        First get parent's string representation, then enhance it
        """
        base_str = super().__str__()  # Call parent's __str__
        return f"Advanced{base_str}"  # Enhance with subclass prefix
    
    def __call__(self, entity_type: str, *args, **kwargs):
        """
        Make instance callable - public method
        Demonstrates different way to use the library
        """
        if entity_type == 'user':
            return self.create_user(*args, **kwargs)
        elif entity_type == 'pet':
            return self.create_pet(*args, **kwargs)
        else:
            raise ValueError(f"Unknown entity type: {entity_type}")
    
    # User methods - public interface
    def create_user(self, payload: dict) -> Response:
        """
        Public method - creates a user
        Demonstrates using protected methods from parent class
        """
        start_time = datetime.now()
        
        # SUPER() USAGE ALTERNATIVE: Using protected method from parent
        # We could use super()._make_request() but _make_request is inherited
        response = self._make_request("POST", "/user", json=payload)
        
        if response.status_code == 200:
            # ACCESS MODIFIERS DEMO: Using protected attribute from parent
            self._created_entities.append(('user', payload['username']))
            self.__record_performance('create_user', start_time)  # Calling private method
        
        return response
    
    def get_user(self, username: str) -> Response:
        """Public method - gets user data"""
        start_time = datetime.now()
        response = self._make_request("GET", f"/user/{username}")
        self.__record_performance('get_user', start_time)
        return response
    
    # Pet methods - public interface
    def create_pet(self, payload: dict) -> Response:
        """Public method - creates a pet"""
        start_time = datetime.now()
        response = self._make_request("POST", "/pet", json=payload)
        
        if response.status_code == 200:
            self._created_entities.append(('pet', payload['id']))
            self.__record_performance('create_pet', start_time)
        
        return response
    
    def get_pet(self, pet_id: int) -> Response:
        """Public method - gets pet data"""
        start_time = datetime.now()
        response = self._make_request("GET", f"/pet/{pet_id}")
        self.__record_performance('get_pet', start_time)
        return response
    
    def find_pets_by_status(self, status: str) -> Response:
        """Public method - finds pets by status"""
        return self._make_request("GET", "/pet/findByStatus", params={"status": status})
    
    def delete_pet(self, pet_id: int) -> Response:
        """Public method - deletes a pet"""
        return self._make_request("DELETE", f"/pet/{pet_id}")
    
    def delete_user(self, username: str) -> Response:
        """Public method - deletes a user"""
        return self._make_request("DELETE", f"/user/{username}")
    
    # Response assertions - public interface
    def should_be_status(self, expected_status: int):
        """Public method - asserts response status"""
        actual_status = self._last_response.status_code
        if actual_status != expected_status:
            raise AssertionError(f"Expected status {expected_status}, but got {actual_status}")
    
    def get_last_json(self):
        """Public method - gets last JSON response"""
        processed_data = self.get_last_processed_data()
        return processed_data.get('data') if processed_data else None
    
    # ===== PRIVATE METHODS (truly private, name mangled) =====
    def __record_performance(self, operation: str, start_time: datetime):
        """
        Private method - name mangling makes it truly private
        Double underscore prefix causes name mangling: _AdvancedPetstoreLibrary__record_performance
        Not accessible from outside the class, not even by subclasses
        """
        duration = (datetime.now() - start_time).total_seconds()
        self.__performance_data.append({
            'operation': operation,
            'duration': duration,
            'timestamp': datetime.now()
        })
    
    def get_performance_stats(self) -> Dict[str, Any]:
        """
        Public method to access private performance data
        Demonstrates encapsulation - private data accessed via public interface
        """
        if not self.__performance_data:
            return {}
        
        durations = [item['duration'] for item in self.__performance_data]
        return {
            'total_operations': len(self.__performance_data),
            'average_duration': sum(durations) / len(durations),
            'min_duration': min(durations),
            'max_duration': max(durations),
            'recent_operations': self.__performance_data[-5:]  # Last 5 operations
        }
    
    def cleanup_created(self):
        """
        Public method - enhanced cleanup with performance tracking
        Demonstrates using both protected and private methods
        """
        cleanup_start = datetime.now()
        
        # ACCESS MODIFIERS DEMO: Using protected attribute from parent
        for entity_type, identifier in self._created_entities:
            try:
                if entity_type == 'user':
                    self.delete_user(identifier)
                elif entity_type == 'pet':
                    self.delete_pet(identifier)
            except Exception as e:
                print(f"Cleanup warning for {entity_type} {identifier}: {e}")
        
        self._created_entities = []
        self.__record_performance('cleanup', cleanup_start)  # Calling private method